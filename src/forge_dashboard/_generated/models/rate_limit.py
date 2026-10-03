from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rate_limit_severity import RateLimitSeverity
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="RateLimit")



@_attrs_define
class RateLimit:
    """ One of a forge API's own request budgets for the credential the last refresh used — see
    ForgeHealth.rateLimitGraphQL/rateLimitREST for which budget this is and when each is (or isn't) reported.

        Attributes:
            limit (int): Requests allowed per window.
            remaining (int): Requests left in the current window.
            resets_at (datetime.datetime): When the window resets and remaining goes back to limit.
            severity (RateLimitSeverity): How worried a client should be about this budget, graded by
                the server as of the response, so no client needs its own
                threshold or clock check. `exceeded`: nothing left and the
                reset hasn't been seen to pass. `low`: under 5% left (also a
                spent budget whose reset time has passed, until the next
                snapshot says otherwise). `ok`: everything else.
            cost (int | Unset): The point price the most recent call was actually charged — GraphQL-specific, since a REST
                request has no separate cost concept beyond the flat one-request-one-point REST's own budget already counts.
                Omitted for a REST-sourced RateLimit.
     """

    limit: int
    remaining: int
    resets_at: datetime.datetime
    severity: RateLimitSeverity
    cost: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        remaining = self.remaining

        resets_at = self.resets_at.isoformat()

        severity = self.severity.value

        cost = self.cost


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "limit": limit,
            "remaining": remaining,
            "resetsAt": resets_at,
            "severity": severity,
        })
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        remaining = d.pop("remaining")

        resets_at = datetime.datetime.fromisoformat(d.pop("resetsAt"))




        severity = RateLimitSeverity(d.pop("severity"))




        cost = d.pop("cost", UNSET)

        rate_limit = cls(
            limit=limit,
            remaining=remaining,
            resets_at=resets_at,
            severity=severity,
            cost=cost,
        )


        rate_limit.additional_properties = d
        return rate_limit

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
