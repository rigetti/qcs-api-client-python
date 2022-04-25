from typing import Dict, Optional
from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.networks import HttpUrl
from enum import Enum
from qcs_api_client.client._configuration.environment import EnvironmentModel
from qcs_api_client.client._configuration.file import QCSClientConfigurationFile


class QCSAuthServer(BaseModel):
    """Specifies an OAuth2 authorization server against which to refresh tokens."""

    client_id: str
    issuer: str

    def authorize_url(self):
        return f"{self.issuer}/v1/authorize"

    def token_url(self):
        return f"{self.issuer}/v1/token"

    @staticmethod
    def scopes():
        return ["offline_access"]

    class Config:
        env_prefix = "QCS_SETTINGS_AUTH_SERVER_"


_DEFAULT_AUTH_SERVER = QCSAuthServer(
    client_id="0oa3ykoirzDKpkfzk357",
    issuer="https://auth.qcs.rigetti.com/oauth2/aus8jcovzG0gW2TUG355",
)


class QCSClientConfigurationSettingsApplicationsCLI(EnvironmentModel):
    verbosity: str = ""

    class Config:
        env_prefix = "QCS_SETTINGS_APPLICATIONS_CLI_"


class QCSClientConfigurationSettingsApplicationsPyquil(EnvironmentModel):
    qvm_url: str = "http://127.0.0.1:5000"
    quilc_url: str = "tcp://127.0.0.1:5555"

    class Config:
        env_prefix = "QCS_SETTINGS_APPLICATIONS_PYQUIL_"


class QCSClientConfigurationSettingsApplications(BaseModel):
    """Section of a profile specifying per-application settings."""

    cli: QCSClientConfigurationSettingsApplicationsCLI = Field(
        default_factory=QCSClientConfigurationSettingsApplicationsCLI
    )

    pyquil: QCSClientConfigurationSettingsApplicationsPyquil = Field(
        default_factory=QCSClientConfigurationSettingsApplicationsPyquil
    )


class QCSAccountType(Enum):
    user = "user"
    group = "group"


class QCSClientConfigurationSettingsProfile(EnvironmentModel):
    """Specifies the authorization server, credentials, and API URL.

    The attributes of this class can be used to initialize an
    ``httpx.Client`` with the correct base URL and the ``QCSAuth``
    middleware for making authenticated API calls against the QCS API.

    ``QCSClientConfigurationSettings`` may contain several profiles, which
    ``QCSClientConfiguration.profile_name`` may key into.
    """

    api_url: HttpUrl = "https://api.qcs.rigetti.com"
    """URL of the QCS API to use for all API calls"""

    auth_server_name: str = "default"
    """Which of the configured ``QCSClientConfigurationSettings.auth_servers`` to use"""

    applications: QCSClientConfigurationSettingsApplications = Field(
        default_factory=QCSClientConfigurationSettingsApplications
    )
    """Application-specific configuration values"""

    credentials_name: str = "default"
    """Which of the configured ``QCSClientConfigurationSecrets.credentials`` to use and update"""

    account_id: Optional[str] = None
    """
    Account ID on behalf of which to make requests. If set to ``None``,
    QCS services will use your personal user account. Clients may also set
    this to a QCS group name for which they are authorized to make requests.
    """

    account_type: Optional[QCSAccountType] = None
    """
    Account type on behalf of which to make requests. When setting the ``account_id``
    to a group name, this must be set to ``AccountType.group``.
    """

    class Config:
        env_prefix = "QCS_SETTINGS_"


class QCSClientConfigurationSettings(QCSClientConfigurationFile):
    """A fully parsed settings configuration file.

    This contains all of the user's configured authorization servers
    and profiles. It may optionally contain a ``default_profile_name``
    to use to override the "default" value.

    ``QCSClientConfiguration`` keys into these configured values when
    instantiated.
    """

    default_profile_name: str = "default"
    """
    Which profile to select settings from when none is specified.

    See ``QCSClientConfiguration.load``.
    """

    profiles: Dict[str, QCSClientConfigurationSettingsProfile] = Field(
        default_factory=lambda: dict(default=QCSClientConfigurationSettingsProfile())
    )
    """All available configuration profiles, keyed by name"""

    auth_servers: Dict[str, QCSAuthServer] = Field(default_factory=lambda: {"default": _DEFAULT_AUTH_SERVER})
    """All available authorization servers, keyed by name"""
