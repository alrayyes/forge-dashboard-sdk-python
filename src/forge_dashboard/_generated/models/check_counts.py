from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CheckCounts")



@_attrs_define
class CheckCounts:
    """ How many of a pull request's checks are in each state, so a client can
    say how far a pipeline is without opening it. The server tallies
    them from what it already reads to work out `ci`, so they cost no
    request. Always present, all zero when there are no checks.

    `waiting` is a check that has not started: queued, or pending where the
    forge doesn't tell queued from running. The counts agree with `ci`: a
    pull request whose `ci` is `pending` has `failed` at 0, and one whose
    `ci` is `success` has nothing running, waiting or failed. Two kinds of
    run are therefore in none of the four. A run held for approval:
    `awaitingWorkflowApproval` says that. A cancelled run: a push or a
    concurrency group superseded it, and the overall state does not read it
    as a failure while others still run. A timed-out or stale check counts
    as `failed`, a skipped, neutral or bare completed one as `passed`.

    On GitHub the counts come from the same rollup as `ci`; on Forgejo from
    the statuses of the combined commit status, where nothing is ever
    `running`. Forgejo answers one page of those statuses, and when its
    total says there are more than the page holds the counts are all zero
    rather than an undercount. When GitHub's rollup is of an earlier
    commit than the head (a push still being processed), the counts are
    zero too. GitHub's unauthenticated fallback has no such counts, so
    there they are all zero.

        Attributes:
            passed (int):
            running (int):
            waiting (int):
            failed (int):
     """

    passed: int
    running: int
    waiting: int
    failed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        passed = self.passed

        running = self.running

        waiting = self.waiting

        failed = self.failed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "passed": passed,
            "running": running,
            "waiting": waiting,
            "failed": failed,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        passed = d.pop("passed")

        running = d.pop("running")

        waiting = d.pop("waiting")

        failed = d.pop("failed")

        check_counts = cls(
            passed=passed,
            running=running,
            waiting=waiting,
            failed=failed,
        )


        check_counts.additional_properties = d
        return check_counts

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
