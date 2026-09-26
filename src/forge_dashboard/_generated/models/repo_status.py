from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.forge import Forge






T = TypeVar("T", bound="RepoStatus")



@_attrs_define
class RepoStatus:
    """ One tracked repository, whether or not it currently has anything
    open — repoCount alone can't name it, and it wouldn't otherwise
    appear anywhere pullRequests/issues don't already mention it.

        Attributes:
            forge (Forge):
            full_name (str):
            url (str): The repo's own page on its forge, for linking out.
            ignored (bool): Whether the signed-in user has ignored this repo in either
                scope below (#363, #511) — true whenever ignoredPRs or
                ignoredIssues is true. The repo itself still appears here
                with accurate hasWebhook/canManageWebhooks regardless.
            ignored_p_rs (bool): Whether the signed-in user has ignored this repo's pull
                requests specifically (#511) — its pullRequests entries are
                excluded from this same response and from Insights.
            ignored_issues (bool): Whether the signed-in user has ignored this repo's issues
                specifically (#511) — its issues entries are excluded from
                this same response and from Insights.
            has_webhook (bool): Whether this app has ever recorded a signature-verified
                webhook delivery for this repo. Passive: it reflects a real
                delivery having arrived, not whether a webhook object exists
                on the forge — a correctly configured webhook that just
                hasn't fired yet still reads false here, the same as a
                misconfigured one would.
            can_manage_webhooks (bool): Whether the signed-in user's own permission on this repo is
                enough to list/create its webhooks — GitHub requires admin
                specifically (write/maintain can push but still 404 on the
                hooks endpoint, by GitHub's own design); Forgejo's equivalent
                is its own admin permission flag. Always false for a repo
                reached through an unauthenticated, username-only listing.
                A point-in-time snapshot: a permission change since the last
                refresh can still make a following ensure-webhook call fail
                despite this having said true.
            auto_update_branch (bool): Whether the signed-in user has turned on automatic branch
                updates for this repo (#365) — any of its pull requests the
                background refresh finds behind its base branch gets updated
                the same way a manual "Update branch" click would. A
                Dependabot pull request gets its own rebase comment instead,
                and a Renovate one its own rebase label, mirroring their
                manual action buttons. A release-please pull request is
                always skipped: it regenerates its own branch and changelog
                on every push to the base branch, and has no dedicated
                rebase/label action the way Dependabot and Renovate do.
     """

    forge: Forge
    full_name: str
    url: str
    ignored: bool
    ignored_p_rs: bool
    ignored_issues: bool
    has_webhook: bool
    can_manage_webhooks: bool
    auto_update_branch: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        forge = self.forge.value

        full_name = self.full_name

        url = self.url

        ignored = self.ignored

        ignored_p_rs = self.ignored_p_rs

        ignored_issues = self.ignored_issues

        has_webhook = self.has_webhook

        can_manage_webhooks = self.can_manage_webhooks

        auto_update_branch = self.auto_update_branch


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "forge": forge,
            "fullName": full_name,
            "url": url,
            "ignored": ignored,
            "ignoredPRs": ignored_p_rs,
            "ignoredIssues": ignored_issues,
            "hasWebhook": has_webhook,
            "canManageWebhooks": can_manage_webhooks,
            "autoUpdateBranch": auto_update_branch,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forge = Forge(d.pop("forge"))




        full_name = d.pop("fullName")

        url = d.pop("url")

        ignored = d.pop("ignored")

        ignored_p_rs = d.pop("ignoredPRs")

        ignored_issues = d.pop("ignoredIssues")

        has_webhook = d.pop("hasWebhook")

        can_manage_webhooks = d.pop("canManageWebhooks")

        auto_update_branch = d.pop("autoUpdateBranch")

        repo_status = cls(
            forge=forge,
            full_name=full_name,
            url=url,
            ignored=ignored,
            ignored_p_rs=ignored_p_rs,
            ignored_issues=ignored_issues,
            has_webhook=has_webhook,
            can_manage_webhooks=can_manage_webhooks,
            auto_update_branch=auto_update_branch,
        )


        repo_status.additional_properties = d
        return repo_status

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
