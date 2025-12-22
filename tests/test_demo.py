"""Module for tests to setup ci"""

from sample_library.demo import divide


def test_divde_pass():
    """_summary_"""
    assert divide(10, 5) == 2


def test_divide_fail():
    """_summary_"""
    assert divide(10, 0) == 0
