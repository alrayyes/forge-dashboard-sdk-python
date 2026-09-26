from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SettingsRequest")



@_attrs_define
class SettingsRequest:
    """ Replaces the signed-in user's saved GitHub/Forgejo configuration.
    A blank `githubToken` or `forgejoToken` keeps whatever token is
    already saved for that forge rather than clearing it — this is
    the only way to update the username fields without having to
    resubmit a token you don't want to re-paste. Theme isn't
    settable here at all — see PUT /api/settings/theme.

        Attributes:
            github_token (str | Unset):
            github_username (str | Unset):
            forgejo_url (str | Unset):
            forgejo_token (str | Unset):
            forgejo_username (str | Unset):
            renovate_rebase_label (str | Unset):
     """

    github_token: str | Unset = UNSET
    github_username: str | Unset = UNSET
    forgejo_url: str | Unset = UNSET
    forgejo_token: str | Unset = UNSET
    forgejo_username: str | Unset = UNSET
    renovate_rebase_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        github_token = self.github_token

        github_username = self.github_username

        forgejo_url = self.forgejo_url

        forgejo_token = self.forgejo_token

        forgejo_username = self.forgejo_username

        renovate_rebase_label = self.renovate_rebase_label


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if github_token is not UNSET:
            field_dict["githubToken"] = github_token
        if github_username is not UNSET:
            field_dict["githubUsername"] = github_username
        if forgejo_url is not UNSET:
            field_dict["forgejoUrl"] = forgejo_url
        if forgejo_token is not UNSET:
            field_dict["forgejoToken"] = forgejo_token
        if forgejo_username is not UNSET:
            field_dict["forgejoUsername"] = forgejo_username
        if renovate_rebase_label is not UNSET:
            field_dict["renovateRebaseLabel"] = renovate_rebase_label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        github_token = d.pop("githubToken", UNSET)

        github_username = d.pop("githubUsername", UNSET)

        forgejo_url = d.pop("forgejoUrl", UNSET)

        forgejo_token = d.pop("forgejoToken", UNSET)

        forgejo_username = d.pop("forgejoUsername", UNSET)

        renovate_rebase_label = d.pop("renovateRebaseLabel", UNSET)

        settings_request = cls(
            github_token=github_token,
            github_username=github_username,
            forgejo_url=forgejo_url,
            forgejo_token=forgejo_token,
            forgejo_username=forgejo_username,
            renovate_rebase_label=renovate_rebase_label,
        )


        settings_request.additional_properties = d
        return settings_request

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
