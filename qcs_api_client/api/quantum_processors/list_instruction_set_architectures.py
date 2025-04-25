from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from tenacity import retry

from ...types import Response, UNSET
from ...util.errors import raise_for_status
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.list_instruction_set_architecture_response import (
    ListInstructionSetArchitectureResponse,
)
from ...models.validation_error import ValidationError
from ...types import Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = 5,
    page_token: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/instructionSetArchitectures",
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[ListInstructionSetArchitectureResponse, ValidationError]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListInstructionSetArchitectureResponse.from_dict(response.json())

        return response_200
    else:
        raise_for_status(response)


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ListInstructionSetArchitectureResponse, ValidationError]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    page_size: Union[Unset, int] = 5,
    page_token: Union[Unset, str] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ListInstructionSetArchitectureResponse, ValidationError]]:
    """List Instruction Set Architectures

     Retrieve all Instruction Set Architectures available to the user.

    Args:
        page_size (Union[Unset, int]):  Default: 5.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListInstructionSetArchitectureResponse, ValidationError]]
    """

    kwargs = _get_kwargs(
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
    *,
    client: httpx.Client,
    page_size: Union[Unset, int] = 5,
    page_token: Union[Unset, str] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ListInstructionSetArchitectureResponse, ValidationError]]:
    kwargs = _get_kwargs(
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
    *,
    client: httpx.AsyncClient,
    page_size: Union[Unset, int] = 5,
    page_token: Union[Unset, str] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ListInstructionSetArchitectureResponse, ValidationError]]:
    """List Instruction Set Architectures

     Retrieve all Instruction Set Architectures available to the user.

    Args:
        page_size (Union[Unset, int]):  Default: 5.
        page_token (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListInstructionSetArchitectureResponse, ValidationError]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    *,
    client: httpx.AsyncClient,
    page_size: Union[Unset, int] = 5,
    page_token: Union[Unset, str] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[ListInstructionSetArchitectureResponse, ValidationError]]:
    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_token=page_token,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
