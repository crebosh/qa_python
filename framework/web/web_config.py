"""Module For WebConfig class"""

from dataclasses import dataclass
from typing import List, Tuple

from loguru import logger

from framework.config_utils import get_dict_from_yaml


@dataclass
class DriverConfig:
    """Dataclass for Driver Configurations"""

    name: str = None
    browser: str = None
    browser_version: str = None
    path: str = None
    headless: bool = None
    window_size: Tuple[int, int] = None
    remote: bool = None


@dataclass
class WebConfig:
    """Dataclass for Web Configurationss"""

    drivers: List[DriverConfig] = None
    find_timeout: float = None
    base_url: str = None


DEFAULT_WEB = WebConfig(
    drivers=[
        DriverConfig(
            name="chrome_desktop", browser="chrome", window_size="full", headless=False
        ),
        DriverConfig(
            name="firefox_desktop",
            browser="firefox",
            window_size="full",
            headless=False,
        ),
    ],
    find_timeout=3.0,
)


def _parse_dict_to_webconfig(data: dict) -> WebConfig:
    """private fuction that handles parsing dict to dataclass"""
    wc_dict = data.pop("web_config")

    if "drivers" in wc_dict.keys():
        drivers = wc_dict.pop("drivers")
        driver_list = []
        for d in drivers:
            driver_list.append(DriverConfig(**d))
    else:
        driver_list = None

    wc = WebConfig(**wc_dict)
    wc.drivers = driver_list
    logger.debug(wc)
    return wc


def generate_web_config(path: str) -> WebConfig:
    """Returns the data classes based on the path

    Args:
        path (str): path to config file

    Returns:
        WebConfig:
    """
    data = get_dict_from_yaml(path)
    return _parse_dict_to_webconfig(data)
