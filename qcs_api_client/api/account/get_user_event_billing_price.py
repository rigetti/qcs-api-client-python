from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from tenacity import retry

from ...types import Response
from ...util.errors import raise_for_status
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.event_billing_price_rate import EventBillingPriceRate
from ...models.get_account_event_billing_price_request import (
    GetAccountEventBillingPriceRequest,
)
from ...models.error import Error


def _get_kwargs(
    user_id: str,
    *,
    body: GetAccountEventBillingPriceRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/users/{user_id}/eventBillingPrices:get".format(
            user_id=user_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Error, EventBillingPriceRate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EventBillingPriceRate.from_dict(response.json())

        return response_200
    else:
        raise_for_status(response)


def _build_response(*, response: httpx.Response) -> Response[Union[Error, EventBillingPriceRate]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    user_id: str,
    *,
    client: httpx.Client,
    body: GetAccountEventBillingPriceRequest,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, EventBillingPriceRate]]:
    """Retrieve `EventBillingPrice` for a user for a specific event. If no price is configured this
    operation will return a default `EventBillingPrice` for the specified `product`.

    Args:
        user_id (str):
        body (GetAccountEventBillingPriceRequest): Property `quantumProcessorId` is currently
            required for all `product`s, however in the future there may be `product`s that do not
            require a `quantumProcessorId`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, EventBillingPriceRate]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
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
    body: Dict,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, EventBillingPriceRate]]:
    kwargs = _get_kwargs(
        user_id=user_id,
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
    user_id: str,
    *,
    client: httpx.AsyncClient,
    body: GetAccountEventBillingPriceRequest,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, EventBillingPriceRate]]:
    """Retrieve `EventBillingPrice` for a user for a specific event. If no price is configured this
    operation will return a default `EventBillingPrice` for the specified `product`.

    Args:
        user_id (str):
        body (GetAccountEventBillingPriceRequest): Property `quantumProcessorId` is currently
            required for all `product`s, however in the future there may be `product`s that do not
            require a `quantumProcessorId`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, EventBillingPriceRate]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    user_id: str,
    *,
    client: httpx.AsyncClient,
    body: Dict,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, EventBillingPriceRate]]:
    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        body=body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
