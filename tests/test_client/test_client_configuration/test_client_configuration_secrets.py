from pathlib import Path

from qcs_api_client.client._configuration.secrets import QCSClientConfigurationSecrets, TokenPayload


def test_load_valid_secrets(fixture_directory: Path) -> QCSClientConfigurationSecrets:
    """
    Test loading the valid secrets from the fixture file.

    Note that this test is also used directly by other tests out of convenience.
    """
    return QCSClientConfigurationSecrets.parse_file(fixture_directory / "secrets.toml")


def test_secrets_dict():
    """
    Assert that the secrets file path is not serialized into its dict.
    """
    secrets = QCSClientConfigurationSecrets(credentials={})
    assert secrets.dict() == dict(credentials={})


def test_update_token_payload(fixture_directory: Path):
    """
    Assert that the credential's token payload is written back to the file on update.
    """
    secrets = test_load_valid_secrets(fixture_directory)
    secrets.update_token(credentials_name="new_credentials", token=TokenPayload(access_token="new_access_token"))

    assert "new_credentials" in secrets.credentials
    assert secrets.credentials["new_credentials"].token_payload.access_token == "new_access_token"

    reloaded_secrets = test_load_valid_secrets(fixture_directory)
    assert "new_credentials" in reloaded_secrets.credentials
    assert reloaded_secrets.credentials["new_credentials"].token_payload.access_token == "new_access_token"
