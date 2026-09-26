from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="AdminInviteCreateResponse")



@_attrs_define
class AdminInviteCreateResponse:
    """ The one and only response that ever carries the raw invite token
    — shown to the admin once, at creation time, for them to copy
    into a `/login?invite=<token>` link and hand to the invitee out
    of band. Only its hash is stored, so it can't be recovered from
    here again.

        Attributes:
            token (str):
            username (str):
            display_name (str):
            expires_at (datetime.datetime):
     """

    token: str
    username: str
    display_name: str
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        token = self.token

        username = self.username

        display_name = self.display_name

        expires_at = self.expires_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "token": token,
            "username": username,
            "displayName": display_name,
            "expiresAt": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        username = d.pop("username")

        display_name = d.pop("displayName")

        expires_at = datetime.datetime.fromisoformat(d.pop("expiresAt"))




        admin_invite_create_response = cls(
            token=token,
            username=username,
            display_name=display_name,
            expires_at=expires_at,
        )


        admin_invite_create_response.additional_properties = d
        return admin_invite_create_response

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
