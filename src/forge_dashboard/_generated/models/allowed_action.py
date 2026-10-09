from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.allowed_action_blocked import AllowedActionBlocked





T = TypeVar("T", bound="AllowedAction")



@_attrs_define
class AllowedAction:
    """ 
        Attributes:
            action (str): One of the values below today, and the server may learn more.
                A client should treat a value it doesn't know as an action it
                can't offer, not as an error. Declared with `x-extensible-enum`
                so adding a value is a minor SDK release.
            blocked (AllowedActionBlocked | Unset): Present when the action is offered but can't be taken yet. Merge
                is never hidden for an open pull request, only blocked.
     """

    action: str
    blocked: AllowedActionBlocked | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.allowed_action_blocked import AllowedActionBlocked # noqa: PLC0415
        action = self.action

        blocked: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blocked, Unset):
            blocked = self.blocked.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
        })
        if blocked is not UNSET:
            field_dict["blocked"] = blocked

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowed_action_blocked import AllowedActionBlocked # noqa: PLC0415
        d = dict(src_dict)
        action = d.pop("action")

        _blocked = d.pop("blocked", UNSET)
        blocked: AllowedActionBlocked | Unset
        if isinstance(_blocked,  Unset):
            blocked = UNSET
        else:
            blocked = AllowedActionBlocked.from_dict(_blocked)




        allowed_action = cls(
            action=action,
            blocked=blocked,
        )


        allowed_action.additional_properties = d
        return allowed_action

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
