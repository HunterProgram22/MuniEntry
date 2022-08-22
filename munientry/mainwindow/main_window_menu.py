"""Module containing all functions for the mainwindow menu."""
import os

from loguru import logger
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut

from munientry.mainwindow.batch_fta_entries import run_batch_fta_arraignments
from munientry.settings import LOG_PATH, SAVE_PATH, USER_LOG_NAME
from munientry.widgets.message_boxes import InfoBox


def open_current_log(signal=None) -> None:
    """Menu function that opens the user logs directly or with keyboard shortcut."""
    if signal is False:
        signal = 'Menu'
    else:
        signal = 'Keyboard Shortcut'
    logger.info(f'Log opened from {signal}.')
    os.startfile(f'{LOG_PATH}{USER_LOG_NAME}')


def open_batch_entries_folder(_signal=None) -> None:
    """Menu function that opens the folder where batch entries are saved."""
    logger.info('Opened batch entries folder.')
    os.startfile(f'{SAVE_PATH}batch\\')


def run_batch_fta_process(_signal=None) -> None:
    """Creates batch entries for failure to appear and opens folder where entries are saved."""
    entries_created = run_batch_fta_arraignments()
    message = f'The batch process created {entries_created} entries.'
    InfoBox(message, 'Entries Created').exec()
    os.startfile(f'{SAVE_PATH}batch\\')


def connect_menu_functions(main_window) -> None:
    """Connects all menu functions from the main window."""
    main_window.log_shortcut = QShortcut(QKeySequence('Ctrl+L'), main_window)
    main_window.log_shortcut.activated.connect(open_current_log)
    main_window.actionOpen_Current_Log.triggered.connect(open_current_log)
    main_window.actionOpen_batch_FTA_Entries_Folder.triggered.connect(open_batch_entries_folder)
    main_window.actionRun_batch_FTA_Entries.triggered.connect(run_batch_fta_process)
