from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from tenacity import retry

from ...types import Response
from ...util.errors import raise_for_status
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.billing_customer import BillingCustomer
from ...models.error import Error


def _get_kwargs(
    group_name: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/groups/{group_name}/billingCustomer".format(
            group_name=group_name,
        ),
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[BillingCustomer, Error]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BillingCustomer.from_dict(response.json())

        return response_200
    else:
        raise_for_status(response)


def _build_response(*, response: httpx.Response) -> Response[Union[BillingCustomer, Error]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    group_name: str,
    *,
    client: httpx.Client,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[BillingCustomer, Error]]:
    """Retrieve billing customer for a QCS group account.

    Args:
        group_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillingCustomer, Error]]
    """

    kwargs = _get_kwargs(
        group_name=group_name,
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
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[BillingCustomer, Error]]:
    kwargs = _get_kwargs(
        group_name=group_name,
        client=client,
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
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[BillingCustomer, Error]]:
    """Retrieve billing customer for a QCS group account.

    Args:
        group_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BillingCustomer, Error]]
    """

    kwargs = _get_kwargs(
        group_name=group_name,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    group_name: str,
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[BillingCustomer, Error]]:
    kwargs = _get_kwargs(
        group_name=group_name,
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
