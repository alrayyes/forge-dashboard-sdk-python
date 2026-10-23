from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.check_state import CheckState
from ..types import UNSET, Unset






T = TypeVar("T", bound="Check")



@_attrs_define
class Check:
    """ One job/check run against a pull request's head commit.

        Attributes:
            name (str):
            state (CheckState): One job/check's own status — the per-job detail CIStatus
                deliberately doesn't carry, since CIStatus is the combined result
                across every one of them.

                "awaiting_approval" is a GitHub workflow run held until a
                maintainer approves it. It has no jobs yet, so it is not queued and
                not failed; its `url` is the run's page, where the approve button is.
            url (str): That job's own page on the forge that ran it — never the pull request's own page.
            job_id (int | Unset): The Actions job (or check run) id to pass to GET /api/checks/log.
                Absent for a legacy commit status and for a workflow held for
                approval, which have no output to read.
            required (bool | Unset): Whether the base branch's protection makes this check block the
                merge (GitHub required status checks and rulesets, Forgejo
                `status_check_contexts`). Absent when the forge can't tell — a
                token that can't read protection, or a check that can't be
                mapped to a protection entry. Absent is not the same as false.
            duration_seconds (int | Unset): How long a completed check ran. Absent while it runs, or when
                the forge doesn't say. GitHub only: Forgejo's API doesn't give
                a job's timing.
            run_attempt (int | Unset): Which attempt of its workflow run the job belongs to. Forgejo
                only: it keeps a job's id and page when a run is retried, so this
                is what tells a retry's output from the first attempt's. Absent
                when the forge doesn't number attempts.
            failed_step (str | Unset): The name of the step of a failed job that broke. Absent when
                the check isn't a job the token can read (a third-party check,
                a forge with no step data, a token without access).
            excerpt (str | Unset): The tail of the failed job's log as plain text: the last lines,
                with per-line timestamps and colour codes removed, at most 2,000
                characters. Never markup, and a client must render it as text.
                Whatever the forge already masks stays masked. Absent when the
                log can't be read or has expired. GitHub fills it for at most
                the first five failed jobs of a list, in the list's order.
                Forgejo never fills it in a list, since that would read a log
                while the list is built: ask for it through
                GET /api/checks/log with `excerpt=true`. The whole output is read
                through GET /api/checks/log.
     """

    name: str
    state: CheckState
    url: str
    job_id: int | Unset = UNSET
    required: bool | Unset = UNSET
    duration_seconds: int | Unset = UNSET
    run_attempt: int | Unset = UNSET
    failed_step: str | Unset = UNSET
    excerpt: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        state = self.state.value

        url = self.url

        job_id = self.job_id

        required = self.required

        duration_seconds = self.duration_seconds

        run_attempt = self.run_attempt

        failed_step = self.failed_step

        excerpt = self.excerpt


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "state": state,
            "url": url,
        })
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if required is not UNSET:
            field_dict["required"] = required
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if run_attempt is not UNSET:
            field_dict["runAttempt"] = run_attempt
        if failed_step is not UNSET:
            field_dict["failedStep"] = failed_step
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        state = CheckState(d.pop("state"))




        url = d.pop("url")

        job_id = d.pop("jobId", UNSET)

        required = d.pop("required", UNSET)

        duration_seconds = d.pop("durationSeconds", UNSET)

        run_attempt = d.pop("runAttempt", UNSET)

        failed_step = d.pop("failedStep", UNSET)

        excerpt = d.pop("excerpt", UNSET)

        check = cls(
            name=name,
            state=state,
            url=url,
            job_id=job_id,
            required=required,
            duration_seconds=duration_seconds,
            run_attempt=run_attempt,
            failed_step=failed_step,
            excerpt=excerpt,
        )


        check.additional_properties = d
        return check

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
