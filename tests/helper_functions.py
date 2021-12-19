from pytestqt.plugin import QtBot
from PyQt5 import QtCore


def enter_data(field, data: str):
    return QtBot.keyClicks(field, data)

def mouse_click(button):
    return QtBot.mouseClick(button, QtCore.Qt.LeftButton)