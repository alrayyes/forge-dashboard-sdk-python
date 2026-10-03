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
  from ..models.allowed_action import AllowedAction
  from ..models.label import Label
  from ..models.review_state import ReviewState





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
            empty (bool): Whether merging this pull request would produce an empty
                commit — its content already landed on the base branch some
                other way. False whenever this service can't tell (the
                unauthenticated GitHub REST fallback, or a Forgejo instance
                old enough not to report additions/deletions/changed_files on
                its list endpoint), never a false positive: a pull request
                this never confirms empty just renders as it always has.
            allowed_actions (list[AllowedAction]): The actions this pull request offers, worked out on the server
                from its own fields, so a client needs no copy of the rules. An
                action that doesn't apply (Update branch on a pull request that
                isn't behind, a Dependabot command on a Renovate pull request)
                is absent, not listed as blocked. Always present; `close` is
                always in it. Live state is the client's: a rate-limited or
                unreachable forge, a missing token and an action already in
                flight can still stop an offered action.
            auto_merge_enabled (bool | Unset): Whether auto-merge is currently scheduled on this pull request.
                Omitted when the owning forge has no way to report this at all
                (Forgejo, today) — never false in that case, since this service
                genuinely doesn't know.
            auto_merge_allowed (bool | Unset): Whether GitHub will accept an "Enable auto-merge" request for
                this pull request from the signed-in viewer, read from the
                GraphQL `PullRequest.viewerCanEnableAutoMerge` field. GitHub
                decides this per viewer and per pull request: auto-merge needs
                something on the base branch to wait for (required checks or
                reviews from a branch protection rule or ruleset), so a stacked
                pull request on an unprotected base reports false even when the
                repository allows auto-merge. Omitted when unknown (the
                unauthenticated REST fallback, and Forgejo), never false in
                that case, so clients keep today's behaviour.
            review (ReviewState | Unset): Where a pull request stands on code review. The whole object is
                omitted when the owning forge couldn't report it (a Forgejo
                reviews call that failed, a draft Forgejo pull request this
                service doesn't spend a call on), so a missing "review" means
                "unknown" and never "nobody reviewed it."

                GitHub: read from fields on the existing GraphQL query
                (reviewDecision, reviewRequests, latestReviews), so it adds no
                per-pull-request requests. Forgejo: requestedReviewers comes free
                on the pull request list, but approvals and the decision need one
                reviews call per open, non-draft pull request, cached until that
                pull request's updatedAt changes.
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
    empty: bool
    allowed_actions: list[AllowedAction]
    auto_merge_enabled: bool | Unset = UNSET
    auto_merge_allowed: bool | Unset = UNSET
    review: ReviewState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.allowed_action import AllowedAction # noqa: PLC0415
        from ..models.label import Label # noqa: PLC0415
        from ..models.review_state import ReviewState # noqa: PLC0415
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

        empty = self.empty

        allowed_actions = []
        for allowed_actions_item_data in self.allowed_actions:
            allowed_actions_item = allowed_actions_item_data.to_dict()
            allowed_actions.append(allowed_actions_item)



        auto_merge_enabled = self.auto_merge_enabled

        auto_merge_allowed = self.auto_merge_allowed

        review: dict[str, Any] | Unset = UNSET
        if not isinstance(self.review, Unset):
            review = self.review.to_dict()


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
            "empty": empty,
            "allowedActions": allowed_actions,
        })
        if auto_merge_enabled is not UNSET:
            field_dict["autoMergeEnabled"] = auto_merge_enabled
        if auto_merge_allowed is not UNSET:
            field_dict["autoMergeAllowed"] = auto_merge_allowed
        if review is not UNSET:
            field_dict["review"] = review

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_action import AllowedAction # noqa: PLC0415
        from ..models.label import Label # noqa: PLC0415
        from ..models.review_state import ReviewState # noqa: PLC0415
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

        empty = d.pop("empty")

        allowed_actions = []
        _allowed_actions = d.pop("allowedActions")
        for allowed_actions_item_data in (_allowed_actions):
            allowed_actions_item = AllowedAction.from_dict(allowed_actions_item_data)



            allowed_actions.append(allowed_actions_item)


        auto_merge_enabled = d.pop("autoMergeEnabled", UNSET)

        auto_merge_allowed = d.pop("autoMergeAllowed", UNSET)

        _review = d.pop("review", UNSET)
        review: ReviewState | Unset
        if isinstance(_review,  Unset):
            review = UNSET
        else:
            review = ReviewState.from_dict(_review)




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
            empty=empty,
            allowed_actions=allowed_actions,
            auto_merge_enabled=auto_merge_enabled,
            auto_merge_allowed=auto_merge_allowed,
            review=review,
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
