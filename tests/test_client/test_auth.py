from pathlib import Path
import respx
import pytest
import asyncio
from uuid import uuid4
from httpx import Response
from unittest.mock import patch

from qcs_api_client.client import QCSAuth, QCSAccountType, QCSClientConfiguration
from qcs_api_client.client._configuration.secrets import toml


@pytest.mark.parametrize(
    "execute_async",
    [
        (True,),
        (False,),
    ],
)
@respx.mock(assert_all_mocked=True)
def test_qcs_auth_refresh_token(fixture_directory: Path, execute_async: bool, respx_mock: respx.MockRouter = None):
    """
    Assert that the credential's token payload is written back to the file on update during the
    QCSAuth refresh flows.
    """

    configuration = QCSClientConfiguration.load(
        profile_name="staging1",
        settings_file_path=fixture_directory / "settings.toml",
        secrets_file_path=fixture_directory / "secrets.toml",
    )
    credentials_name = configuration.profile.credentials_name

    group_profile = configuration.profile.copy()
    group_profile.account_id = "group0"
    group_profile.account_type = QCSAccountType.group
    configuration.settings.profiles["my-group-profile"] = group_profile
    # Importantly here, the profile name is not the same as the credentials name (staging1).
    # The credentials update should be written to the credentials name, not profile name.
    configuration.profile_name = "my-group-profile"

    # Set the access token to a UUID to increase confidence in our assertion below that
    # the new token is indeed being updated.
    new_access_token = str(uuid4())
    response_mock = Response(200, json={"access_token": new_access_token})
    respx_mock.post(configuration.auth_server.token_url()).mock(return_value=response_mock)

    # Don't actually write the update to the fixture files.
    with patch.object(toml, "dump"):
        auth = QCSAuth(client_configuration=configuration)
        if execute_async:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(auth.async_refresh_token())
        else:
            auth.sync_refresh_token()

        assert "my-group-profile" not in configuration.secrets.credentials
        assert new_access_token == configuration.secrets.credentials[credentials_name].token_payload.access_token
        assert new_access_token == configuration.credentials.token_payload.access_token
