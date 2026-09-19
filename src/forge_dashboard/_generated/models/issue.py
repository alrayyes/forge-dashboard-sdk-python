from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.forge import Forge
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.label import Label





T = TypeVar("T", bound="Issue")



@_attrs_define
class Issue:
    """ 
        Attributes:
            forge (Forge):
            repo (str):
            number (int):
            title (str):
            url (str): The real issue URL on its own forge.
            author (str):
            labels (list[Label]):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
     """

    forge: Forge
    repo: str
    number: int
    title: str
    url: str
    author: str
    labels: list[Label]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.label import Label # noqa: PLC0415
        forge = self.forge.value

        repo = self.repo

        number = self.number

        title = self.title

        url = self.url

        author = self.author

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)



        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "forge": forge,
            "repo": repo,
            "number": number,
            "title": title,
            "url": url,
            "author": author,
            "labels": labels,
            "createdAt": created_at,
            "updatedAt": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label import Label # noqa: PLC0415
        d = dict(src_dict)
        forge = Forge(d.pop("forge"))




        repo = d.pop("repo")

        number = d.pop("number")

        title = d.pop("title")

        url = d.pop("url")

        author = d.pop("author")

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in (_labels):
            labels_item = Label.from_dict(labels_item_data)



            labels.append(labels_item)


        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))




        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))




        issue = cls(
            forge=forge,
            repo=repo,
            number=number,
            title=title,
            url=url,
            author=author,
            labels=labels,
            created_at=created_at,
            updated_at=updated_at,
        )


        issue.additional_properties = d
        return issue

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
