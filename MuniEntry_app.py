"""
Copyright 2021 Justin Kudela.

The main application entry point.
"""
import multiprocessing
import sys
import socket

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from MuniEntry import logging_module
from settings import ICON_PATH, VERSION_NUMBER, SOCKET_NAME

from loguru import logger


def load_window():
    """The main window is loaded as a separate function so the splash screen appears sooner.

    By nesting the import of the MainWinow inside the load_window function, all the database
    loading and other functions that are done in creating the MainWindow don't occur until after
    the splash screen has appeared.
    """
    from main_window import MainWindow

    return MainWindow()


@logger.catch
def main():
    """The main applicaiton loop."""
    logger.info(f'MuniEntry Version {VERSION_NUMBER} Loading on {SOCKET_NAME}')
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(f'{ICON_PATH}gavel.png'))
    splash.show()
    splash.showMessage(
        f'<h1>Loading - Version {VERSION_NUMBER}</h1>',
        Qt.AlignBottom | Qt.AlignCenter,
    )
    logger.info('Splash Screen Shown')
    win = load_window()
    win.show()
    logger.success('Main Window Open')
    splash.close()
    app.exec()
    logger.info('Application Exited')
    sys.exit()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
