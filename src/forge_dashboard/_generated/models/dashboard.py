from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.forge_health import ForgeHealth
  from ..models.issue import Issue
  from ..models.pull_request import PullRequest
  from ..models.repo_status import RepoStatus





T = TypeVar("T", bound="Dashboard")



@_attrs_define
class Dashboard:
    """ 
        Attributes:
            generated_at (datetime.datetime): When this snapshot was refreshed, not when it was requested.
            forges (list[ForgeHealth]):
            pull_requests (list[PullRequest]):
            issues (list[Issue]):
            repos (list[RepoStatus]):
     """

    generated_at: datetime.datetime
    forges: list[ForgeHealth]
    pull_requests: list[PullRequest]
    issues: list[Issue]
    repos: list[RepoStatus]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.forge_health import ForgeHealth # noqa: PLC0415
        from ..models.issue import Issue # noqa: PLC0415
        from ..models.pull_request import PullRequest # noqa: PLC0415
        from ..models.repo_status import RepoStatus # noqa: PLC0415
        generated_at = self.generated_at.isoformat()

        forges = []
        for forges_item_data in self.forges:
            forges_item = forges_item_data.to_dict()
            forges.append(forges_item)



        pull_requests = []
        for pull_requests_item_data in self.pull_requests:
            pull_requests_item = pull_requests_item_data.to_dict()
            pull_requests.append(pull_requests_item)



        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)



        repos = []
        for repos_item_data in self.repos:
            repos_item = repos_item_data.to_dict()
            repos.append(repos_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "generatedAt": generated_at,
            "forges": forges,
            "pullRequests": pull_requests,
            "issues": issues,
            "repos": repos,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.forge_health import ForgeHealth # noqa: PLC0415
        from ..models.issue import Issue # noqa: PLC0415
        from ..models.pull_request import PullRequest # noqa: PLC0415
        from ..models.repo_status import RepoStatus # noqa: PLC0415
        d = dict(src_dict)
        generated_at = datetime.datetime.fromisoformat(d.pop("generatedAt"))




        forges = []
        _forges = d.pop("forges")
        for forges_item_data in (_forges):
            forges_item = ForgeHealth.from_dict(forges_item_data)



            forges.append(forges_item)


        pull_requests = []
        _pull_requests = d.pop("pullRequests")
        for pull_requests_item_data in (_pull_requests):
            pull_requests_item = PullRequest.from_dict(pull_requests_item_data)



            pull_requests.append(pull_requests_item)


        issues = []
        _issues = d.pop("issues")
        for issues_item_data in (_issues):
            issues_item = Issue.from_dict(issues_item_data)



            issues.append(issues_item)


        repos = []
        _repos = d.pop("repos")
        for repos_item_data in (_repos):
            repos_item = RepoStatus.from_dict(repos_item_data)



            repos.append(repos_item)


        dashboard = cls(
            generated_at=generated_at,
            forges=forges,
            pull_requests=pull_requests,
            issues=issues,
            repos=repos,
        )


        dashboard.additional_properties = d
        return dashboard

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
