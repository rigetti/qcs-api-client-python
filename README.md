# QCS API Client

A client library for accessing the [Rigetti QCS API](https://docs.api.qcs.rigetti.com/).

## Usage

### Synchronous Usage

```python
from qcs_api_client.client import build_sync_client
from qcs_api_client.models import ListReservationsResponse
from qcs_api_client.operations.sync import list_reservations

with build_sync_client() as client:
    response: ListReservationsResponse = list_reservations(client=client).parsed
```

### Asynchronous Usage

```python
from qcs_api_client.client import build_async_client
from qcs_api_client.models import ListReservationsResponse
from qcs_api_client.operations.asyncio import list_reservations

# Within an event loop:
async with build_async_client() as client:
    response: ListReservationsResponse = await list_reservations(client=client).parsed
```

### Configuration

By default, initializing your client with `build_sync_client` or `build_async_client` will
use `QCSClientConfiguation.load` to load default configuration values. This function accepts:

- A profile name (env: `QCS_PROFILE_NAME`). The name of the profile referenced in your settings
  file. If not provided, `QCSClientConfiguation.load` will evaluate this to a `default_profile_name`
  set in your settings file or "default".
- A settings file path (env: `QCS_SETTINGS_FILE_PATH`). A path to the current user's settings file in TOML format. If not provided,  `QCSClientConfiguation.load` will evaluate this to `~/.qcs/settings.toml`.
- A secrets file path (env: `QCS_SECRETS_FILE_PATH`). A path to the current user's secrets file in TOML format. If not provided,  `QCSClientConfiguation.load` will evaluate this to `~/.qcs/secrets.toml`. The user should have write access to this file, as the client will attempt to update the file with refreshed access tokens as necessary.
     
If you need to specify a custom profile name or path you can initialize your client accordingly:

```python
from qcs_api_client.client import build_sync_client, QCSClientConfiguration
from qcs_api_client.models import ListReservationsResponse
from qcs_api_client.operations.sync import list_reservations

configuration = QCSClientConfiguration.load(
    profile_name='custom',
    secrets_file_path='./path/to/custom/secrets.toml',
    settings_file_path='./path/to/custom/settings.toml',
)

with build_sync_client(configuration=configuration) as client:
    response: ListReservationsResponse = list_reservations(client=client).parsed
```

## Development

The source code for this repository is largely automatically generated and is synchronized from another source. No commits made directly to GitHub will be retained.
