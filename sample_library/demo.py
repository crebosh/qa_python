"""Demo module for setting up testing and ci"""

from loguru import logger


@logger.catch
def divide(a: int, b: int) -> float:
    """divide two numbers

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        float: _description_
    """
    return a / b
