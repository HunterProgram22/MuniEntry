# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package\views\ui\FailureToAppearDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FailureToAppearDialog(object):
    def setupUi(self, FailureToAppearDialog):
        FailureToAppearDialog.setObjectName("FailureToAppearDialog")
        FailureToAppearDialog.setWindowModality(QtCore.Qt.NonModal)
        FailureToAppearDialog.resize(988, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FailureToAppearDialog.sizePolicy().hasHeightForWidth())
        FailureToAppearDialog.setSizePolicy(sizePolicy)
        FailureToAppearDialog.setMinimumSize(QtCore.QSize(0, 0))
        FailureToAppearDialog.setMaximumSize(QtCore.QSize(2500, 3500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        FailureToAppearDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        FailureToAppearDialog.setFont(font)
        FailureToAppearDialog.setToolTip("")
        FailureToAppearDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        FailureToAppearDialog.setSizeGripEnabled(True)
        FailureToAppearDialog.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(FailureToAppearDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_4 = QtWidgets.QFrame(FailureToAppearDialog)
        self.frame_4.setStyleSheet("background-color: rgb(29, 61, 102);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 948, 685))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.case_name_Frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_name_Frame.sizePolicy().hasHeightForWidth())
        self.case_name_Frame.setSizePolicy(sizePolicy)
        self.case_name_Frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.case_name_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_name_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_name_Frame.setObjectName("case_name_Frame")
        self.gridLayout = QtWidgets.QGridLayout(self.case_name_Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.plea_trial_date = QtWidgets.QDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
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
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 3, 0, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 3, 3, 1, 1)
        self.defense_counsel_type_box = QtWidgets.QComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 3, 2, 1, 1)
        self.defense_counsel_name_box = QtWidgets.QComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.appearance_reason_box = QtWidgets.QComboBox(self.case_name_Frame)
        self.appearance_reason_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.appearance_reason_box.setEditable(True)
        self.appearance_reason_box.setObjectName("appearance_reason_box")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.gridLayout.addWidget(self.appearance_reason_box, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)
        self.bond_type_box = QtWidgets.QComboBox(self.frame_5)
        self.bond_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bond_type_box.setObjectName("bond_type_box")
        self.bond_type_box.addItem("")
        self.bond_type_box.addItem("")
        self.bond_type_box.addItem("")
        self.bond_type_box.addItem("")
        self.gridLayout_5.addWidget(self.bond_type_box, 0, 1, 1, 1)
        self.bond_amount_box = QtWidgets.QComboBox(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bond_amount_box.setFont(font)
        self.bond_amount_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bond_amount_box.setEditable(False)
        self.bond_amount_box.setObjectName("bond_amount_box")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.gridLayout_5.addWidget(self.bond_amount_box, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setStyleSheet("\n"
"background-color: rgb(255, 255, 127);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_8)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_10.addWidget(self.create_entry_Button, 0, 0, 1, 1)
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_8)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(170, 58, 63);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_10.addWidget(self.close_dialog_Button, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_8, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(16)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.arrest_warrant_checkBox = QtWidgets.QCheckBox(self.frame)
        self.arrest_warrant_checkBox.setObjectName("arrest_warrant_checkBox")
        self.gridLayout_3.addWidget(self.arrest_warrant_checkBox, 0, 0, 1, 1)
        self.non_resident_license_checkBox = QtWidgets.QCheckBox(self.frame)
        self.non_resident_license_checkBox.setObjectName("non_resident_license_checkBox")
        self.gridLayout_3.addWidget(self.non_resident_license_checkBox, 0, 1, 1, 1)
        self.set_no_trial_checkBox = QtWidgets.QCheckBox(self.frame)
        self.set_no_trial_checkBox.setObjectName("set_no_trial_checkBox")
        self.gridLayout_3.addWidget(self.set_no_trial_checkBox, 1, 0, 1, 1)
        self.proof_of_service_checkBox = QtWidgets.QCheckBox(self.frame)
        self.proof_of_service_checkBox.setObjectName("proof_of_service_checkBox")
        self.gridLayout_3.addWidget(self.proof_of_service_checkBox, 1, 1, 1, 1)
        self.supplemental_summons_checkBox = QtWidgets.QCheckBox(self.frame)
        self.supplemental_summons_checkBox.setObjectName("supplemental_summons_checkBox")
        self.gridLayout_3.addWidget(self.supplemental_summons_checkBox, 2, 1, 1, 1)
        self.operator_license_checkBox = QtWidgets.QCheckBox(self.frame)
        self.operator_license_checkBox.setObjectName("operator_license_checkBox")
        self.gridLayout_3.addWidget(self.operator_license_checkBox, 3, 0, 1, 1)
        self.registration_block_checkBox = QtWidgets.QCheckBox(self.frame)
        self.registration_block_checkBox.setObjectName("registration_block_checkBox")
        self.gridLayout_3.addWidget(self.registration_block_checkBox, 3, 1, 1, 1)
        self.bond_forfeited_checkBox = QtWidgets.QCheckBox(self.frame)
        self.bond_forfeited_checkBox.setObjectName("bond_forfeited_checkBox")
        self.gridLayout_3.addWidget(self.bond_forfeited_checkBox, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(FailureToAppearDialog)
        QtCore.QMetaObject.connectSlotsByName(FailureToAppearDialog)
        FailureToAppearDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        FailureToAppearDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        FailureToAppearDialog.setTabOrder(self.case_number_lineEdit, self.defense_counsel_name_box)
        FailureToAppearDialog.setTabOrder(self.defense_counsel_name_box, self.defense_counsel_type_box)
        FailureToAppearDialog.setTabOrder(self.defense_counsel_type_box, self.defense_counsel_waived_checkBox)
        FailureToAppearDialog.setTabOrder(self.defense_counsel_waived_checkBox, self.bond_type_box)
        FailureToAppearDialog.setTabOrder(self.bond_type_box, self.bond_amount_box)
        FailureToAppearDialog.setTabOrder(self.bond_amount_box, self.create_entry_Button)
        FailureToAppearDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, FailureToAppearDialog):
        _translate = QtCore.QCoreApplication.translate
        FailureToAppearDialog.setWindowTitle(_translate("FailureToAppearDialog", "Failure To Appear Case Information"))
        self.label.setText(_translate("FailureToAppearDialog", "Def. First Name:"))
        self.label_26.setText(_translate("FailureToAppearDialog", "Date:"))
        self.cancel_Button.setText(_translate("FailureToAppearDialog", "Cancel"))
        self.label_2.setText(_translate("FailureToAppearDialog", "Def. Last Name:"))
        self.clear_fields_case_Button.setText(_translate("FailureToAppearDialog", "Clear Fields"))
        self.label_3.setText(_translate("FailureToAppearDialog", "Case Number:"))
        self.label_24.setText(_translate("FailureToAppearDialog", "Def. Counsel:"))
        self.defense_counsel_waived_checkBox.setText(_translate("FailureToAppearDialog", "Defendant appeared without counsel"))
        self.defense_counsel_type_box.setItemText(0, _translate("FailureToAppearDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("FailureToAppearDialog", "Private Counsel"))
        self.label_11.setText(_translate("FailureToAppearDialog", "Appearance Reason:"))
        self.appearance_reason_box.setItemText(0, _translate("FailureToAppearDialog", "arraignment"))
        self.appearance_reason_box.setItemText(1, _translate("FailureToAppearDialog", "motion hearing"))
        self.appearance_reason_box.setItemText(2, _translate("FailureToAppearDialog", "warrant for failure to appear"))
        self.label_8.setText(_translate("FailureToAppearDialog", "Bond Type:"))
        self.label_9.setText(_translate("FailureToAppearDialog", "Bond Amount:"))
        self.bond_type_box.setItemText(0, _translate("FailureToAppearDialog", "Recognizance (OR) Bond"))
        self.bond_type_box.setItemText(1, _translate("FailureToAppearDialog", "No Bond"))
        self.bond_type_box.setItemText(2, _translate("FailureToAppearDialog", "10% Deposit, Cash or Surety Bond"))
        self.bond_type_box.setItemText(3, _translate("FailureToAppearDialog", "Cash or Surety Bond"))
        self.bond_amount_box.setItemText(0, _translate("FailureToAppearDialog", "None (OR Bond)"))
        self.bond_amount_box.setItemText(1, _translate("FailureToAppearDialog", "None (No Bond)"))
        self.bond_amount_box.setItemText(2, _translate("FailureToAppearDialog", "$1,000"))
        self.bond_amount_box.setItemText(3, _translate("FailureToAppearDialog", "$1,500"))
        self.bond_amount_box.setItemText(4, _translate("FailureToAppearDialog", "$2,000"))
        self.bond_amount_box.setItemText(5, _translate("FailureToAppearDialog", "$2,500"))
        self.bond_amount_box.setItemText(6, _translate("FailureToAppearDialog", "$3,000"))
        self.bond_amount_box.setItemText(7, _translate("FailureToAppearDialog", "$3,500"))
        self.bond_amount_box.setItemText(8, _translate("FailureToAppearDialog", "$5,000"))
        self.bond_amount_box.setItemText(9, _translate("FailureToAppearDialog", "$10,000"))
        self.create_entry_Button.setText(_translate("FailureToAppearDialog", "Open Entry"))
        self.close_dialog_Button.setText(_translate("FailureToAppearDialog", "Close Dialog"))
        self.arrest_warrant_checkBox.setText(_translate("FailureToAppearDialog", "Issue Warrant for Arrest forthwith"))
        self.non_resident_license_checkBox.setText(_translate("FailureToAppearDialog", "Defendant has Non-Resident Violator compact state OL"))
        self.set_no_trial_checkBox.setText(_translate("FailureToAppearDialog", "Set no trial until Defendant appears"))
        self.proof_of_service_checkBox.setText(_translate("FailureToAppearDialog", "Absent proof of service of warrant/summons in 28 days case closed subject to reopen"))
        self.supplemental_summons_checkBox.setText(_translate("FailureToAppearDialog", "Clerk issue supplemental summons by regular mail"))
        self.operator_license_checkBox.setText(_translate("FailureToAppearDialog", "Forfeit Defendant OL/CDL/permit"))
        self.registration_block_checkBox.setText(_translate("FailureToAppearDialog", "Defendant Vehicle Registration is blocked absent compliance in 30 days"))
        self.bond_forfeited_checkBox.setText(_translate("FailureToAppearDialog", "Bond forfeited, hearing date vacated"))
        self.label_4.setText(_translate("FailureToAppearDialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Failure To Appear Actions</span></p></body></html>"))
