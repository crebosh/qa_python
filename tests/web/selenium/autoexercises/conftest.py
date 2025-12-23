"""Module holding the conftest for automation exercises tests"""

import os

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from framework.web.driver_management import generate_driver
from framework.web.web_config import DEFAULT_WEB, generate_web_config


def pytest_configure(config):
    path = os.getenv("CONFIG_PATH")
    if path:
        wc = generate_web_config(path)
    else:
        wc = DEFAULT_WEB

    config.web_config = wc


def pytest_generate_tests(metafunc):
    driverconfig_list = metafunc.config.web_config.drivers
    driver_ids = [d.name for d in driverconfig_list]
    if "driver_config" in metafunc.fixturenames:
        metafunc.parametrize("driver_config", driverconfig_list, ids=driver_ids)


@pytest.fixture
def browser(driver_config) -> WebDriver:
    d = generate_driver(driver_config=driver_config)
    yield d
    d.quit()
