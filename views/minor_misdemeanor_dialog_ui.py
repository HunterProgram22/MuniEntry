# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/MinorMisdemeanorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MinorMisdemeanorDialog(object):
    def setupUi(self, MinorMisdemeanorDialog):
        MinorMisdemeanorDialog.setObjectName("MinorMisdemeanorDialog")
        MinorMisdemeanorDialog.setWindowModality(QtCore.Qt.NonModal)
        MinorMisdemeanorDialog.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MinorMisdemeanorDialog.sizePolicy().hasHeightForWidth())
        MinorMisdemeanorDialog.setSizePolicy(sizePolicy)
        MinorMisdemeanorDialog.setMinimumSize(QtCore.QSize(1000, 800))
        MinorMisdemeanorDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        MinorMisdemeanorDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MinorMisdemeanorDialog.setFont(font)
        MinorMisdemeanorDialog.setToolTip("")
        MinorMisdemeanorDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        MinorMisdemeanorDialog.setModal(True)
        self.frame = QtWidgets.QFrame(MinorMisdemeanorDialog)
        self.frame.setGeometry(QtCore.QRect(10, 130, 981, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(833, 10, 143, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.clear_fields_charge_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.clear_fields_charge_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_charge_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_charge_Button.setObjectName("clear_fields_charge_Button")
        self.gridLayout.addWidget(self.clear_fields_charge_Button, 0, 0, 1, 1)
        self.add_charge_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.add_charge_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.add_charge_Button.setObjectName("add_charge_Button")
        self.gridLayout.addWidget(self.add_charge_Button, 2, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 9, 811, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.statute_choice_box = QtWidgets.QComboBox(self.layoutWidget1)
        self.statute_choice_box.setEnabled(True)
        self.statute_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.statute_choice_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.statute_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.statute_choice_box.setEditable(True)
        self.statute_choice_box.setObjectName("statute_choice_box")
        self.gridLayout_3.addWidget(self.statute_choice_box, 0, 1, 1, 1)
        self.freeform_entry_checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
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
        self.gridLayout_3.addWidget(self.freeform_entry_checkBox, 0, 2, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)
        self.offense_choice_box = QtWidgets.QComboBox(self.layoutWidget1)
        self.offense_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.offense_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.offense_choice_box.setEditable(True)
        self.offense_choice_box.setObjectName("offense_choice_box")
        self.gridLayout_3.addWidget(self.offense_choice_box, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 1, 2, 1, 1)
        self.degree_choice_box = QtWidgets.QComboBox(self.layoutWidget1)
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
        self.gridLayout_3.addWidget(self.degree_choice_box, 1, 3, 1, 1)
        self.frame_2 = QtWidgets.QFrame(MinorMisdemeanorDialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 240, 981, 361))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 961, 261))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.charges_gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.charges_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.plea_label_1 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plea_label_1.setFont(font)
        self.plea_label_1.setObjectName("plea_label_1")
        self.charges_gridLayout.addWidget(self.plea_label_1, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.charges_gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.charges_gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.charges_gridLayout.addWidget(self.label_17, 5, 0, 1, 1)
        self.offense_label_1 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.offense_label_1.setFont(font)
        self.offense_label_1.setWordWrap(True)
        self.offense_label_1.setObjectName("offense_label_1")
        self.charges_gridLayout.addWidget(self.offense_label_1, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.charges_gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.charges_gridLayout.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.charges_gridLayout.addWidget(self.label_25, 7, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(MinorMisdemeanorDialog)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 981, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-color: rgb(160, 48, 35);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.frame_3)
        self.clear_fields_case_Button.setGeometry(QtCore.QRect(835, 70, 141, 33))
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.cancel_Button = QtWidgets.QPushButton(self.frame_3)
        self.cancel_Button.setGeometry(QtCore.QRect(835, 12, 141, 33))
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(480, 11, 341, 96))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_26.setObjectName("label_26")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.plea_trial_date = QtWidgets.QDateEdit(self.layoutWidget2)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plea_trial_date)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.operator_license_number_lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.operator_license_number_lineEdit.setEnabled(False)
        self.operator_license_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.operator_license_number_lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.operator_license_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.operator_license_number_lineEdit.setObjectName("operator_license_number_lineEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.operator_license_number_lineEdit)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setToolTip("")
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.defendant_birth_date = QtWidgets.QDateEdit(self.layoutWidget2)
        self.defendant_birth_date.setEnabled(False)
        self.defendant_birth_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.defendant_birth_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_birth_date.setDateTime(QtCore.QDateTime(QtCore.QDate(1980, 1, 1), QtCore.QTime(0, 0, 0)))
        self.defendant_birth_date.setCalendarPopup(True)
        self.defendant_birth_date.setObjectName("defendant_birth_date")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.defendant_birth_date)
        self.layoutWidget3 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 10, 441, 98))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.layoutWidget3)
        self.defendant_first_name_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.defendant_first_name_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.layoutWidget3)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.defendant_last_name_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.layoutWidget3)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.case_number_lineEdit)
        self.frame_4 = QtWidgets.QFrame(MinorMisdemeanorDialog)
        self.frame_4.setGeometry(QtCore.QRect(10, 610, 491, 81))
        self.frame_4.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.frame_4.setObjectName("frame_4")
        self.layoutWidget4 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget4.setGeometry(QtCore.QRect(11, 10, 471, 64))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget4)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.ability_to_pay_box = QtWidgets.QComboBox(self.layoutWidget4)
        self.ability_to_pay_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ability_to_pay_box.setObjectName("ability_to_pay_box")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ability_to_pay_box)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.balance_due_date = QtWidgets.QDateEdit(self.layoutWidget4)
        self.balance_due_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.balance_due_date.setObjectName("balance_due_date")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.balance_due_date)
        self.create_entry_Button = QtWidgets.QPushButton(MinorMisdemeanorDialog)
        self.create_entry_Button.setGeometry(QtCore.QRect(810, 760, 181, 31))
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.frame_5 = QtWidgets.QFrame(MinorMisdemeanorDialog)
        self.frame_5.setGeometry(QtCore.QRect(10, 710, 491, 81))
        self.frame_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.layoutWidget5 = QtWidgets.QWidget(self.frame_5)
        self.layoutWidget5.setGeometry(QtCore.QRect(11, 10, 471, 66))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget5)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.fra_in_file_box = QtWidgets.QComboBox(self.layoutWidget5)
        self.fra_in_file_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_file_box.setObjectName("fra_in_file_box")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fra_in_file_box)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_22.setObjectName("label_22")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.fra_in_court_box = QtWidgets.QComboBox(self.layoutWidget5)
        self.fra_in_court_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_court_box.setObjectName("fra_in_court_box")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fra_in_court_box)
        self.frame_6 = QtWidgets.QFrame(MinorMisdemeanorDialog)
        self.frame_6.setGeometry(QtCore.QRect(510, 610, 481, 141))
        self.frame_6.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 75 9pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setGeometry(QtCore.QRect(14, 10, 451, 16))
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
        self.layoutWidget6 = QtWidgets.QWidget(self.frame_6)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 31, 461, 101))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.license_suspension_checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.license_suspension_checkBox.setObjectName("license_suspension_checkBox")
        self.gridLayout_5.addWidget(self.license_suspension_checkBox, 0, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_5.addWidget(self.checkBox_4, 0, 1, 1, 1)
        self.community_service_checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.community_service_checkBox.setObjectName("community_service_checkBox")
        self.gridLayout_5.addWidget(self.community_service_checkBox, 1, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_5.setEnabled(False)
        self.checkBox_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_5.addWidget(self.checkBox_5, 1, 1, 1, 1)
        self.community_control_checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.community_control_checkBox.setEnabled(False)
        self.community_control_checkBox.setObjectName("community_control_checkBox")
        self.gridLayout_5.addWidget(self.community_control_checkBox, 2, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 2, 1, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_7.setEnabled(False)
        self.checkBox_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_5.addWidget(self.checkBox_7, 3, 0, 1, 1)
        self.other_conditions_checkBox = QtWidgets.QCheckBox(self.layoutWidget6)
        self.other_conditions_checkBox.setEnabled(True)
        self.other_conditions_checkBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.other_conditions_checkBox.setObjectName("other_conditions_checkBox")
        self.gridLayout_5.addWidget(self.other_conditions_checkBox, 3, 1, 1, 1)
        self.add_conditions_Button = QtWidgets.QPushButton(MinorMisdemeanorDialog)
        self.add_conditions_Button.setGeometry(QtCore.QRect(510, 760, 181, 31))
        self.add_conditions_Button.setStyleSheet("background-color: rgb(157, 53, 36);")
        self.add_conditions_Button.setAutoDefault(False)
        self.add_conditions_Button.setObjectName("add_conditions_Button")

        self.retranslateUi(MinorMisdemeanorDialog)
        self.cancel_Button.pressed.connect(MinorMisdemeanorDialog.reject)
        self.clear_fields_case_Button.pressed.connect(self.defendant_first_name_lineEdit.clear)
        self.clear_fields_case_Button.pressed.connect(self.operator_license_number_lineEdit.clear)
        self.clear_fields_case_Button.pressed.connect(self.case_number_lineEdit.clear)
        self.clear_fields_case_Button.pressed.connect(self.defendant_last_name_lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MinorMisdemeanorDialog)
        MinorMisdemeanorDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        MinorMisdemeanorDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        MinorMisdemeanorDialog.setTabOrder(self.case_number_lineEdit, self.statute_choice_box)
        MinorMisdemeanorDialog.setTabOrder(self.statute_choice_box, self.offense_choice_box)
        MinorMisdemeanorDialog.setTabOrder(self.offense_choice_box, self.add_charge_Button)
        MinorMisdemeanorDialog.setTabOrder(self.add_charge_Button, self.ability_to_pay_box)
        MinorMisdemeanorDialog.setTabOrder(self.ability_to_pay_box, self.balance_due_date)
        MinorMisdemeanorDialog.setTabOrder(self.balance_due_date, self.fra_in_file_box)
        MinorMisdemeanorDialog.setTabOrder(self.fra_in_file_box, self.fra_in_court_box)
        MinorMisdemeanorDialog.setTabOrder(self.fra_in_court_box, self.license_suspension_checkBox)
        MinorMisdemeanorDialog.setTabOrder(self.license_suspension_checkBox, self.community_service_checkBox)
        MinorMisdemeanorDialog.setTabOrder(self.community_service_checkBox, self.community_control_checkBox)
        MinorMisdemeanorDialog.setTabOrder(self.community_control_checkBox, self.add_conditions_Button)
        MinorMisdemeanorDialog.setTabOrder(self.add_conditions_Button, self.create_entry_Button)

    def retranslateUi(self, MinorMisdemeanorDialog):
        _translate = QtCore.QCoreApplication.translate
        MinorMisdemeanorDialog.setWindowTitle(_translate("MinorMisdemeanorDialog", "Minor Misdemeanor Case Information"))
        self.clear_fields_charge_Button.setText(_translate("MinorMisdemeanorDialog", "Clear Fields"))
        self.add_charge_Button.setText(_translate("MinorMisdemeanorDialog", "Add Charge"))
        self.label_6.setText(_translate("MinorMisdemeanorDialog", "Statute:"))
        self.freeform_entry_checkBox.setText(_translate("MinorMisdemeanorDialog", "Enable freeform entry for offense/statute"))
        self.label_15.setText(_translate("MinorMisdemeanorDialog", "Offense:"))
        self.label_23.setText(_translate("MinorMisdemeanorDialog", "Degree:"))
        self.degree_choice_box.setItemText(0, _translate("MinorMisdemeanorDialog", "Minor Misdemeanor"))
        self.degree_choice_box.setItemText(1, _translate("MinorMisdemeanorDialog", "M1"))
        self.degree_choice_box.setItemText(2, _translate("MinorMisdemeanorDialog", "M2"))
        self.degree_choice_box.setItemText(3, _translate("MinorMisdemeanorDialog", "M3"))
        self.degree_choice_box.setItemText(4, _translate("MinorMisdemeanorDialog", "M4"))
        self.degree_choice_box.setItemText(5, _translate("MinorMisdemeanorDialog", "Unclassified Misdemeanor"))
        self.plea_label_1.setText(_translate("MinorMisdemeanorDialog", "Plea:"))
        self.label_10.setText(_translate("MinorMisdemeanorDialog", "Fines Suspended:"))
        self.label_20.setText(_translate("MinorMisdemeanorDialog", "Degree:"))
        self.label_17.setText(_translate("MinorMisdemeanorDialog", "Fines:"))
        self.offense_label_1.setText(_translate("MinorMisdemeanorDialog", "Offense:"))
        self.label_19.setText(_translate("MinorMisdemeanorDialog", "Statute:"))
        self.label_14.setText(_translate("MinorMisdemeanorDialog", "Finding:"))
        self.clear_fields_case_Button.setText(_translate("MinorMisdemeanorDialog", "Clear Fields"))
        self.cancel_Button.setText(_translate("MinorMisdemeanorDialog", "Cancel"))
        self.label_26.setText(_translate("MinorMisdemeanorDialog", "Date:"))
        self.label_4.setText(_translate("MinorMisdemeanorDialog", "License No."))
        self.label_5.setText(_translate("MinorMisdemeanorDialog", "Date of Birth:"))
        self.label.setText(_translate("MinorMisdemeanorDialog", "Def. First Name:"))
        self.label_2.setText(_translate("MinorMisdemeanorDialog", "Def. Last Name:"))
        self.label_3.setText(_translate("MinorMisdemeanorDialog", "Case Number:"))
        self.label_9.setText(_translate("MinorMisdemeanorDialog", "Pay fines and costs:"))
        self.ability_to_pay_box.setItemText(0, _translate("MinorMisdemeanorDialog", "forthwith"))
        self.ability_to_pay_box.setItemText(1, _translate("MinorMisdemeanorDialog", "within 30 days"))
        self.ability_to_pay_box.setItemText(2, _translate("MinorMisdemeanorDialog", "within 60 days"))
        self.ability_to_pay_box.setItemText(3, _translate("MinorMisdemeanorDialog", "within 90 days"))
        self.label_18.setText(_translate("MinorMisdemeanorDialog", "Balance of fines and costs due:"))
        self.create_entry_Button.setText(_translate("MinorMisdemeanorDialog", "Create Entry"))
        self.label_21.setText(_translate("MinorMisdemeanorDialog", "FRA shown in complaint/file:"))
        self.fra_in_file_box.setItemText(0, _translate("MinorMisdemeanorDialog", "N/A"))
        self.fra_in_file_box.setItemText(1, _translate("MinorMisdemeanorDialog", "Yes"))
        self.fra_in_file_box.setItemText(2, _translate("MinorMisdemeanorDialog", "No"))
        self.label_22.setText(_translate("MinorMisdemeanorDialog", "FRA shown in court:"))
        self.fra_in_court_box.setItemText(0, _translate("MinorMisdemeanorDialog", "N/A"))
        self.fra_in_court_box.setItemText(1, _translate("MinorMisdemeanorDialog", "Yes"))
        self.fra_in_court_box.setItemText(2, _translate("MinorMisdemeanorDialog", "No"))
        self.label_24.setText(_translate("MinorMisdemeanorDialog", "Additional Conditions"))
        self.license_suspension_checkBox.setText(_translate("MinorMisdemeanorDialog", "License Suspension"))
        self.checkBox_4.setText(_translate("MinorMisdemeanorDialog", "Commitment"))
        self.community_service_checkBox.setText(_translate("MinorMisdemeanorDialog", "Community Service"))
        self.checkBox_5.setText(_translate("MinorMisdemeanorDialog", "Forfeiture"))
        self.community_control_checkBox.setText(_translate("MinorMisdemeanorDialog", "Community Control"))
        self.checkBox_3.setText(_translate("MinorMisdemeanorDialog", "Fingerprinting"))
        self.checkBox_7.setText(_translate("MinorMisdemeanorDialog", "Vehicle Conditions"))
        self.other_conditions_checkBox.setText(_translate("MinorMisdemeanorDialog", "Other"))
        self.add_conditions_Button.setText(_translate("MinorMisdemeanorDialog", "Add Conditions"))
