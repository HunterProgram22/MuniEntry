from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox, QMenu
from loguru import logger
from munientry.data.connections import open_db_connection, close_db_connection
from munientry.data.sql_lite_functions import query_attorney_list


class DailyCaseListComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setEnabled(False)
        self.setMinimumSize(QtCore.QSize(0, 40))
        self.setStyleSheet( "background-color: rgb(255, 255, 255);\n"
                            "selection-background-color: rgb(85, 170, 255);")
        self.setEditable(False)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_menu)

    def setup_combo_box(self, name, radio_button, main_window):
        self.name = name
        self.radio_button = radio_button
        self.main_window = main_window
        self.radio_button.clicked.connect(self.set_daily_case_list)
        self.radio_button.toggled.connect(self.show_hide_case_list)

    def show_hide_case_list(self):
        if self.radio_button.isChecked():
            self.setEnabled(True)
            self.setHidden(False)
            self.setFocus()
        else:
            self.setCurrentText('')
            self.setEnabled(False)
            self.setHidden(True)

    def set_daily_case_list(self):
        self.main_window.daily_case_list = self

    def show_menu(self, pos):
        menu = QMenu()
        menu.addAction("Delete Case", self.delete_case)
        menu.exec_(self.mapToGlobal(pos))

    def delete_case(self):
        index = self.currentIndex()
        case = self.itemText(index)
        self.removeItem(index)
        logger.action(f'Case {case} deleted from {self.objectName()}.')

    def all_items(self) -> list:
        return [self.itemText(index) for index in range(self.count())]

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super(DailyCaseListComboBox, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Delete:
            self.delete_case()


class NoScrollComboBox(QComboBox):
    def __init__(self, parent=None):
        super(QComboBox, self).__init__(parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def wheelEvent(self, event):
        if event == QtCore.QEvent.Wheel:
            event.ignore()


class DefenseCounselComboBox(NoScrollComboBox):
    def __init__(self, parent=None):
        super(NoScrollComboBox, self).__init__(parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def load_attorneys(self):
        db_connection = open_db_connection('con_attorneys')
        attorney_list = query_attorney_list(db_connection)
        attorney_count = len(attorney_list)
        logger.info(f'{attorney_count} attorneys loaded.')
        for attorney in attorney_list:
            self.addItem(attorney)
        close_db_connection(db_connection)


class DegreeComboBox(NoScrollComboBox):
    def __init__(self, degree, parent=None):
        super(NoScrollComboBox, self).__init__(parent)
        self.set_up_widget(degree)

    def set_up_widget(self, degree):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setEditable(False)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setObjectName("degree_choice_box")
        self.addItem("")
        self.addItem("M1")
        self.addItem("M2")
        self.addItem("M3")
        self.addItem("M4")
        self.addItem("MM")
        self.addItem("UCM")
        self.addItem("No Data")
        self.setCurrentText(degree)


class PleaComboBox(NoScrollComboBox):
    def __init__(self, column, dialog=None, parent=None):
        super(NoScrollComboBox, self).__init__(parent)
        self.column = column
        self.dialog = dialog
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setEditable(False)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setObjectName("plea_choice_box")
        if self.dialog.objectName() == 'TrialSentencingDialog':
            self.addItem('Court')
            self.addItem('Jury')
            self.addItem('Dismissed')
        else:
            self.addItem("")
            self.addItem("Guilty")
            self.addItem("No Contest")
            self.addItem("Not Guilty")
            self.addItem("Dismissed")


class FindingComboBox(NoScrollComboBox):
    def __init__(self, parent=None):
        super(NoScrollComboBox, self).__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setMaximumSize(QtCore.QSize(200, 50))
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setEditable(False)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setObjectName("finding_choice_box")
        self.addItem("")
        self.addItem("Guilty")
        self.addItem("Not Guilty")
        self.addItem("Lesser Included")
        self.addItem("Guilty - Allied Offense")
        self.addItem("Not Guilty - Allied Offense")