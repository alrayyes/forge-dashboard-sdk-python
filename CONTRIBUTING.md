# Contributing

## Requirements

- Python 3.12 or later.
- [uv](https://docs.astral.sh/uv/) for the environment and lockfile.
- [lefthook](https://github.com/evilmartians/lefthook) and
  [bun](https://bun.sh) (for commitlint). `bun install` then
  `lefthook install` once, after cloning.
- [gitleaks](https://github.com/gitleaks/gitleaks) on your `PATH`. It scans
  for secrets in the `pre-commit` and `pre-push` hooks and in CI.

## Building and testing

```sh
uv sync --all-groups
uv run pytest
uv run ruff format --check .
uv run ruff check .
uv run mypy .
uv run bandit -r src/forge_dashboard -x src/forge_dashboard/_generated
uv run pip-audit
uv run mutmut run
```

`lefthook run pre-push` runs the fast subset of the above (format, lint,
type check, tests) before every push, plus a gitleaks scan of the whole
history; mutation testing runs in CI, not the
hook, since a full `mutmut run` is too slow for every push.

## Regenerating the client

`src/forge_dashboard/_generated/` is generated from `openapi/openapi.yaml`
by [openapi-python-client](https://github.com/openapi-generators/openapi-python-client)
— never hand-edit it. The spec itself is pinned to a commit of
[alrayyes/forge-dashboard](https://github.com/alrayyes/forge-dashboard)
recorded in `openapi/SPEC_COMMIT`; `.github/workflows/regenerate.yml` bumps
that pin weekly and opens a pull request when forge-dashboard's spec has
moved. To do it by hand:

```sh
./hack/fetch-spec.sh
uv run openapi-python-client generate --path openapi/openapi.yaml \
  --meta none --output-path src/forge_dashboard/_generated --overwrite
```

Diff `openapi/openapi.yaml` (not the generated Python) to decide whether a
change needs a major, minor or patch bump — see the "Versioning tracks the
contract, not the commits" note this repo's global config links to.

## Commits and releases

Commit messages follow [Conventional
Commits](https://www.conventionalcommits.org/), linted by commitlint on
`commit-msg`. Merging to `main` is what
[release-please](https://github.com/googleapis/release-please) reads to
keep an open release pull request with the next version and changelog;
merging that pull request tags the release and, once tagged, publishes to
PyPI via Trusted Publishing.

## Branching

Every change lands through a pull request; nothing is pushed straight to
`main`.

## Dependency advisories

Two jobs share the work, both through
[advisory-scan](https://github.com/alrayyes/advisory-scan). The `audit` job in
`ci.yml` runs `bun audit` and `pip-audit` on a pull request and on its base, and fails only on
advisories the pull request adds, so an advisory published overnight doesn't
turn unrelated pull requests red. It runs when a manifest or lockfile
changes, and on every push to `main`. `advisory-scan.yml` audits `main`
daily, on every push that changes a manifest or lockfile, and on demand, and
keeps one open issue titled "Dependency advisories" listing what it finds. It
closes that issue when the audit is clean. There's no ignore list: an advisory
with no fix stays in that issue until one ships.

No pre-push hook runs the audit: it would fail every push the day an
advisory lands on `main`, whatever the push changed. CI owns the gate. To
check by hand, run `uv run pip-audit` (and `bun audit`).
