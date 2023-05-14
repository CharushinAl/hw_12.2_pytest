import pytest

dictionary = {1: '11', 2: '22', 3: '33'}


@pytest.fixture
def dictionary_fixture():
    return dictionary
