from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bot_pr_updates_response import BotPrUpdatesResponse
from ...models.error import Error
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/settings/bot-pr-updates",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BotPrUpdatesResponse | Error | None:
    if response.status_code == 200:
        response_200 = BotPrUpdatesResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BotPrUpdatesResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[BotPrUpdatesResponse | Error]:
    """ Whether bot-managed pull request branches can be updated

     A lightweight, side-effect-free read of one field —
    allowBotPrUpdates — for the dashboard page to check on every
    load. Deliberately not GET /api/settings itself: that handler
    also provisions webhook credentials on first call
    (EnsureWebhookCredentials), which the dashboard visiting on a
    user's behalf shouldn't trigger for someone who's never opened
    Settings at all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotPrUpdatesResponse | Error]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> BotPrUpdatesResponse | Error | None:
    """ Whether bot-managed pull request branches can be updated

     A lightweight, side-effect-free read of one field —
    allowBotPrUpdates — for the dashboard page to check on every
    load. Deliberately not GET /api/settings itself: that handler
    also provisions webhook credentials on first call
    (EnsureWebhookCredentials), which the dashboard visiting on a
    user's behalf shouldn't trigger for someone who's never opened
    Settings at all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotPrUpdatesResponse | Error
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[BotPrUpdatesResponse | Error]:
    """ Whether bot-managed pull request branches can be updated

     A lightweight, side-effect-free read of one field —
    allowBotPrUpdates — for the dashboard page to check on every
    load. Deliberately not GET /api/settings itself: that handler
    also provisions webhook credentials on first call
    (EnsureWebhookCredentials), which the dashboard visiting on a
    user's behalf shouldn't trigger for someone who's never opened
    Settings at all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotPrUpdatesResponse | Error]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> BotPrUpdatesResponse | Error | None:
    """ Whether bot-managed pull request branches can be updated

     A lightweight, side-effect-free read of one field —
    allowBotPrUpdates — for the dashboard page to check on every
    load. Deliberately not GET /api/settings itself: that handler
    also provisions webhook credentials on first call
    (EnsureWebhookCredentials), which the dashboard visiting on a
    user's behalf shouldn't trigger for someone who's never opened
    Settings at all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotPrUpdatesResponse | Error
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
