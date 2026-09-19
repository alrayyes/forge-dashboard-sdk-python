from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="BotPrUpdatesResponse")



@_attrs_define
class BotPrUpdatesResponse:
    """ See GET /api/settings/bot-pr-updates's own description.

        Attributes:
            allow_bot_pr_updates (bool):
     """

    allow_bot_pr_updates: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allow_bot_pr_updates = self.allow_bot_pr_updates


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "allowBotPrUpdates": allow_bot_pr_updates,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_bot_pr_updates = d.pop("allowBotPrUpdates")

        bot_pr_updates_response = cls(
            allow_bot_pr_updates=allow_bot_pr_updates,
        )


        bot_pr_updates_response.additional_properties = d
        return bot_pr_updates_response

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
