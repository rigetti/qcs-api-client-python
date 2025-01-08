from http import HTTPStatus
from typing import Any, Dict, Union

import httpx
from tenacity import retry

from ...types import Response
from ...util.errors import QCSHTTPStatusError
from ...util.retry import DEFAULT_RETRY_ARGUMENTS

from ...models.viewer_user_onboarding_completed import ViewerUserOnboardingCompleted
from ...models.error import Error


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/viewer/onboardingCompleted",
    }

    return _kwargs


def _parse_response(*, response: httpx.Response) -> Union[Error, ViewerUserOnboardingCompleted]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ViewerUserOnboardingCompleted.from_dict(response.json())

        return response_200
    else:
        raise QCSHTTPStatusError(f"Unexpected response: status code {response.status_code}")


def _build_response(*, response: httpx.Response) -> Response[Union[Error, ViewerUserOnboardingCompleted]]:
    """Construct the Response class from the raw ``httpx.Response``."""
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ViewerUserOnboardingCompleted]]:
    """Get the onboarding status of the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ViewerUserOnboardingCompleted]]
    """

    kwargs = _get_kwargs()
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync_from_dict(
    *,
    client: httpx.Client,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ViewerUserOnboardingCompleted]]:
    kwargs = _get_kwargs(
        client=client,
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
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ViewerUserOnboardingCompleted]]:
    """Get the onboarding status of the authenticated user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ViewerUserOnboardingCompleted]]
    """

    kwargs = _get_kwargs()
    kwargs.update(httpx_request_kwargs)
    response = await client.request(**kwargs)
    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    *,
    client: httpx.AsyncClient,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[Union[Error, ViewerUserOnboardingCompleted]]:
    kwargs = _get_kwargs(
        client=client,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)
