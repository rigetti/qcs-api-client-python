from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from tenacity import retry

from ...types import Response
from ...util.errors import raise_for_status
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.reservation import Reservation
from ...models.error import Error


def _get_kwargs(
    reservation_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/v1/reservations/{reservation_id}".format(
            reservation_id=reservation_id,
        ),
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Error, Reservation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Reservation.from_dict(response.json())

        return response_200
    else:
        raise_for_status(response)


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Reservation]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    reservation_id: int,
    *,
    client: httpx.Client,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, Reservation]]:
    """Delete Reservation

     Cancel an existing reservation for the user.

    Args:
        reservation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Reservation]]
    """

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    reservation_id: int,
    *,
    client: httpx.Client,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, Reservation]]:
    kwargs = _get_kwargs(
        reservation_id=reservation_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    reservation_id: int,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, Reservation]]:
    """Delete Reservation

     Cancel an existing reservation for the user.

    Args:
        reservation_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Reservation]]
    """

    kwargs = _get_kwargs(
        reservation_id=reservation_id,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    reservation_id: int,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, Reservation]]:
    kwargs = _get_kwargs(
        reservation_id=reservation_id,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
