from http import HTTPStatus
from typing import Any, Dict, Union, cast

import httpx
from tenacity import retry

from ...types import Response
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.error import Error


def _get_kwargs(
    announcement_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/v1/viewer/announcements/{announcement_id}".format(
            announcement_id=announcement_id,
        ),
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Any, Error]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Error]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    announcement_id: int,
    *,
    client: httpx.Client,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Any, Error]]:
    """Dismiss an announcement for an authenticating user, indicating that they do not want to see it
    again.

    Args:
        announcement_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        announcement_id=announcement_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    announcement_id: int,
    *,
    client: httpx.Client,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Any, Error]]:
    kwargs = _get_kwargs(
        announcement_id=announcement_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    announcement_id: int,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Any, Error]]:
    """Dismiss an announcement for an authenticating user, indicating that they do not want to see it
    again.

    Args:
        announcement_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        announcement_id=announcement_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    announcement_id: int,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Any, Error]]:
    kwargs = _get_kwargs(
        announcement_id=announcement_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
