from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from tenacity import retry

from ...types import Response, UNSET
from ...util.errors import raise_for_status
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...types import Unset
from ...models.error import Error
from ...models.list_account_billing_invoices_response import (
    ListAccountBillingInvoicesResponse,
)


def _get_kwargs(
    group_name: str,
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
        "url": "/v1/groups/{group_name}/billingInvoices".format(
            group_name=group_name,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Error, ListAccountBillingInvoicesResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListAccountBillingInvoicesResponse.from_dict(response.json())

        return response_200
    else:
        raise_for_status(response)


def _build_response(*, response: httpx.Response) -> Response[Union[Error, ListAccountBillingInvoicesResponse]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    group_name: str,
    *,
    client: httpx.Client,
    page_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ListAccountBillingInvoicesResponse]]:
    """Retrieve billing invoices for a QCS group account.

    Args:
        group_name (str):
        page_token (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ListAccountBillingInvoicesResponse]]
    """

    kwargs = _get_kwargs(
        group_name=group_name,
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
    group_name: str,
    *,
    client: httpx.Client,
    page_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ListAccountBillingInvoicesResponse]]:
    kwargs = _get_kwargs(
        group_name=group_name,
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
    group_name: str,
    *,
    client: httpx.AsyncClient,
    page_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ListAccountBillingInvoicesResponse]]:
    """Retrieve billing invoices for a QCS group account.

    Args:
        group_name (str):
        page_token (Union[Unset, str]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ListAccountBillingInvoicesResponse]]
    """

    kwargs = _get_kwargs(
        group_name=group_name,
        page_token=page_token,
        page_size=page_size,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    group_name: str,
    *,
    client: httpx.AsyncClient,
    page_token: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ListAccountBillingInvoicesResponse]]:
    kwargs = _get_kwargs(
        group_name=group_name,
        client=client,
        page_token=page_token,
        page_size=page_size,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
