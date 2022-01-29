# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package\views\ui\NoJailPleaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NoJailPleaDialog(object):
    def setupUi(self, NoJailPleaDialog):
        NoJailPleaDialog.setObjectName("NoJailPleaDialog")
        NoJailPleaDialog.setWindowModality(QtCore.Qt.NonModal)
        NoJailPleaDialog.resize(1043, 878)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NoJailPleaDialog.sizePolicy().hasHeightForWidth())
        NoJailPleaDialog.setSizePolicy(sizePolicy)
        NoJailPleaDialog.setMinimumSize(QtCore.QSize(0, 0))
        NoJailPleaDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        NoJailPleaDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        NoJailPleaDialog.setFont(font)
        NoJailPleaDialog.setToolTip("")
        NoJailPleaDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        NoJailPleaDialog.setSizeGripEnabled(True)
        NoJailPleaDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(NoJailPleaDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(NoJailPleaDialog)
        self.scrollArea.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1021, 856))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
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
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.plea_trial_date = QtWidgets.QDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.defense_counsel_name_box = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 3, 1, 1, 1)
        self.defense_counsel_type_box = QtWidgets.QComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 3, 2, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 3, 3, 1, 1)
        self.gridLayout_4.addWidget(self.case_name_Frame, 0, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_2)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_6.addWidget(self.create_entry_Button, 0, 0, 1, 1)
        self.print_entry_Button = QtWidgets.QPushButton(self.frame_2)
        self.print_entry_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.print_entry_Button.setAutoDefault(False)
        self.print_entry_Button.setObjectName("print_entry_Button")
        self.gridLayout_6.addWidget(self.print_entry_Button, 1, 0, 1, 1)
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_2)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(170, 58, 63);")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_6.addWidget(self.close_dialog_Button, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 3, 2, 4, 1)
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
        self.guilty_all_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guilty_all_Button.sizePolicy().hasHeightForWidth())
        self.guilty_all_Button.setSizePolicy(sizePolicy)
        self.guilty_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.guilty_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.guilty_all_Button.setObjectName("guilty_all_Button")
        self.gridLayout_3.addWidget(self.guilty_all_Button, 1, 0, 1, 1)
        self.costs_and_fines_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.costs_and_fines_Button.sizePolicy().hasHeightForWidth())
        self.costs_and_fines_Button.setSizePolicy(sizePolicy)
        self.costs_and_fines_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.costs_and_fines_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.costs_and_fines_Button.setFlat(False)
        self.costs_and_fines_Button.setObjectName("costs_and_fines_Button")
        self.gridLayout_3.addWidget(self.costs_and_fines_Button, 1, 2, 1, 1)
        self.no_contest_all_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_contest_all_Button.sizePolicy().hasHeightForWidth())
        self.no_contest_all_Button.setSizePolicy(sizePolicy)
        self.no_contest_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.no_contest_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.no_contest_all_Button.setObjectName("no_contest_all_Button")
        self.gridLayout_3.addWidget(self.no_contest_all_Button, 1, 1, 1, 1)
        self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
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
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.charges_gridLayout.addWidget(self.label_5, 10, 0, 1, 1)
        self.dismissed_label = QtWidgets.QLabel(self.frame)
        self.dismissed_label.setObjectName("dismissed_label")
        self.charges_gridLayout.addWidget(self.dismissed_label, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.charges_gridLayout, 0, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 3)
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setLineWidth(2)
        self.frame_7.setObjectName("frame_7")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout_2.setObjectName("formLayout_2")
        self.fra_in_file_box = QtWidgets.QComboBox(self.frame_7)
        self.fra_in_file_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_file_box.setObjectName("fra_in_file_box")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fra_in_file_box)
        self.label_22 = QtWidgets.QLabel(self.frame_7)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.fra_in_court_box = QtWidgets.QComboBox(self.frame_7)
        self.fra_in_court_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_court_box.setObjectName("fra_in_court_box")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fra_in_court_box)
        self.label_21 = QtWidgets.QLabel(self.frame_7)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.gridLayout_4.addWidget(self.frame_7, 6, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.clear_fields_charge_Button = QtWidgets.QPushButton(self.frame_3)
        self.clear_fields_charge_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_charge_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_charge_Button.setObjectName("clear_fields_charge_Button")
        self.gridLayout_2.addWidget(self.clear_fields_charge_Button, 0, 4, 1, 1)
        self.offense_choice_box = QtWidgets.QComboBox(self.frame_3)
        self.offense_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.offense_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.offense_choice_box.setEditable(True)
        self.offense_choice_box.setObjectName("offense_choice_box")
        self.gridLayout_2.addWidget(self.offense_choice_box, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.statute_choice_box = QtWidgets.QComboBox(self.frame_3)
        self.statute_choice_box.setEnabled(True)
        self.statute_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.statute_choice_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.statute_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.statute_choice_box.setEditable(True)
        self.statute_choice_box.setObjectName("statute_choice_box")
        self.gridLayout_2.addWidget(self.statute_choice_box, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 1, 2, 1, 1)
        self.degree_choice_box = QtWidgets.QComboBox(self.frame_3)
        self.degree_choice_box.setEnabled(True)
        self.degree_choice_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.degree_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.degree_choice_box.setObjectName("degree_choice_box")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.gridLayout_2.addWidget(self.degree_choice_box, 1, 3, 1, 1)
        self.add_charge_Button = QtWidgets.QPushButton(self.frame_3)
        self.add_charge_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.add_charge_Button.setObjectName("add_charge_Button")
        self.gridLayout_2.addWidget(self.add_charge_Button, 1, 4, 1, 1)
        self.freeform_entry_checkBox = QtWidgets.QCheckBox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.freeform_entry_checkBox.setFont(font)
        self.freeform_entry_checkBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.freeform_entry_checkBox.setStyleSheet("font: 75 9pt \"Palatino Linotype\";")
        self.freeform_entry_checkBox.setObjectName("freeform_entry_checkBox")
        self.gridLayout_2.addWidget(self.freeform_entry_checkBox, 0, 2, 1, 2)
        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 3)
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
        self.other_conditions_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.other_conditions_checkBox.setEnabled(True)
        self.other_conditions_checkBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.other_conditions_checkBox.setObjectName("other_conditions_checkBox")
        self.gridLayout_5.addWidget(self.other_conditions_checkBox, 3, 0, 1, 1)
        self.license_suspension_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.license_suspension_checkBox.setObjectName("license_suspension_checkBox")
        self.gridLayout_5.addWidget(self.license_suspension_checkBox, 1, 0, 1, 1)
        self.community_service_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.community_service_checkBox.setObjectName("community_service_checkBox")
        self.gridLayout_5.addWidget(self.community_service_checkBox, 2, 0, 1, 1)
        self.add_conditions_Button = QtWidgets.QPushButton(self.frame_6)
        self.add_conditions_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_conditions_Button.setAutoDefault(False)
        self.add_conditions_Button.setObjectName("add_conditions_Button")
        self.gridLayout_5.addWidget(self.add_conditions_Button, 4, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_6, 3, 1, 4, 1)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.formLayout = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout.setObjectName("formLayout")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.court_costs_box = QtWidgets.QComboBox(self.frame_5)
        self.court_costs_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.court_costs_box.setObjectName("court_costs_box")
        self.court_costs_box.addItem("")
        self.court_costs_box.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.court_costs_box)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.ability_to_pay_box = QtWidgets.QComboBox(self.frame_5)
        self.ability_to_pay_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ability_to_pay_box.setObjectName("ability_to_pay_box")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ability_to_pay_box)
        self.label_18 = QtWidgets.QLabel(self.frame_5)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.balance_due_date = QtWidgets.QDateEdit(self.frame_5)
        self.balance_due_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.balance_due_date.setObjectName("balance_due_date")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.balance_due_date)
        self.gridLayout_4.addWidget(self.frame_5, 3, 0, 3, 1)
        self.gridLayout_4.setRowStretch(0, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(NoJailPleaDialog)
        QtCore.QMetaObject.connectSlotsByName(NoJailPleaDialog)
        NoJailPleaDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        NoJailPleaDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        NoJailPleaDialog.setTabOrder(self.case_number_lineEdit, self.statute_choice_box)
        NoJailPleaDialog.setTabOrder(self.statute_choice_box, self.offense_choice_box)
        NoJailPleaDialog.setTabOrder(self.offense_choice_box, self.add_charge_Button)
        NoJailPleaDialog.setTabOrder(self.add_charge_Button, self.court_costs_box)
        NoJailPleaDialog.setTabOrder(self.court_costs_box, self.ability_to_pay_box)
        NoJailPleaDialog.setTabOrder(self.ability_to_pay_box, self.balance_due_date)
        NoJailPleaDialog.setTabOrder(self.balance_due_date, self.fra_in_file_box)
        NoJailPleaDialog.setTabOrder(self.fra_in_file_box, self.fra_in_court_box)
        NoJailPleaDialog.setTabOrder(self.fra_in_court_box, self.license_suspension_checkBox)
        NoJailPleaDialog.setTabOrder(self.license_suspension_checkBox, self.community_service_checkBox)
        NoJailPleaDialog.setTabOrder(self.community_service_checkBox, self.scrollArea)

    def retranslateUi(self, NoJailPleaDialog):
        _translate = QtCore.QCoreApplication.translate
        NoJailPleaDialog.setWindowTitle(_translate("NoJailPleaDialog", "No Jail Plea Case Information"))
        self.clear_fields_case_Button.setText(_translate("NoJailPleaDialog", "Clear Fields"))
        self.label.setText(_translate("NoJailPleaDialog", "Def. First Name:"))
        self.label_26.setText(_translate("NoJailPleaDialog", "Date:"))
        self.label_2.setText(_translate("NoJailPleaDialog", "Def. Last Name:"))
        self.cancel_Button.setText(_translate("NoJailPleaDialog", "Cancel"))
        self.label_3.setText(_translate("NoJailPleaDialog", "Case Number:"))
        self.label_8.setText(_translate("NoJailPleaDialog", "Def. Counsel:"))
        self.defense_counsel_type_box.setItemText(0, _translate("NoJailPleaDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("NoJailPleaDialog", "Private"))
        self.defense_counsel_waived_checkBox.setText(_translate("NoJailPleaDialog", "Defendant waived right to counsel"))
        self.create_entry_Button.setText(_translate("NoJailPleaDialog", "Open Entry"))
        self.print_entry_Button.setText(_translate("NoJailPleaDialog", "Print and Open Entry"))
        self.close_dialog_Button.setText(_translate("NoJailPleaDialog", "Close Dialog"))
        self.guilty_all_Button.setText(_translate("NoJailPleaDialog", "Guilty All"))
        self.costs_and_fines_Button.setText(_translate("NoJailPleaDialog", "Costs/Fines"))
        self.no_contest_all_Button.setText(_translate("NoJailPleaDialog", "No Contest All"))
        self.allied_label.setText(_translate("NoJailPleaDialog", "Allied:"))
        self.plea_label.setText(_translate("NoJailPleaDialog", "Plea:"))
        self.statute_label.setText(_translate("NoJailPleaDialog", "Statute:"))
        self.degree_label.setText(_translate("NoJailPleaDialog", "Degree:"))
        self.offense_label.setText(_translate("NoJailPleaDialog", "Offense:"))
        self.fines_suspended_label.setText(_translate("NoJailPleaDialog", "Fines Suspended:"))
        self.finding_label.setText(_translate("NoJailPleaDialog", "Finding:"))
        self.fines_label.setText(_translate("NoJailPleaDialog", "Fines:"))
        self.dismissed_label.setText(_translate("NoJailPleaDialog", "Dismissed:"))
        self.fra_in_file_box.setItemText(0, _translate("NoJailPleaDialog", "N/A"))
        self.fra_in_file_box.setItemText(1, _translate("NoJailPleaDialog", "Yes"))
        self.fra_in_file_box.setItemText(2, _translate("NoJailPleaDialog", "No"))
        self.label_22.setText(_translate("NoJailPleaDialog", "FRA shown in court:"))
        self.fra_in_court_box.setItemText(0, _translate("NoJailPleaDialog", "N/A"))
        self.fra_in_court_box.setItemText(1, _translate("NoJailPleaDialog", "Yes"))
        self.fra_in_court_box.setItemText(2, _translate("NoJailPleaDialog", "No"))
        self.label_21.setText(_translate("NoJailPleaDialog", "FRA shown in complaint/file:"))
        self.label_15.setText(_translate("NoJailPleaDialog", "Offense:"))
        self.clear_fields_charge_Button.setText(_translate("NoJailPleaDialog", "Clear Fields"))
        self.label_6.setText(_translate("NoJailPleaDialog", "Statute:"))
        self.label_23.setText(_translate("NoJailPleaDialog", "Degree:"))
        self.degree_choice_box.setItemText(0, _translate("NoJailPleaDialog", "Minor Misdemeanor"))
        self.degree_choice_box.setItemText(1, _translate("NoJailPleaDialog", "M1"))
        self.degree_choice_box.setItemText(2, _translate("NoJailPleaDialog", "M2"))
        self.degree_choice_box.setItemText(3, _translate("NoJailPleaDialog", "M3"))
        self.degree_choice_box.setItemText(4, _translate("NoJailPleaDialog", "M4"))
        self.degree_choice_box.setItemText(5, _translate("NoJailPleaDialog", "Unclassified Misdemeanor"))
        self.add_charge_Button.setText(_translate("NoJailPleaDialog", "Add Charge"))
        self.freeform_entry_checkBox.setText(_translate("NoJailPleaDialog", "Enable freeform entry for offense/statute"))
        self.other_conditions_checkBox.setText(_translate("NoJailPleaDialog", "Other"))
        self.license_suspension_checkBox.setText(_translate("NoJailPleaDialog", "License Suspension"))
        self.community_service_checkBox.setText(_translate("NoJailPleaDialog", "Community Service"))
        self.add_conditions_Button.setText(_translate("NoJailPleaDialog", "Add Conditions"))
        self.label_24.setText(_translate("NoJailPleaDialog", "Additional Conditions"))
        self.label_11.setText(_translate("NoJailPleaDialog", "Court Costs:"))
        self.court_costs_box.setItemText(0, _translate("NoJailPleaDialog", "Yes"))
        self.court_costs_box.setItemText(1, _translate("NoJailPleaDialog", "No"))
        self.label_9.setText(_translate("NoJailPleaDialog", "Time to pay fines/costs:"))
        self.ability_to_pay_box.setItemText(0, _translate("NoJailPleaDialog", "forthwith"))
        self.ability_to_pay_box.setItemText(1, _translate("NoJailPleaDialog", "within 30 days"))
        self.ability_to_pay_box.setItemText(2, _translate("NoJailPleaDialog", "within 60 days"))
        self.ability_to_pay_box.setItemText(3, _translate("NoJailPleaDialog", "within 90 days"))
        self.label_18.setText(_translate("NoJailPleaDialog", "Fines/costs due date:"))
