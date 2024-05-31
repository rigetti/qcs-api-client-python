from datetime import timedelta
from http import HTTPStatus
from .errors import QCSHTTPStatusError
from tenacity import stop_after_attempt, wait_random_exponential, retry_if_exception


DEFAULT_RETRY_STATUS_CODES = {
    HTTPStatus.BAD_GATEWAY,
    HTTPStatus.SERVICE_UNAVAILABLE,
    HTTPStatus.GATEWAY_TIMEOUT,
}


def _is_exception_retryable(exception):
    if isinstance(exception, QCSHTTPStatusError):
        return exception.response.status_code in DEFAULT_RETRY_STATUS_CODES
    return False


DEFAULT_RETRY_ARGUMENTS = {
    "stop": stop_after_attempt(3),
    "wait": wait_random_exponential(multiplier=200, min=timedelta(milliseconds=1), max=timedelta(seconds=1)),
    "reraise": True,
    "retry": retry_if_exception(_is_exception_retryable),
}
