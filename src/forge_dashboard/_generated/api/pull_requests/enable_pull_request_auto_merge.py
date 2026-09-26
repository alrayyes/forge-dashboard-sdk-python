from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.pull_request_action_request import PullRequestActionRequest
from typing import cast



def _get_kwargs(
    *,
    body: PullRequestActionRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/pull-requests/auto-merge",
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
    body: PullRequestActionRequest,

) -> Response[Any | Error]:
    """ Arm a pull request's own native auto-merge, on the signed-in user's behalf

     GitHub only, today. Enables the named pull request's own
    auto-merge via GitHub's `enablePullRequestAutoMerge` GraphQL
    mutation — REST has no equivalent endpoint. Unlike Merge, that
    mutation asks for an explicit merge method rather than picking
    the repo's own default itself, so this looks the repo's allowed
    methods up first and picks one with the same merge > squash >
    rebase precedence Merge already uses; no override is exposed
    here either. The pull request stays open and unmerged until the
    forge's own required checks pass on their own.

    Args:
        body (PullRequestActionRequest): Which pull request to act on.

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
    body: PullRequestActionRequest,

) -> Any | Error | None:
    """ Arm a pull request's own native auto-merge, on the signed-in user's behalf

     GitHub only, today. Enables the named pull request's own
    auto-merge via GitHub's `enablePullRequestAutoMerge` GraphQL
    mutation — REST has no equivalent endpoint. Unlike Merge, that
    mutation asks for an explicit merge method rather than picking
    the repo's own default itself, so this looks the repo's allowed
    methods up first and picks one with the same merge > squash >
    rebase precedence Merge already uses; no override is exposed
    here either. The pull request stays open and unmerged until the
    forge's own required checks pass on their own.

    Args:
        body (PullRequestActionRequest): Which pull request to act on.

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
    body: PullRequestActionRequest,

) -> Response[Any | Error]:
    """ Arm a pull request's own native auto-merge, on the signed-in user's behalf

     GitHub only, today. Enables the named pull request's own
    auto-merge via GitHub's `enablePullRequestAutoMerge` GraphQL
    mutation — REST has no equivalent endpoint. Unlike Merge, that
    mutation asks for an explicit merge method rather than picking
    the repo's own default itself, so this looks the repo's allowed
    methods up first and picks one with the same merge > squash >
    rebase precedence Merge already uses; no override is exposed
    here either. The pull request stays open and unmerged until the
    forge's own required checks pass on their own.

    Args:
        body (PullRequestActionRequest): Which pull request to act on.

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
    body: PullRequestActionRequest,

) -> Any | Error | None:
    """ Arm a pull request's own native auto-merge, on the signed-in user's behalf

     GitHub only, today. Enables the named pull request's own
    auto-merge via GitHub's `enablePullRequestAutoMerge` GraphQL
    mutation — REST has no equivalent endpoint. Unlike Merge, that
    mutation asks for an explicit merge method rather than picking
    the repo's own default itself, so this looks the repo's allowed
    methods up first and picks one with the same merge > squash >
    rebase precedence Merge already uses; no override is exposed
    here either. The pull request stays open and unmerged until the
    forge's own required checks pass on their own.

    Args:
        body (PullRequestActionRequest): Which pull request to act on.

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
