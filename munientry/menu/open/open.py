from os import startfile

from loguru import logger
from munientry.menu.menu_folder_actions import FOLDER_PATH


def open_entries_folder(folder: str, _signal=None) -> None:
    """Menu function that opens the folder where specific types of entries are saved.

    Args:
        folder (str): A string that identifies the type entry folder to open.
    """
    folder_path = FOLDER_PATH.get(folder)
    startfile(f'{folder_path}')
    logger.info(f'The {folder} folder was opened.')
