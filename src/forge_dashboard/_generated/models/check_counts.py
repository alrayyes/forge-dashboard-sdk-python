from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CheckCounts")



@_attrs_define
class CheckCounts:
    """ How many checks are in each state, so a client can say how far a
    pipeline is without opening it. It is on every pull request and on
    every default branch, for a passed, a failed and a running pipeline
    alike. The server tallies them from what it already reads to work out
    the overall state, so they cost no request. Always present, all zero
    when there are no checks.

    `waiting` is a check that has not started: queued, or pending where the
    forge doesn't tell queued from running. A failed pipeline can still have
    checks running or waiting, and says so. A pull request's counts agree
    with its `ci`: one whose `ci` is `pending` has `failed` at 0, and one
    whose `ci` is `success` has nothing running, waiting or failed. On a
    pull request two kinds of run are therefore in none of the four, as
    long as something else explains the state. A run held for approval:
    `awaitingWorkflowApproval` says that. A cancelled run: a push or a
    concurrency group superseded it, and the overall state does not read it
    as a failure while others still run. A pull request whose `ci` is
    `cancelled` counts its cancelled runs in `cancelled`. A default branch
    counts every job its pipeline lists, so its cancelled jobs are in
    `cancelled` and its held runs in `held`, never in `failed`: a failed
    branch can have a `failed` of 0 when a held or cancelled run is what
    failed it. A timed-out or stale check counts as `failed`, a skipped,
    neutral or bare completed one as `passed`, on Forgejo too.

    `unknown` is how many checks are in a state the server cannot grade: a
    status or conclusion the forge added after the server was written. It
    is none of the others, so a check nobody can name is not hidden in a
    count that means something. A pull request or branch whose only odd
    check is unknown is neither failing nor passing: a branch that would
    read `passed` reads `running` while one is present. The server always
    sends it; a client that may talk to an older server reads a missing
    one as zero.

    `skipped` is a newer field and says how many of the `passed` checks
    were skipped. It never exceeds `passed`: it is inside `passed`, not
    beside it, so `passed` still counts every check that needs nothing more
    and the counts still add up to the checks the pipeline lists on a default
    branch (on a pull request, bar its cancelled and held runs). The
    server always sends it, which is why it is required; a client that may
    talk to an older server may read a missing one as zero. A neutral or bare
    completed check is passed without being skipped. A client that draws the
    two side by side must subtract `skipped` from `passed` for the passed figure, or a skipped check is
    counted twice, and a pipeline where every passed check was skipped can
    read as skipped.

    On GitHub the counts come from the same rollup as the overall state,
    for a pull request and a branch alike; on Forgejo a pull request counts
    the statuses of the combined commit status, which only say pending, and
    takes the running ones out of the pending count by reading the jobs of
    the commit's runs that are still going. When a run has failed, a
    pending status of a job in a run that has failed is no wait: its
    needs failed, so Forgejo leaves it blocked and nothing will start it,
    and it is in none of the four. A default branch counts it as `cancelled`: it
    counts the jobs of the workflow runs of the newest commit that has one,
    where a running job is `running`, a queued one `waiting`, and a blocked
    one `waiting` unless its run has failed. A run
    whose jobs can't be read counts as one check by its own status. Forgejo
    answers one page of those statuses, and when its total says there are
    more than the page holds a pull request's counts are all zero rather
    than an undercount. When GitHub's rollup of a pull request is of an
    earlier commit than the head (a push still being processed), the counts
    are zero too. GitHub's unauthenticated fallback has no such counts, so
    there they are all zero.

        Attributes:
            passed (int):
            running (int):
            waiting (int):
            failed (int):
            skipped (int):
            unknown (int):
            cancelled (int | Unset): On a pull request, absent unless its `ci` is `cancelled`, then how
                many runs were cancelled. On a default branch, always how many
                jobs were cancelled, so its counts add up to the jobs the pipeline
                lists. A newer field, so a client treats a missing one as 0.
            held (int | Unset): On a default branch, how many runs are held for approval, so its
                counts add up. A pull request never sets it: it says so with
                `awaitingWorkflowApproval`. A newer field, so a client treats a
                missing one as 0.
     """

    passed: int
    running: int
    waiting: int
    failed: int
    skipped: int
    unknown: int
    cancelled: int | Unset = UNSET
    held: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        passed = self.passed

        running = self.running

        waiting = self.waiting

        failed = self.failed

        skipped = self.skipped

        unknown = self.unknown

        cancelled = self.cancelled

        held = self.held


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "passed": passed,
            "running": running,
            "waiting": waiting,
            "failed": failed,
            "skipped": skipped,
            "unknown": unknown,
        })
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if held is not UNSET:
            field_dict["held"] = held

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        passed = d.pop("passed")

        running = d.pop("running")

        waiting = d.pop("waiting")

        failed = d.pop("failed")

        skipped = d.pop("skipped")

        unknown = d.pop("unknown")

        cancelled = d.pop("cancelled", UNSET)

        held = d.pop("held", UNSET)

        check_counts = cls(
            passed=passed,
            running=running,
            waiting=waiting,
            failed=failed,
            skipped=skipped,
            unknown=unknown,
            cancelled=cancelled,
            held=held,
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
