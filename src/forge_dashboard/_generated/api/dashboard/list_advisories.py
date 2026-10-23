from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.advisory_list import AdvisoryList
from ...models.error import Error
from ...models.forge import Forge
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
        "url": "/api/main-branches/advisories",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AdvisoryList | Error | None:
    if response.status_code == 200:
        response_200 = AdvisoryList.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AdvisoryList | Error]:
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

) -> Response[AdvisoryList | Error]:
    """ List a repository's open dependency advisories in full, on demand

     What the advisories dialog on the Main branches page shows for one
    repository: each open Dependabot alert with the fields GitHub's own
    alert page shows. The list and the detail view are the same answer, so
    opening one advisory costs no second call. Fetched live on every call,
    never as part of GET /api/main-branches' snapshot, so a repository
    nobody opens costs no budget.

    Sorted by severity, highest first, then newest first. Only GitHub reads
    them, through the Dependabot alerts of the repository; a Forgejo
    repository is a 400.

    A forge that can't say is a 200 with `state` "unknown", an empty list
    and the `reason`, the same words as the row's own `advisories`: alerts
    switched off, a credential without the Dependabot alerts permission, a
    rate limit, any other failure, or a repository with more open alerts
    than one read pages through. An empty `known` list means nothing is
    open.

    `description` is Markdown exactly as GitHub stores it, so a client must
    render it with raw HTML disabled. A field GitHub didn't send is left
    out.

    Args:
        forge (Forge):
        full_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdvisoryList | Error]
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

) -> AdvisoryList | Error | None:
    """ List a repository's open dependency advisories in full, on demand

     What the advisories dialog on the Main branches page shows for one
    repository: each open Dependabot alert with the fields GitHub's own
    alert page shows. The list and the detail view are the same answer, so
    opening one advisory costs no second call. Fetched live on every call,
    never as part of GET /api/main-branches' snapshot, so a repository
    nobody opens costs no budget.

    Sorted by severity, highest first, then newest first. Only GitHub reads
    them, through the Dependabot alerts of the repository; a Forgejo
    repository is a 400.

    A forge that can't say is a 200 with `state` "unknown", an empty list
    and the `reason`, the same words as the row's own `advisories`: alerts
    switched off, a credential without the Dependabot alerts permission, a
    rate limit, any other failure, or a repository with more open alerts
    than one read pages through. An empty `known` list means nothing is
    open.

    `description` is Markdown exactly as GitHub stores it, so a client must
    render it with raw HTML disabled. A field GitHub didn't send is left
    out.

    Args:
        forge (Forge):
        full_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdvisoryList | Error
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

) -> Response[AdvisoryList | Error]:
    """ List a repository's open dependency advisories in full, on demand

     What the advisories dialog on the Main branches page shows for one
    repository: each open Dependabot alert with the fields GitHub's own
    alert page shows. The list and the detail view are the same answer, so
    opening one advisory costs no second call. Fetched live on every call,
    never as part of GET /api/main-branches' snapshot, so a repository
    nobody opens costs no budget.

    Sorted by severity, highest first, then newest first. Only GitHub reads
    them, through the Dependabot alerts of the repository; a Forgejo
    repository is a 400.

    A forge that can't say is a 200 with `state` "unknown", an empty list
    and the `reason`, the same words as the row's own `advisories`: alerts
    switched off, a credential without the Dependabot alerts permission, a
    rate limit, any other failure, or a repository with more open alerts
    than one read pages through. An empty `known` list means nothing is
    open.

    `description` is Markdown exactly as GitHub stores it, so a client must
    render it with raw HTML disabled. A field GitHub didn't send is left
    out.

    Args:
        forge (Forge):
        full_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdvisoryList | Error]
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

) -> AdvisoryList | Error | None:
    """ List a repository's open dependency advisories in full, on demand

     What the advisories dialog on the Main branches page shows for one
    repository: each open Dependabot alert with the fields GitHub's own
    alert page shows. The list and the detail view are the same answer, so
    opening one advisory costs no second call. Fetched live on every call,
    never as part of GET /api/main-branches' snapshot, so a repository
    nobody opens costs no budget.

    Sorted by severity, highest first, then newest first. Only GitHub reads
    them, through the Dependabot alerts of the repository; a Forgejo
    repository is a 400.

    A forge that can't say is a 200 with `state` "unknown", an empty list
    and the `reason`, the same words as the row's own `advisories`: alerts
    switched off, a credential without the Dependabot alerts permission, a
    rate limit, any other failure, or a repository with more open alerts
    than one read pages through. An empty `known` list means nothing is
    open.

    `description` is Markdown exactly as GitHub stores it, so a client must
    render it with raw HTML disabled. A field GitHub didn't send is left
    out.

    Args:
        forge (Forge):
        full_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdvisoryList | Error
     """


    return (await asyncio_detailed(
        client=client,
forge=forge,
full_name=full_name,

    )).parsed
