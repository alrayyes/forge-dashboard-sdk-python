from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.forge import Forge
from ...models.pull_request_checks_response import PullRequestChecksResponse
from typing import cast



def _get_kwargs(
    *,
    forge: Forge,
    full_name: str,
    number: int,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_forge = forge.value
    params["forge"] = json_forge

    params["fullName"] = full_name

    params["number"] = number


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/pull-requests/checks",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PullRequestChecksResponse | None:
    if response.status_code == 200:
        response_200 = PullRequestChecksResponse.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PullRequestChecksResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge,
    full_name: str,
    number: int,

) -> Response[Error | PullRequestChecksResponse]:
    """ List every job/check run against a pull request's head commit, on demand

     Fetched live on every call, never as part of GET /api/dashboard's
    own snapshot — this is detail a pull request's row doesn't show
    until a caller actually asks for it, and adding it to the eager
    refresh loop would multiply that refresh's cost by every open
    pull request for data most of them are never opened for.

    Falls back to the legacy combined commit-status API's own
    per-check entries when the forge reports no Actions runs at all
    for that commit (Actions disabled, or an instance too old to
    expose them) — never an error for that case specifically, since
    it's a normal, expected shape for an older or CI-less repo.

    Args:
        forge (Forge):
        full_name (str):
        number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PullRequestChecksResponse]
     """


    kwargs = _get_kwargs(
        forge=forge,
full_name=full_name,
number=number,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge,
    full_name: str,
    number: int,

) -> Error | PullRequestChecksResponse | None:
    """ List every job/check run against a pull request's head commit, on demand

     Fetched live on every call, never as part of GET /api/dashboard's
    own snapshot — this is detail a pull request's row doesn't show
    until a caller actually asks for it, and adding it to the eager
    refresh loop would multiply that refresh's cost by every open
    pull request for data most of them are never opened for.

    Falls back to the legacy combined commit-status API's own
    per-check entries when the forge reports no Actions runs at all
    for that commit (Actions disabled, or an instance too old to
    expose them) — never an error for that case specifically, since
    it's a normal, expected shape for an older or CI-less repo.

    Args:
        forge (Forge):
        full_name (str):
        number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PullRequestChecksResponse
     """


    return sync_detailed(
        client=client,
forge=forge,
full_name=full_name,
number=number,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge,
    full_name: str,
    number: int,

) -> Response[Error | PullRequestChecksResponse]:
    """ List every job/check run against a pull request's head commit, on demand

     Fetched live on every call, never as part of GET /api/dashboard's
    own snapshot — this is detail a pull request's row doesn't show
    until a caller actually asks for it, and adding it to the eager
    refresh loop would multiply that refresh's cost by every open
    pull request for data most of them are never opened for.

    Falls back to the legacy combined commit-status API's own
    per-check entries when the forge reports no Actions runs at all
    for that commit (Actions disabled, or an instance too old to
    expose them) — never an error for that case specifically, since
    it's a normal, expected shape for an older or CI-less repo.

    Args:
        forge (Forge):
        full_name (str):
        number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PullRequestChecksResponse]
     """


    kwargs = _get_kwargs(
        forge=forge,
full_name=full_name,
number=number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge,
    full_name: str,
    number: int,

) -> Error | PullRequestChecksResponse | None:
    """ List every job/check run against a pull request's head commit, on demand

     Fetched live on every call, never as part of GET /api/dashboard's
    own snapshot — this is detail a pull request's row doesn't show
    until a caller actually asks for it, and adding it to the eager
    refresh loop would multiply that refresh's cost by every open
    pull request for data most of them are never opened for.

    Falls back to the legacy combined commit-status API's own
    per-check entries when the forge reports no Actions runs at all
    for that commit (Actions disabled, or an instance too old to
    expose them) — never an error for that case specifically, since
    it's a normal, expected shape for an older or CI-less repo.

    Args:
        forge (Forge):
        full_name (str):
        number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PullRequestChecksResponse
     """


    return (await asyncio_detailed(
        client=client,
forge=forge,
full_name=full_name,
number=number,

    )).parsed
