from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from retrying import retry

from ...types import Response
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.translate_native_quil_to_encrypted_binary_response import (
    TranslateNativeQuilToEncryptedBinaryResponse,
)
from ...models.validation_error import ValidationError
from ...models.translate_native_quil_to_encrypted_binary_request import (
    TranslateNativeQuilToEncryptedBinaryRequest,
)
from ...models.error import Error


def _get_kwargs(
    quantum_processor_id: str,
    *,
    body: TranslateNativeQuilToEncryptedBinaryRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/quantumProcessors/{quantum_processor_id}:translateNativeQuilToEncryptedBinary".format(
            quantum_processor_id=quantum_processor_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, response: httpx.Response
) -> Union[Error, TranslateNativeQuilToEncryptedBinaryResponse, ValidationError]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TranslateNativeQuilToEncryptedBinaryResponse.from_dict(response.json())

        return response_200
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Error, TranslateNativeQuilToEncryptedBinaryResponse, ValidationError]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    quantum_processor_id: str,
    *,
    client: httpx.Client,
    body: TranslateNativeQuilToEncryptedBinaryRequest,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, TranslateNativeQuilToEncryptedBinaryResponse, ValidationError]]:
    """Translate Native Quil To Encrypted Binary

     Compile Rigetti-native Quil code to encrypted binary form, ready for execution on a
    Rigetti Quantum Processor.

    Args:
        quantum_processor_id (str): Public identifier for a quantum processor [example: Aspen-1]
        body (TranslateNativeQuilToEncryptedBinaryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, TranslateNativeQuilToEncryptedBinaryResponse, ValidationError]]
    """

    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        body=body,
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
    body: Dict,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, TranslateNativeQuilToEncryptedBinaryResponse, ValidationError]]:
    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
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
    quantum_processor_id: str,
    *,
    client: httpx.AsyncClient,
    body: TranslateNativeQuilToEncryptedBinaryRequest,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, TranslateNativeQuilToEncryptedBinaryResponse, ValidationError]]:
    """Translate Native Quil To Encrypted Binary

     Compile Rigetti-native Quil code to encrypted binary form, ready for execution on a
    Rigetti Quantum Processor.

    Args:
        quantum_processor_id (str): Public identifier for a quantum processor [example: Aspen-1]
        body (TranslateNativeQuilToEncryptedBinaryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, TranslateNativeQuilToEncryptedBinaryResponse, ValidationError]]
    """

    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    quantum_processor_id: str,
    *,
    client: httpx.AsyncClient,
    body: Dict,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, TranslateNativeQuilToEncryptedBinaryResponse, ValidationError]]:
    kwargs = _get_kwargs(
        quantum_processor_id=quantum_processor_id,
        client=client,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
