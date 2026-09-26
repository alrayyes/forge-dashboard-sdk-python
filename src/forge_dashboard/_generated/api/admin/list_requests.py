from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.forge import Forge
from ...models.request_log_entry import RequestLogEntry
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    forge: Forge | Unset = UNSET,
    account: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_forge: str | Unset = UNSET
    if not isinstance(forge, Unset):
        json_forge = forge.value

    params["forge"] = json_forge

    params["account"] = account


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/admin/requests",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[RequestLogEntry] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = RequestLogEntry.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[RequestLogEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    forge: Forge | Unset = UNSET,
    account: str | Unset = UNSET,

) -> Response[Error | list[RequestLogEntry]]:
    """ List every outbound GitHub/Forgejo request this instance has made

     Every outbound request `internal/github` or `internal/forgejo` has
    made, newest first, across every account — an admin's own
    credential included, since correlating a shared-credential
    problem (like the rate-limit incident that motivated this
    endpoint) needs a cross-account view no single account's own
    session could give.

    Args:
        forge (Forge | Unset):
        account (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[RequestLogEntry]]
     """


    kwargs = _get_kwargs(
        forge=forge,
account=account,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    forge: Forge | Unset = UNSET,
    account: str | Unset = UNSET,

) -> Error | list[RequestLogEntry] | None:
    """ List every outbound GitHub/Forgejo request this instance has made

     Every outbound request `internal/github` or `internal/forgejo` has
    made, newest first, across every account — an admin's own
    credential included, since correlating a shared-credential
    problem (like the rate-limit incident that motivated this
    endpoint) needs a cross-account view no single account's own
    session could give.

    Args:
        forge (Forge | Unset):
        account (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[RequestLogEntry]
     """


    return sync_detailed(
        client=client,
forge=forge,
account=account,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    forge: Forge | Unset = UNSET,
    account: str | Unset = UNSET,

) -> Response[Error | list[RequestLogEntry]]:
    """ List every outbound GitHub/Forgejo request this instance has made

     Every outbound request `internal/github` or `internal/forgejo` has
    made, newest first, across every account — an admin's own
    credential included, since correlating a shared-credential
    problem (like the rate-limit incident that motivated this
    endpoint) needs a cross-account view no single account's own
    session could give.

    Args:
        forge (Forge | Unset):
        account (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[RequestLogEntry]]
     """


    kwargs = _get_kwargs(
        forge=forge,
account=account,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    forge: Forge | Unset = UNSET,
    account: str | Unset = UNSET,

) -> Error | list[RequestLogEntry] | None:
    """ List every outbound GitHub/Forgejo request this instance has made

     Every outbound request `internal/github` or `internal/forgejo` has
    made, newest first, across every account — an admin's own
    credential included, since correlating a shared-credential
    problem (like the rate-limit incident that motivated this
    endpoint) needs a cross-account view no single account's own
    session could give.

    Args:
        forge (Forge | Unset):
        account (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[RequestLogEntry]
     """


    return (await asyncio_detailed(
        client=client,
forge=forge,
account=account,

    )).parsed
