from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.check_log import CheckLog
from ...models.error import Error
from ...models.forge import Forge
from typing import cast



def _get_kwargs(
    *,
    forge: Forge,
    full_name: str,
    job_id: int,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_forge = forge.value
    params["forge"] = json_forge

    params["fullName"] = full_name

    params["jobId"] = job_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/checks/log",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CheckLog | Error | None:
    if response.status_code == 200:
        response_200 = CheckLog.from_dict(response.json())



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

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CheckLog | Error]:
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
    job_id: int,

) -> Response[CheckLog | Error]:
    """ Read the output of one CI job, on demand

     The output behind a `Check` that carries a `jobId`, as plain text: colour
    codes and carriage returns removed, never markup, so a client must render
    it as text. Whatever the forge already masks stays masked. Only the last
    256 KiB are returned; `truncated` says the start was cut.

    Only for a repository the dashboard tracks for you; any other answers 404
    without asking the forge.

    Fetched live on every call and never as part of a snapshot, since a log
    can be large and most are never opened. GitHub reads the job's log
    through its REST API (one request, then a short-lived download). Forgejo
    reads it through the job logs endpoint of its Actions API.

    A forge can refuse: the token may not read logs, the log may have
    expired, or the check may not be an Actions job at all. Those answer 403
    or 404 with a sentence a person can read.

    Args:
        forge (Forge):
        full_name (str):
        job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckLog | Error]
     """


    kwargs = _get_kwargs(
        forge=forge,
full_name=full_name,
job_id=job_id,

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
    job_id: int,

) -> CheckLog | Error | None:
    """ Read the output of one CI job, on demand

     The output behind a `Check` that carries a `jobId`, as plain text: colour
    codes and carriage returns removed, never markup, so a client must render
    it as text. Whatever the forge already masks stays masked. Only the last
    256 KiB are returned; `truncated` says the start was cut.

    Only for a repository the dashboard tracks for you; any other answers 404
    without asking the forge.

    Fetched live on every call and never as part of a snapshot, since a log
    can be large and most are never opened. GitHub reads the job's log
    through its REST API (one request, then a short-lived download). Forgejo
    reads it through the job logs endpoint of its Actions API.

    A forge can refuse: the token may not read logs, the log may have
    expired, or the check may not be an Actions job at all. Those answer 403
    or 404 with a sentence a person can read.

    Args:
        forge (Forge):
        full_name (str):
        job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckLog | Error
     """


    return sync_detailed(
        client=client,
forge=forge,
full_name=full_name,
job_id=job_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    forge: Forge,
    full_name: str,
    job_id: int,

) -> Response[CheckLog | Error]:
    """ Read the output of one CI job, on demand

     The output behind a `Check` that carries a `jobId`, as plain text: colour
    codes and carriage returns removed, never markup, so a client must render
    it as text. Whatever the forge already masks stays masked. Only the last
    256 KiB are returned; `truncated` says the start was cut.

    Only for a repository the dashboard tracks for you; any other answers 404
    without asking the forge.

    Fetched live on every call and never as part of a snapshot, since a log
    can be large and most are never opened. GitHub reads the job's log
    through its REST API (one request, then a short-lived download). Forgejo
    reads it through the job logs endpoint of its Actions API.

    A forge can refuse: the token may not read logs, the log may have
    expired, or the check may not be an Actions job at all. Those answer 403
    or 404 with a sentence a person can read.

    Args:
        forge (Forge):
        full_name (str):
        job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckLog | Error]
     """


    kwargs = _get_kwargs(
        forge=forge,
full_name=full_name,
job_id=job_id,

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
    job_id: int,

) -> CheckLog | Error | None:
    """ Read the output of one CI job, on demand

     The output behind a `Check` that carries a `jobId`, as plain text: colour
    codes and carriage returns removed, never markup, so a client must render
    it as text. Whatever the forge already masks stays masked. Only the last
    256 KiB are returned; `truncated` says the start was cut.

    Only for a repository the dashboard tracks for you; any other answers 404
    without asking the forge.

    Fetched live on every call and never as part of a snapshot, since a log
    can be large and most are never opened. GitHub reads the job's log
    through its REST API (one request, then a short-lived download). Forgejo
    reads it through the job logs endpoint of its Actions API.

    A forge can refuse: the token may not read logs, the log may have
    expired, or the check may not be an Actions job at all. Those answer 403
    or 404 with a sentence a person can read.

    Args:
        forge (Forge):
        full_name (str):
        job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckLog | Error
     """


    return (await asyncio_detailed(
        client=client,
forge=forge,
full_name=full_name,
job_id=job_id,

    )).parsed
