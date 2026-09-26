from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.forge import Forge
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.rate_limit import RateLimit





T = TypeVar("T", bound="RequestLogEntry")



@_attrs_define
class RequestLogEntry:
    """ One outbound request `internal/github` or `internal/forgejo`
    made, as persisted by the request_log table.

        Attributes:
            logged_at (datetime.datetime):
            forge (Forge):
            method (str):
            endpoint (str): The request's own path — GraphQL requests all report "/graphql".
            outcome (str): "success", or the `ForgeErrorKind` the failure was classified as.
            account (str | Unset): The display username of the account whose credential made
                this request, or omitted when the request was made with no
                per-account credential, or when that account has since been
                deleted.
            status_code (int | Unset): Omitted when the request never got a response at all.
            rate_limit (RateLimit | Unset): One of a forge API's own request budgets for the credential the last refresh
                used — see ForgeHealth.rateLimitGraphQL/rateLimitREST for which budget this is and when each is (or isn't)
                reported.
     """

    logged_at: datetime.datetime
    forge: Forge
    method: str
    endpoint: str
    outcome: str
    account: str | Unset = UNSET
    status_code: int | Unset = UNSET
    rate_limit: RateLimit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rate_limit import RateLimit # noqa: PLC0415
        logged_at = self.logged_at.isoformat()

        forge = self.forge.value

        method = self.method

        endpoint = self.endpoint

        outcome = self.outcome

        account = self.account

        status_code = self.status_code

        rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "loggedAt": logged_at,
            "forge": forge,
            "method": method,
            "endpoint": endpoint,
            "outcome": outcome,
        })
        if account is not UNSET:
            field_dict["account"] = account
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rate_limit import RateLimit # noqa: PLC0415
        d = dict(src_dict)
        logged_at = datetime.datetime.fromisoformat(d.pop("loggedAt"))




        forge = Forge(d.pop("forge"))




        method = d.pop("method")

        endpoint = d.pop("endpoint")

        outcome = d.pop("outcome")

        account = d.pop("account", UNSET)

        status_code = d.pop("statusCode", UNSET)

        _rate_limit = d.pop("rateLimit", UNSET)
        rate_limit: RateLimit | Unset
        if isinstance(_rate_limit,  Unset):
            rate_limit = UNSET
        else:
            rate_limit = RateLimit.from_dict(_rate_limit)




        request_log_entry = cls(
            logged_at=logged_at,
            forge=forge,
            method=method,
            endpoint=endpoint,
            outcome=outcome,
            account=account,
            status_code=status_code,
            rate_limit=rate_limit,
        )


        request_log_entry.additional_properties = d
        return request_log_entry

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
