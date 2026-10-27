from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.check_subject_kind import CheckSubjectKind
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.check import Check





T = TypeVar("T", bound="CheckListEvent")



@_attrs_define
class CheckListEvent:
    """ The `data` of a `checks` event on the dashboard stream: one
    subject and its job list, or why it could not be listed.

        Attributes:
            kind (CheckSubjectKind):
            forge (str):
            full_name (str): The repository, as `owner/repo`.
            checks (list[Check] | None): Null when `error` is set.
            number (int | Unset): The pull request number. Required for `pull_request`.
            error (str | Unset):
     """

    kind: CheckSubjectKind
    forge: str
    full_name: str
    checks: list[Check] | None
    number: int | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.check import Check # noqa: PLC0415
        kind = self.kind.value

        forge = self.forge

        full_name = self.full_name

        checks: list[dict[str, Any]] | None
        if isinstance(self.checks, list):
            checks = []
            for checks_type_0_item_data in self.checks:
                checks_type_0_item = checks_type_0_item_data.to_dict()
                checks.append(checks_type_0_item)


        else:
            checks = self.checks

        number = self.number

        error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
            "forge": forge,
            "fullName": full_name,
            "checks": checks,
        })
        if number is not UNSET:
            field_dict["number"] = number
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check import Check # noqa: PLC0415
        d = dict(src_dict)
        kind = CheckSubjectKind(d.pop("kind"))




        forge = d.pop("forge")

        full_name = d.pop("fullName")

        def _parse_checks(data: object) -> list[Check] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                checks_type_0 = []
                _checks_type_0 = data
                for checks_type_0_item_data in (_checks_type_0):
                    checks_type_0_item = Check.from_dict(checks_type_0_item_data)



                    checks_type_0.append(checks_type_0_item)

                return checks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Check] | None, data)

        checks = _parse_checks(d.pop("checks"))


        number = d.pop("number", UNSET)

        error = d.pop("error", UNSET)

        check_list_event = cls(
            kind=kind,
            forge=forge,
            full_name=full_name,
            checks=checks,
            number=number,
            error=error,
        )


        check_list_event.additional_properties = d
        return check_list_event

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
