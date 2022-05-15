"""
Copyright 2021 Justin Kudela.

The main application entry point.
"""
import multiprocessing
import sys

from loguru import logger
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QSplashScreen

from settings import ICON_PATH

logger.add('./resources/logs/Error_log_{time}.log')


def load_window():
    """The main window is loaded as a seperate function to improve application load time."""
    from main_window import Window

    return Window()


@logger.catch
def main():
    print('Loading')
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(f'{ICON_PATH}gavel.png'))
    splash.show()
    splash.showMessage('Loading')
    win = load_window()
    win.show()
    splash.showMessage('Databases Connected')
    splash.close()
    sys.exit(app.exec())


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
