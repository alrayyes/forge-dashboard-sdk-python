from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.action_error_code import ActionErrorCode
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="ActionError")



@_attrs_define
class ActionError:
    """ The structured result of a refused pull request action (Merge, Close, Update branch, Enable auto-merge, Dependabot
    and Renovate rebase). `code` and `message` are what a client should act on and show.

        Attributes:
            error (str): The same string every Error carries. With `code: unknown` it
                is the same plain words as `message`, since the raw text
                (internal prefixes, API paths, URLs) goes to the server log.
                With any other code it is the forge's own text, for logs.
            code (ActionErrorCode): Why the action was refused, from a re-read of the pull
                request's real state. `already_merged` and `already_closed`
                mean the dashboard's row was stale: the pull request has
                nothing left to merge.

                Three codes belong to one action each: `already_up_to_date`
                (Update branch: nothing to bring in), `auto_merge_not_allowed`
                (Enable auto-merge: the repo or pull request doesn't allow it)
                and `ready_to_merge` (Enable auto-merge: already clean, use
                Merge).
            message (str): A short reason in plain words, safe to show a person, always.
                With `code: unknown` it is the forge's own sentence when that
                reads as one, "The forge didn't answer. Try again in a moment."
                when the forge was unreachable (including a 502, 503 or 504),
                and "The forge refused this action and gave no reason."
                otherwise. It never holds an internal prefix, an API path, a
                URL or JSON.
            resets_at (datetime.datetime | Unset): Only with `rate_limited`, when the forge said so. When the budget comes
                back. On Forgejo it comes from the `Retry-After` header, in seconds or as a date.
     """

    error: str
    code: ActionErrorCode
    message: str
    resets_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        error = self.error

        code = self.code.value

        message = self.message

        resets_at: str | Unset = UNSET
        if not isinstance(self.resets_at, Unset):
            resets_at = self.resets_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "error": error,
            "code": code,
            "message": message,
        })
        if resets_at is not UNSET:
            field_dict["resetsAt"] = resets_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        code = ActionErrorCode(d.pop("code"))




        message = d.pop("message")

        _resets_at = d.pop("resetsAt", UNSET)
        resets_at: datetime.datetime | Unset
        if isinstance(_resets_at,  Unset):
            resets_at = UNSET
        else:
            resets_at = datetime.datetime.fromisoformat(_resets_at)




        action_error = cls(
            error=error,
            code=code,
            message=message,
            resets_at=resets_at,
        )


        action_error.additional_properties = d
        return action_error

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
