from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.shared_user import SharedUser





T = TypeVar("T", bound="SharingResponse")



@_attrs_define
class SharingResponse:
    """ 
        Attributes:
            shared_with (list[SharedUser]): Users the signed-in user has shared their own dashboard with.
            shared_with_me (list[SharedUser]): Users who have shared their dashboard with the signed-in user.
     """

    shared_with: list[SharedUser]
    shared_with_me: list[SharedUser]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.shared_user import SharedUser # noqa: PLC0415
        shared_with = []
        for shared_with_item_data in self.shared_with:
            shared_with_item = shared_with_item_data.to_dict()
            shared_with.append(shared_with_item)



        shared_with_me = []
        for shared_with_me_item_data in self.shared_with_me:
            shared_with_me_item = shared_with_me_item_data.to_dict()
            shared_with_me.append(shared_with_me_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sharedWith": shared_with,
            "sharedWithMe": shared_with_me,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shared_user import SharedUser # noqa: PLC0415
        d = dict(src_dict)
        shared_with = []
        _shared_with = d.pop("sharedWith")
        for shared_with_item_data in (_shared_with):
            shared_with_item = SharedUser.from_dict(shared_with_item_data)



            shared_with.append(shared_with_item)


        shared_with_me = []
        _shared_with_me = d.pop("sharedWithMe")
        for shared_with_me_item_data in (_shared_with_me):
            shared_with_me_item = SharedUser.from_dict(shared_with_me_item_data)



            shared_with_me.append(shared_with_me_item)


        sharing_response = cls(
            shared_with=shared_with,
            shared_with_me=shared_with_me,
        )


        sharing_response.additional_properties = d
        return sharing_response

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
