from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from tenacity import retry

from ...types import Response
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.validation_error import ValidationError
from ...models.endpoint import Endpoint
from ...models.error import Error


def _get_kwargs(
    quantum_processor_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/quantumProcessors/{quantum_processor_id}/endpoints:getDefault".format(
            quantum_processor_id=quantum_processor_id,
        ),
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Endpoint, Error, ValidationError]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Endpoint.from_dict(response.json())

        return response_200
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Union[Endpoint, Error, ValidationError]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    quantum_processor_id: str,
    *,
    client: httpx.Client,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Endpoint, Error, ValidationError]]:
    r"""Get Default Endpoint

     Retrieve the endpoint set as \"default\" for the given Quantum Processor.

    If no endpoint is set as the default, return \"not found.\"

    Args:
        quantum_processor_id (str): Public identifier for a quantum processor [example: Aspen-1]

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Endpoint, Error, ValidationError]]
    """

    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
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
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Endpoint, Error, ValidationError]]:
    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        client=client,
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
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Endpoint, Error, ValidationError]]:
    r"""Get Default Endpoint

     Retrieve the endpoint set as \"default\" for the given Quantum Processor.

    If no endpoint is set as the default, return \"not found.\"

    Args:
        quantum_processor_id (str): Public identifier for a quantum processor [example: Aspen-1]

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Endpoint, Error, ValidationError]]
    """

    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    quantum_processor_id: str,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Endpoint, Error, ValidationError]]:
    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
