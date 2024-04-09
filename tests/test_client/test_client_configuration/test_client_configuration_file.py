from pathlib import Path

import toml
from pydantic_settings import SettingsConfigDict

from qcs_api_client.client._configuration.file import QCSClientConfigurationFile


def test_read_precedence(monkeypatch, tmpdir: str):
    """
    Assert that values are read from the four possible sources in the correct order of precedence.
    """
    file_path = Path(tmpdir) / "file.toml"
    with open(file_path, "w") as f:
        toml.dump(dict(from_file="in_file", from_env="wrong", from_kwarg="wrong"), f)

    class PrecedenceFile(QCSClientConfigurationFile):
        from_kwarg: str = "wrong"
        from_env: str = "wrong"
        from_file: str = "wrong"
        from_default: str = "in_default"

        model_config = SettingsConfigDict(env_prefix="TEST_CLIENT_CONFIGURATION_")

    monkeypatch.setenv("TEST_CLIENT_CONFIGURATION_FROM_KWARG", "wrong")
    monkeypatch.setenv("TEST_CLIENT_CONFIGURATION_FROM_ENV", "in_env")

    precedence_file = PrecedenceFile(from_kwarg="in_kwarg", file_path=file_path)

    assert precedence_file.from_kwarg == "in_kwarg"
    assert precedence_file.from_env == "in_env"
    assert precedence_file.from_file == "in_file"
    assert precedence_file.from_default == "in_default"
