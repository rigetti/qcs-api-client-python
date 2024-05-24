from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from retrying import retry

from ...types import Response, UNSET
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.reservation import Reservation
from ...models.error import Error
from ...models.create_reservation_request import CreateReservationRequest
from ...types import Unset
from ...models.account_type import AccountType


def _get_kwargs(
    *,
    body: CreateReservationRequest,
    x_qcs_account_id: Union[Unset, str] = UNSET,
    x_qcs_account_type: Union[Unset, AccountType] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_qcs_account_id, Unset):
        headers["X-QCS-ACCOUNT-ID"] = x_qcs_account_id

    if not isinstance(x_qcs_account_type, Unset):
        headers["X-QCS-ACCOUNT-TYPE"] = str(x_qcs_account_type)

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/reservations",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Error, Reservation]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Reservation.from_dict(response.json())

        return response_201
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Union[Error, Reservation]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    body: CreateReservationRequest,
    x_qcs_account_id: Union[Unset, str] = UNSET,
    x_qcs_account_type: Union[Unset, AccountType] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, Reservation]]:
    r"""Create Reservation

     Create a new reservation.

    The following precedence applies when specifying the reservation subject account
    ID and type:
    * request body `accountId` field, or if unset then `X-QCS-ACCOUNT-ID` header,
    or if unset then requesting user's ID.
    * request body `accountType` field, or if unset then `X-QCS-ACCOUNT-TYPE`
    header, or if unset then \"user\" type.

    Args:
        x_qcs_account_id (Union[Unset, str]): userId for `accountType` "user", group name for
            `accountType` "group".
        x_qcs_account_type (Union[Unset, AccountType]): There are two types of accounts within
            QCS: user (representing a single user in Okta) and group
            (representing one or more users in Okta).
        body (CreateReservationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Reservation]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_qcs_account_id=x_qcs_account_id,
        x_qcs_account_type=x_qcs_account_type,
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
    x_qcs_account_id: Union[Unset, str] = UNSET,
    x_qcs_account_type: Union[Unset, AccountType] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, Reservation]]:
    kwargs = _get_kwargs(
        client=client,
        body=body,
        x_qcs_account_id=x_qcs_account_id,
        x_qcs_account_type=x_qcs_account_type,
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
    body: CreateReservationRequest,
    x_qcs_account_id: Union[Unset, str] = UNSET,
    x_qcs_account_type: Union[Unset, AccountType] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, Reservation]]:
    r"""Create Reservation

     Create a new reservation.

    The following precedence applies when specifying the reservation subject account
    ID and type:
    * request body `accountId` field, or if unset then `X-QCS-ACCOUNT-ID` header,
    or if unset then requesting user's ID.
    * request body `accountType` field, or if unset then `X-QCS-ACCOUNT-TYPE`
    header, or if unset then \"user\" type.

    Args:
        x_qcs_account_id (Union[Unset, str]): userId for `accountType` "user", group name for
            `accountType` "group".
        x_qcs_account_type (Union[Unset, AccountType]): There are two types of accounts within
            QCS: user (representing a single user in Okta) and group
            (representing one or more users in Okta).
        body (CreateReservationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Reservation]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_qcs_account_id=x_qcs_account_id,
        x_qcs_account_type=x_qcs_account_type,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    *,
    client: httpx.AsyncClient,
    body: Dict,
    x_qcs_account_id: Union[Unset, str] = UNSET,
    x_qcs_account_type: Union[Unset, AccountType] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, Reservation]]:
    kwargs = _get_kwargs(
        client=client,
        body=body,
        x_qcs_account_id=x_qcs_account_id,
        x_qcs_account_type=x_qcs_account_type,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
