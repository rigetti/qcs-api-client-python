import os
from typing import Any, Dict

from pydantic import BaseModel
from pydantic.v1.utils import deep_update
from pydantic_settings.sources import _annotation_is_complex


class _EnvironmentBaseModel(BaseModel):
    """
    A utility class meant for inheritance by classes which initialize using environment variables.

    Ensure that ``env_prefix`` is set on the metaclass ``Config``.
    """

    def _read_env(self) -> Dict[str, str]:
        """
        Read the value of each primitive-typed field from the environment.

        Environment variable name is case insensitive. The prefix is set as ``env_prefix``on the
        model's ``Config``.
        """
        if not self.model_config.get("env_prefix"):
            return {}

        data: Dict[str, str] = {}
        env: Dict[str, str] = {k.lower(): v for k, v in os.environ.items()}

        for field_name, field in self.model_fields.items():

            # We only read primitives from the environment, no JSON parsing
            if not _annotation_is_complex(field.annotation, field.metadata):
                env_name = (self.model_config["env_prefix"] + field_name).lower()
                if env_name in env:
                    data[field_name] = env[env_name]

        return data


class EnvironmentModel(_EnvironmentBaseModel):
    """
    A BaseModel which also attempts to read primitive field values from the environment on
    initialization.
    """

    def __init__(self, **kwargs: Any) -> None:
        """
        Load values in this order of precedence:
        1. Runtime keyword arguments
        2. Environment variables
        3. Field default values
        """
        values = deep_update(
            self._read_env(),
            kwargs,
        )
        super().__init__(**values)
