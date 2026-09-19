from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dashboard import Dashboard
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    owner: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["owner"] = owner


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dashboard",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Dashboard | Error | None:
    if response.status_code == 200:
        response_200 = Dashboard.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Dashboard | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner: str | Unset = UNSET,

) -> Response[Dashboard | Error]:
    """ The aggregated view

     Returns the most recently fetched snapshot. The backend refreshes
    this on its own schedule in the background; this endpoint never
    blocks on a live call to either forge, so it answers instantly even
    when a forge is slow or unreachable.

    Omitting `owner` returns the signed-in user's own dashboard. Passing
    it returns that user's dashboard instead — allowed only when they've
    shared it with the caller (or the caller is viewing their own
    username), and refused with a 403 otherwise.

    Args:
        owner (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard | Error]
     """


    kwargs = _get_kwargs(
        owner=owner,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    owner: str | Unset = UNSET,

) -> Dashboard | Error | None:
    """ The aggregated view

     Returns the most recently fetched snapshot. The backend refreshes
    this on its own schedule in the background; this endpoint never
    blocks on a live call to either forge, so it answers instantly even
    when a forge is slow or unreachable.

    Omitting `owner` returns the signed-in user's own dashboard. Passing
    it returns that user's dashboard instead — allowed only when they've
    shared it with the caller (or the caller is viewing their own
    username), and refused with a 403 otherwise.

    Args:
        owner (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard | Error
     """


    return sync_detailed(
        client=client,
owner=owner,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    owner: str | Unset = UNSET,

) -> Response[Dashboard | Error]:
    """ The aggregated view

     Returns the most recently fetched snapshot. The backend refreshes
    this on its own schedule in the background; this endpoint never
    blocks on a live call to either forge, so it answers instantly even
    when a forge is slow or unreachable.

    Omitting `owner` returns the signed-in user's own dashboard. Passing
    it returns that user's dashboard instead — allowed only when they've
    shared it with the caller (or the caller is viewing their own
    username), and refused with a 403 otherwise.

    Args:
        owner (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard | Error]
     """


    kwargs = _get_kwargs(
        owner=owner,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    owner: str | Unset = UNSET,

) -> Dashboard | Error | None:
    """ The aggregated view

     Returns the most recently fetched snapshot. The backend refreshes
    this on its own schedule in the background; this endpoint never
    blocks on a live call to either forge, so it answers instantly even
    when a forge is slow or unreachable.

    Omitting `owner` returns the signed-in user's own dashboard. Passing
    it returns that user's dashboard instead — allowed only when they've
    shared it with the caller (or the caller is viewing their own
    username), and refused with a 403 otherwise.

    Args:
        owner (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard | Error
     """


    return (await asyncio_detailed(
        client=client,
owner=owner,

    )).parsed
