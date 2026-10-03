from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.health import Health
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/readyz",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Health | None:
    if response.status_code == 200:
        response_200 = Health.from_dict(response.json())



        return response_200

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Health]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | Health]:
    """ Readiness

     Answers 200 once the server can actually serve: the database answers
    a ping with its schema in place, and the first dashboard refresh has
    completed, or 30 seconds have passed since it started. The wait is
    bounded because how fast a forge answers is how fresh the data is,
    not whether the server can serve: a slow or unreachable forge must not
    keep the container unready. A refresh that finished with a forge
    unreachable counts, and a forge going unreachable afterwards never
    turns this into a 503. See forges[].reachable on the dashboard
    response for that. Before any account has signed in there is no
    refresh to wait for, so only the database is checked.

    The container's HEALTHCHECK probes this path (`/healthz` stays the
    cheap liveness answer), so Docker's single health state and Compose's
    `depends_on: condition: service_healthy` mean "ready", not just
    "started".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Health]
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

) -> Error | Health | None:
    """ Readiness

     Answers 200 once the server can actually serve: the database answers
    a ping with its schema in place, and the first dashboard refresh has
    completed, or 30 seconds have passed since it started. The wait is
    bounded because how fast a forge answers is how fresh the data is,
    not whether the server can serve: a slow or unreachable forge must not
    keep the container unready. A refresh that finished with a forge
    unreachable counts, and a forge going unreachable afterwards never
    turns this into a 503. See forges[].reachable on the dashboard
    response for that. Before any account has signed in there is no
    refresh to wait for, so only the database is checked.

    The container's HEALTHCHECK probes this path (`/healthz` stays the
    cheap liveness answer), so Docker's single health state and Compose's
    `depends_on: condition: service_healthy` mean "ready", not just
    "started".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Health
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | Health]:
    """ Readiness

     Answers 200 once the server can actually serve: the database answers
    a ping with its schema in place, and the first dashboard refresh has
    completed, or 30 seconds have passed since it started. The wait is
    bounded because how fast a forge answers is how fresh the data is,
    not whether the server can serve: a slow or unreachable forge must not
    keep the container unready. A refresh that finished with a forge
    unreachable counts, and a forge going unreachable afterwards never
    turns this into a 503. See forges[].reachable on the dashboard
    response for that. Before any account has signed in there is no
    refresh to wait for, so only the database is checked.

    The container's HEALTHCHECK probes this path (`/healthz` stays the
    cheap liveness answer), so Docker's single health state and Compose's
    `depends_on: condition: service_healthy` mean "ready", not just
    "started".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Health]
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

) -> Error | Health | None:
    """ Readiness

     Answers 200 once the server can actually serve: the database answers
    a ping with its schema in place, and the first dashboard refresh has
    completed, or 30 seconds have passed since it started. The wait is
    bounded because how fast a forge answers is how fresh the data is,
    not whether the server can serve: a slow or unreachable forge must not
    keep the container unready. A refresh that finished with a forge
    unreachable counts, and a forge going unreachable afterwards never
    turns this into a 503. See forges[].reachable on the dashboard
    response for that. Before any account has signed in there is no
    refresh to wait for, so only the database is checked.

    The container's HEALTHCHECK probes this path (`/healthz` stays the
    cheap liveness answer), so Docker's single health state and Compose's
    `depends_on: condition: service_healthy` mean "ready", not just
    "started".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Health
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
