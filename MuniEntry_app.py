"""
Copyright 2021 Justin Kudela.

The main application entry point.
"""
import multiprocessing
import socket
import sys

from loguru import logger
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from settings import ICON_PATH, VERSION_NUMBER

logger.add('./resources/logs/Error_log_{time}.log')


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
    logger.info(f'MuniEntry Version {VERSION_NUMBER} Loading on {socket.gethostname()}')
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(f'{ICON_PATH}gavel.png'))
    splash.show()
    splash.showMessage(
        f'<h1>Loading - Version {VERSION_NUMBER}</h1>',
        Qt.AlignBottom | Qt.AlignCenter,
    )
    win = load_window()
    win.show()
    splash.close()
    app.exec()
    logger.info('Application Exited')
    sys.exit()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
