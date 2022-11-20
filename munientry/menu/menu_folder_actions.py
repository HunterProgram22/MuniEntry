import os

from loguru import logger
from munientry.paths import BATCH_SAVE_PATH, DRIVE_SAVE_PATH, CRIMTRAFFIC_SAVE_PATH, \
    SCHEDULING_SAVE_PATH, JURY_PAY_SAVE_PATH


def open_batch_entries_folder(_signal=None) -> None:
    """Menu function that opens the folder where batch entries are saved."""
    os.startfile(f'{BATCH_SAVE_PATH}')
    logger.info('Batch entries folder opened.')


def open_driving_privileges_folder(_signal=None) -> None:
    """Menu function that opens the folder where Driving Privileges entries are saved."""
    os.startfile(f'{DRIVE_SAVE_PATH}')
    logger.info('Driving Privileges entries folder opened.')


def open_crimtraffic_entries_folder(_signal=None) -> None:
    """Menu function that opens the folder where Driving Privileges entries are saved."""
    os.startfile(f'{CRIMTRAFFIC_SAVE_PATH}')
    logger.info('Crim Traffic entries folder opened.')


def open_scheduling_entries_folder(_signal=None) -> None:
    """Menu function that opens the folder where Driving Privileges entries are saved."""
    os.startfile(f'{SCHEDULING_SAVE_PATH}')
    logger.info('Scheduling entries folder opened.')


def open_jury_pay_entries_folder(_signal=None) -> None:
    """Menu function that opens the folder where Jury Pay entries are saved."""
    os.startfile(f'{JURY_PAY_SAVE_PATH}')
    logger.info('Jury Pay entries folder opened.')
