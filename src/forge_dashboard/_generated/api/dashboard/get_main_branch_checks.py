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

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_forge = forge.value
    params["forge"] = json_forge

    params["fullName"] = full_name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/main-branches/checks",
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
    client: AuthenticatedClient,
    forge: Forge,
    full_name: str,

) -> Response[Error | PullRequestChecksResponse]:
    """ List every job/check of a repository's default-branch pipeline, on demand

     The jobs behind one Main branches row's status: the same `Check` list,
    in the same response shape, as GET /api/pull-requests/checks, so one
    pipeline panel shows either. Fetched live on every call, never as part
    of GET /api/main-branches' snapshot, for the same reason a pull
    request's jobs are not: a job list for every row would spend the
    forge's budget on rows nobody opens.

    The commit is the one the row reports: the newest commit on the
    default branch that a check ran on. A release bot's commit that skips
    CI has none, so the commit before it answers. `required` is never set,
    since it is a pull request's base-branch notion.

    GitHub reads the newest commits' check runs (one request for the
    commits, one per commit until a check is found, and up to 2 more per
    failed job for its failed step). Forgejo reads the repository, the
    Actions runs of the default branch and each run's jobs, the same
    reading GET /api/main-branches counts its `checks` from, so the list
    and the counts describe the same jobs. A run whose jobs can't be read
    is listed as one check named after its workflow.

    Empty when the repository has no default branch, no commit with a
    check, or no run. The error answers are those of GET
    /api/pull-requests/checks.

    Args:
        forge (Forge):
        full_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PullRequestChecksResponse]
     """


    kwargs = _get_kwargs(
        forge=forge,
full_name=full_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    forge: Forge,
    full_name: str,

) -> Error | PullRequestChecksResponse | None:
    """ List every job/check of a repository's default-branch pipeline, on demand

     The jobs behind one Main branches row's status: the same `Check` list,
    in the same response shape, as GET /api/pull-requests/checks, so one
    pipeline panel shows either. Fetched live on every call, never as part
    of GET /api/main-branches' snapshot, for the same reason a pull
    request's jobs are not: a job list for every row would spend the
    forge's budget on rows nobody opens.

    The commit is the one the row reports: the newest commit on the
    default branch that a check ran on. A release bot's commit that skips
    CI has none, so the commit before it answers. `required` is never set,
    since it is a pull request's base-branch notion.

    GitHub reads the newest commits' check runs (one request for the
    commits, one per commit until a check is found, and up to 2 more per
    failed job for its failed step). Forgejo reads the repository, the
    Actions runs of the default branch and each run's jobs, the same
    reading GET /api/main-branches counts its `checks` from, so the list
    and the counts describe the same jobs. A run whose jobs can't be read
    is listed as one check named after its workflow.

    Empty when the repository has no default branch, no commit with a
    check, or no run. The error answers are those of GET
    /api/pull-requests/checks.

    Args:
        forge (Forge):
        full_name (str):

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

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    forge: Forge,
    full_name: str,

) -> Response[Error | PullRequestChecksResponse]:
    """ List every job/check of a repository's default-branch pipeline, on demand

     The jobs behind one Main branches row's status: the same `Check` list,
    in the same response shape, as GET /api/pull-requests/checks, so one
    pipeline panel shows either. Fetched live on every call, never as part
    of GET /api/main-branches' snapshot, for the same reason a pull
    request's jobs are not: a job list for every row would spend the
    forge's budget on rows nobody opens.

    The commit is the one the row reports: the newest commit on the
    default branch that a check ran on. A release bot's commit that skips
    CI has none, so the commit before it answers. `required` is never set,
    since it is a pull request's base-branch notion.

    GitHub reads the newest commits' check runs (one request for the
    commits, one per commit until a check is found, and up to 2 more per
    failed job for its failed step). Forgejo reads the repository, the
    Actions runs of the default branch and each run's jobs, the same
    reading GET /api/main-branches counts its `checks` from, so the list
    and the counts describe the same jobs. A run whose jobs can't be read
    is listed as one check named after its workflow.

    Empty when the repository has no default branch, no commit with a
    check, or no run. The error answers are those of GET
    /api/pull-requests/checks.

    Args:
        forge (Forge):
        full_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PullRequestChecksResponse]
     """


    kwargs = _get_kwargs(
        forge=forge,
full_name=full_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    forge: Forge,
    full_name: str,

) -> Error | PullRequestChecksResponse | None:
    """ List every job/check of a repository's default-branch pipeline, on demand

     The jobs behind one Main branches row's status: the same `Check` list,
    in the same response shape, as GET /api/pull-requests/checks, so one
    pipeline panel shows either. Fetched live on every call, never as part
    of GET /api/main-branches' snapshot, for the same reason a pull
    request's jobs are not: a job list for every row would spend the
    forge's budget on rows nobody opens.

    The commit is the one the row reports: the newest commit on the
    default branch that a check ran on. A release bot's commit that skips
    CI has none, so the commit before it answers. `required` is never set,
    since it is a pull request's base-branch notion.

    GitHub reads the newest commits' check runs (one request for the
    commits, one per commit until a check is found, and up to 2 more per
    failed job for its failed step). Forgejo reads the repository, the
    Actions runs of the default branch and each run's jobs, the same
    reading GET /api/main-branches counts its `checks` from, so the list
    and the counts describe the same jobs. A run whose jobs can't be read
    is listed as one check named after its workflow.

    Empty when the repository has no default branch, no commit with a
    check, or no run. The error answers are those of GET
    /api/pull-requests/checks.

    Args:
        forge (Forge):
        full_name (str):

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

    )).parsed
