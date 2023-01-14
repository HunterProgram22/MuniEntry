"""Module for application shortcuts."""
from PyQt6.QtGui import QKeySequence, QShortcut


class Shortcuts(object):

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.set_shortcuts()

    def set_shortcuts(self):
        self.mainwindow.actionOpen_Current_Log.setShortcut(QKeySequence('Ctrl+L'))
        self.mainwindow.actionArraignments.setShortcut(QKeySequence('Ctrl+A'))
        self.mainwindow.actionFinal_Pretrials.setShortcut(QKeySequence('Ctrl+F'))
        self.mainwindow.actionTrials_To_Court.setShortcut(QKeySequence('Ctrl+T'))
