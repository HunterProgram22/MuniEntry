"""Actions that are triggered by a menu function."""
import os

from loguru import logger

from munientry.paths import (
    BATCH_SAVE_PATH,
    CRIMTRAFFIC_SAVE_PATH,
    DRIVE_SAVE_PATH,
    JURY_PAY_SAVE_PATH,
    SCHEDULING_SAVE_PATH,
)

FOLDER_PATH = {
    'batch_entries': BATCH_SAVE_PATH,
    'crimtraffic_entries': CRIMTRAFFIC_SAVE_PATH,
    'driving_privileges': DRIVE_SAVE_PATH,
    'jury_pay_entries': JURY_PAY_SAVE_PATH,
    'scheduling_entries': SCHEDULING_SAVE_PATH,
}


def open_entries_folder(folder, _singal=None):
    """Menu function that opens the chosen folder where the chosen entries are saved."""
    folder_path = FOLDER_PATH.get(folder)
    os.startfile(f'{folder_path}')
    logger.info(f'The {folder} folder was opened.')
