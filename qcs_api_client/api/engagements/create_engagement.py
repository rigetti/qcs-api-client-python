from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from retrying import retry

from ...types import Response, UNSET
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.create_engagement_request import CreateEngagementRequest
from ...models.engagement_with_credentials import EngagementWithCredentials
from ...models.error import Error
from ...types import Unset
from ...models.account_type import AccountType


def _get_kwargs(
    *,
    body: CreateEngagementRequest,
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
        "url": "/v1/engagements",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Any, EngagementWithCredentials, Error]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EngagementWithCredentials.from_dict(response.json())

        return response_200
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Union[Any, EngagementWithCredentials, Error]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    body: CreateEngagementRequest,
    x_qcs_account_id: Union[Unset, str] = UNSET,
    x_qcs_account_type: Union[Unset, AccountType] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Any, EngagementWithCredentials, Error]]:
    """Create Engagement

     Create a new engagement using the specified parameters.

    At least one of the following parameters must be supplied:
    - **endpointId**: The ID of the endpoint on which to engage.
    - **quantumProcessorId**: The ID of the quantum processor on which to engage, allowing the
        service to select a default endpoint. Ignored if **endpointId** is set.

    Args:
        x_qcs_account_id (Union[Unset, str]): userId for `accountType` "user", group name for
            `accountType` "group".
        x_qcs_account_type (Union[Unset, AccountType]): There are two types of accounts within
            QCS: user (representing a single user in Okta) and group
            (representing one or more users in Okta).
        body (CreateEngagementRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EngagementWithCredentials, Error]]
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
) -> Response[Union[Any, EngagementWithCredentials, Error]]:
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
    body: CreateEngagementRequest,
    x_qcs_account_id: Union[Unset, str] = UNSET,
    x_qcs_account_type: Union[Unset, AccountType] = UNSET,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Any, EngagementWithCredentials, Error]]:
    """Create Engagement

     Create a new engagement using the specified parameters.

    At least one of the following parameters must be supplied:
    - **endpointId**: The ID of the endpoint on which to engage.
    - **quantumProcessorId**: The ID of the quantum processor on which to engage, allowing the
        service to select a default endpoint. Ignored if **endpointId** is set.

    Args:
        x_qcs_account_id (Union[Unset, str]): userId for `accountType` "user", group name for
            `accountType` "group".
        x_qcs_account_type (Union[Unset, AccountType]): There are two types of accounts within
            QCS: user (representing a single user in Okta) and group
            (representing one or more users in Okta).
        body (CreateEngagementRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EngagementWithCredentials, Error]]
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
) -> Response[Union[Any, EngagementWithCredentials, Error]]:
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
