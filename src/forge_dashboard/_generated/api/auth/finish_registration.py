from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.session_user import SessionUser
from ...models.web_authn_ceremony_options import WebAuthnCeremonyOptions
from typing import cast



def _get_kwargs(
    *,
    body: WebAuthnCeremonyOptions,
    username: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["username"] = username


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/register/finish",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SessionUser | None:
    if response.status_code == 200:
        response_200 = SessionUser.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SessionUser]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WebAuthnCeremonyOptions,
    username: str,

) -> Response[Error | SessionUser]:
    """ Complete a passkey registration ceremony

    Args:
        username (str):
        body (WebAuthnCeremonyOptions): The WebAuthn specification's own JSON shape for
            `PublicKeyCredentialCreationOptions`/`PublicKeyCredentialRequestOptions`
            (the begin responses) and `PublicKeyCredential`
            (the finish request bodies) — passed through to and from the
            browser's own `navigator.credentials` API untouched, so this
            contract intentionally doesn't re-model WebAuthn's own schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SessionUser]
     """


    kwargs = _get_kwargs(
        body=body,
username=username,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: WebAuthnCeremonyOptions,
    username: str,

) -> Error | SessionUser | None:
    """ Complete a passkey registration ceremony

    Args:
        username (str):
        body (WebAuthnCeremonyOptions): The WebAuthn specification's own JSON shape for
            `PublicKeyCredentialCreationOptions`/`PublicKeyCredentialRequestOptions`
            (the begin responses) and `PublicKeyCredential`
            (the finish request bodies) — passed through to and from the
            browser's own `navigator.credentials` API untouched, so this
            contract intentionally doesn't re-model WebAuthn's own schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SessionUser
     """


    return sync_detailed(
        client=client,
body=body,
username=username,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WebAuthnCeremonyOptions,
    username: str,

) -> Response[Error | SessionUser]:
    """ Complete a passkey registration ceremony

    Args:
        username (str):
        body (WebAuthnCeremonyOptions): The WebAuthn specification's own JSON shape for
            `PublicKeyCredentialCreationOptions`/`PublicKeyCredentialRequestOptions`
            (the begin responses) and `PublicKeyCredential`
            (the finish request bodies) — passed through to and from the
            browser's own `navigator.credentials` API untouched, so this
            contract intentionally doesn't re-model WebAuthn's own schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SessionUser]
     """


    kwargs = _get_kwargs(
        body=body,
username=username,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: WebAuthnCeremonyOptions,
    username: str,

) -> Error | SessionUser | None:
    """ Complete a passkey registration ceremony

    Args:
        username (str):
        body (WebAuthnCeremonyOptions): The WebAuthn specification's own JSON shape for
            `PublicKeyCredentialCreationOptions`/`PublicKeyCredentialRequestOptions`
            (the begin responses) and `PublicKeyCredential`
            (the finish request bodies) — passed through to and from the
            browser's own `navigator.credentials` API untouched, so this
            contract intentionally doesn't re-model WebAuthn's own schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SessionUser
     """


    return (await asyncio_detailed(
        client=client,
body=body,
username=username,

    )).parsed
