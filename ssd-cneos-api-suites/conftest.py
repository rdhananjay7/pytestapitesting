import pytest
from pytest import fixture
from config import Config
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="master",
        help="environment, e.g. beta"
    )

    parser.addoption(
        "--auth",
        action="store",
        default="basic",
        help="authentication, e.g. basic"
    )


@fixture(scope="session")
def get_env(request):
    return request.config.getoption("--env")


@fixture(scope="session")
def get_auth(request):
    return request.config.getoption("--auth")


@fixture(scope="session")
def app_config(get_env, get_auth):
    """Initialising a fixture with a session scope that holds all the command line arguments"""
    cfg = Config(get_env, get_auth)
    return cfg


@fixture(scope="session")
def get_session_id(app_config):
    # placeholder for adding logic to retrieve
    # session based cookies for authentication enabled apis
    pass
