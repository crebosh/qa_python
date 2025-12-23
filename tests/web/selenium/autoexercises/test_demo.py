import time


def test_driver_fixture(browser):
    browser.get("https://automationexercise.com/")
    time.sleep(1)
