from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.forge import Forge
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
        "url": "/api/admin/requests/export",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | str | None:
    if response.status_code == 200:
        response_200 = response.text
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | str]:
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

) -> Response[Error | str]:
    """ Export the (filtered) outbound-request log as CSV

     The same rows GET /api/admin/requests would return for the same
    filter, as a downloadable CSV file with one header row.

    Args:
        forge (Forge | Unset):
        account (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | str]
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

) -> Error | str | None:
    """ Export the (filtered) outbound-request log as CSV

     The same rows GET /api/admin/requests would return for the same
    filter, as a downloadable CSV file with one header row.

    Args:
        forge (Forge | Unset):
        account (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | str
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

) -> Response[Error | str]:
    """ Export the (filtered) outbound-request log as CSV

     The same rows GET /api/admin/requests would return for the same
    filter, as a downloadable CSV file with one header row.

    Args:
        forge (Forge | Unset):
        account (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | str]
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

) -> Error | str | None:
    """ Export the (filtered) outbound-request log as CSV

     The same rows GET /api/admin/requests would return for the same
    filter, as a downloadable CSV file with one header row.

    Args:
        forge (Forge | Unset):
        account (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | str
     """


    return (await asyncio_detailed(
        client=client,
forge=forge,
account=account,

    )).parsed
