from typing import Any, Dict

import httpx
from retrying import retry

from ...models.check_client_application_request import CheckClientApplicationRequest
from ...models.check_client_application_response import CheckClientApplicationResponse
from ...types import Response
from ...util.errors import QCSHTTPStatusError, raise_for_status
from ...util.retry import DEFAULT_RETRY_ARGUMENTS


def _get_kwargs(
    *,
    client: httpx.Client,
    json_body: CheckClientApplicationRequest,
) -> Dict[str, Any]:
    url = "{}/v1/clientApplications:check".format(client.base_url)

    headers = {k: v for (k, v) in client.headers.items()}
    cookies = {k: v for (k, v) in client.cookies}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.timeout,
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> CheckClientApplicationResponse:
    raise_for_status(response)
    if response.status_code == 200:
        response_200 = CheckClientApplicationResponse.from_dict(response.json())

        return response_200
    else:
        raise QCSHTTPStatusError(
            f"Unexpected response: status code {response.status_code}", response=response, error=None
        )


def _build_response(*, response: httpx.Response) -> Response[CheckClientApplicationResponse]:
    """
    Construct the Response class from the raw ``httpx.Response``.
    """
    return Response.build_from_httpx_response(response=response, parse_function=_parse_response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
def sync(
    *,
    client: httpx.Client,
    json_body: CheckClientApplicationRequest,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[CheckClientApplicationResponse]:
    """Check Client Application

     Check the requested client application version against the latest and minimum version.

    Args:
        json_body (CheckClientApplicationRequest):

    Returns:
        Response[CheckClientApplicationResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body_dict: Dict,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[CheckClientApplicationResponse]:
    json_body = CheckClientApplicationRequest.from_dict(json_body_dict)

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: CheckClientApplicationRequest,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[CheckClientApplicationResponse]:
    """Check Client Application

     Check the requested client application version against the latest and minimum version.

    Args:
        json_body (CheckClientApplicationRequest):

    Returns:
        Response[CheckClientApplicationResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )
    kwargs.update(httpx_request_kwargs)
    response = await client.request(
        **kwargs,
    )

    return _build_response(response=response)


@retry(**DEFAULT_RETRY_ARGUMENTS)
async def asyncio_from_dict(
    *,
    client: httpx.AsyncClient,
    json_body_dict: Dict,
    httpx_request_kwargs: Dict[str, Any] = {},
) -> Response[CheckClientApplicationResponse]:
    json_body = CheckClientApplicationRequest.from_dict(json_body_dict)

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )
    kwargs.update(httpx_request_kwargs)
    response = client.request(
        **kwargs,
    )

    return _build_response(response=response)
