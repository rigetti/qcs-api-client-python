import os
import pathlib
from pathlib import Path
from unittest.mock import create_autospec

import pytest
import respx
from httpx import Request, Response
from typing import cast
from qcs_api_client.client import build_async_client, build_sync_client
from qcs_api_client.client.auth import QCSAuth
from qcs_api_client.client._configuration import QCSClientConfiguration, QCSClientConfigurationError
from qcs_api_client.client._configuration.settings import _DEFAULT_AUTH_SERVER
from qcs_api_client.models.health import Health
from qcs_api_client.operations.sync import get_health
from qcs_api_client.operations.asyncio import get_health as asyncio_get_health


MOCK_URL = "http://mock.url"
FIXTURE_DIRECTORY = pathlib.Path(os.path.dirname(os.path.realpath(__file__)), "__fixtures__")


@pytest.fixture
def client_configuration(fixture_directory: Path) -> QCSClientConfiguration:
    client_configuration = QCSClientConfiguration.load(
        settings_file_path=fixture_directory / "settings.toml",
        secrets_file_path=fixture_directory / "secrets.toml",
    )
    client_configuration.profile.api_url = MOCK_URL
    return client_configuration


def test_initialization(client_configuration: QCSClientConfiguration):
    """
    Assert that the client can load settings and secrets from respective files.
    """

    assert client_configuration.profile_name == "staging1"
    assert client_configuration.profile.applications.cli.verbosity == "info"
    assert client_configuration.profile.auth_server_name == "staging"
    assert client_configuration.auth_server.client_id == "0oarkug104njPxvTZ0h7"
    assert client_configuration.profile.api_url == "http://mock.url"

    assert (
        client_configuration.credentials.access_token
        == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImNvdyIsImlhdCI6MTYwNTU1MzI2MH0.lRhv60Z5iN0w1g3uwDDi-cNAI4-qLIFkBCe-2__PSVo"
    )

    assert client_configuration.credentials.refresh_token == "refresh1"


def test_config_missing_auth_server():
    """
    Assert QCSClientConfigurationError raised if auth server does not exist.
    """

    client_configuration = QCSClientConfiguration.load(
        settings_file_path=FIXTURE_DIRECTORY / "settings.toml",
        secrets_file_path=FIXTURE_DIRECTORY / "secrets.toml",
        profile_name="missing_auth_server",
    )
    with pytest.raises(QCSClientConfigurationError):
        client_configuration.auth_server


def test_config_missing_credentials(fixture_directory: Path):
    """
    Assert QCSClientConfigurationError raised if profile does not exist.
    """

    client_configuration = QCSClientConfiguration.load(
        settings_file_path=fixture_directory / "settings.toml",
        secrets_file_path=fixture_directory / "secrets.toml",
        profile_name="doesntexist",
    )
    with pytest.raises(QCSClientConfigurationError):
        client_configuration.profile


def test_settings_file_does_not_exist(fixture_directory: Path):
    """
    Assert defaults populated if settings file does not exist
    """

    client_configuration = QCSClientConfiguration.load(
        settings_file_path=fixture_directory / "doesntexist.toml", secrets_file_path=fixture_directory / "secrets.toml"
    )
    assert client_configuration.auth_server.client_id == _DEFAULT_AUTH_SERVER.client_id
    assert client_configuration.auth_server.issuer == _DEFAULT_AUTH_SERVER.issuer

    assert client_configuration.profile_name == "default"
    assert client_configuration.credentials.refresh_token == "refresh"


def test_secrets_file_does_not_exist(fixture_directory: Path):
    """
    Assert defaults loaded if secrets file doesn't exist.
    """

    client_configuration = QCSClientConfiguration.load(
        settings_file_path=fixture_directory / "settings.toml",
        secrets_file_path=fixture_directory / "doesntexist.toml",
        profile_name="staging1",
    )

    client_configuration.profile.api_url = MOCK_URL
    client_configuration.profile.credentials_name = "default"

    assert client_configuration.credentials.token_payload is None
    assert client_configuration.credentials.access_token is None
    assert client_configuration.credentials.refresh_token is None


