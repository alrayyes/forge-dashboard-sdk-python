from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.advisory_severity import AdvisorySeverity
from ..models.advisory_state import AdvisoryState
from ..types import UNSET, Unset






T = TypeVar("T", bound="Advisories")



@_attrs_define
class Advisories:
    """ The open dependency advisories on a repository's default branch, read
    from the forge's own source (GitHub's Dependabot alerts). Absent from
    the row when no source reads them for its forge. A source that can't
    answer, such as alerts switched off or a token without the
    `security_events` scope, gives `state` "unknown", never a count of
    zero.

        Attributes:
            state (AdvisoryState): "known" is an answer the forge gave. "unknown" is no answer, and must
                never be shown as zero.
            count (int): How many advisories are open. Only meaningful when `state` is "known".
            highest (AdvisorySeverity | Unset): The worst severity among the open advisories. Absent when there are none.
            url (str | Unset): Where to see the advisories on the forge. Absent when there are none or the state is unknown.
     """

    state: AdvisoryState
    count: int
    highest: AdvisorySeverity | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        count = self.count

        highest: str | Unset = UNSET
        if not isinstance(self.highest, Unset):
            highest = self.highest.value


        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "state": state,
            "count": count,
        })
        if highest is not UNSET:
            field_dict["highest"] = highest
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = AdvisoryState(d.pop("state"))




        count = d.pop("count")

        _highest = d.pop("highest", UNSET)
        highest: AdvisorySeverity | Unset
        if isinstance(_highest,  Unset):
            highest = UNSET
        else:
            highest = AdvisorySeverity(_highest)




        url = d.pop("url", UNSET)

        advisories = cls(
            state=state,
            count=count,
            highest=highest,
            url=url,
        )


        advisories.additional_properties = d
        return advisories

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
