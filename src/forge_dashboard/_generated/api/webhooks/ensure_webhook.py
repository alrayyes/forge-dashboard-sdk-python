from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.webhook_ensure_request import WebhookEnsureRequest
from typing import cast



def _get_kwargs(
    *,
    body: WebhookEnsureRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/webhooks/ensure",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookEnsureRequest,

) -> Response[Any | Error]:
    """ Create or fix up a webhook on one tracked repo, on the signed-in user's behalf

     Creates a webhook on the named repo, pointed at the signed-in
    user's own webhook URL and secret, subscribed to the events
    docs/webhooks.md's manual steps recommend. If one already exists
    there (found the same way GET /api/dashboard's own `hasWebhook`
    does — matching by URL path, not object identity) it's brought
    back to active with the right events instead of creating a
    duplicate.

    One of a small number of endpoints in this API that write to a
    forge rather than just reading from it — see also the
    pull-requests tag.

    Args:
        body (WebhookEnsureRequest): Which repo to create or fix up a webhook on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: WebhookEnsureRequest,

) -> Any | Error | None:
    """ Create or fix up a webhook on one tracked repo, on the signed-in user's behalf

     Creates a webhook on the named repo, pointed at the signed-in
    user's own webhook URL and secret, subscribed to the events
    docs/webhooks.md's manual steps recommend. If one already exists
    there (found the same way GET /api/dashboard's own `hasWebhook`
    does — matching by URL path, not object identity) it's brought
    back to active with the right events instead of creating a
    duplicate.

    One of a small number of endpoints in this API that write to a
    forge rather than just reading from it — see also the
    pull-requests tag.

    Args:
        body (WebhookEnsureRequest): Which repo to create or fix up a webhook on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookEnsureRequest,

) -> Response[Any | Error]:
    """ Create or fix up a webhook on one tracked repo, on the signed-in user's behalf

     Creates a webhook on the named repo, pointed at the signed-in
    user's own webhook URL and secret, subscribed to the events
    docs/webhooks.md's manual steps recommend. If one already exists
    there (found the same way GET /api/dashboard's own `hasWebhook`
    does — matching by URL path, not object identity) it's brought
    back to active with the right events instead of creating a
    duplicate.

    One of a small number of endpoints in this API that write to a
    forge rather than just reading from it — see also the
    pull-requests tag.

    Args:
        body (WebhookEnsureRequest): Which repo to create or fix up a webhook on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: WebhookEnsureRequest,

) -> Any | Error | None:
    """ Create or fix up a webhook on one tracked repo, on the signed-in user's behalf

     Creates a webhook on the named repo, pointed at the signed-in
    user's own webhook URL and secret, subscribed to the events
    docs/webhooks.md's manual steps recommend. If one already exists
    there (found the same way GET /api/dashboard's own `hasWebhook`
    does — matching by URL path, not object identity) it's brought
    back to active with the right events instead of creating a
    duplicate.

    One of a small number of endpoints in this API that write to a
    forge rather than just reading from it — see also the
    pull-requests tag.

    Args:
        body (WebhookEnsureRequest): Which repo to create or fix up a webhook on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
