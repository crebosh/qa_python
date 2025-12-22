"""Module For WebConfig class"""

from dataclasses import dataclass
from typing import List, Tuple

from loguru import logger


@dataclass
class DriverConfig:
    browser: str = None
    browser_version: str = None
    path: str = None
    headless: bool = None
    window_size: Tuple[int, int] = None
    remote: bool = None


@dataclass
class WebConfig:
    drivers: List[DriverConfig] = None
    find_timeout: float = None
    base_url: str = None


def parse_dict_to_WebConfig(data: dict) -> WebConfig:
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
