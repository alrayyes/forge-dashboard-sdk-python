from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ci_status import CIStatus
from ..models.forge import Forge
from ..models.merge_status import MergeStatus
from ..models.pull_request_kind import PullRequestKind
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.allowed_action import AllowedAction
  from ..models.auto_merge_status import AutoMergeStatus
  from ..models.bot_request import BotRequest
  from ..models.label import Label
  from ..models.review_state import ReviewState
  from ..models.stack_position import StackPosition
  from ..models.stack_ref import StackRef
  from ..models.update_request import UpdateRequest





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
                "unstable" is GitHub's UNSTABLE: the pull request can be merged, but
                a check that branch protection doesn't require is failing or still
                running. Merge stays available.
                "unknown" covers both a forge that hasn't determined this yet and
                this service being unable to determine it.
            behind (bool): Whether this pull request's base branch has moved since its
                merge-base was computed. Deliberately its own field rather
                than a mergeStatus value: on Forgejo a pull request can be
                both mergeable and behind at once (its mergeable flag doesn't
                get recomputed just because the base moved), so folding this
                into mergeStatus would force picking one and losing the
                other.
            head_sha (str): The commit the pull request's head branch points at. A bot's
                rebase moves it, which shows the bot acted even when the pull
                request is still reported behind, or wasn't behind to begin
                with. Empty when the forge didn't say. Always present.
            kind (PullRequestKind): What sort of pull request this is, decided by the server so no
                client keeps its own copy of the rule. `release`: release-please's,
                by its `autorelease:` label (a person opens these, so the label is
                the only signal, and it wins over any bot author). `dependency`:
                opened by Dependabot or Renovate, in either spelling of the login
                (the bare slug GraphQL gives, or REST's `[bot]` form), on either
                forge. `regular`: everything else. Always present.
            base_branch (str): The branch the pull request targets. Empty when the forge didn't
                say.
            head_branch (str): The branch the pull request comes from. Empty when the forge
                didn't say.
            cross_repository (bool): True when the head branch lives in another repository (a fork).
                A fork pull request is never part of a stack.
            stack (None | StackPosition): Where this pull request sits in a stack of pull requests, or
                null when it is in none. A stack is worked out on the server:
                pull request B is stacked on A when B's base branch is A's head
                branch, in the same repository on the same forge, and neither is
                a fork. A branch with several open pull requests takes the one
                with the lowest number as parent, and a loop of branches is
                treated as no stack. The snapshot holds open pull requests
                only, so a base branch that no open pull request owns (a parent
                that already merged and was not retargeted) is not flagged.
            stacked_on (None | StackRef): The open pull request this one is stacked on, or null when its
                base is not another open pull request's head.
            stack_children (list[int]): The numbers of the open pull requests stacked directly on this
                one. Always a list, empty when none.
            requested_reviewer_logins (list[str]): The logins of the users asked to review this pull request, on
                both forges. A team request has no login and is left out.
                Always present, and empty when nobody was asked. Costs no
                extra request: GitHub returns it with the reviewRequests count
                already queried, Forgejo with the pull request itself.
            review_requested_from_me (bool): True when this open, non-draft pull request asks the signed-in
                user to review it, matched without regard to case against the
                username saved in Settings for its forge. False when no
                username is saved for that forge. Always present.
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
            ready_to_merge (bool): True when the pull request is mergeable, its CI is green and it
                isn't a draft: what the Ready quick filter lists. Always
                present. A pull request with no checks isn't ready.
            needs_review (bool): True when a review is outstanding: the forge requires one, or a
                reviewer was asked and hasn't answered, and the pull request
                isn't a draft. Unreviewed with nobody asked, approved, changes
                requested and an unknown review state are all false. Always
                present.
            bot_request (BotRequest | None | Unset): A Dependabot or Renovate rebase asked for through this app and not
                settled yet, or null. The server keeps it, so a reload during the
                wait still shows it, and moves it along on every snapshot that
                came from a fetch started after the request. Held in memory per
                account: a server restart forgets it.
            update_request (None | Unset | UpdateRequest): An Update branch the forge accepted and that no snapshot has
                shown
                landing yet, or null. The server keeps it, so a reload during the
                wait still shows it. It is dropped once a snapshot from a fetch
                started after the request shows the pull request no longer
                behind, or when the pull request is gone. Held in memory per
                account: a server restart forgets it.
            auto_merge_enabled (bool | Unset): Whether auto-merge is currently scheduled on this pull request.
                On Forgejo it is true when the signed-in user armed it in this
                app, which holds the intent itself. Otherwise omitted when the
                owning forge has no way to report this — never false in that
                case, since this service genuinely doesn't know.
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
            auto_merge (AutoMergeStatus | Unset): Where an armed Forgejo pull request stands, so the row can say why
                auto-merge is waiting or stopped in words and not by colour. Present
                only while the signed-in user has auto-merge armed on it. This app
                holds that intent itself, so GitHub's own auto-merge never has it.
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
    head_sha: str
    kind: PullRequestKind
    base_branch: str
    head_branch: str
    cross_repository: bool
    stack: None | StackPosition
    stacked_on: None | StackRef
    stack_children: list[int]
    requested_reviewer_logins: list[str]
    review_requested_from_me: bool
    empty: bool
    allowed_actions: list[AllowedAction]
    ready_to_merge: bool
    needs_review: bool
    bot_request: BotRequest | None | Unset = UNSET
    update_request: None | Unset | UpdateRequest = UNSET
    auto_merge_enabled: bool | Unset = UNSET
    auto_merge_allowed: bool | Unset = UNSET
    review: ReviewState | Unset = UNSET
    auto_merge: AutoMergeStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.allowed_action import AllowedAction # noqa: PLC0415
        from ..models.auto_merge_status import AutoMergeStatus # noqa: PLC0415
        from ..models.bot_request import BotRequest # noqa: PLC0415
        from ..models.label import Label # noqa: PLC0415
        from ..models.review_state import ReviewState # noqa: PLC0415
        from ..models.stack_position import StackPosition # noqa: PLC0415
        from ..models.stack_ref import StackRef # noqa: PLC0415
        from ..models.update_request import UpdateRequest # noqa: PLC0415
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

        head_sha = self.head_sha

        kind = self.kind.value

        base_branch = self.base_branch

        head_branch = self.head_branch

        cross_repository = self.cross_repository

        stack: dict[str, Any] | None
        if isinstance(self.stack, StackPosition):
            stack = self.stack.to_dict()
        else:
            stack = self.stack

        stacked_on: dict[str, Any] | None
        if isinstance(self.stacked_on, StackRef):
            stacked_on = self.stacked_on.to_dict()
        else:
            stacked_on = self.stacked_on

        stack_children = self.stack_children



        requested_reviewer_logins = self.requested_reviewer_logins



        review_requested_from_me = self.review_requested_from_me

        empty = self.empty

        allowed_actions = []
        for allowed_actions_item_data in self.allowed_actions:
            allowed_actions_item = allowed_actions_item_data.to_dict()
            allowed_actions.append(allowed_actions_item)



        ready_to_merge = self.ready_to_merge

        needs_review = self.needs_review

        bot_request: dict[str, Any] | None | Unset
        if isinstance(self.bot_request, Unset):
            bot_request = UNSET
        elif isinstance(self.bot_request, BotRequest):
            bot_request = self.bot_request.to_dict()
        else:
            bot_request = self.bot_request

        update_request: dict[str, Any] | None | Unset
        if isinstance(self.update_request, Unset):
            update_request = UNSET
        elif isinstance(self.update_request, UpdateRequest):
            update_request = self.update_request.to_dict()
        else:
            update_request = self.update_request

        auto_merge_enabled = self.auto_merge_enabled

        auto_merge_allowed = self.auto_merge_allowed

        review: dict[str, Any] | Unset = UNSET
        if not isinstance(self.review, Unset):
            review = self.review.to_dict()

        auto_merge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_merge, Unset):
            auto_merge = self.auto_merge.to_dict()


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
            "headSha": head_sha,
            "kind": kind,
            "baseBranch": base_branch,
            "headBranch": head_branch,
            "crossRepository": cross_repository,
            "stack": stack,
            "stackedOn": stacked_on,
            "stackChildren": stack_children,
            "requestedReviewerLogins": requested_reviewer_logins,
            "reviewRequestedFromMe": review_requested_from_me,
            "empty": empty,
            "allowedActions": allowed_actions,
            "readyToMerge": ready_to_merge,
            "needsReview": needs_review,
        })
        if bot_request is not UNSET:
            field_dict["botRequest"] = bot_request
        if update_request is not UNSET:
            field_dict["updateRequest"] = update_request
        if auto_merge_enabled is not UNSET:
            field_dict["autoMergeEnabled"] = auto_merge_enabled
        if auto_merge_allowed is not UNSET:
            field_dict["autoMergeAllowed"] = auto_merge_allowed
        if review is not UNSET:
            field_dict["review"] = review
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_action import AllowedAction # noqa: PLC0415
        from ..models.auto_merge_status import AutoMergeStatus # noqa: PLC0415
        from ..models.bot_request import BotRequest # noqa: PLC0415
        from ..models.label import Label # noqa: PLC0415
        from ..models.review_state import ReviewState # noqa: PLC0415
        from ..models.stack_position import StackPosition # noqa: PLC0415
        from ..models.stack_ref import StackRef # noqa: PLC0415
        from ..models.update_request import UpdateRequest # noqa: PLC0415
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

        head_sha = d.pop("headSha")

        kind = PullRequestKind(d.pop("kind"))




        base_branch = d.pop("baseBranch")

        head_branch = d.pop("headBranch")

        cross_repository = d.pop("crossRepository")

        def _parse_stack(data: object) -> None | StackPosition:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stack_type_1 = StackPosition.from_dict(data)



                return stack_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StackPosition, data)

        stack = _parse_stack(d.pop("stack"))


        def _parse_stacked_on(data: object) -> None | StackRef:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stacked_on_type_1 = StackRef.from_dict(data)



                return stacked_on_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StackRef, data)

        stacked_on = _parse_stacked_on(d.pop("stackedOn"))


        stack_children = cast(list[int], d.pop("stackChildren"))


        requested_reviewer_logins = cast(list[str], d.pop("requestedReviewerLogins"))


        review_requested_from_me = d.pop("reviewRequestedFromMe")

        empty = d.pop("empty")

        allowed_actions = []
        _allowed_actions = d.pop("allowedActions")
        for allowed_actions_item_data in (_allowed_actions):
            allowed_actions_item = AllowedAction.from_dict(allowed_actions_item_data)



            allowed_actions.append(allowed_actions_item)


        ready_to_merge = d.pop("readyToMerge")

        needs_review = d.pop("needsReview")

        def _parse_bot_request(data: object) -> BotRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bot_request_type_1 = BotRequest.from_dict(data)



                return bot_request_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BotRequest | None | Unset, data)

        bot_request = _parse_bot_request(d.pop("botRequest", UNSET))


        def _parse_update_request(data: object) -> None | Unset | UpdateRequest:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                update_request_type_1 = UpdateRequest.from_dict(data)



                return update_request_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateRequest, data)

        update_request = _parse_update_request(d.pop("updateRequest", UNSET))


        auto_merge_enabled = d.pop("autoMergeEnabled", UNSET)

        auto_merge_allowed = d.pop("autoMergeAllowed", UNSET)

        _review = d.pop("review", UNSET)
        review: ReviewState | Unset
        if isinstance(_review,  Unset):
            review = UNSET
        else:
            review = ReviewState.from_dict(_review)




        _auto_merge = d.pop("autoMerge", UNSET)
        auto_merge: AutoMergeStatus | Unset
        if isinstance(_auto_merge,  Unset):
            auto_merge = UNSET
        else:
            auto_merge = AutoMergeStatus.from_dict(_auto_merge)




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
            head_sha=head_sha,
            kind=kind,
            base_branch=base_branch,
            head_branch=head_branch,
            cross_repository=cross_repository,
            stack=stack,
            stacked_on=stacked_on,
            stack_children=stack_children,
            requested_reviewer_logins=requested_reviewer_logins,
            review_requested_from_me=review_requested_from_me,
            empty=empty,
            allowed_actions=allowed_actions,
            ready_to_merge=ready_to_merge,
            needs_review=needs_review,
            bot_request=bot_request,
            update_request=update_request,
            auto_merge_enabled=auto_merge_enabled,
            auto_merge_allowed=auto_merge_allowed,
            review=review,
            auto_merge=auto_merge,
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
