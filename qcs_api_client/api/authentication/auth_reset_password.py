from http import HTTPStatus
from typing import Any, Dict, Union, cast

import httpx
from tenacity import retry

from ...types import Response
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.auth_reset_password_request import AuthResetPasswordRequest
from ...models.error import Error


def _get_kwargs(
    *,
    body: AuthResetPasswordRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth:resetPassword",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Any, Error]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    body: AuthResetPasswordRequest,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Any, Error]]:
    """Reset Password

     Reset the password using the user's existing password. Note, this is an authenticated route.

    Args:
        body (AuthResetPasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    *,
    client: httpx.Client,
    body: Dict,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Any, Error]]:
    kwargs = _get_kwargs(
        client=client,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    *,
    client: httpx.AsyncClient,
    body: AuthResetPasswordRequest,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Any, Error]]:
    """Reset Password

     Reset the password using the user's existing password. Note, this is an authenticated route.

    Args:
        body (AuthResetPasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    *,
    client: httpx.AsyncClient,
    body: Dict,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Any, Error]]:
    kwargs = _get_kwargs(
        client=client,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
