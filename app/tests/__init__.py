import pytest
from pytest_asyncio import asyncio_mode

asyncio_mode = pytest.mark.asyncio(mode='auto')