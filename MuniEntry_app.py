"""
Copyright 2021 Justin Kudela.

The main application entry point.
"""

#  This import exists only for the pyinstaller executable bootloader splash screen.
#  The import is not available if application is run directly from the python interpreter
#  so the try/except block allows application to run as .exe or .py file.
try:
    import pyi_splash
except ModuleNotFoundError:
    pass

import multiprocessing
import sys

from loguru import logger
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QSplashScreen

from munientry import logging_module
from munientry.settings import SOCKET_NAME, VERSION_NUMBER
from munientry.paths import ICON_PATH


def load_window():
    """The main window is loaded as a separate function so the splash screen appears sooner.

    By nesting the import of the MainWinow inside the load_window function, all the database
    loading and other functions that are done in creating the MainWindow don't occur until after
    the main PyQT splash screen has appeared.
    """
    from munientry.mainwindow.main_window import MainWindow

    return MainWindow()


@logger.catch
def main():
    """The main application loop."""
    logger.info(f'MuniEntry Version {VERSION_NUMBER} Loading on {SOCKET_NAME}')
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(f'{ICON_PATH}gavel_main_splash.png'))
    splash.show()
    splash.showMessage(
        f'<h1>Loading - Version {VERSION_NUMBER}</h1>',
        Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter,
    )
    logger.info('Splash Screen Shown')
    try:
        pyi_splash.close()
        logger.info('Bootloader Splash Screen Closed')
    except NameError as error:
        logger.warning(error)
    win = load_window()
    win.show()
    logger.success('Main Window Open')
    splash.close()
    logger.info('Splash Screen Closed')
    app.exec()
    logger.info('Application Exited')
    sys.exit()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
