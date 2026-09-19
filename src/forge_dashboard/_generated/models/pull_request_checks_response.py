from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.check import Check





T = TypeVar("T", bound="PullRequestChecksResponse")



@_attrs_define
class PullRequestChecksResponse:
    """ 
        Attributes:
            checks (list[Check]):
     """

    checks: list[Check]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.check import Check # noqa: PLC0415
        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()
            checks.append(checks_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "checks": checks,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check import Check # noqa: PLC0415
        d = dict(src_dict)
        checks = []
        _checks = d.pop("checks")
        for checks_item_data in (_checks):
            checks_item = Check.from_dict(checks_item_data)



            checks.append(checks_item)


        pull_request_checks_response = cls(
            checks=checks,
        )


        pull_request_checks_response.additional_properties = d
        return pull_request_checks_response

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
