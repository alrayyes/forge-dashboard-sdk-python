from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="AdminInvite")



@_attrs_define
class AdminInvite:
    """ An outstanding (unconsumed, unexpired) invite's own metadata —
    never the raw token, which only AdminInviteCreateResponse ever
    carries, once, at creation time.

        Attributes:
            id (str): The invite's own stable identifier — pass this back to POST
                /api/admin/invites/{token}/revoke, not the raw token an
                invitee registers with.
            username (str):
            display_name (str):
            expires_at (datetime.datetime):
     """

    id: str
    username: str
    display_name: str
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        username = self.username

        display_name = self.display_name

        expires_at = self.expires_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "username": username,
            "displayName": display_name,
            "expiresAt": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        username = d.pop("username")

        display_name = d.pop("displayName")

        expires_at = datetime.datetime.fromisoformat(d.pop("expiresAt"))




        admin_invite = cls(
            id=id,
            username=username,
            display_name=display_name,
            expires_at=expires_at,
        )


        admin_invite.additional_properties = d
        return admin_invite

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
