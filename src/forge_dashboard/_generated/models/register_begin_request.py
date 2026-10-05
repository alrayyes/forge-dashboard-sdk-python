from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RegisterBeginRequest")



@_attrs_define
class RegisterBeginRequest:
    """ 
        Attributes:
            username (str): Surrounding whitespace is trimmed by the server, and what is
                left must not be empty. Clients may check the same pattern for
                quick feedback; the server decides.
            display_name (str): Ignored once an invite is required (any account already
                exists) — the invite's own displayName (set by the admin who
                issued it) is what's actually used. Only the very first,
                bootstrap registration on a fresh instance takes this value.
            invite_token (str | Unset): Required once any account already exists (see GET
                /api/auth/registration-status) — a single-use token from POST
                /api/admin/invites, issued for exactly this username. Omitted
                or ignored for the very first, bootstrap registration.
     """

    username: str
    display_name: str
    invite_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        username = self.username

        display_name = self.display_name

        invite_token = self.invite_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "username": username,
            "displayName": display_name,
        })
        if invite_token is not UNSET:
            field_dict["inviteToken"] = invite_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        display_name = d.pop("displayName")

        invite_token = d.pop("inviteToken", UNSET)

        register_begin_request = cls(
            username=username,
            display_name=display_name,
            invite_token=invite_token,
        )


        register_begin_request.additional_properties = d
        return register_begin_request

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
