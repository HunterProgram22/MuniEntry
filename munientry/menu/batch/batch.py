"""Module for running batch processes."""
from os import startfile

from loguru import logger

from munientry.appsettings.paths import BATCH_SAVE_PATH
from munientry.menu.batch.batch_entries import run_batch_fta_arraignments
from munientry.widgets import message_boxes


def run_batch_fta_process(_signal=None) -> None:
    """Creates batch entries for failure to appear and opens folder where entries are saved."""
    entries_created = run_batch_fta_arraignments()
    message = f'The batch process created {entries_created} entries.'
    message_boxes.InfoBox(message, 'Entries Created').exec()
    startfile(f'{BATCH_SAVE_PATH}')
    logger.info(f'{message}')
