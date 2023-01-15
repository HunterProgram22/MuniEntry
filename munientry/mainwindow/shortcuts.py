"""Module for application shortcuts."""
from PyQt6.QtGui import QKeySequence


def set_mainwindow_shortcuts(mainwindow) -> None:
    """Sets the mainwindow shortcuts when called from init of MainWindow."""
    mainwindow.actionOpen_Current_Log.setShortcut(QKeySequence('Ctrl+L'))
    mainwindow.actionArraignments.setShortcut(QKeySequence('Ctrl+A'))
    mainwindow.actionFinal_Pretrials.setShortcut(QKeySequence('Ctrl+F'))
    mainwindow.actionTrials_To_Court.setShortcut(QKeySequence('Ctrl+T'))
    mainwindow.actionPleas.setShortcut(QKeySequence('Ctrl+P'))
