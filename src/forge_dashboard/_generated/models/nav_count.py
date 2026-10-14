from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="NavCount")



@_attrs_define
class NavCount:
    """ The Branches page's numbers (#1458): how many default branches it
    lists and how many of those have a pipeline running, failed and
    passed, the same four as `NavPullRequestCount`. A branch with no
    pipeline counts in `total` only, so the four numbers need not add up.
    All four are always present.

        Attributes:
            total (int): How many default branches the page lists.
            running (int): How many of them have a pipeline that is still running.
            failed (int): How many of them have a failing pipeline.
            passed (int): How many of them have a pipeline that passed.
     """

    total: int
    running: int
    failed: int
    passed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total = self.total

        running = self.running

        failed = self.failed

        passed = self.passed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total": total,
            "running": running,
            "failed": failed,
            "passed": passed,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        running = d.pop("running")

        failed = d.pop("failed")

        passed = d.pop("passed")

        nav_count = cls(
            total=total,
            running=running,
            failed=failed,
            passed=passed,
        )


        nav_count.additional_properties = d
        return nav_count

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
