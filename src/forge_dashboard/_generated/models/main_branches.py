from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.main_branch import MainBranch
  from ..models.main_branch_counts import MainBranchCounts





T = TypeVar("T", bound="MainBranches")



@_attrs_define
class MainBranches:
    """ 
        Attributes:
            generated_at (datetime.datetime): When the snapshot was refreshed, not when it was requested.
            counts (MainBranchCounts): How many rows are in each status, the numbers on the filter pills.
                `total` is every row, so it equals the sum of the other five.
            branches (list[MainBranch]):
     """

    generated_at: datetime.datetime
    counts: MainBranchCounts
    branches: list[MainBranch]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.main_branch import MainBranch # noqa: PLC0415
        from ..models.main_branch_counts import MainBranchCounts # noqa: PLC0415
        generated_at = self.generated_at.isoformat()

        counts = self.counts.to_dict()

        branches = []
        for branches_item_data in self.branches:
            branches_item = branches_item_data.to_dict()
            branches.append(branches_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "generatedAt": generated_at,
            "counts": counts,
            "branches": branches,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.main_branch import MainBranch # noqa: PLC0415
        from ..models.main_branch_counts import MainBranchCounts # noqa: PLC0415
        d = dict(src_dict)
        generated_at = datetime.datetime.fromisoformat(d.pop("generatedAt"))




        counts = MainBranchCounts.from_dict(d.pop("counts"))




        branches = []
        _branches = d.pop("branches")
        for branches_item_data in (_branches):
            branches_item = MainBranch.from_dict(branches_item_data)



            branches.append(branches_item)


        main_branches = cls(
            generated_at=generated_at,
            counts=counts,
            branches=branches,
        )


        main_branches.additional_properties = d
        return main_branches

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
