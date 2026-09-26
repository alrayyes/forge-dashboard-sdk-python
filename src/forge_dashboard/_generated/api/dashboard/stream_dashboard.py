from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dashboard import Dashboard
from ...models.error import Error
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dashboard/stream",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Dashboard | Error | None:
    if response.status_code == 200:
        response_200 = Dashboard.from_dict(response.text)



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

) -> Response[Dashboard | Error]:
    """ Server-Sent Events stream of the signed-in user's own dashboard

     Pushes a fresh snapshot every time this user's background
    refresh produces one — most notably right after a verified
    webhook delivery (see the webhooks tag) triggers an immediate
    one, which is what turns that into a live update instead of
    something only the next scheduled refresh picks up.

    Doesn't support `owner` the way GET /api/dashboard does — only
    ever the signed-in user's own dashboard, never a shared one.
    The frontend's own 30-second poll against GET /api/dashboard
    keeps running unconditionally, connected or not — a browser or
    proxy that can't hold an SSE connection open just never
    benefits from this, rather than the dashboard going stale
    silently.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard | Error]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Dashboard | Error | None:
    """ Server-Sent Events stream of the signed-in user's own dashboard

     Pushes a fresh snapshot every time this user's background
    refresh produces one — most notably right after a verified
    webhook delivery (see the webhooks tag) triggers an immediate
    one, which is what turns that into a live update instead of
    something only the next scheduled refresh picks up.

    Doesn't support `owner` the way GET /api/dashboard does — only
    ever the signed-in user's own dashboard, never a shared one.
    The frontend's own 30-second poll against GET /api/dashboard
    keeps running unconditionally, connected or not — a browser or
    proxy that can't hold an SSE connection open just never
    benefits from this, rather than the dashboard going stale
    silently.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard | Error
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Dashboard | Error]:
    """ Server-Sent Events stream of the signed-in user's own dashboard

     Pushes a fresh snapshot every time this user's background
    refresh produces one — most notably right after a verified
    webhook delivery (see the webhooks tag) triggers an immediate
    one, which is what turns that into a live update instead of
    something only the next scheduled refresh picks up.

    Doesn't support `owner` the way GET /api/dashboard does — only
    ever the signed-in user's own dashboard, never a shared one.
    The frontend's own 30-second poll against GET /api/dashboard
    keeps running unconditionally, connected or not — a browser or
    proxy that can't hold an SSE connection open just never
    benefits from this, rather than the dashboard going stale
    silently.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Dashboard | Error]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Dashboard | Error | None:
    """ Server-Sent Events stream of the signed-in user's own dashboard

     Pushes a fresh snapshot every time this user's background
    refresh produces one — most notably right after a verified
    webhook delivery (see the webhooks tag) triggers an immediate
    one, which is what turns that into a live update instead of
    something only the next scheduled refresh picks up.

    Doesn't support `owner` the way GET /api/dashboard does — only
    ever the signed-in user's own dashboard, never a shared one.
    The frontend's own 30-second poll against GET /api/dashboard
    keeps running unconditionally, connected or not — a browser or
    proxy that can't hold an SSE connection open just never
    benefits from this, rather than the dashboard going stale
    silently.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Dashboard | Error
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
