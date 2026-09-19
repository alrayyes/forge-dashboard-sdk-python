# forge-dashboard-sdk-python

[![CI](https://github.com/alrayyes/forge-dashboard-sdk-python/actions/workflows/ci.yml/badge.svg)](https://github.com/alrayyes/forge-dashboard-sdk-python/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/forge-dashboard-sdk.svg)](https://pypi.org/project/forge-dashboard-sdk/)
[![Codecov](https://codecov.io/gh/alrayyes/forge-dashboard-sdk-python/graph/badge.svg)](https://codecov.io/gh/alrayyes/forge-dashboard-sdk-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![docs](https://img.shields.io/badge/docs-mkdocs-blue)](https://alrayyes.github.io/forge-dashboard-sdk-python/)

A Python client for [forge-dashboard](https://github.com/alrayyes/forge-dashboard)'s
REST API, generated from its OpenAPI spec with
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client).
It saves you from hand-rolling HTTP requests, auth and retries against the
API yourself.

## Requirements

- Python 3.12 or later.
- A running forge-dashboard instance.
- A personal API token for that instance (see "Authentication" below) —
  every endpoint except `health`, `get_version` and the two webhook
  receivers needs one.

## Installation

```sh
pip install forge-dashboard-sdk
```

Pin an exact version in your own `pyproject.toml`/`requirements.txt` rather
than tracking the latest release in anything but a quick trial.

## Authentication

forge-dashboard accepts either a browser's passkey session cookie or a
personal API token — `Authorization: Bearer <token>` — as an alternative
that needs no WebAuthn ceremony. This SDK only speaks the token half, the
one a script can actually use. Mint one by signing into the dashboard once
and calling `POST /api/tokens`, then pass it to `ForgeDashboardClient` or
set `FORGE_DASHBOARD_API_TOKEN` in the environment:

```python
import os
from forge_dashboard import ForgeDashboardClient

client = ForgeDashboardClient(
    "https://forge-dashboard.example.com",
    api_token=os.environ.get("FORGE_DASHBOARD_API_TOKEN"),
)
```

## Usage

`health` and `get_version` need no token and are good first calls to prove
the client reaches the server at all:

```python
from forge_dashboard import ForgeDashboardClient

with ForgeDashboardClient("https://forge-dashboard.example.com") as client:
    version = client.get_version()
    print("server version:", version.version)
```

The aggregated dashboard needs a token, and demonstrates error handling:

```python
import os
from forge_dashboard import APIError, ForgeDashboardClient, decode_error
from forge_dashboard._generated.api.dashboard import get_dashboard

client = ForgeDashboardClient(
    "https://forge-dashboard.example.com",
    api_token=os.environ.get("FORGE_DASHBOARD_API_TOKEN"),
)

try:
    response = get_dashboard.sync_detailed(client=client.raw)
    if error := decode_error(response):
        raise error
    for pr in response.parsed.pull_requests:
        print(pr.title, pr.ci)
except APIError as e:
    if e.status_code == 401:
        raise SystemExit("API token expired or invalid") from e
    raise
```

Every other operation follows the generated client's pattern —
`forge_dashboard._generated.api.<tag>.<operation>.sync_detailed(client=client.raw, ...)`
(or `asyncio_detailed` for async) returns a typed `Response` whose `.parsed`
field holds the decoded body for a documented status code. Use
`decode_error` to turn any error response into a `forge_dashboard.APIError`
uniformly:

```python
from forge_dashboard import decode_error
from forge_dashboard._generated.api.dashboard import get_dashboard

response = get_dashboard.sync_detailed(client=client.raw)
if error := decode_error(response):
    raise error
dashboard = response.parsed
```

The client retries a `429` or `5xx` response with exponential backoff and
jitter (honoring a server-sent `Retry-After`), and never retries any other
`4xx`. Tune it by passing a `forge_dashboard.RetryConfig` as `retry=`, or
swap the underlying `httpx.Client`/`httpx.AsyncClient` entirely with
`httpx_client=`/`httpx_async_client=`.

## Regenerating the client

See [CONTRIBUTING.md](CONTRIBUTING.md) — the generated code is pinned to a
specific forge-dashboard commit and shouldn't drift from it silently.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for building, testing and the release
process.

## License

[MIT](LICENSE) — a permissive license for the client, independent of
forge-dashboard's own AGPL-3.0.
