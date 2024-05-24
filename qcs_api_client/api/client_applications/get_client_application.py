from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from retrying import retry

from ...types import Response
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.client_application import ClientApplication
from ...models.error import Error


def _get_kwargs(
    client_application_name: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/clientApplications/{client_application_name}".format(
            client_application_name=client_application_name,
        ),
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[ClientApplication, Error]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ClientApplication.from_dict(response.json())

        return response_200
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Union[ClientApplication, Error]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    client_application_name: str,
    *,
    client: httpx.Client,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ClientApplication, Error]]:
    """Get Client Application

     Get details of a specific Rigetti system component along with its latest and minimum supported
    versions.

    Args:
        client_application_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientApplication, Error]]
    """

    kwargs = _get_kwargs(
        client_application_name=client_application_name,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    client_application_name: str,
    *,
    client: httpx.Client,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ClientApplication, Error]]:
    kwargs = _get_kwargs(
        client_application_name=client_application_name,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    client_application_name: str,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ClientApplication, Error]]:
    """Get Client Application

     Get details of a specific Rigetti system component along with its latest and minimum supported
    versions.

    Args:
        client_application_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientApplication, Error]]
    """

    kwargs = _get_kwargs(
        client_application_name=client_application_name,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    client_application_name: str,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ClientApplication, Error]]:
    kwargs = _get_kwargs(
        client_application_name=client_application_name,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
