# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package\views\ui\JailCCPleaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JailCCPleaDialog(object):
    def setupUi(self, JailCCPleaDialog):
        JailCCPleaDialog.setObjectName("JailCCPleaDialog")
        JailCCPleaDialog.setWindowModality(QtCore.Qt.NonModal)
        JailCCPleaDialog.resize(1142, 855)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JailCCPleaDialog.sizePolicy().hasHeightForWidth())
        JailCCPleaDialog.setSizePolicy(sizePolicy)
        JailCCPleaDialog.setMinimumSize(QtCore.QSize(0, 0))
        JailCCPleaDialog.setMaximumSize(QtCore.QSize(2500, 3500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        JailCCPleaDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        JailCCPleaDialog.setFont(font)
        JailCCPleaDialog.setToolTip("")
        JailCCPleaDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        JailCCPleaDialog.setSizeGripEnabled(True)
        JailCCPleaDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(JailCCPleaDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(JailCCPleaDialog)
        self.scrollArea.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1120, 833))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fra_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fra_frame.sizePolicy().hasHeightForWidth())
        self.fra_frame.setSizePolicy(sizePolicy)
        self.fra_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.fra_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.fra_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fra_frame.setLineWidth(2)
        self.fra_frame.setObjectName("fra_frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.fra_frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_21 = QtWidgets.QLabel(self.fra_frame)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.fra_in_file_box = QtWidgets.QComboBox(self.fra_frame)
        self.fra_in_file_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_file_box.setObjectName("fra_in_file_box")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fra_in_file_box)
        self.label_22 = QtWidgets.QLabel(self.fra_frame)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.fra_in_court_box = QtWidgets.QComboBox(self.fra_frame)
        self.fra_in_court_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_court_box.setObjectName("fra_in_court_box")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fra_in_court_box)
        self.gridLayout_4.addWidget(self.fra_frame, 3, 0, 1, 1)
        self.case_name_Frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_name_Frame.sizePolicy().hasHeightForWidth())
        self.case_name_Frame.setSizePolicy(sizePolicy)
        self.case_name_Frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.case_name_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.case_name_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_name_Frame.setObjectName("case_name_Frame")
        self.gridLayout = QtWidgets.QGridLayout(self.case_name_Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.plea_trial_date = QtWidgets.QDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 3, 0, 1, 1)
        self.defense_counsel_type_box = QtWidgets.QComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 3, 2, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 3, 3, 1, 1)
        self.defense_counsel_name_box = QtWidgets.QComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 3, 1, 1, 1)
        self.appearance_reason_box = QtWidgets.QComboBox(self.case_name_Frame)
        self.appearance_reason_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.appearance_reason_box.setObjectName("appearance_reason_box")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.gridLayout.addWidget(self.appearance_reason_box, 2, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.case_name_Frame, 0, 0, 1, 3)
        self.costs_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.costs_frame.sizePolicy().hasHeightForWidth())
        self.costs_frame.setSizePolicy(sizePolicy)
        self.costs_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.costs_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.costs_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.costs_frame.setLineWidth(2)
        self.costs_frame.setObjectName("costs_frame")
        self.formLayout = QtWidgets.QFormLayout(self.costs_frame)
        self.formLayout.setObjectName("formLayout")
        self.label_11 = QtWidgets.QLabel(self.costs_frame)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.court_costs_box = QtWidgets.QComboBox(self.costs_frame)
        self.court_costs_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.court_costs_box.setObjectName("court_costs_box")
        self.court_costs_box.addItem("")
        self.court_costs_box.addItem("")
        self.court_costs_box.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.court_costs_box)
        self.label_9 = QtWidgets.QLabel(self.costs_frame)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.ability_to_pay_box = QtWidgets.QComboBox(self.costs_frame)
        self.ability_to_pay_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ability_to_pay_box.setObjectName("ability_to_pay_box")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ability_to_pay_box)
        self.label_18 = QtWidgets.QLabel(self.costs_frame)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.balance_due_date = QtWidgets.QDateEdit(self.costs_frame)
        self.balance_due_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.balance_due_date.setCalendarPopup(True)
        self.balance_due_date.setObjectName("balance_due_date")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.balance_due_date)
        self.costs_and_fines_Button = QtWidgets.QPushButton(self.costs_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.costs_and_fines_Button.sizePolicy().hasHeightForWidth())
        self.costs_and_fines_Button.setSizePolicy(sizePolicy)
        self.costs_and_fines_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.costs_and_fines_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.costs_and_fines_Button.setFlat(False)
        self.costs_and_fines_Button.setObjectName("costs_and_fines_Button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.costs_and_fines_Button)
        self.gridLayout_4.addWidget(self.costs_frame, 2, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_2)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(170, 58, 63);")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_7.addWidget(self.close_dialog_Button, 1, 0, 1, 1)
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_2)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_7.addWidget(self.create_entry_Button, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 3, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.no_contest_all_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_contest_all_Button.sizePolicy().hasHeightForWidth())
        self.no_contest_all_Button.setSizePolicy(sizePolicy)
        self.no_contest_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.no_contest_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.no_contest_all_Button.setObjectName("no_contest_all_Button")
        self.gridLayout_3.addWidget(self.no_contest_all_Button, 2, 1, 1, 1)
        self.guilty_all_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guilty_all_Button.sizePolicy().hasHeightForWidth())
        self.guilty_all_Button.setSizePolicy(sizePolicy)
        self.guilty_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.guilty_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.guilty_all_Button.setObjectName("guilty_all_Button")
        self.gridLayout_3.addWidget(self.guilty_all_Button, 2, 2, 1, 1)
        self.add_charge_Button = QtWidgets.QPushButton(self.frame)
        self.add_charge_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_charge_Button.setObjectName("add_charge_Button")
        self.gridLayout_3.addWidget(self.add_charge_Button, 2, 0, 1, 1)
        self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.charges_gridLayout.addWidget(self.label_5, 12, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.charges_gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.charges_gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.charges_gridLayout.addWidget(self.label_14, 6, 0, 1, 1)
        self.plea_label_1 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plea_label_1.setFont(font)
        self.plea_label_1.setObjectName("plea_label_1")
        self.charges_gridLayout.addWidget(self.plea_label_1, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.charges_gridLayout.addWidget(self.label_12, 10, 0, 1, 1)
        self.offense_label_1 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.offense_label_1.setFont(font)
        self.offense_label_1.setWordWrap(True)
        self.offense_label_1.setObjectName("offense_label_1")
        self.charges_gridLayout.addWidget(self.offense_label_1, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.charges_gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.charges_gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.charges_gridLayout.addWidget(self.label_17, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.charges_gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.charges_gridLayout.addWidget(self.label_4, 11, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setObjectName("label_25")
        self.charges_gridLayout.addWidget(self.label_25, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.charges_gridLayout, 0, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 3)
        self.jail_time_credit_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.jail_time_credit_frame.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 75 9pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.jail_time_credit_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.jail_time_credit_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.jail_time_credit_frame.setLineWidth(2)
        self.jail_time_credit_frame.setObjectName("jail_time_credit_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.jail_time_credit_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.in_jail_box = QtWidgets.QComboBox(self.jail_time_credit_frame)
        self.in_jail_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.in_jail_box.setObjectName("in_jail_box")
        self.in_jail_box.addItem("")
        self.in_jail_box.setItemText(0, "")
        self.in_jail_box.addItem("")
        self.in_jail_box.addItem("")
        self.gridLayout_6.addWidget(self.in_jail_box, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.jail_time_credit_frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.jail_time_credit_frame)
        self.label_16.setObjectName("label_16")
        self.gridLayout_6.addWidget(self.label_16, 4, 0, 1, 1)
        self.jail_time_credit_box = QtWidgets.QLineEdit(self.jail_time_credit_frame)
        self.jail_time_credit_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jail_time_credit_box.setObjectName("jail_time_credit_box")
        self.gridLayout_6.addWidget(self.jail_time_credit_box, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.jail_time_credit_frame)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 3, 0, 1, 1)
        self.jail_time_credit_label = QtWidgets.QLabel(self.jail_time_credit_frame)
        self.jail_time_credit_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.jail_time_credit_label.setFont(font)
        self.jail_time_credit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.jail_time_credit_label.setObjectName("jail_time_credit_label")
        self.gridLayout_6.addWidget(self.jail_time_credit_label, 0, 0, 1, 2)
        self.jail_time_credit_apply_box = QtWidgets.QComboBox(self.jail_time_credit_frame)
        self.jail_time_credit_apply_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jail_time_credit_apply_box.setObjectName("jail_time_credit_apply_box")
        self.jail_time_credit_apply_box.addItem("")
        self.jail_time_credit_apply_box.setItemText(0, "")
        self.jail_time_credit_apply_box.addItem("")
        self.jail_time_credit_apply_box.addItem("")
        self.gridLayout_6.addWidget(self.jail_time_credit_apply_box, 4, 1, 1, 1)
        self.gridLayout_4.addWidget(self.jail_time_credit_frame, 2, 2, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 75 9pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.add_conditions_Button = QtWidgets.QPushButton(self.frame_6)
        self.add_conditions_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_conditions_Button.setAutoDefault(False)
        self.add_conditions_Button.setObjectName("add_conditions_Button")
        self.gridLayout_5.addWidget(self.add_conditions_Button, 7, 0, 1, 3)
        self.community_control_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.community_control_checkBox.setObjectName("community_control_checkBox")
        self.gridLayout_5.addWidget(self.community_control_checkBox, 3, 0, 1, 1)
        self.victim_notification_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.victim_notification_checkBox.setObjectName("victim_notification_checkBox")
        self.gridLayout_5.addWidget(self.victim_notification_checkBox, 4, 2, 1, 1)
        self.community_service_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.community_service_checkBox.setObjectName("community_service_checkBox")
        self.gridLayout_5.addWidget(self.community_service_checkBox, 3, 2, 1, 1)
        self.other_conditions_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.other_conditions_checkBox.setEnabled(True)
        self.other_conditions_checkBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.other_conditions_checkBox.setObjectName("other_conditions_checkBox")
        self.gridLayout_5.addWidget(self.other_conditions_checkBox, 5, 2, 1, 1)
        self.license_suspension_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.license_suspension_checkBox.setObjectName("license_suspension_checkBox")
        self.gridLayout_5.addWidget(self.license_suspension_checkBox, 4, 0, 1, 1)
        self.impoundment_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.impoundment_checkBox.setObjectName("impoundment_checkBox")
        self.gridLayout_5.addWidget(self.impoundment_checkBox, 5, 0, 1, 1)
        self.add_conditions_label = QtWidgets.QLabel(self.frame_6)
        self.add_conditions_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.add_conditions_label.setFont(font)
        self.add_conditions_label.setAlignment(QtCore.Qt.AlignCenter)
        self.add_conditions_label.setObjectName("add_conditions_label")
        self.gridLayout_5.addWidget(self.add_conditions_label, 1, 0, 1, 3)
        self.diversion_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.diversion_checkBox.setObjectName("diversion_checkBox")
        self.gridLayout_5.addWidget(self.diversion_checkBox, 0, 0, 1, 1)
        self.jail_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.jail_checkBox.setObjectName("jail_checkBox")
        self.gridLayout_5.addWidget(self.jail_checkBox, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.frame_6, 2, 1, 2, 1)
        self.gridLayout_4.setRowStretch(0, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(JailCCPleaDialog)
        QtCore.QMetaObject.connectSlotsByName(JailCCPleaDialog)
        JailCCPleaDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        JailCCPleaDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        JailCCPleaDialog.setTabOrder(self.case_number_lineEdit, self.defense_counsel_name_box)
        JailCCPleaDialog.setTabOrder(self.defense_counsel_name_box, self.defense_counsel_type_box)
        JailCCPleaDialog.setTabOrder(self.defense_counsel_type_box, self.defense_counsel_waived_checkBox)
        JailCCPleaDialog.setTabOrder(self.defense_counsel_waived_checkBox, self.court_costs_box)
        JailCCPleaDialog.setTabOrder(self.court_costs_box, self.ability_to_pay_box)
        JailCCPleaDialog.setTabOrder(self.ability_to_pay_box, self.balance_due_date)
        JailCCPleaDialog.setTabOrder(self.balance_due_date, self.fra_in_file_box)
        JailCCPleaDialog.setTabOrder(self.fra_in_file_box, self.fra_in_court_box)
        JailCCPleaDialog.setTabOrder(self.fra_in_court_box, self.community_control_checkBox)
        JailCCPleaDialog.setTabOrder(self.community_control_checkBox, self.add_conditions_Button)
        JailCCPleaDialog.setTabOrder(self.add_conditions_Button, self.jail_time_credit_box)
        JailCCPleaDialog.setTabOrder(self.jail_time_credit_box, self.jail_time_credit_apply_box)
        JailCCPleaDialog.setTabOrder(self.jail_time_credit_apply_box, self.create_entry_Button)
        JailCCPleaDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)
        JailCCPleaDialog.setTabOrder(self.close_dialog_Button, self.scrollArea)

    def retranslateUi(self, JailCCPleaDialog):
        _translate = QtCore.QCoreApplication.translate
        JailCCPleaDialog.setWindowTitle(_translate("JailCCPleaDialog", "Jail Community Control Plea Case Information"))
        self.label_21.setText(_translate("JailCCPleaDialog", "FRA shown in complaint/file:"))
        self.fra_in_file_box.setItemText(0, _translate("JailCCPleaDialog", "N/A"))
        self.fra_in_file_box.setItemText(1, _translate("JailCCPleaDialog", "Yes"))
        self.fra_in_file_box.setItemText(2, _translate("JailCCPleaDialog", "No"))
        self.label_22.setText(_translate("JailCCPleaDialog", "FRA shown in court:"))
        self.fra_in_court_box.setItemText(0, _translate("JailCCPleaDialog", "N/A"))
        self.fra_in_court_box.setItemText(1, _translate("JailCCPleaDialog", "Yes"))
        self.fra_in_court_box.setItemText(2, _translate("JailCCPleaDialog", "No"))
        self.label_26.setText(_translate("JailCCPleaDialog", "Date:"))
        self.label.setText(_translate("JailCCPleaDialog", "Def. First Name:"))
        self.label_2.setText(_translate("JailCCPleaDialog", "Def. Last Name:"))
        self.cancel_Button.setText(_translate("JailCCPleaDialog", "Cancel"))
        self.label_3.setText(_translate("JailCCPleaDialog", "Case Number:"))
        self.clear_fields_case_Button.setText(_translate("JailCCPleaDialog", "Clear Fields"))
        self.label_24.setText(_translate("JailCCPleaDialog", "Def. Counsel:"))
        self.defense_counsel_type_box.setItemText(0, _translate("JailCCPleaDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("JailCCPleaDialog", "Private Counsel"))
        self.defense_counsel_waived_checkBox.setText(_translate("JailCCPleaDialog", "Defendant waived right to counsel"))
        self.appearance_reason_box.setItemText(0, _translate("JailCCPleaDialog", "arraignment"))
        self.appearance_reason_box.setItemText(1, _translate("JailCCPleaDialog", "change of plea"))
        self.appearance_reason_box.setItemText(2, _translate("JailCCPleaDialog", "trial to court"))
        self.appearance_reason_box.setItemText(3, _translate("JailCCPleaDialog", "jury trial"))
        self.appearance_reason_box.setItemText(4, _translate("JailCCPleaDialog", "LEAP sentencing"))
        self.label_27.setText(_translate("JailCCPleaDialog", "Appearance Reason:"))
        self.label_11.setText(_translate("JailCCPleaDialog", "Court Costs:"))
        self.court_costs_box.setItemText(0, _translate("JailCCPleaDialog", "Yes"))
        self.court_costs_box.setItemText(1, _translate("JailCCPleaDialog", "Waived"))
        self.court_costs_box.setItemText(2, _translate("JailCCPleaDialog", "No"))
        self.label_9.setText(_translate("JailCCPleaDialog", "Time to pay fines/costs:"))
        self.ability_to_pay_box.setItemText(0, _translate("JailCCPleaDialog", "forthwith"))
        self.ability_to_pay_box.setItemText(1, _translate("JailCCPleaDialog", "within 30 days"))
        self.ability_to_pay_box.setItemText(2, _translate("JailCCPleaDialog", "within 60 days"))
        self.ability_to_pay_box.setItemText(3, _translate("JailCCPleaDialog", "within 90 days"))
        self.label_18.setText(_translate("JailCCPleaDialog", "Fines/costs due date:"))
        self.costs_and_fines_Button.setText(_translate("JailCCPleaDialog", "Show Costs/Fines"))
        self.close_dialog_Button.setText(_translate("JailCCPleaDialog", "Close Dialog"))
        self.create_entry_Button.setText(_translate("JailCCPleaDialog", "Open Entry"))
        self.no_contest_all_Button.setText(_translate("JailCCPleaDialog", "No Contest All"))
        self.guilty_all_Button.setText(_translate("JailCCPleaDialog", "Guilty All"))
        self.add_charge_Button.setText(_translate("JailCCPleaDialog", "Add Charge"))
        self.label_10.setText(_translate("JailCCPleaDialog", "Fines Suspended:"))
        self.label_20.setText(_translate("JailCCPleaDialog", "Degree:"))
        self.label_14.setText(_translate("JailCCPleaDialog", "Finding:"))
        self.plea_label_1.setText(_translate("JailCCPleaDialog", "Plea:"))
        self.label_12.setText(_translate("JailCCPleaDialog", "Jail Days Suspended:"))
        self.offense_label_1.setText(_translate("JailCCPleaDialog", "Offense:"))
        self.label_19.setText(_translate("JailCCPleaDialog", "Statute:"))
        self.label_8.setText(_translate("JailCCPleaDialog", "Jail Days:"))
        self.label_17.setText(_translate("JailCCPleaDialog", "Fines:"))
        self.label_7.setText(_translate("JailCCPleaDialog", "Allied:"))
        self.label_25.setText(_translate("JailCCPleaDialog", "Dismissed:"))
        self.in_jail_box.setItemText(1, _translate("JailCCPleaDialog", "Yes"))
        self.in_jail_box.setItemText(2, _translate("JailCCPleaDialog", "No"))
        self.label_6.setText(_translate("JailCCPleaDialog", "Currently In Jail:"))
        self.label_16.setText(_translate("JailCCPleaDialog", "Apply JTC to:"))
        self.label_13.setText(_translate("JailCCPleaDialog", "Days In Jail:"))
        self.jail_time_credit_label.setText(_translate("JailCCPleaDialog", "Jail Time Credit"))
        self.jail_time_credit_apply_box.setItemText(1, _translate("JailCCPleaDialog", "Costs and Fines"))
        self.jail_time_credit_apply_box.setItemText(2, _translate("JailCCPleaDialog", "Sentence"))
        self.add_conditions_Button.setText(_translate("JailCCPleaDialog", "Add Diversion, Jail or  Additional Conditions"))
        self.community_control_checkBox.setText(_translate("JailCCPleaDialog", "Community Control"))
        self.victim_notification_checkBox.setText(_translate("JailCCPleaDialog", "Victim Notification"))
        self.community_service_checkBox.setText(_translate("JailCCPleaDialog", "Community Service"))
        self.other_conditions_checkBox.setText(_translate("JailCCPleaDialog", "Other"))
        self.license_suspension_checkBox.setText(_translate("JailCCPleaDialog", "License Suspension"))
        self.impoundment_checkBox.setText(_translate("JailCCPleaDialog", "Immobilize/Impound"))
        self.add_conditions_label.setText(_translate("JailCCPleaDialog", "Additional Conditions"))
        self.diversion_checkBox.setText(_translate("JailCCPleaDialog", "Diversion"))
        self.jail_checkBox.setText(_translate("JailCCPleaDialog", "Set Jail Reporting Terms"))
