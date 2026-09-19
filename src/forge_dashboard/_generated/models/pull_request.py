from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ci_status import CIStatus
from ..models.forge import Forge
from ..models.merge_status import MergeStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.label import Label





T = TypeVar("T", bound="PullRequest")



@_attrs_define
class PullRequest:
    """ 
        Attributes:
            forge (Forge):
            repo (str): Owner-qualified repository name.
            number (int):
            title (str):
            url (str): The real pull request URL on its own forge.
            author (str):
            draft (bool):
            labels (list[Label]):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            ci (CIStatus): The combined result across every check reported against the pull
                request's head commit. "none" means neither forge reported any
                check at all, not that one failed.
            merge_status (MergeStatus): A pull request's mergeable/blocked state, as coarse as every forge
                this service talks to can agree on. "blocked" covers anything
                stopping a merge that isn't confirmed to be a real conflict —
                including Forgejo's own mergeable flag reporting false, since its
                server computes that asynchronously and can report it stale.
                "unknown" covers both a forge that hasn't determined this yet and
                this service being unable to determine it.
            behind (bool): Whether this pull request's base branch has moved since its
                merge-base was computed. Deliberately its own field rather
                than a mergeStatus value: on Forgejo a pull request can be
                both mergeable and behind at once (its mergeable flag doesn't
                get recomputed just because the base moved), so folding this
                into mergeStatus would force picking one and losing the
                other.
            auto_merge_enabled (bool | Unset): Whether auto-merge is currently scheduled on this pull request.
                Omitted when the owning forge has no way to report this at all
                (Forgejo, today) — never false in that case, since this service
                genuinely doesn't know.
     """

    forge: Forge
    repo: str
    number: int
    title: str
    url: str
    author: str
    draft: bool
    labels: list[Label]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    ci: CIStatus
    merge_status: MergeStatus
    behind: bool
    auto_merge_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.label import Label # noqa: PLC0415
        forge = self.forge.value

        repo = self.repo

        number = self.number

        title = self.title

        url = self.url

        author = self.author

        draft = self.draft

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)



        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        ci = self.ci.value

        merge_status = self.merge_status.value

        behind = self.behind

        auto_merge_enabled = self.auto_merge_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "forge": forge,
            "repo": repo,
            "number": number,
            "title": title,
            "url": url,
            "author": author,
            "draft": draft,
            "labels": labels,
            "createdAt": created_at,
            "updatedAt": updated_at,
            "ci": ci,
            "mergeStatus": merge_status,
            "behind": behind,
        })
        if auto_merge_enabled is not UNSET:
            field_dict["autoMergeEnabled"] = auto_merge_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label import Label # noqa: PLC0415
        d = dict(src_dict)
        forge = Forge(d.pop("forge"))




        repo = d.pop("repo")

        number = d.pop("number")

        title = d.pop("title")

        url = d.pop("url")

        author = d.pop("author")

        draft = d.pop("draft")

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in (_labels):
            labels_item = Label.from_dict(labels_item_data)



            labels.append(labels_item)


        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))




        ci = CIStatus(d.pop("ci"))




        merge_status = MergeStatus(d.pop("mergeStatus"))




        behind = d.pop("behind")

        auto_merge_enabled = d.pop("autoMergeEnabled", UNSET)

        pull_request = cls(
            forge=forge,
            repo=repo,
            number=number,
            title=title,
            url=url,
            author=author,
            draft=draft,
            labels=labels,
            created_at=created_at,
            updated_at=updated_at,
            ci=ci,
            merge_status=merge_status,
            behind=behind,
            auto_merge_enabled=auto_merge_enabled,
        )


        pull_request.additional_properties = d
        return pull_request

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
