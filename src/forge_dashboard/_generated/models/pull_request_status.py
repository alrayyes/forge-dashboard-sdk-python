from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PullRequestStatus")



@_attrs_define
class PullRequestStatus:
    """ Why a pull request is waiting on something or can't be merged, in one
    place for a client to show. Same shape as
    `AllowedAction.blocked`.

        Attributes:
            code (str): The same codes as `AllowedAction.blocked.code`. The server may
                learn more, so a client should show `message` for a code it
                doesn't know. Declared with `x-extensible-enum`.
            message (str): Plain words, safe to show a person.
            next_ (str | Unset): What unlocks it or what to do about it, when there is something.
     """

    code: str
    message: str
    next_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        next_ = self.next_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "message": message,
        })
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        next_ = d.pop("next", UNSET)

        pull_request_status = cls(
            code=code,
            message=message,
            next_=next_,
        )


        pull_request_status.additional_properties = d
        return pull_request_status

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
