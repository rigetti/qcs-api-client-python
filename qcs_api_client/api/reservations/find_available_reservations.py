from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from retrying import retry
from rfc3339 import rfc3339

from ...types import Response, UNSET
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.find_available_reservations_response import (
    FindAvailableReservationsResponse,
)
import datetime
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    *,
    page_size: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    quantum_processor_id: str,
    start_time_from: datetime.datetime,
    duration: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params["quantumProcessorId"] = quantum_processor_id

    assert start_time_from.tzinfo is not None, "Datetime must have timezone information"
    json_start_time_from = rfc3339(start_time_from)

    params["startTimeFrom"] = json_start_time_from

    params["duration"] = duration

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/reservations:findAvailable",
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Error, FindAvailableReservationsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FindAvailableReservationsResponse.from_dict(response.json())

        return response_200
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Union[Error, FindAvailableReservationsResponse]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    page_size: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    quantum_processor_id: str,
    start_time_from: datetime.datetime,
    duration: str,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, FindAvailableReservationsResponse]]:
    """Find Available Reservations

     List currently available reservations on the requested Rigetti quantum computer.

    Args:
        page_size (Union[Unset, int]):
        page_token (Union[Unset, str]):
        quantum_processor_id (str):
        start_time_from (datetime.datetime):
        duration (str): Formatted as specified for golang
            https://golang.org/pkg/time/#ParseDuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FindAvailableReservationsResponse]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        quantum_processor_id=quantum_processor_id,
        start_time_from=start_time_from,
        duration=duration,
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
    page_size: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    quantum_processor_id: str,
    start_time_from: datetime.datetime,
    duration: str,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, FindAvailableReservationsResponse]]:
    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_token=page_token,
        quantum_processor_id=quantum_processor_id,
        start_time_from=start_time_from,
        duration=duration,
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
    page_size: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    quantum_processor_id: str,
    start_time_from: datetime.datetime,
    duration: str,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, FindAvailableReservationsResponse]]:
    """Find Available Reservations

     List currently available reservations on the requested Rigetti quantum computer.

    Args:
        page_size (Union[Unset, int]):
        page_token (Union[Unset, str]):
        quantum_processor_id (str):
        start_time_from (datetime.datetime):
        duration (str): Formatted as specified for golang
            https://golang.org/pkg/time/#ParseDuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, FindAvailableReservationsResponse]]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        page_token=page_token,
        quantum_processor_id=quantum_processor_id,
        start_time_from=start_time_from,
        duration=duration,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    *,
    client: httpx.AsyncClient,
    page_size: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    quantum_processor_id: str,
    start_time_from: datetime.datetime,
    duration: str,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, FindAvailableReservationsResponse]]:
    kwargs = _get_kwargs(
        client=client,
        page_size=page_size,
        page_token=page_token,
        quantum_processor_id=quantum_processor_id,
        start_time_from=start_time_from,
        duration=duration,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
