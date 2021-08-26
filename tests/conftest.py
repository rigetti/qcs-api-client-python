from pathlib import Path
from shutil import copytree, rmtree

import pytest

FIXTURE_BASE_PATH = Path(__file__).parent / "__fixtures__"


@pytest.fixture
def fixture_directory(tmpdir):
    temporary_fixture_directory = Path(tmpdir) / "fixtures"
    copytree(FIXTURE_BASE_PATH, temporary_fixture_directory)
    yield temporary_fixture_directory
    rmtree(temporary_fixture_directory)