def test_env_overrides(monkeypatch):
    """
    Assert that certain values can be overridden via environment variables.
    """
    monkeypatch.setenv("QCS_SECRETS_FILE_PATH", "secrets-path.file")
    monkeypatch.setenv("QCS_SETTINGS_FILE_PATH", "settings-path.file")
    monkeypatch.setenv("QCS_SETTINGS_API_URL", "http://api.mock")
    monkeypatch.setenv("QCS_SETTINGS_APPLICATIONS_CLI_VERBOSITY", "fatal")

    client_configuration = QCSClientConfiguration.load()

    assert client_configuration.secrets.file_path == Path("secrets-path.file")
    assert client_configuration.settings.file_path == Path("settings-path.file")
    assert client_configuration.profile.api_url == "http://api.mock"
    assert client_configuration.profile.applications.cli.verbosity == "fatal"


@respx.mock(assert_all_mocked=True)
def test_sync_client(client_configuration: QCSClientConfiguration, respx_mock: respx.MockRouter = None):
    """
    Assert that a sync client can be constructed and make a call with authorization header.
    """

    with build_sync_client(configuration=client_configuration) as client:
        target_route = respx_mock.get(MOCK_URL).mock(return_value=Response(200))
        response = client.get(MOCK_URL)
        assert target_route.called
        assert response.status_code == 200
        access_token = client_configuration.credentials.access_token
        assert response.request.headers.get("Authorization") == f"Bearer {access_token}"


@respx.mock(assert_all_mocked=True)
def test_sync_client_api_call(client_configuration: QCSClientConfiguration, respx_mock: respx.MockRouter = None):
    """Assert that a generated request function can be called with a sync client."""

    def assert_request(request: Request):
        assert request.headers.get("foo") == "bar"
        return Response(200, json=dict(status="PASS"))

    respx_mock.get(MOCK_URL).mock(side_effect=assert_request)
    with build_sync_client(configuration=client_configuration) as client:
        response = get_health(client=client, httpx_request_kwargs={"headers": {"foo": "bar"}})
        assert response.status_code == 200
        assert response.parsed == Health(status="PASS")


@respx.mock(assert_all_mocked=True)
def test_sync_client_api_call_empty_config(fixture_directory: Path, respx_mock: respx.MockRouter = None):
    """Assert that the client makes sync requests with authentication if configuration is empty."""

    client_configuration = QCSClientConfiguration.load(
        settings_file_path=fixture_directory / "doesntexist.toml",
        secrets_file_path=fixture_directory / "doesntexist.toml",
    )

    def assert_request(request: Request):
        return Response(200, json=dict(status="PASS"))

    respx_mock.get("https://api.qcs.rigetti.com/").mock(side_effect=assert_request)
    with build_sync_client(configuration=client_configuration) as client:
        qcs_auth = cast(QCSAuth, client.auth)
        qcs_auth.sync_refresh_token = create_autospec(qcs_auth.sync_refresh_token)
        response = get_health(client=client)
        assert response.status_code == 200
        assert response.parsed == Health(status="PASS")

        assert response.request.headers.get("Authorization") is None
        assert qcs_auth.sync_refresh_token.call_count == 0


@respx.mock(assert_all_mocked=True)
@pytest.mark.asyncio
async def test_async_client(client_configuration: QCSClientConfiguration, respx_mock: respx.MockRouter = None):
    """
    Assert that an async client can be constructed and make a call with authorization header.
    """
    async with build_async_client(configuration=client_configuration) as client:
        target_route = respx_mock.get(MOCK_URL).mock(return_value=Response(200))
        response = await client.get(MOCK_URL)
        assert target_route.called
        assert response.status_code == 200
        access_token = client_configuration.credentials.access_token
        assert response.request.headers.get("Authorization") == f"Bearer {access_token}"


@respx.mock(assert_all_mocked=True)
async def test_async_client_api_call_empty_config(fixture_directory: Path, respx_mock: respx.MockRouter = None):
    """Assert that the client makes async requests with authentication if configuration is empty."""

    client_configuration = QCSClientConfiguration.load(
        settings_file_path=fixture_directory / "doesntexist.toml",
        secrets_file_path=fixture_directory / "doesntexist.toml",
    )

    def assert_request(request: Request):
        return Response(200, json=dict(status="PASS"))

    respx_mock.get("https://api.qcs.rigetti.com/").mock(side_effect=assert_request)
    async with build_async_client(configuration=client_configuration) as client:
        qcs_auth = cast(QCSAuth, client.auth)
        qcs_auth.async_refresh_token = create_autospec(qcs_auth.async_refresh_token)
        response = await asyncio_get_health(client=client)
        assert response.status_code == 200
        assert response.parsed == Health(status="PASS")

        assert response.request.headers.get("Authorization") is None
        assert qcs_auth.async_refresh_token.call_count == 0
