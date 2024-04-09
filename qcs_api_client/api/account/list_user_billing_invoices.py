from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from retrying import retry

from ...types import Response, UNSET
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.list_account_billing_invoices_response import (
    ListAccountBillingInvoicesResponse,
)
from ...models.error import Error
from ...types import Unset


def _get_kwargs(
    user_id: str,
    *,
    page_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageToken"] = page_token

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/billingInvoices".format(
            user_id=user_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Error, ListAccountBillingInvoicesResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListAccountBillingInvoicesResponse.from_dict(response.json())

        return response_200
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Union[Error, ListAccountBillingInvoicesResponse]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    user_id: str,
    *,
    client: httpx.Client,
    page_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ListAccountBillingInvoicesResponse]]:
    """Retrieve billing invoices for a QCS user account.

    Args:
        user_id (str):
        page_token (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ListAccountBillingInvoicesResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        page_token=page_token,
        page_size=page_size,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    user_id: str,
    *,
    client: httpx.Client,
    page_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ListAccountBillingInvoicesResponse]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        page_token=page_token,
        page_size=page_size,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio(
    user_id: str,
    *,
    client: httpx.AsyncClient,
    page_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ListAccountBillingInvoicesResponse]]:
    """Retrieve billing invoices for a QCS user account.

    Args:
        user_id (str):
        page_token (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ListAccountBillingInvoicesResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        page_token=page_token,
        page_size=page_size,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    user_id: str,
    *,
    client: httpx.AsyncClient,
    page_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ListAccountBillingInvoicesResponse]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        page_token=page_token,
        page_size=page_size,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
