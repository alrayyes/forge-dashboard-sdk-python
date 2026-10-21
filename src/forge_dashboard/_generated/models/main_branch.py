from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.forge import Forge
from ..models.main_branch_status import MainBranchStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.advisories import Advisories
  from ..models.check_counts import CheckCounts
  from ..models.main_branch_commit import MainBranchCommit
  from ..models.main_branch_release import MainBranchRelease





T = TypeVar("T", bound="MainBranch")



@_attrs_define
class MainBranch:
    """ One tracked repository and the CI status of its default branch.

        Attributes:
            forge (Forge):
            full_name (str): "owner/repo", matching a Repo.fullName from GET /api/dashboard.
            url (str): The repository's own page on its forge.
            branch (str): The repository's default branch. Empty for a repository the forge reports no default branch for.
            status (MainBranchStatus): The result of the latest pipeline on a default branch's newest
                commit, across all its workflows. "failed" when any job failed,
                "running" when none failed and some are still queued or running,
                "cancelled" when nothing failed and nothing is running but some run
                was cancelled (a newer push or a person stopped it, so nothing broke),
                "awaiting_approval" when GitHub holds the commit's workflow runs until
                a maintainer approves them (they create no check runs, so nothing
                runs), "passed" when all finished green, "none" when the commit has
                no pipeline at all (or the repository has no commit yet).
            commit (MainBranchCommit | None): The newest commit, or null when the forge reported none (an empty repository,
                or no run on Forgejo to name one from).
            failing_jobs (list[str]): The names of the failed jobs (GitHub checks, Forgejo Actions
                jobs), or of the failed workflow when its jobs couldn't be read.
                Always present and empty unless `status` is "failed".
            finished_at (datetime.datetime | None): When the pipeline's last job finished. Null while it runs, or when the
                forge didn't say.
            duration_seconds (int | None): How long the pipeline ran, from its first job starting to its last
                finishing. Null while it runs, or when the forge didn't say.
            run_url (str): Where to see the run on the forge: the failed job's page for a
                failed pipeline, else the run's, else the commit's. Falls back to
                the repository's `url`.
            checks (CheckCounts): How many checks are in each state, so a client can say how far a
                pipeline is without opening it. It is on every pull request and on
                every default branch, for a passed, a failed and a running pipeline
                alike. The server tallies them from what it already reads to work out
                the overall state, so they cost no request. Always present, all zero
                when there are no checks.

                `waiting` is a check that has not started: queued, or pending where the
                forge doesn't tell queued from running. A failed pipeline can still have
                checks running or waiting, and says so. A pull request's counts agree
                with its `ci`: one whose `ci` is `pending` has `failed` at 0, and one
                whose `ci` is `success` has nothing running, waiting or failed. Two
                kinds of run are therefore in none of the four, as long as something
                else explains the state. A run held for approval: on a pull request
                `awaitingWorkflowApproval` says that. A cancelled run: a push or a
                concurrency group superseded it, and the overall state does not read it
                as a failure while others still run. When cancelled runs (and, on a
                branch, held ones) are the only reason a pipeline reads as failed, they
                count as `failed` (a held run first, where both are there), so a failed
                pipeline always has a failed count on GitHub. A branch whose status is
                `cancelled` has `failed` at 0. A timed-out or stale check counts as `failed`, a skipped,
                neutral or bare completed one as `passed`, on Forgejo too.

                `skipped` is a newer field and says how many of the `passed` checks
                were skipped. It never exceeds `passed`: it is inside `passed`, not
                beside it, so `passed` still counts every check that needs nothing more
                and the four states still add up to the checks the pipeline lists. The
                server always sends it; a client that may talk to an older server
                reads a missing one as none. A neutral or bare completed check is passed without
                being skipped. A client that draws the two side by side must subtract
                `skipped` from `passed` for the passed figure, or a skipped check is
                counted twice, and a pipeline where every passed check was skipped can
                read as skipped.

                On GitHub the counts come from the same rollup as the overall state,
                for a pull request and a branch alike; on Forgejo a pull request counts
                the statuses of the combined commit status, where nothing is ever
                `running`, and a default branch counts the workflow runs of the newest
                commit that has one (a job count would cost a request per run), where a
                running run is `running` and a queued or blocked one `waiting`. Forgejo
                answers one page of those statuses, and when its total says there are
                more than the page holds a pull request's counts are all zero rather
                than an undercount. When GitHub's rollup of a pull request is of an
                earlier commit than the head (a push still being processed), the counts
                are zero too. GitHub's unauthenticated fallback has no such counts, so
                there they are all zero.
            latest_release (MainBranchRelease | None): The repository's latest published release, for a link to its
                notes. Null when the repository has none, when its only releases
                are drafts or pre-releases, and for every Forgejo repository,
                whose latest release is a separate read per repository that the
                refresh does not make.
            stale (bool): True when this row is the last known one because its forge
                couldn't be read or its rate limit is spent. A client offers no
                write on a stale row.
            stale_since (datetime.datetime | None): When this row was last fetched. Null unless `stale`.
            advisories (Advisories | Unset): The open dependency advisories on a repository's default branch, read
                from the forge's own source (GitHub's Dependabot alerts). Absent from
                the row when no source reads them for its forge. A source that can't
                answer, such as alerts switched off or a token without the
                `security_events` scope, gives `state` "unknown", never a count of
                zero.
     """

    forge: Forge
    full_name: str
    url: str
    branch: str
    status: MainBranchStatus
    commit: MainBranchCommit | None
    failing_jobs: list[str]
    finished_at: datetime.datetime | None
    duration_seconds: int | None
    run_url: str
    checks: CheckCounts
    latest_release: MainBranchRelease | None
    stale: bool
    stale_since: datetime.datetime | None
    advisories: Advisories | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.advisories import Advisories # noqa: PLC0415
        from ..models.check_counts import CheckCounts # noqa: PLC0415
        from ..models.main_branch_commit import MainBranchCommit # noqa: PLC0415
        from ..models.main_branch_release import MainBranchRelease # noqa: PLC0415
        forge = self.forge.value

        full_name = self.full_name

        url = self.url

        branch = self.branch

        status = self.status.value

        commit: dict[str, Any] | None
        if isinstance(self.commit, MainBranchCommit):
            commit = self.commit.to_dict()
        else:
            commit = self.commit

        failing_jobs = self.failing_jobs



        finished_at: None | str
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        duration_seconds: int | None
        duration_seconds = self.duration_seconds

        run_url = self.run_url

        checks = self.checks.to_dict()

        latest_release: dict[str, Any] | None
        if isinstance(self.latest_release, MainBranchRelease):
            latest_release = self.latest_release.to_dict()
        else:
            latest_release = self.latest_release

        stale = self.stale

        stale_since: None | str
        if isinstance(self.stale_since, datetime.datetime):
            stale_since = self.stale_since.isoformat()
        else:
            stale_since = self.stale_since

        advisories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advisories, Unset):
            advisories = self.advisories.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "forge": forge,
            "fullName": full_name,
            "url": url,
            "branch": branch,
            "status": status,
            "commit": commit,
            "failingJobs": failing_jobs,
            "finishedAt": finished_at,
            "durationSeconds": duration_seconds,
            "runUrl": run_url,
            "checks": checks,
            "latestRelease": latest_release,
            "stale": stale,
            "staleSince": stale_since,
        })
        if advisories is not UNSET:
            field_dict["advisories"] = advisories

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advisories import Advisories # noqa: PLC0415
        from ..models.check_counts import CheckCounts # noqa: PLC0415
        from ..models.main_branch_commit import MainBranchCommit # noqa: PLC0415
        from ..models.main_branch_release import MainBranchRelease # noqa: PLC0415
        d = dict(src_dict)
        forge = Forge(d.pop("forge"))




        full_name = d.pop("fullName")

        url = d.pop("url")

        branch = d.pop("branch")

        status = MainBranchStatus(d.pop("status"))




        def _parse_commit(data: object) -> MainBranchCommit | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                commit_type_0 = MainBranchCommit.from_dict(data)



                return commit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MainBranchCommit | None, data)

        commit = _parse_commit(d.pop("commit"))


        failing_jobs = cast(list[str], d.pop("failingJobs"))


        def _parse_finished_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)



                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        finished_at = _parse_finished_at(d.pop("finishedAt"))


        def _parse_duration_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duration_seconds = _parse_duration_seconds(d.pop("durationSeconds"))


        run_url = d.pop("runUrl")

        checks = CheckCounts.from_dict(d.pop("checks"))




        def _parse_latest_release(data: object) -> MainBranchRelease | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_release_type_0 = MainBranchRelease.from_dict(data)



                return latest_release_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MainBranchRelease | None, data)

        latest_release = _parse_latest_release(d.pop("latestRelease"))


        stale = d.pop("stale")

        def _parse_stale_since(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stale_since_type_0 = datetime.datetime.fromisoformat(data)



                return stale_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        stale_since = _parse_stale_since(d.pop("staleSince"))


        _advisories = d.pop("advisories", UNSET)
        advisories: Advisories | Unset
        if isinstance(_advisories,  Unset):
            advisories = UNSET
        else:
            advisories = Advisories.from_dict(_advisories)




        main_branch = cls(
            forge=forge,
            full_name=full_name,
            url=url,
            branch=branch,
            status=status,
            commit=commit,
            failing_jobs=failing_jobs,
            finished_at=finished_at,
            duration_seconds=duration_seconds,
            run_url=run_url,
            checks=checks,
            latest_release=latest_release,
            stale=stale,
            stale_since=stale_since,
            advisories=advisories,
        )


        main_branch.additional_properties = d
        return main_branch

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
