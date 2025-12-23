"""Module for creating WebDriver"""

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

from framework.web.web_config import DriverConfig


class NotSupportedBrowser(Exception):
    """Exception raised for passing an invalid browser type

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def generate_driver(driver_config: DriverConfig) -> WebDriver:
    """Returns driver based on driver_config passed

    Args:
        driver_config (DriverConfig):

    Raises:
        NotSupportedBrowser: Raised if the browser field in DriverConfig
                             isn't supported

    Returns:
        WebDriver:
    """
    match driver_config.browser:
        case "firefox":
            options = _create_firfox_options(driver_config)
            return _create_and_setup_firefox_driver(
                driver_config=driver_config, options=options
            )
        case "chrome":
            options = _create_chrome_options(driver_config=driver_config)
            return _create_and_setup_chrome_driver(
                driver_config=driver_config, options=options
            )
        case _:
            raise NotSupportedBrowser(f"unsupported browser: {driver_config.browser}")


def _create_firfox_options(driver_config: DriverConfig) -> FirefoxOptions:
    options = FirefoxOptions()
    if driver_config.headless:
        options.add_argument("--headless")
    return options


def _create_chrome_options(driver_config: DriverConfig) -> ChromeOptions:
    options = ChromeOptions()
    if driver_config.headless:
        options.add_argument("--headless")
    return options


def _create_and_setup_firefox_driver(
    driver_config: DriverConfig, options: FirefoxOptions
) -> WebDriver:

    driver = webdriver.Firefox(options=options)
    if driver_config.window_size is not None:
        if driver_config.window_size == "full":
            driver.maximize_window()
        else:
            driver.set_window_size(*_convert_to_tuple(driver_config.window_size))
    return driver


def _create_and_setup_chrome_driver(
    driver_config: DriverConfig, options: ChromeOptions
) -> WebDriver:

    driver = webdriver.Chrome(options=options)
    if driver_config.window_size is not None:
        if driver_config.window_size == "full":
            driver.maximize_window()
        else:
            driver.set_window_size(*_convert_to_tuple(driver_config.window_size))
    return driver


def _convert_to_tuple(s: str) -> tuple:
    s2 = s[1:-1].split(",")
    return tuple((int(i) for i in s2))
