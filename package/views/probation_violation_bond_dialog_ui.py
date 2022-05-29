# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package\views\ui\ProbationViolationBondDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProbationViolationBondDialog(object):
    def setupUi(self, ProbationViolationBondDialog):
        ProbationViolationBondDialog.setObjectName("ProbationViolationBondDialog")
        ProbationViolationBondDialog.setWindowModality(QtCore.Qt.NonModal)
        ProbationViolationBondDialog.resize(988, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProbationViolationBondDialog.sizePolicy().hasHeightForWidth())
        ProbationViolationBondDialog.setSizePolicy(sizePolicy)
        ProbationViolationBondDialog.setMinimumSize(QtCore.QSize(0, 0))
        ProbationViolationBondDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        ProbationViolationBondDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        ProbationViolationBondDialog.setFont(font)
        ProbationViolationBondDialog.setToolTip("")
        ProbationViolationBondDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        ProbationViolationBondDialog.setSizeGripEnabled(True)
        ProbationViolationBondDialog.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(ProbationViolationBondDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_4 = QtWidgets.QFrame(ProbationViolationBondDialog)
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
        self.bond_conditions_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.bond_conditions_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.bond_conditions_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.bond_conditions_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bond_conditions_frame.setLineWidth(2)
        self.bond_conditions_frame.setObjectName("bond_conditions_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.bond_conditions_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.no_alcohol_drugs_checkBox = QtWidgets.QCheckBox(self.bond_conditions_frame)
        self.no_alcohol_drugs_checkBox.setObjectName("no_alcohol_drugs_checkBox")
        self.gridLayout_6.addWidget(self.no_alcohol_drugs_checkBox, 1, 0, 1, 1)
        self.monitoring_checkBox = QtWidgets.QCheckBox(self.bond_conditions_frame)
        self.monitoring_checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.monitoring_checkBox.setObjectName("monitoring_checkBox")
        self.gridLayout_6.addWidget(self.monitoring_checkBox, 1, 1, 1, 1)
        self.comply_protection_order_checkBox = QtWidgets.QCheckBox(self.bond_conditions_frame)
        self.comply_protection_order_checkBox.setObjectName("comply_protection_order_checkBox")
        self.gridLayout_6.addWidget(self.comply_protection_order_checkBox, 2, 0, 1, 1)
        self.monitoring_type_box = NoScrollComboBox(self.bond_conditions_frame)
        self.monitoring_type_box.setEnabled(True)
        self.monitoring_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.monitoring_type_box.setObjectName("monitoring_type_box")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.gridLayout_6.addWidget(self.monitoring_type_box, 2, 1, 1, 1)
        self.cc_violation_other_conditions_checkBox = QtWidgets.QCheckBox(self.bond_conditions_frame)
        self.cc_violation_other_conditions_checkBox.setObjectName("cc_violation_other_conditions_checkBox")
        self.gridLayout_6.addWidget(self.cc_violation_other_conditions_checkBox, 3, 0, 1, 1)
        self.alcohol_test_kiosk_checkBox = QtWidgets.QCheckBox(self.bond_conditions_frame)
        self.alcohol_test_kiosk_checkBox.setObjectName("alcohol_test_kiosk_checkBox")
        self.gridLayout_6.addWidget(self.alcohol_test_kiosk_checkBox, 3, 1, 1, 1)
        self.cc_violation_other_conditions_terms_box = QtWidgets.QLineEdit(self.bond_conditions_frame)
        self.cc_violation_other_conditions_terms_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cc_violation_other_conditions_terms_box.setObjectName("cc_violation_other_conditions_terms_box")
        self.gridLayout_6.addWidget(self.cc_violation_other_conditions_terms_box, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.bond_conditions_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 2)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_2.addWidget(self.bond_conditions_frame, 3, 0, 1, 1)
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
        self.defense_counsel_type_box = NoScrollComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 2, 2, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 2, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.defense_counsel_name_box = DefenseCounselComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.appearance_reason_box = NoScrollComboBox(self.case_name_Frame)
        self.appearance_reason_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.appearance_reason_box.setEditable(True)
        self.appearance_reason_box.setObjectName("appearance_reason_box")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.gridLayout.addWidget(self.appearance_reason_box, 4, 1, 1, 2)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
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
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.case_name_Frame)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)
        self.bond_type_box = NoScrollComboBox(self.frame_5)
        self.bond_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bond_type_box.setObjectName("bond_type_box")
        self.bond_type_box.addItem("")
        self.bond_type_box.addItem("")
        self.bond_type_box.addItem("")
        self.bond_type_box.addItem("")
        self.gridLayout_5.addWidget(self.bond_type_box, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 1)
        self.bond_amount_box = NoScrollComboBox(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bond_amount_box.setFont(font)
        self.bond_amount_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bond_amount_box.setEditable(True)
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
        self.gridLayout_5.addWidget(self.bond_amount_box, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setVerticalSpacing(16)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 2)
        self.probable_cause_finding_box = NoScrollComboBox(self.frame)
        self.probable_cause_finding_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.probable_cause_finding_box.setObjectName("probable_cause_finding_box")
        self.probable_cause_finding_box.addItem("")
        self.probable_cause_finding_box.addItem("")
        self.probable_cause_finding_box.addItem("")
        self.gridLayout_3.addWidget(self.probable_cause_finding_box, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setStyleSheet("\n"
"background-color: rgb(255, 255, 127);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_8)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(255, 96, 82);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_10.addWidget(self.close_dialog_Button, 2, 1, 1, 1)
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_8)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_10.addWidget(self.create_entry_Button, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_8)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_10.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout_10.setColumnStretch(0, 2)
        self.gridLayout_10.setColumnStretch(1, 1)
        self.gridLayout_2.addWidget(self.frame_8, 4, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(ProbationViolationBondDialog)
        QtCore.QMetaObject.connectSlotsByName(ProbationViolationBondDialog)
        ProbationViolationBondDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        ProbationViolationBondDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        ProbationViolationBondDialog.setTabOrder(self.case_number_lineEdit, self.bond_type_box)
        ProbationViolationBondDialog.setTabOrder(self.bond_type_box, self.bond_amount_box)
        ProbationViolationBondDialog.setTabOrder(self.bond_amount_box, self.monitoring_checkBox)
        ProbationViolationBondDialog.setTabOrder(self.monitoring_checkBox, self.create_entry_Button)
        ProbationViolationBondDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, ProbationViolationBondDialog):
        _translate = QtCore.QCoreApplication.translate
        ProbationViolationBondDialog.setWindowTitle(_translate("ProbationViolationBondDialog", "Community Control Violation Bond Case Information"))
        self.no_alcohol_drugs_checkBox.setText(_translate("ProbationViolationBondDialog", " No alcohol/drugs of abuse."))
        self.monitoring_checkBox.setText(_translate("ProbationViolationBondDialog", "Monitoring (GPS/Scram/Smart Start):"))
        self.comply_protection_order_checkBox.setText(_translate("ProbationViolationBondDialog", " Comply with Terms of Protection Order"))
        self.monitoring_type_box.setItemText(0, _translate("ProbationViolationBondDialog", "SCRAM Only"))
        self.monitoring_type_box.setItemText(1, _translate("ProbationViolationBondDialog", "GPS Only"))
        self.monitoring_type_box.setItemText(2, _translate("ProbationViolationBondDialog", "Smart Start Only"))
        self.monitoring_type_box.setItemText(3, _translate("ProbationViolationBondDialog", "GPS and SCRAM"))
        self.monitoring_type_box.setItemText(4, _translate("ProbationViolationBondDialog", "GPS and Smart Start"))
        self.monitoring_type_box.setItemText(5, _translate("ProbationViolationBondDialog", "SCRAM and Smart Start"))
        self.monitoring_type_box.setItemText(6, _translate("ProbationViolationBondDialog", "GPS, SCRAM and Smart Start"))
        self.cc_violation_other_conditions_checkBox.setText(_translate("ProbationViolationBondDialog", "Other Conditions"))
        self.alcohol_test_kiosk_checkBox.setText(_translate("ProbationViolationBondDialog", " Alcohol Kiosk testing."))
        self.cc_violation_other_conditions_terms_box.setPlaceholderText(_translate("ProbationViolationBondDialog", "Other Conditions"))
        self.label_7.setText(_translate("ProbationViolationBondDialog", "BOND CONDITIONS"))
        self.defense_counsel_type_box.setItemText(0, _translate("ProbationViolationBondDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("ProbationViolationBondDialog", "Private Counsel"))
        self.defense_counsel_waived_checkBox.setText(_translate("ProbationViolationBondDialog", "Defendant appeared without counsel"))
        self.label_26.setText(_translate("ProbationViolationBondDialog", "Date:"))
        self.label_24.setText(_translate("ProbationViolationBondDialog", "Def. Counsel:"))
        self.label_11.setText(_translate("ProbationViolationBondDialog", "Appearance Reason:"))
        self.label_2.setText(_translate("ProbationViolationBondDialog", "Def. Last Name:"))
        self.appearance_reason_box.setItemText(0, _translate("ProbationViolationBondDialog", "Preliminary Community Control Violation Hearing"))
        self.appearance_reason_box.setItemText(1, _translate("ProbationViolationBondDialog", "warrant for failure to appear"))
        self.cancel_Button.setText(_translate("ProbationViolationBondDialog", "Cancel"))
        self.clear_fields_case_Button.setText(_translate("ProbationViolationBondDialog", "Clear Fields"))
        self.label_3.setText(_translate("ProbationViolationBondDialog", "Case Number:"))
        self.label.setText(_translate("ProbationViolationBondDialog", "Def. First Name:"))
        self.label_8.setText(_translate("ProbationViolationBondDialog", "Bond Type:"))
        self.bond_type_box.setItemText(0, _translate("ProbationViolationBondDialog", "No Bond"))
        self.bond_type_box.setItemText(1, _translate("ProbationViolationBondDialog", "Recognizance (OR) Bond"))
        self.bond_type_box.setItemText(2, _translate("ProbationViolationBondDialog", "10% Deposit, Cash or Surety Bond"))
        self.bond_type_box.setItemText(3, _translate("ProbationViolationBondDialog", "Cash or Surety Bond"))
        self.label_9.setText(_translate("ProbationViolationBondDialog", "Bond Amount:"))
        self.bond_amount_box.setItemText(0, _translate("ProbationViolationBondDialog", "None"))
        self.bond_amount_box.setItemText(1, _translate("ProbationViolationBondDialog", "$1,000"))
        self.bond_amount_box.setItemText(2, _translate("ProbationViolationBondDialog", "$1,500"))
        self.bond_amount_box.setItemText(3, _translate("ProbationViolationBondDialog", "$2,000"))
        self.bond_amount_box.setItemText(4, _translate("ProbationViolationBondDialog", "$2,500"))
        self.bond_amount_box.setItemText(5, _translate("ProbationViolationBondDialog", "$3,000"))
        self.bond_amount_box.setItemText(6, _translate("ProbationViolationBondDialog", "$3,500"))
        self.bond_amount_box.setItemText(7, _translate("ProbationViolationBondDialog", "$5,000"))
        self.bond_amount_box.setItemText(8, _translate("ProbationViolationBondDialog", "$10,000"))
        self.label_12.setText(_translate("ProbationViolationBondDialog", "BOND"))
        self.label_4.setText(_translate("ProbationViolationBondDialog", "Probable Cause for Community Control Violation:"))
        self.label_10.setText(_translate("ProbationViolationBondDialog", "PROBABLE CAUSE FINDING"))
        self.probable_cause_finding_box.setItemText(0, _translate("ProbationViolationBondDialog", "Defendant stipulates probable cause exists"))
        self.probable_cause_finding_box.setItemText(1, _translate("ProbationViolationBondDialog", "Court finds probable cause"))
        self.probable_cause_finding_box.setItemText(2, _translate("ProbationViolationBondDialog", "No probable cause"))
        self.close_dialog_Button.setText(_translate("ProbationViolationBondDialog", "Close Dialog"))
        self.create_entry_Button.setText(_translate("ProbationViolationBondDialog", "Open Entry"))
from .custom_widgets import DefenseCounselComboBox, NoScrollComboBox, NoScrollDateEdit
