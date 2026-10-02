from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.check_state import CheckState
from ..types import UNSET, Unset






T = TypeVar("T", bound="Check")



@_attrs_define
class Check:
    """ One job/check run against a pull request's head commit.

        Attributes:
            name (str):
            state (CheckState): One job/check's own status — the per-job detail CIStatus
                deliberately doesn't carry, since CIStatus is the combined result
                across every one of them.
            url (str): That job's own page on the forge that ran it — never the pull request's own page.
            required (bool | Unset): Whether the base branch's protection makes this check block the
                merge (GitHub required status checks and rulesets, Forgejo
                `status_check_contexts`). Absent when the forge can't tell — a
                token that can't read protection, or a check that can't be
                mapped to a protection entry. Absent is not the same as false.
     """

    name: str
    state: CheckState
    url: str
    required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        state = self.state.value

        url = self.url

        required = self.required


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "state": state,
            "url": url,
        })
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        state = CheckState(d.pop("state"))




        url = d.pop("url")

        required = d.pop("required", UNSET)

        check = cls(
            name=name,
            state=state,
            url=url,
            required=required,
        )


        check.additional_properties = d
        return check

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
