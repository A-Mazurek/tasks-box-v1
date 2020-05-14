from json import load, dump
from typing import List, Dict
from app.api import config

FOLDER = config.APP_CONFIG["STORAGE_FOLDER"]
FILE = config.APP_CONFIG["DATA_FILE"]


def read_file() -> List[Dict[str, str]]:
    """
        Get data from json file.
    """
    with open(f'{FOLDER}/{FILE}') as file:
        return load(file)


def save_to_file(data) -> None:
    """
        Save data to json file.
    """
    with open(f'{FOLDER}/{FILE}', 'w') as file:
        dump(data, file)
