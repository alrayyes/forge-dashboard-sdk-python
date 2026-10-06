from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.action_error import ActionError
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
        "url": "/api/pull-requests/rerun-checks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ActionError | Any | Error | None:
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
        response_403 = ActionError.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ActionError.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ActionError.from_dict(response.json())



        return response_409

    if response.status_code == 429:
        response_429 = ActionError.from_dict(response.json())



        return response_429

    if response.status_code == 502:
        response_502 = ActionError.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ActionError | Any | Error]:
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

) -> Response[ActionError | Any | Error]:
    """ Rerun only the failed jobs of one pull request's checks, on the signed-in user's behalf

     Asks the forge to rerun the failed jobs of the Actions workflow
    runs on the pull request's head commit, and nothing that passed. It
    answers once the forge has queued them, not when they finish, so a
    client shows a queued state and lets the next refresh carry the
    result.

    A pull request offers it as a `rerun_checks` entry in
    `allowedActions`, on GitHub and Forgejo, when its CI is failing. A
    Forgejo commit status doesn't say which workflow run it came from, so
    Forgejo's runs are found by the head commit instead. A failed check
    that isn't an Actions job (a third-party check, a legacy status, an
    external CI) can't be rerun here and is skipped. A Forgejo instance
    too old to have the rerun route refuses with its own words.

    Refusals are an `ActionError` (see Merge). `not_mergeable` with a 409
    means the pull request has no failed check to rerun. Anything the
    forge refuses (the token may not write to Actions, the run is too
    old or already running) arrives with its own plain-words `message`.

    Args:
        body (PullRequestActionRequest): Which pull request to act on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionError | Any | Error]
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

) -> ActionError | Any | Error | None:
    """ Rerun only the failed jobs of one pull request's checks, on the signed-in user's behalf

     Asks the forge to rerun the failed jobs of the Actions workflow
    runs on the pull request's head commit, and nothing that passed. It
    answers once the forge has queued them, not when they finish, so a
    client shows a queued state and lets the next refresh carry the
    result.

    A pull request offers it as a `rerun_checks` entry in
    `allowedActions`, on GitHub and Forgejo, when its CI is failing. A
    Forgejo commit status doesn't say which workflow run it came from, so
    Forgejo's runs are found by the head commit instead. A failed check
    that isn't an Actions job (a third-party check, a legacy status, an
    external CI) can't be rerun here and is skipped. A Forgejo instance
    too old to have the rerun route refuses with its own words.

    Refusals are an `ActionError` (see Merge). `not_mergeable` with a 409
    means the pull request has no failed check to rerun. Anything the
    forge refuses (the token may not write to Actions, the run is too
    old or already running) arrives with its own plain-words `message`.

    Args:
        body (PullRequestActionRequest): Which pull request to act on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionError | Any | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PullRequestActionRequest,

) -> Response[ActionError | Any | Error]:
    """ Rerun only the failed jobs of one pull request's checks, on the signed-in user's behalf

     Asks the forge to rerun the failed jobs of the Actions workflow
    runs on the pull request's head commit, and nothing that passed. It
    answers once the forge has queued them, not when they finish, so a
    client shows a queued state and lets the next refresh carry the
    result.

    A pull request offers it as a `rerun_checks` entry in
    `allowedActions`, on GitHub and Forgejo, when its CI is failing. A
    Forgejo commit status doesn't say which workflow run it came from, so
    Forgejo's runs are found by the head commit instead. A failed check
    that isn't an Actions job (a third-party check, a legacy status, an
    external CI) can't be rerun here and is skipped. A Forgejo instance
    too old to have the rerun route refuses with its own words.

    Refusals are an `ActionError` (see Merge). `not_mergeable` with a 409
    means the pull request has no failed check to rerun. Anything the
    forge refuses (the token may not write to Actions, the run is too
    old or already running) arrives with its own plain-words `message`.

    Args:
        body (PullRequestActionRequest): Which pull request to act on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionError | Any | Error]
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

) -> ActionError | Any | Error | None:
    """ Rerun only the failed jobs of one pull request's checks, on the signed-in user's behalf

     Asks the forge to rerun the failed jobs of the Actions workflow
    runs on the pull request's head commit, and nothing that passed. It
    answers once the forge has queued them, not when they finish, so a
    client shows a queued state and lets the next refresh carry the
    result.

    A pull request offers it as a `rerun_checks` entry in
    `allowedActions`, on GitHub and Forgejo, when its CI is failing. A
    Forgejo commit status doesn't say which workflow run it came from, so
    Forgejo's runs are found by the head commit instead. A failed check
    that isn't an Actions job (a third-party check, a legacy status, an
    external CI) can't be rerun here and is skipped. A Forgejo instance
    too old to have the rerun route refuses with its own words.

    Refusals are an `ActionError` (see Merge). `not_mergeable` with a 409
    means the pull request has no failed check to rerun. Anything the
    forge refuses (the token may not write to Actions, the run is too
    old or already running) arrives with its own plain-words `message`.

    Args:
        body (PullRequestActionRequest): Which pull request to act on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionError | Any | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
