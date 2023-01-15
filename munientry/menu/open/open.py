import types
from os import startfile

from loguru import logger
from munientry.appsettings.paths import BATCH_SAVE_PATH, CRIMTRAFFIC_SAVE_PATH, DRIVE_SAVE_PATH, \
    JURY_PAY_SAVE_PATH, SCHEDULING_SAVE_PATH


FOLDER_PATH = types.MappingProxyType({
    'batch_entries': BATCH_SAVE_PATH,
    'crimtraffic_entries': CRIMTRAFFIC_SAVE_PATH,
    'driving_privileges': DRIVE_SAVE_PATH,
    'jury_pay_entries': JURY_PAY_SAVE_PATH,
    'scheduling_entries': SCHEDULING_SAVE_PATH,
})


def open_entries_folder(folder: str, _signal=None) -> None:
    """Menu function that opens the folder where specific types of entries are saved.

    Args:
        folder (str): A string that identifies the type entry folder to open.
    """
    folder_path = FOLDER_PATH.get(folder)
    startfile(f'{folder_path}')
    logger.info(f'The {folder} folder was opened.')
