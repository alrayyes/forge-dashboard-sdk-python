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





T = TypeVar("T", bound="RunEvent")



@_attrs_define
class RunEvent:
    """ The `data` of a `run` event on the dashboard stream: the jobs of
    one workflow run attempt of one subject, or one check that belongs
    to no run. A later event with the same `key` replaces the earlier
    one. An event with no `key` and no `checks` says the subject has
    none. An event with `error` set stands in for the whole listing.

        Attributes:
            kind (CheckSubjectKind):
            forge (str):
            full_name (str): The repository, as `owner/repo`.
            number (int | Unset): The pull request number. Required for `pull_request`.
            key (str | Unset): Names the unit this event replaces: `run/<runId>/<attempt>`
                for a run attempt, `job/<url>|<name>` for a check with no
                run. Absent when the subject has no checks or on an error.
            run_id (int | Unset): Absent for a check with no run.
            run_attempt (int | Unset): Absent when the check has no run or the forge doesn't
                number attempts.
            checks (list[Check] | Unset): Absent when `gone` or `error` is set.
            gone (bool | Unset): The unit named by `key` is no longer listed; drop it.
            final (bool | Unset): Set on the last event of a listing, so a client can draw
                once the whole listing has arrived.
            error (str | Unset):
     """

    kind: CheckSubjectKind
    forge: str
    full_name: str
    number: int | Unset = UNSET
    key: str | Unset = UNSET
    run_id: int | Unset = UNSET
    run_attempt: int | Unset = UNSET
    checks: list[Check] | Unset = UNSET
    gone: bool | Unset = UNSET
    final: bool | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.check import Check # noqa: PLC0415
        kind = self.kind.value

        forge = self.forge

        full_name = self.full_name

        number = self.number

        key = self.key

        run_id = self.run_id

        run_attempt = self.run_attempt

        checks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.checks, Unset):
            checks = []
            for checks_item_data in self.checks:
                checks_item = checks_item_data.to_dict()
                checks.append(checks_item)



        gone = self.gone

        final = self.final

        error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
            "forge": forge,
            "fullName": full_name,
        })
        if number is not UNSET:
            field_dict["number"] = number
        if key is not UNSET:
            field_dict["key"] = key
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if run_attempt is not UNSET:
            field_dict["runAttempt"] = run_attempt
        if checks is not UNSET:
            field_dict["checks"] = checks
        if gone is not UNSET:
            field_dict["gone"] = gone
        if final is not UNSET:
            field_dict["final"] = final
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

        number = d.pop("number", UNSET)

        key = d.pop("key", UNSET)

        run_id = d.pop("runId", UNSET)

        run_attempt = d.pop("runAttempt", UNSET)

        _checks = d.pop("checks", UNSET)
        checks: list[Check] | Unset = UNSET
        if _checks is not UNSET:
            checks = []
            for checks_item_data in _checks:
                checks_item = Check.from_dict(checks_item_data)



                checks.append(checks_item)


        gone = d.pop("gone", UNSET)

        final = d.pop("final", UNSET)

        error = d.pop("error", UNSET)

        run_event = cls(
            kind=kind,
            forge=forge,
            full_name=full_name,
            number=number,
            key=key,
            run_id=run_id,
            run_attempt=run_attempt,
            checks=checks,
            gone=gone,
            final=final,
            error=error,
        )


        run_event.additional_properties = d
        return run_event

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
