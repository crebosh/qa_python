"""Module for testing the web_config module of framework"""

import pytest

from framework.web.web_config import DriverConfig, WebConfig, parse_dict_to_WebConfig

VALID_DICT = {
    "web_config": {
        "drivers": [
            {
                "browser": "chrome",
                "browser_version": 146.0,
                "path": "my/path",
                "headless": False,
                "window_size": "(1920,1080)",
                "remote": False,
            },
            {
                "browser": "firefox",
                "browser_version": 146.0,
                "path": "my/path",
                "headless": False,
                "window_size": "(1920,1080)",
                "remote": False,
            },
        ],
        "find_timeout": 3.0,
        "base_url": "http://www.executeautomation.com",
    }
}

MISSING_DRIVERS = {
    "web_config": {"find_timeout": 3.0, "base_url": "http://www.executeautomation.com"}
}

MISSING_VALUES = {
    "web_config": {
        "drivers": [
            {
                "browser": "chrome",
                "path": "my/path",
                "headless": False,
                "window_size": "(1920,1080)",
                "remote": False,
            },
            {
                "browser": "firefox",
                "browser_version": 146.0,
                "path": "my/path",
                "headless": False,
                "window_size": "(1920,1080)",
            },
        ],
        "find_timeout": 3.0,
    }
}

EXTRA_VALUES = {
    "web_config": {
        "drivers": [
            {
                "browser": "chrome",
                "browser_version": 146.0,
                "path": "my/path",
                "headless": False,
                "window_size": "(1920,1080)",
                "remote": False,
            },
            {
                "browser": "firefox",
                "browser_version": 146.0,
                "path": "my/path",
                "headless": False,
                "window_size": "(1920,1080)",
                "remote": False,
            },
        ],
        "find_timeout": 3.0,
        "base_url": "http://www.executeautomation.com",
        "wrong": "notrealvalue",
    }
}


class TestParseToDict:
    """Holds tests for the parse_dict_to_WebConfig function"""

    def test_with_valid(self):
        """Test valid input"""
        wc = parse_dict_to_WebConfig(VALID_DICT)

        assert isinstance(wc, WebConfig)
        for i in wc.drivers:
            assert isinstance(i, DriverConfig)

    def test_missing_drivers(self):
        """test with no drivers"""
        wc = parse_dict_to_WebConfig(MISSING_DRIVERS)

        assert isinstance(wc, WebConfig)
        assert wc.drivers is None

    def test_missing_values(self):
        """test with missing values"""
        wc = parse_dict_to_WebConfig(MISSING_VALUES)

        assert isinstance(wc, WebConfig)
        for i in wc.drivers:
            assert isinstance(i, DriverConfig)
        assert wc.drivers[0].browser_version is None
        assert wc.base_url is None

    def test_extra_values(self):
        """test with extra values"""
        with pytest.raises(TypeError):
            parse_dict_to_WebConfig(EXTRA_VALUES)
