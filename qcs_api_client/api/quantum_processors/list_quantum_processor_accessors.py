from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from retrying import retry

from ...types import Response, UNSET
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.validation_error import ValidationError
from ...models.list_quantum_processor_accessors_response import (
    ListQuantumProcessorAccessorsResponse,
)
from ...types import Unset


def _get_kwargs(
    quantum_processor_id: str,
    *,
    page_size: Union[Unset, int] = 10,
    page_token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/quantumProcessors/{quantum_processor_id}/accessors".format(
            quantum_processor_id=quantum_processor_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[ListQuantumProcessorAccessorsResponse, ValidationError]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListQuantumProcessorAccessorsResponse.from_dict(response.json())

        return response_200
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ListQuantumProcessorAccessorsResponse, ValidationError]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    quantum_processor_id: str,
    *,
    client: httpx.Client,
    page_size: Union[Unset, int] = 10,
    page_token: Union[Unset, str] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ListQuantumProcessorAccessorsResponse, ValidationError]]:
    """List Quantum Processor Accessors

     List all means of accessing a QuantumProcessor available to the user.

    Args:
        quantum_processor_id (str): Public identifier for a quantum processor [example: Aspen-1]
        page_size (Union[Unset, int]):  Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListQuantumProcessorAccessorsResponse, ValidationError]]
    """

    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    quantum_processor_id: str,
    *,
    client: httpx.Client,
    page_size: Union[Unset, int] = 10,
    page_token: Union[Unset, str] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ListQuantumProcessorAccessorsResponse, ValidationError]]:
    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    quantum_processor_id: str,
    *,
    client: httpx.AsyncClient,
    page_size: Union[Unset, int] = 10,
    page_token: Union[Unset, str] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ListQuantumProcessorAccessorsResponse, ValidationError]]:
    """List Quantum Processor Accessors

     List all means of accessing a QuantumProcessor available to the user.

    Args:
        quantum_processor_id (str): Public identifier for a quantum processor [example: Aspen-1]
        page_size (Union[Unset, int]):  Default: 10.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListQuantumProcessorAccessorsResponse, ValidationError]]
    """

    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    quantum_processor_id: str,
    *,
    client: httpx.AsyncClient,
    page_size: Union[Unset, int] = 10,
    page_token: Union[Unset, str] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ListQuantumProcessorAccessorsResponse, ValidationError]]:
    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
