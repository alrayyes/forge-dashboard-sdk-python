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
    include_drafts: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["includeDrafts"] = include_drafts


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/dashboard/refresh",
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
    client: AuthenticatedClient,
    include_drafts: bool | Unset = False,

) -> Response[Dashboard | Error]:
    """ Trigger an immediate refresh of the signed-in user's own dashboard

     Blocks until an immediate, out-of-band refresh of the signed-in
    user's own dashboard completes, then returns the resulting
    snapshot — for retrying right away after a forge was only
    briefly unreachable, instead of waiting for the next scheduled
    background refresh.

    Doesn't support `owner` the way GET /api/dashboard does — only
    ever the signed-in user's own dashboard, never a shared one, so
    a user with shared access to someone else's dashboard can never
    spend that owner's own forge rate-limit budget on their own
    schedule.

    Args:
        include_drafts (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard | Error]
     """


    kwargs = _get_kwargs(
        include_drafts=include_drafts,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    include_drafts: bool | Unset = False,

) -> Dashboard | Error | None:
    """ Trigger an immediate refresh of the signed-in user's own dashboard

     Blocks until an immediate, out-of-band refresh of the signed-in
    user's own dashboard completes, then returns the resulting
    snapshot — for retrying right away after a forge was only
    briefly unreachable, instead of waiting for the next scheduled
    background refresh.

    Doesn't support `owner` the way GET /api/dashboard does — only
    ever the signed-in user's own dashboard, never a shared one, so
    a user with shared access to someone else's dashboard can never
    spend that owner's own forge rate-limit budget on their own
    schedule.

    Args:
        include_drafts (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard | Error
     """


    return sync_detailed(
        client=client,
include_drafts=include_drafts,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include_drafts: bool | Unset = False,

) -> Response[Dashboard | Error]:
    """ Trigger an immediate refresh of the signed-in user's own dashboard

     Blocks until an immediate, out-of-band refresh of the signed-in
    user's own dashboard completes, then returns the resulting
    snapshot — for retrying right away after a forge was only
    briefly unreachable, instead of waiting for the next scheduled
    background refresh.

    Doesn't support `owner` the way GET /api/dashboard does — only
    ever the signed-in user's own dashboard, never a shared one, so
    a user with shared access to someone else's dashboard can never
    spend that owner's own forge rate-limit budget on their own
    schedule.

    Args:
        include_drafts (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard | Error]
     """


    kwargs = _get_kwargs(
        include_drafts=include_drafts,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    include_drafts: bool | Unset = False,

) -> Dashboard | Error | None:
    """ Trigger an immediate refresh of the signed-in user's own dashboard

     Blocks until an immediate, out-of-band refresh of the signed-in
    user's own dashboard completes, then returns the resulting
    snapshot — for retrying right away after a forge was only
    briefly unreachable, instead of waiting for the next scheduled
    background refresh.

    Doesn't support `owner` the way GET /api/dashboard does — only
    ever the signed-in user's own dashboard, never a shared one, so
    a user with shared access to someone else's dashboard can never
    spend that owner's own forge rate-limit budget on their own
    schedule.

    Args:
        include_drafts (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard | Error
     """


    return (await asyncio_detailed(
        client=client,
include_drafts=include_drafts,

    )).parsed
