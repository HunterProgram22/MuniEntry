# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './munientry/views/ui/LeapPleaValidDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LeapPleaValidDialog(object):
    def setupUi(self, LeapPleaValidDialog):
        LeapPleaValidDialog.setObjectName("LeapPleaValidDialog")
        LeapPleaValidDialog.setWindowModality(QtCore.Qt.NonModal)
        LeapPleaValidDialog.resize(1000, 792)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LeapPleaValidDialog.sizePolicy().hasHeightForWidth())
        LeapPleaValidDialog.setSizePolicy(sizePolicy)
        LeapPleaValidDialog.setMinimumSize(QtCore.QSize(0, 0))
        LeapPleaValidDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        LeapPleaValidDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        LeapPleaValidDialog.setFont(font)
        LeapPleaValidDialog.setToolTip("")
        LeapPleaValidDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        LeapPleaValidDialog.setSizeGripEnabled(True)
        LeapPleaValidDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(LeapPleaValidDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(LeapPleaValidDialog)
        self.frame_4.setStyleSheet("background-color: rgb(25, 49, 91);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 960, 752))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.add_charge_Button = QtWidgets.QPushButton(self.frame_6)
        self.add_charge_Button.setStyleSheet("background-color: rgb(62, 146, 255);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.add_charge_Button.setObjectName("add_charge_Button")
        self.gridLayout_2.addWidget(self.add_charge_Button, 2, 0, 1, 1)
        self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setObjectName("label_5")
        self.charges_gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.charges_gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.charges_gridLayout.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.charges_gridLayout.addWidget(self.label_21, 2, 0, 1, 1)
        self.offense_label_1 = QtWidgets.QLabel(self.frame_6)
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
        self.plea_label_1 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plea_label_1.setFont(font)
        self.plea_label_1.setObjectName("plea_label_1")
        self.charges_gridLayout.addWidget(self.plea_label_1, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.charges_gridLayout, 0, 0, 1, 2)
        self.guilty_all_Button = QtWidgets.QPushButton(self.frame_6)
        self.guilty_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.guilty_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.guilty_all_Button.setObjectName("guilty_all_Button")
        self.gridLayout_2.addWidget(self.guilty_all_Button, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_6)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)
        self.gridLayout_5.addWidget(self.frame_6, 1, 0, 1, 1)
        self.case_name_Frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_name_Frame.sizePolicy().hasHeightForWidth())
        self.case_name_Frame.setSizePolicy(sizePolicy)
        self.case_name_Frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.case_name_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_name_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.case_name_Frame.setLineWidth(2)
        self.case_name_Frame.setObjectName("case_name_Frame")
        self.gridLayout = QtWidgets.QGridLayout(self.case_name_Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 2, 3, 1, 1)
        self.defense_counsel_name_box = DefenseCounselComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 2, 1, 1, 1)
        self.defense_counsel_type_box = NoScrollComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 2, 2, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.appearance_reason_box = NoScrollComboBox(self.case_name_Frame)
        self.appearance_reason_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.appearance_reason_box.setObjectName("appearance_reason_box")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.gridLayout.addWidget(self.appearance_reason_box, 4, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.case_name_Frame)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 5)
        self.gridLayout_5.addWidget(self.case_name_Frame, 0, 0, 1, 1)
        self.create_entry_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_5.addWidget(self.create_entry_Button, 2, 0, 1, 1)
        self.close_dialog_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(170, 58, 63);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_5.addWidget(self.close_dialog_Button, 3, 0, 1, 1)
        self.gridLayout_5.setRowStretch(0, 2)
        self.gridLayout_5.setRowStretch(1, 2)
        self.gridLayout_5.setRowStretch(2, 1)
        self.gridLayout_5.setRowStretch(3, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout.setStretch(0, 2)

        self.retranslateUi(LeapPleaValidDialog)
        QtCore.QMetaObject.connectSlotsByName(LeapPleaValidDialog)
        LeapPleaValidDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        LeapPleaValidDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        LeapPleaValidDialog.setTabOrder(self.case_number_lineEdit, self.create_entry_Button)
        LeapPleaValidDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, LeapPleaValidDialog):
        _translate = QtCore.QCoreApplication.translate
        LeapPleaValidDialog.setWindowTitle(_translate("LeapPleaValidDialog", "LEAP Plea - Already Valid Case Information"))
        self.add_charge_Button.setText(_translate("LeapPleaValidDialog", "Add Charge"))
        self.label_5.setText(_translate("LeapPleaValidDialog", "Dismissed:"))
        self.label_20.setText(_translate("LeapPleaValidDialog", "Statute:"))
        self.label_21.setText(_translate("LeapPleaValidDialog", "Degree:"))
        self.offense_label_1.setText(_translate("LeapPleaValidDialog", "Offense:"))
        self.plea_label_1.setText(_translate("LeapPleaValidDialog", "Plea:"))
        self.guilty_all_Button.setText(_translate("LeapPleaValidDialog", "Guilty All"))
        self.label_24.setText(_translate("LeapPleaValidDialog", "Def. Counsel:"))
        self.defense_counsel_waived_checkBox.setText(_translate("LeapPleaValidDialog", "Defendant waived right to counsel"))
        self.defense_counsel_type_box.setItemText(0, _translate("LeapPleaValidDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("LeapPleaValidDialog", "Private Counsel"))
        self.label_26.setText(_translate("LeapPleaValidDialog", "Date:"))
        self.cancel_Button.setText(_translate("LeapPleaValidDialog", "Cancel"))
        self.clear_fields_case_Button.setText(_translate("LeapPleaValidDialog", "Clear Fields"))
        self.label_2.setText(_translate("LeapPleaValidDialog", "Def. Last Name:"))
        self.label_3.setText(_translate("LeapPleaValidDialog", "Case Number:"))
        self.label.setText(_translate("LeapPleaValidDialog", "Def. First Name:"))
        self.label_7.setText(_translate("LeapPleaValidDialog", "Appearance Reason:"))
        self.appearance_reason_box.setItemText(0, _translate("LeapPleaValidDialog", "arraignment"))
        self.appearance_reason_box.setItemText(1, _translate("LeapPleaValidDialog", "change of plea"))
        self.appearance_reason_box.setItemText(2, _translate("LeapPleaValidDialog", "trial to court"))
        self.appearance_reason_box.setItemText(3, _translate("LeapPleaValidDialog", "jury trial"))
        self.appearance_reason_box.setItemText(4, _translate("LeapPleaValidDialog", "LEAP sentencing"))
        self.create_entry_Button.setText(_translate("LeapPleaValidDialog", "Open Entry"))
        self.close_dialog_Button.setText(_translate("LeapPleaValidDialog", "Close Dialog"))
from .custom_widgets import DefenseCounselComboBox, NoScrollComboBox, NoScrollDateEdit