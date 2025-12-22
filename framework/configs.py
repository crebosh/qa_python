"""Module for generic configuration functions"""

import yaml
from loguru import logger


@logger.catch
def get_dict_from_yaml(path: str) -> dict:
    """parse a yaml file and return it as a dictionary

    Args:
        path (str): path to yaml file

    Returns:
        dict: dictionary object of yaml file
        None: if an error is caught
    """
    with open(path, "r", encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    return data
