from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.settings_response_theme import SettingsResponseTheme






T = TypeVar("T", bound="SettingsResponse")



@_attrs_define
class SettingsResponse:
    """ The signed-in user's own GitHub/Forgejo configuration. Never
    includes a forge token's value — only whether one is currently
    saved, so the UI can show a "Configured" badge without the secret
    ever reaching the browser. webhookToken/webhookSecret are the
    exception: they're ours to hand back in the clear, since the user
    has to paste them into the forge's own webhook setup.

        Attributes:
            github_username (str): Used as a token-free public-repos fallback when no GitHub token is set.
            github_token_set (bool): Whether a GitHub token is currently saved.
            forgejo_url (str):
            forgejo_username (str): Used as a token-free public-repos fallback when no Forgejo token is set.
            forgejo_token_set (bool): Whether a Forgejo token is currently saved.
            webhook_token (str): Identifies this user in a webhook URL
                (`/api/webhooks/{provider}/{webhookToken}`). Generated on
                first visit to Settings and stable after that.
            webhook_secret (str): Pasted into the forge's own webhook "Secret" field, used to
                verify the signature header on incoming webhook deliveries
                (`X-Hub-Signature-256` on GitHub, `X-Forgejo-Signature` on
                Forgejo). Never appears in the webhook URL itself.
            renovate_rebase_label (str): The label Renovate's own rebase/retry trigger listens for on
                a repo (Renovate's own `rebaseLabel` config option — genuinely
                per-repo configurable, so this is a user-set override rather
                than a hardcoded constant). Empty means Renovate's own
                documented default, `rebase`.
            theme (SettingsResponseTheme): The signed-in user's own theme preference (#352). Empty
                means "system" — follow the browser's prefers-color-scheme
                rather than a saved choice. Set only from Settings; every
                other page reads it via the lightweight
                GET /api/settings/theme instead of this endpoint.
     """

    github_username: str
    github_token_set: bool
    forgejo_url: str
    forgejo_username: str
    forgejo_token_set: bool
    webhook_token: str
    webhook_secret: str
    renovate_rebase_label: str
    theme: SettingsResponseTheme
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        github_username = self.github_username

        github_token_set = self.github_token_set

        forgejo_url = self.forgejo_url

        forgejo_username = self.forgejo_username

        forgejo_token_set = self.forgejo_token_set

        webhook_token = self.webhook_token

        webhook_secret = self.webhook_secret

        renovate_rebase_label = self.renovate_rebase_label

        theme = self.theme.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "githubUsername": github_username,
            "githubTokenSet": github_token_set,
            "forgejoUrl": forgejo_url,
            "forgejoUsername": forgejo_username,
            "forgejoTokenSet": forgejo_token_set,
            "webhookToken": webhook_token,
            "webhookSecret": webhook_secret,
            "renovateRebaseLabel": renovate_rebase_label,
            "theme": theme,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        github_username = d.pop("githubUsername")

        github_token_set = d.pop("githubTokenSet")

        forgejo_url = d.pop("forgejoUrl")

        forgejo_username = d.pop("forgejoUsername")

        forgejo_token_set = d.pop("forgejoTokenSet")

        webhook_token = d.pop("webhookToken")

        webhook_secret = d.pop("webhookSecret")

        renovate_rebase_label = d.pop("renovateRebaseLabel")

        theme = SettingsResponseTheme(d.pop("theme"))




        settings_response = cls(
            github_username=github_username,
            github_token_set=github_token_set,
            forgejo_url=forgejo_url,
            forgejo_username=forgejo_username,
            forgejo_token_set=forgejo_token_set,
            webhook_token=webhook_token,
            webhook_secret=webhook_secret,
            renovate_rebase_label=renovate_rebase_label,
            theme=theme,
        )


        settings_response.additional_properties = d
        return settings_response

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
