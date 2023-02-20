import pytest
from humidifier import Humidifier


@pytest.fixture
def humidify():
    humidifier = Humidifier()
    return humidifier.humidify
