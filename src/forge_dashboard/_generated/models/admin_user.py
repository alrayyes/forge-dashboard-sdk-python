from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="AdminUser")



@_attrs_define
class AdminUser:
    """ 
        Attributes:
            username (str):
            display_name (str):
            is_admin (bool):
            created_at (datetime.datetime):
     """

    username: str
    display_name: str
    is_admin: bool
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        username = self.username

        display_name = self.display_name

        is_admin = self.is_admin

        created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "username": username,
            "displayName": display_name,
            "isAdmin": is_admin,
            "createdAt": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        display_name = d.pop("displayName")

        is_admin = d.pop("isAdmin")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))




        admin_user = cls(
            username=username,
            display_name=display_name,
            is_admin=is_admin,
            created_at=created_at,
        )


        admin_user.additional_properties = d
        return admin_user

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
