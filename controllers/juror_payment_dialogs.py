from loguru import logger

from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QMessageBox

from views.juror_payment_dialog_ui import Ui_JurorPaymentDialog

class JurorPaymentDialog(QDialog, Ui_JurorPaymentDialog):
    """This class is a base class"""
    def __init__(self, judicial_officer, case=None, parent=None):
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.case = case
        self.setupUi(self)
        # self.modify_view()
        # self.connect_signals_to_slots()
        self.doc = None
        self.docname = None
