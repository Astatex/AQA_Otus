import pytest


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru/", help="Это URL-адрес запроса")
    parser.addoption("--status_code", action="store", default=200, type=int)


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
