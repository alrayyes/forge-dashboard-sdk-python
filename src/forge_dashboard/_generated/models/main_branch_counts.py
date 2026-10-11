from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="MainBranchCounts")



@_attrs_define
class MainBranchCounts:
    """ How many rows are in each status, the numbers on the filter pills.
    `total` is every row, so it equals the sum of the other four.

        Attributes:
            failed (int):
            passed (int):
            running (int):
            none (int):
            total (int):
     """

    failed: int
    passed: int
    running: int
    none: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        failed = self.failed

        passed = self.passed

        running = self.running

        none = self.none

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "failed": failed,
            "passed": passed,
            "running": running,
            "none": none,
            "total": total,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed = d.pop("failed")

        passed = d.pop("passed")

        running = d.pop("running")

        none = d.pop("none")

        total = d.pop("total")

        main_branch_counts = cls(
            failed=failed,
            passed=passed,
            running=running,
            none=none,
            total=total,
        )


        main_branch_counts.additional_properties = d
        return main_branch_counts

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
