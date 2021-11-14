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
        MinorMisdemeanorDialog.resize(1000, 789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MinorMisdemeanorDialog.sizePolicy().hasHeightForWidth())
        MinorMisdemeanorDialog.setSizePolicy(sizePolicy)
        MinorMisdemeanorDialog.setMinimumSize(QtCore.QSize(0, 0))
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
        MinorMisdemeanorDialog.setSizeGripEnabled(True)
        MinorMisdemeanorDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(MinorMisdemeanorDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(MinorMisdemeanorDialog)
        self.frame_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.frame_2)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.frame_2)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.plea_trial_date = QtWidgets.QDateEdit(self.frame_2)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.defendant_first_name_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(MinorMisdemeanorDialog)
        self.frame_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.offense_choice_box = QtWidgets.QComboBox(self.frame_3)
        self.offense_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.offense_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.offense_choice_box.setEditable(True)
        self.offense_choice_box.setObjectName("offense_choice_box")
        self.gridLayout_2.addWidget(self.offense_choice_box, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 1, 2, 1, 1)
        self.statute_choice_box = QtWidgets.QComboBox(self.frame_3)
        self.statute_choice_box.setEnabled(True)
        self.statute_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.statute_choice_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.statute_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.statute_choice_box.setEditable(True)
        self.statute_choice_box.setObjectName("statute_choice_box")
        self.gridLayout_2.addWidget(self.statute_choice_box, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.clear_fields_charge_Button = QtWidgets.QPushButton(self.frame_3)
        self.clear_fields_charge_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_charge_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_charge_Button.setObjectName("clear_fields_charge_Button")
        self.gridLayout_2.addWidget(self.clear_fields_charge_Button, 0, 4, 1, 1)
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
        self.verticalLayout.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(MinorMisdemeanorDialog)
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.plea_label_1 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plea_label_1.setFont(font)
        self.plea_label_1.setObjectName("plea_label_1")
        self.charges_gridLayout.addWidget(self.plea_label_1, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.charges_gridLayout.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.charges_gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.charges_gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.charges_gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.charges_gridLayout.addWidget(self.label_17, 6, 0, 1, 1)
        self.offense_label_1 = QtWidgets.QLabel(self.frame)
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
        self.label_19 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.charges_gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.charges_gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.charges_gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.charges_gridLayout, 0, 0, 1, 3)
        self.guilty_all_Button = QtWidgets.QPushButton(self.frame)
        self.guilty_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.guilty_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.guilty_all_Button.setObjectName("guilty_all_Button")
        self.gridLayout_3.addWidget(self.guilty_all_Button, 1, 0, 1, 1)
        self.no_contest_all_Button = QtWidgets.QPushButton(self.frame)
        self.no_contest_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.no_contest_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.no_contest_all_Button.setObjectName("no_contest_all_Button")
        self.gridLayout_3.addWidget(self.no_contest_all_Button, 1, 1, 1, 1)
        self.costs_and_fines_Button = QtWidgets.QPushButton(self.frame)
        self.costs_and_fines_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.costs_and_fines_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.costs_and_fines_Button.setFlat(False)
        self.costs_and_fines_Button.setObjectName("costs_and_fines_Button")
        self.gridLayout_3.addWidget(self.costs_and_fines_Button, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(MinorMisdemeanorDialog)
        self.frame_4.setStyleSheet("background-color: rgb(25, 49, 91);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
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
        self.gridLayout_4.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 75 9pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
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
        self.gridLayout_6.addWidget(self.label_24, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.license_suspension_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.license_suspension_checkBox.setObjectName("license_suspension_checkBox")
        self.gridLayout_5.addWidget(self.license_suspension_checkBox, 0, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_5.addWidget(self.checkBox_4, 0, 1, 1, 1)
        self.community_service_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.community_service_checkBox.setObjectName("community_service_checkBox")
        self.gridLayout_5.addWidget(self.community_service_checkBox, 1, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_5.setEnabled(False)
        self.checkBox_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_5.addWidget(self.checkBox_5, 1, 1, 1, 1)
        self.community_control_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.community_control_checkBox.setEnabled(False)
        self.community_control_checkBox.setObjectName("community_control_checkBox")
        self.gridLayout_5.addWidget(self.community_control_checkBox, 2, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 2, 1, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_7.setEnabled(False)
        self.checkBox_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_5.addWidget(self.checkBox_7, 3, 0, 1, 1)
        self.other_conditions_checkBox = QtWidgets.QCheckBox(self.frame_6)
        self.other_conditions_checkBox.setEnabled(True)
        self.other_conditions_checkBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.other_conditions_checkBox.setObjectName("other_conditions_checkBox")
        self.gridLayout_5.addWidget(self.other_conditions_checkBox, 3, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_6, 0, 1, 2, 2)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setLineWidth(2)
        self.frame_7.setObjectName("frame_7")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_21 = QtWidgets.QLabel(self.frame_7)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
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
        self.gridLayout_4.addWidget(self.frame_7, 1, 0, 2, 1)
        self.add_conditions_Button = QtWidgets.QPushButton(self.frame_4)
        self.add_conditions_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_conditions_Button.setAutoDefault(False)
        self.add_conditions_Button.setObjectName("add_conditions_Button")
        self.gridLayout_4.addWidget(self.add_conditions_Button, 2, 1, 1, 1)
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_4)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_4.addWidget(self.create_entry_Button, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 2)

        self.retranslateUi(MinorMisdemeanorDialog)
        QtCore.QMetaObject.connectSlotsByName(MinorMisdemeanorDialog)
        MinorMisdemeanorDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        MinorMisdemeanorDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        MinorMisdemeanorDialog.setTabOrder(self.case_number_lineEdit, self.statute_choice_box)
        MinorMisdemeanorDialog.setTabOrder(self.statute_choice_box, self.offense_choice_box)
        MinorMisdemeanorDialog.setTabOrder(self.offense_choice_box, self.add_charge_Button)
        MinorMisdemeanorDialog.setTabOrder(self.add_charge_Button, self.court_costs_box)
        MinorMisdemeanorDialog.setTabOrder(self.court_costs_box, self.ability_to_pay_box)
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
        self.label_2.setText(_translate("MinorMisdemeanorDialog", "Def. Last Name:"))
        self.label_3.setText(_translate("MinorMisdemeanorDialog", "Case Number:"))
        self.label.setText(_translate("MinorMisdemeanorDialog", "Def. First Name:"))
        self.clear_fields_case_Button.setText(_translate("MinorMisdemeanorDialog", "Clear Fields"))
        self.cancel_Button.setText(_translate("MinorMisdemeanorDialog", "Cancel"))
        self.label_26.setText(_translate("MinorMisdemeanorDialog", "Date:"))
        self.label_6.setText(_translate("MinorMisdemeanorDialog", "Statute:"))
        self.label_23.setText(_translate("MinorMisdemeanorDialog", "Degree:"))
        self.label_15.setText(_translate("MinorMisdemeanorDialog", "Offense:"))
        self.clear_fields_charge_Button.setText(_translate("MinorMisdemeanorDialog", "Clear Fields"))
        self.degree_choice_box.setItemText(0, _translate("MinorMisdemeanorDialog", "Minor Misdemeanor"))
        self.degree_choice_box.setItemText(1, _translate("MinorMisdemeanorDialog", "M1"))
        self.degree_choice_box.setItemText(2, _translate("MinorMisdemeanorDialog", "M2"))
        self.degree_choice_box.setItemText(3, _translate("MinorMisdemeanorDialog", "M3"))
        self.degree_choice_box.setItemText(4, _translate("MinorMisdemeanorDialog", "M4"))
        self.degree_choice_box.setItemText(5, _translate("MinorMisdemeanorDialog", "Unclassified Misdemeanor"))
        self.add_charge_Button.setText(_translate("MinorMisdemeanorDialog", "Add Charge"))
        self.freeform_entry_checkBox.setText(_translate("MinorMisdemeanorDialog", "Enable freeform entry for offense/statute"))
        self.plea_label_1.setText(_translate("MinorMisdemeanorDialog", "Plea:"))
        self.label_14.setText(_translate("MinorMisdemeanorDialog", "Finding:"))
        self.label_10.setText(_translate("MinorMisdemeanorDialog", "Fines Suspended:"))
        self.label_20.setText(_translate("MinorMisdemeanorDialog", "Degree:"))
        self.label_17.setText(_translate("MinorMisdemeanorDialog", "Fines:"))
        self.offense_label_1.setText(_translate("MinorMisdemeanorDialog", "Offense:"))
        self.label_19.setText(_translate("MinorMisdemeanorDialog", "Statute:"))
        self.label_7.setText(_translate("MinorMisdemeanorDialog", "Allied Offense:"))
        self.guilty_all_Button.setText(_translate("MinorMisdemeanorDialog", "Guilty All"))
        self.no_contest_all_Button.setText(_translate("MinorMisdemeanorDialog", "No Contest All"))
        self.costs_and_fines_Button.setText(_translate("MinorMisdemeanorDialog", "Costs/Fines"))
        self.label_11.setText(_translate("MinorMisdemeanorDialog", "Court Costs:"))
        self.court_costs_box.setItemText(0, _translate("MinorMisdemeanorDialog", "Yes"))
        self.court_costs_box.setItemText(1, _translate("MinorMisdemeanorDialog", "No"))
        self.label_9.setText(_translate("MinorMisdemeanorDialog", "Time to pay fines/costs:"))
        self.ability_to_pay_box.setItemText(0, _translate("MinorMisdemeanorDialog", "forthwith"))
        self.ability_to_pay_box.setItemText(1, _translate("MinorMisdemeanorDialog", "within 30 days"))
        self.ability_to_pay_box.setItemText(2, _translate("MinorMisdemeanorDialog", "within 60 days"))
        self.ability_to_pay_box.setItemText(3, _translate("MinorMisdemeanorDialog", "within 90 days"))
        self.label_18.setText(_translate("MinorMisdemeanorDialog", "Fines/costs due date:"))
        self.label_24.setText(_translate("MinorMisdemeanorDialog", "Additional Conditions"))
        self.license_suspension_checkBox.setText(_translate("MinorMisdemeanorDialog", "License Suspension"))
        self.checkBox_4.setText(_translate("MinorMisdemeanorDialog", "Commitment"))
        self.community_service_checkBox.setText(_translate("MinorMisdemeanorDialog", "Community Service"))
        self.checkBox_5.setText(_translate("MinorMisdemeanorDialog", "Forfeiture"))
        self.community_control_checkBox.setText(_translate("MinorMisdemeanorDialog", "Community Control"))
        self.checkBox_3.setText(_translate("MinorMisdemeanorDialog", "Fingerprinting"))
        self.checkBox_7.setText(_translate("MinorMisdemeanorDialog", "Vehicle Conditions"))
        self.other_conditions_checkBox.setText(_translate("MinorMisdemeanorDialog", "Other"))
        self.label_21.setText(_translate("MinorMisdemeanorDialog", "FRA shown in complaint/file:"))
        self.fra_in_file_box.setItemText(0, _translate("MinorMisdemeanorDialog", "N/A"))
        self.fra_in_file_box.setItemText(1, _translate("MinorMisdemeanorDialog", "Yes"))
        self.fra_in_file_box.setItemText(2, _translate("MinorMisdemeanorDialog", "No"))
        self.label_22.setText(_translate("MinorMisdemeanorDialog", "FRA shown in court:"))
        self.fra_in_court_box.setItemText(0, _translate("MinorMisdemeanorDialog", "N/A"))
        self.fra_in_court_box.setItemText(1, _translate("MinorMisdemeanorDialog", "Yes"))
        self.fra_in_court_box.setItemText(2, _translate("MinorMisdemeanorDialog", "No"))
        self.add_conditions_Button.setText(_translate("MinorMisdemeanorDialog", "Add Conditions"))
        self.create_entry_Button.setText(_translate("MinorMisdemeanorDialog", "Create Entry"))
