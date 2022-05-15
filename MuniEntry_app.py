"""
Copyright 2021 Justin Kudela

The main application entry point.
"""
import multiprocessing
import sys

from loguru import logger
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtCore import QTimer

from settings import ICON_PATH

logger.add("./resources/logs/Error_log_{time}.log")


@logger.catch
def main():
    print("Loading")
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(ICON_PATH + 'gavel.png'))
    splash.show()
    win = load_window()
    win.show()
    splash.close()
    print(QSqlDatabase.connectionNames())
    sys.exit(app.exec())

def load_window():
    from main_window import Window

    return Window()


if __name__ == "__main__":
    # __spec__ = None # Used to get Python Debugger to work - may have other ramifications(?)
    multiprocessing.freeze_support()
    # Process(target=main).start()
    main()
