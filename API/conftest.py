import pytest


@pytest.fixture
def api_url():
    return "https://gorest.co.in/"


@pytest.fixture
def auth_token():
    return "bearer 5227faa436d189ffd6585d5482f91dda4797cd4fc2aa5014be41d9c531d3a40a"
