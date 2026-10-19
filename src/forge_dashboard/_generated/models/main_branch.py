from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.forge import Forge
from ..models.main_branch_status import MainBranchStatus
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.main_branch_commit import MainBranchCommit





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
                "passed" when all finished green, "none" when the commit has no
                pipeline at all (or the repository has no commit yet).
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
            stale (bool): True when this row is the last known one because its forge
                couldn't be read or its rate limit is spent. A client offers no
                write on a stale row.
            stale_since (datetime.datetime | None): When this row was last fetched. Null unless `stale`.
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
    stale: bool
    stale_since: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.main_branch_commit import MainBranchCommit # noqa: PLC0415
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

        stale = self.stale

        stale_since: None | str
        if isinstance(self.stale_since, datetime.datetime):
            stale_since = self.stale_since.isoformat()
        else:
            stale_since = self.stale_since


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
            "stale": stale,
            "staleSince": stale_since,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.main_branch_commit import MainBranchCommit # noqa: PLC0415
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
            stale=stale,
            stale_since=stale_since,
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
