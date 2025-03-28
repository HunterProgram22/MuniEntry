# Form implementation generated from reading ui file './views/ui/FineOnlyPleaDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from munientry.widgets.combo_boxes import DefenseCounselComboBox, NoScrollComboBox
from munientry.widgets.custom_widgets import NoScrollDateEdit
from munientry.widgets.charges_grids import FineOnlyChargeGrid


class Ui_FineOnlyPleaDialog(object):
    def setupUi(self, FineOnlyPleaDialog):
        FineOnlyPleaDialog.setObjectName("FineOnlyPleaDialog")
        FineOnlyPleaDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        FineOnlyPleaDialog.setEnabled(True)
        FineOnlyPleaDialog.resize(1246, 853)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FineOnlyPleaDialog.sizePolicy().hasHeightForWidth())
        FineOnlyPleaDialog.setSizePolicy(sizePolicy)
        FineOnlyPleaDialog.setMinimumSize(QtCore.QSize(0, 0))
        FineOnlyPleaDialog.setMaximumSize(QtCore.QSize(2500, 3500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        FineOnlyPleaDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        FineOnlyPleaDialog.setFont(font)
        FineOnlyPleaDialog.setToolTip("")
        FineOnlyPleaDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        FineOnlyPleaDialog.setSizeGripEnabled(True)
        FineOnlyPleaDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(FineOnlyPleaDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(FineOnlyPleaDialog)
        self.scrollArea.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1226, 833))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.no_contest_all_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_contest_all_Button.sizePolicy().hasHeightForWidth())
        self.no_contest_all_Button.setSizePolicy(sizePolicy)
        self.no_contest_all_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.no_contest_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.no_contest_all_Button.setObjectName("no_contest_all_Button")
        self.gridLayout_3.addWidget(self.no_contest_all_Button, 2, 1, 1, 1)
        self.charges_gridLayout = FineOnlyChargeGrid()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.statute_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.statute_label.setFont(font)
        self.statute_label.setObjectName("statute_label")
        self.charges_gridLayout.addWidget(self.statute_label, 1, 0, 1, 1)
        self.allied_label = QtWidgets.QLabel(self.frame)
        self.allied_label.setObjectName("allied_label")
        self.charges_gridLayout.addWidget(self.allied_label, 4, 0, 1, 1)
        self.plea_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plea_label.setFont(font)
        self.plea_label.setObjectName("plea_label")
        self.charges_gridLayout.addWidget(self.plea_label, 5, 0, 1, 1)
        self.degree_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.degree_label.setFont(font)
        self.degree_label.setObjectName("degree_label")
        self.charges_gridLayout.addWidget(self.degree_label, 2, 0, 1, 1)
        self.finding_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.finding_label.setFont(font)
        self.finding_label.setObjectName("finding_label")
        self.charges_gridLayout.addWidget(self.finding_label, 6, 0, 1, 1)
        self.offense_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.offense_label.setFont(font)
        self.offense_label.setWordWrap(True)
        self.offense_label.setObjectName("offense_label")
        self.charges_gridLayout.addWidget(self.offense_label, 0, 0, 1, 1)
        self.fines_suspended_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fines_suspended_label.setFont(font)
        self.fines_suspended_label.setObjectName("fines_suspended_label")
        self.charges_gridLayout.addWidget(self.fines_suspended_label, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.charges_gridLayout.addWidget(self.label_5, 10, 0, 1, 1)
        self.fines_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.fines_label.setFont(font)
        self.fines_label.setObjectName("fines_label")
        self.charges_gridLayout.addWidget(self.fines_label, 7, 0, 1, 1)
        self.amend_row_label = QtWidgets.QLabel(self.frame)
        self.amend_row_label.setText("")
        self.amend_row_label.setObjectName("amend_row_label")
        self.charges_gridLayout.addWidget(self.amend_row_label, 9, 0, 1, 1)
        self.dismissed_label = QtWidgets.QLabel(self.frame)
        self.dismissed_label.setObjectName("dismissed_label")
        self.charges_gridLayout.addWidget(self.dismissed_label, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.charges_gridLayout, 0, 0, 1, 3)
        self.guilty_all_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guilty_all_Button.sizePolicy().hasHeightForWidth())
        self.guilty_all_Button.setSizePolicy(sizePolicy)
        self.guilty_all_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.guilty_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.guilty_all_Button.setObjectName("guilty_all_Button")
        self.gridLayout_3.addWidget(self.guilty_all_Button, 2, 2, 1, 1)
        self.add_charge_Button = QtWidgets.QPushButton(self.frame)
        self.add_charge_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_charge_Button.setObjectName("add_charge_Button")
        self.gridLayout_3.addWidget(self.add_charge_Button, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 4)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.monthly_pay_box = QtWidgets.QLineEdit(self.frame_5)
        self.monthly_pay_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.monthly_pay_box.setObjectName("monthly_pay_box")
        self.gridLayout_5.addWidget(self.monthly_pay_box, 6, 1, 1, 3)
        self.costs_and_fines_Button = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.costs_and_fines_Button.sizePolicy().hasHeightForWidth())
        self.costs_and_fines_Button.setSizePolicy(sizePolicy)
        self.costs_and_fines_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.costs_and_fines_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.costs_and_fines_Button.setFlat(False)
        self.costs_and_fines_Button.setObjectName("costs_and_fines_Button")
        self.gridLayout_5.addWidget(self.costs_and_fines_Button, 8, 0, 1, 4)
        self.balance_due_date = NoScrollDateEdit(self.frame_5)
        self.balance_due_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.balance_due_date.setCalendarPopup(True)
        self.balance_due_date.setObjectName("balance_due_date")
        self.gridLayout_5.addWidget(self.balance_due_date, 3, 1, 1, 3)
        self.balance_due_date_label = QtWidgets.QLabel(self.frame_5)
        self.balance_due_date_label.setObjectName("balance_due_date_label")
        self.gridLayout_5.addWidget(self.balance_due_date_label, 3, 0, 1, 1)
        self.credit_for_jail_checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.credit_for_jail_checkBox.setObjectName("credit_for_jail_checkBox")
        self.gridLayout_5.addWidget(self.credit_for_jail_checkBox, 7, 0, 1, 3)
        self.jail_time_credit_box = QtWidgets.QLineEdit(self.frame_5)
        self.jail_time_credit_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jail_time_credit_box.setObjectName("jail_time_credit_box")
        self.gridLayout_5.addWidget(self.jail_time_credit_box, 7, 3, 1, 1)
        self.court_costs_box = NoScrollComboBox(self.frame_5)
        self.court_costs_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.court_costs_box.setObjectName("court_costs_box")
        self.court_costs_box.addItem("")
        self.court_costs_box.addItem("")
        self.court_costs_box.addItem("")
        self.court_costs_box.addItem("")
        self.gridLayout_5.addWidget(self.court_costs_box, 1, 1, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 1, 0, 1, 1)
        self.ability_to_pay_box = NoScrollComboBox(self.frame_5)
        self.ability_to_pay_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ability_to_pay_box.setObjectName("ability_to_pay_box")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.gridLayout_5.addWidget(self.ability_to_pay_box, 2, 1, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 1)
        self.monthly_pay_label = QtWidgets.QLabel(self.frame_5)
        self.monthly_pay_label.setObjectName("monthly_pay_label")
        self.gridLayout_5.addWidget(self.monthly_pay_label, 6, 0, 1, 1)
        self.pay_today_label = QtWidgets.QLabel(self.frame_5)
        self.pay_today_label.setObjectName("pay_today_label")
        self.gridLayout_5.addWidget(self.pay_today_label, 5, 0, 1, 1)
        self.pay_today_box = QtWidgets.QLineEdit(self.frame_5)
        self.pay_today_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pay_today_box.setObjectName("pay_today_box")
        self.gridLayout_5.addWidget(self.pay_today_box, 5, 1, 1, 3)
        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 1)
        self.case_name_Frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_name_Frame.sizePolicy().hasHeightForWidth())
        self.case_name_Frame.setSizePolicy(sizePolicy)
        self.case_name_Frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.case_name_Frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.case_name_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.case_name_Frame.setLineWidth(2)
        self.case_name_Frame.setObjectName("case_name_Frame")
        self.gridLayout = QtWidgets.QGridLayout(self.case_name_Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.appearance_reason_box = NoScrollComboBox(self.case_name_Frame)
        self.appearance_reason_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.appearance_reason_box.setObjectName("appearance_reason_box")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.gridLayout.addWidget(self.appearance_reason_box, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.defense_counsel_name_box = DefenseCounselComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 3, 1, 1, 1)
        self.defense_counsel_type_box = NoScrollComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 3, 2, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 3, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.case_name_Frame)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 4)
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 75 9pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 0, 0, 1, 1)
        self.license_suspension_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.license_suspension_checkBox.setObjectName("license_suspension_checkBox")
        self.gridLayout_4.addWidget(self.license_suspension_checkBox, 1, 0, 1, 1)
        self.community_service_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.community_service_checkBox.setObjectName("community_service_checkBox")
        self.gridLayout_4.addWidget(self.community_service_checkBox, 2, 0, 1, 1)
        self.add_conditions_Button = QtWidgets.QPushButton(self.frame_6)
        self.add_conditions_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_conditions_Button.setAutoDefault(False)
        self.add_conditions_Button.setObjectName("add_conditions_Button")
        self.gridLayout_4.addWidget(self.add_conditions_Button, 4, 0, 1, 1)
        self.other_conditions_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.other_conditions_checkBox.setEnabled(True)
        self.other_conditions_checkBox.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.other_conditions_checkBox.setObjectName("other_conditions_checkBox")
        self.gridLayout_4.addWidget(self.other_conditions_checkBox, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 2, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_2)
        self.close_dialog_Button.setMinimumSize(QtCore.QSize(120, 30))
        self.close_dialog_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(255, 96, 82);")
        self.close_dialog_Button.setAutoDefault(False)
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_6.addWidget(self.close_dialog_Button, 3, 0, 1, 1)
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_2)
        self.create_entry_Button.setMinimumSize(QtCore.QSize(120, 30))
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_6.addWidget(self.create_entry_Button, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 2, 3, 1, 1)
        self.fra_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fra_frame.sizePolicy().hasHeightForWidth())
        self.fra_frame.setSizePolicy(sizePolicy)
        self.fra_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.fra_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.fra_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_frame.setLineWidth(2)
        self.fra_frame.setObjectName("fra_frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.fra_frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.distracted_driving_checkBox = QtWidgets.QCheckBox(self.fra_frame)
        self.distracted_driving_checkBox.setObjectName("distracted_driving_checkBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.distracted_driving_checkBox)
        self.label_21 = QtWidgets.QLabel(self.fra_frame)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_21)
        self.fra_in_file_box = NoScrollComboBox(self.fra_frame)
        self.fra_in_file_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_file_box.setObjectName("fra_in_file_box")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.fra_in_file_box)
        self.label_22 = QtWidgets.QLabel(self.fra_frame)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_22)
        self.fra_in_court_box = NoScrollComboBox(self.fra_frame)
        self.fra_in_court_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_court_box.setObjectName("fra_in_court_box")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.fra_in_court_box)
        self.gridLayout_2.addWidget(self.fra_frame, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(FineOnlyPleaDialog)
        QtCore.QMetaObject.connectSlotsByName(FineOnlyPleaDialog)
        FineOnlyPleaDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        FineOnlyPleaDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        FineOnlyPleaDialog.setTabOrder(self.case_number_lineEdit, self.defense_counsel_name_box)
        FineOnlyPleaDialog.setTabOrder(self.defense_counsel_name_box, self.defense_counsel_type_box)
        FineOnlyPleaDialog.setTabOrder(self.defense_counsel_type_box, self.defense_counsel_waived_checkBox)
        FineOnlyPleaDialog.setTabOrder(self.defense_counsel_waived_checkBox, self.appearance_reason_box)
        FineOnlyPleaDialog.setTabOrder(self.appearance_reason_box, self.add_charge_Button)
        FineOnlyPleaDialog.setTabOrder(self.add_charge_Button, self.court_costs_box)
        FineOnlyPleaDialog.setTabOrder(self.court_costs_box, self.ability_to_pay_box)
        FineOnlyPleaDialog.setTabOrder(self.ability_to_pay_box, self.balance_due_date)
        FineOnlyPleaDialog.setTabOrder(self.balance_due_date, self.pay_today_box)
        FineOnlyPleaDialog.setTabOrder(self.pay_today_box, self.monthly_pay_box)
        FineOnlyPleaDialog.setTabOrder(self.monthly_pay_box, self.credit_for_jail_checkBox)
        FineOnlyPleaDialog.setTabOrder(self.credit_for_jail_checkBox, self.jail_time_credit_box)
        FineOnlyPleaDialog.setTabOrder(self.jail_time_credit_box, self.distracted_driving_checkBox)
        FineOnlyPleaDialog.setTabOrder(self.distracted_driving_checkBox, self.fra_in_file_box)
        FineOnlyPleaDialog.setTabOrder(self.fra_in_file_box, self.fra_in_court_box)
        FineOnlyPleaDialog.setTabOrder(self.fra_in_court_box, self.license_suspension_checkBox)
        FineOnlyPleaDialog.setTabOrder(self.license_suspension_checkBox, self.community_service_checkBox)
        FineOnlyPleaDialog.setTabOrder(self.community_service_checkBox, self.other_conditions_checkBox)
        FineOnlyPleaDialog.setTabOrder(self.other_conditions_checkBox, self.add_conditions_Button)
        FineOnlyPleaDialog.setTabOrder(self.add_conditions_Button, self.create_entry_Button)
        FineOnlyPleaDialog.setTabOrder(self.create_entry_Button, self.scrollArea)

    def retranslateUi(self, FineOnlyPleaDialog):
        _translate = QtCore.QCoreApplication.translate
        FineOnlyPleaDialog.setWindowTitle(_translate("FineOnlyPleaDialog", "Fine Only Plea Case Information"))
        self.no_contest_all_Button.setText(_translate("FineOnlyPleaDialog", "No Contest All"))
        self.statute_label.setText(_translate("FineOnlyPleaDialog", "Statute:"))
        self.allied_label.setText(_translate("FineOnlyPleaDialog", "Allied:"))
        self.plea_label.setText(_translate("FineOnlyPleaDialog", "Plea:"))
        self.degree_label.setText(_translate("FineOnlyPleaDialog", "Degree:"))
        self.finding_label.setText(_translate("FineOnlyPleaDialog", "Finding:"))
        self.offense_label.setText(_translate("FineOnlyPleaDialog", "Offense:"))
        self.fines_suspended_label.setText(_translate("FineOnlyPleaDialog", "Fines Suspended:"))
        self.fines_label.setText(_translate("FineOnlyPleaDialog", "Fines:"))
        self.dismissed_label.setText(_translate("FineOnlyPleaDialog", "Dismissed:"))
        self.guilty_all_Button.setText(_translate("FineOnlyPleaDialog", "Guilty All"))
        self.add_charge_Button.setText(_translate("FineOnlyPleaDialog", "Add Charge"))
        self.costs_and_fines_Button.setText(_translate("FineOnlyPleaDialog", "Show Costs/Fines"))
        self.balance_due_date_label.setText(_translate("FineOnlyPleaDialog", "Due date:"))
        self.credit_for_jail_checkBox.setText(_translate("FineOnlyPleaDialog", "Credit $50/day in jail"))
        self.jail_time_credit_box.setPlaceholderText(_translate("FineOnlyPleaDialog", "Days in jail"))
        self.court_costs_box.setItemText(0, _translate("FineOnlyPleaDialog", "Yes"))
        self.court_costs_box.setItemText(1, _translate("FineOnlyPleaDialog", "Waived"))
        self.court_costs_box.setItemText(2, _translate("FineOnlyPleaDialog", "Imposed in companion case"))
        self.court_costs_box.setItemText(3, _translate("FineOnlyPleaDialog", "No"))
        self.label_11.setText(_translate("FineOnlyPleaDialog", "Court Costs:"))
        self.ability_to_pay_box.setItemText(0, _translate("FineOnlyPleaDialog", "forthwith"))
        self.ability_to_pay_box.setItemText(1, _translate("FineOnlyPleaDialog", "monthly pay"))
        self.ability_to_pay_box.setItemText(2, _translate("FineOnlyPleaDialog", "partial forthwith then monthly pay"))
        self.label_9.setText(_translate("FineOnlyPleaDialog", "Time to pay:"))
        self.monthly_pay_label.setText(_translate("FineOnlyPleaDialog", "Monthly Pay:"))
        self.pay_today_label.setText(_translate("FineOnlyPleaDialog", "Pay Today:"))
        self.label.setText(_translate("FineOnlyPleaDialog", "Def. First Name:"))
        self.cancel_Button.setText(_translate("FineOnlyPleaDialog", "Cancel"))
        self.appearance_reason_box.setItemText(0, _translate("FineOnlyPleaDialog", "arraignment"))
        self.appearance_reason_box.setItemText(1, _translate("FineOnlyPleaDialog", "a change of plea"))
        self.appearance_reason_box.setItemText(2, _translate("FineOnlyPleaDialog", "sentencing"))
        self.label_3.setText(_translate("FineOnlyPleaDialog", "Case Number:"))
        self.label_26.setText(_translate("FineOnlyPleaDialog", "Date:"))
        self.label_2.setText(_translate("FineOnlyPleaDialog", "Def. Last Name:"))
        self.label_4.setText(_translate("FineOnlyPleaDialog", "Appearance Reason:"))
        self.clear_fields_case_Button.setText(_translate("FineOnlyPleaDialog", "Clear Fields"))
        self.label_8.setText(_translate("FineOnlyPleaDialog", "Def. Counsel:"))
        self.defense_counsel_type_box.setItemText(0, _translate("FineOnlyPleaDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("FineOnlyPleaDialog", "Private Counsel"))
        self.defense_counsel_waived_checkBox.setText(_translate("FineOnlyPleaDialog", "Defendant waived right to counsel"))
        self.label_24.setText(_translate("FineOnlyPleaDialog", "ADDITIONAL CONDITIONS"))
        self.license_suspension_checkBox.setText(_translate("FineOnlyPleaDialog", "License Suspension           "))
        self.community_service_checkBox.setText(_translate("FineOnlyPleaDialog", "Community Service             "))
        self.add_conditions_Button.setText(_translate("FineOnlyPleaDialog", "Add Conditions"))
        self.other_conditions_checkBox.setText(_translate("FineOnlyPleaDialog", "Other                                                      "))
        self.close_dialog_Button.setText(_translate("FineOnlyPleaDialog", "Close Dialog"))
        self.create_entry_Button.setText(_translate("FineOnlyPleaDialog", "Open Entry"))
        self.distracted_driving_checkBox.setText(_translate("FineOnlyPleaDialog", "Add Distracted Driving Course Language"))
        self.label_21.setText(_translate("FineOnlyPleaDialog", "FRA shown in complaint:"))
        self.fra_in_file_box.setItemText(0, _translate("FineOnlyPleaDialog", "N/A"))
        self.fra_in_file_box.setItemText(1, _translate("FineOnlyPleaDialog", "Yes"))
        self.fra_in_file_box.setItemText(2, _translate("FineOnlyPleaDialog", "No"))
        self.label_22.setText(_translate("FineOnlyPleaDialog", "FRA shown in court:"))
        self.fra_in_court_box.setItemText(0, _translate("FineOnlyPleaDialog", "N/A"))
        self.fra_in_court_box.setItemText(1, _translate("FineOnlyPleaDialog", "Yes"))
        self.fra_in_court_box.setItemText(2, _translate("FineOnlyPleaDialog", "No"))
