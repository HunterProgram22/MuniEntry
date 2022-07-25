# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'munientry/views/ui/LeapAdmissionPleaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LeapAdmissionPleaDialog(object):
    def setupUi(self, LeapAdmissionPleaDialog):
        LeapAdmissionPleaDialog.setObjectName("LeapAdmissionPleaDialog")
        LeapAdmissionPleaDialog.setWindowModality(QtCore.Qt.NonModal)
        LeapAdmissionPleaDialog.resize(985, 823)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LeapAdmissionPleaDialog.sizePolicy().hasHeightForWidth())
        LeapAdmissionPleaDialog.setSizePolicy(sizePolicy)
        LeapAdmissionPleaDialog.setMinimumSize(QtCore.QSize(0, 0))
        LeapAdmissionPleaDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        LeapAdmissionPleaDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        LeapAdmissionPleaDialog.setFont(font)
        LeapAdmissionPleaDialog.setToolTip("")
        LeapAdmissionPleaDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        LeapAdmissionPleaDialog.setSizeGripEnabled(True)
        LeapAdmissionPleaDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(LeapAdmissionPleaDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(LeapAdmissionPleaDialog)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 945, 783))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.time_to_complete_box = NoScrollComboBox(self.frame_5)
        self.time_to_complete_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.time_to_complete_box.setObjectName("time_to_complete_box")
        self.time_to_complete_box.addItem("")
        self.time_to_complete_box.addItem("")
        self.time_to_complete_box.addItem("")
        self.gridLayout_3.addWidget(self.time_to_complete_box, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)
        self.sentencing_date = NoScrollDateEdit(self.frame_5)
        self.sentencing_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sentencing_date.setCalendarPopup(True)
        self.sentencing_date.setObjectName("sentencing_date")
        self.gridLayout_3.addWidget(self.sentencing_date, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_5, 2, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line = QtWidgets.QFrame(self.frame_6)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 3)
        self.add_charge_Button = QtWidgets.QPushButton(self.frame_6)
        self.add_charge_Button.setStyleSheet("background-color: rgb(62, 146, 255);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.add_charge_Button.setObjectName("add_charge_Button")
        self.gridLayout_2.addWidget(self.add_charge_Button, 2, 0, 1, 1)
        self.no_contest_all_Button = QtWidgets.QPushButton(self.frame_6)
        self.no_contest_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.no_contest_all_Button.setObjectName("no_contest_all_Button")
        self.gridLayout_2.addWidget(self.no_contest_all_Button, 2, 1, 1, 1)
        self.guilty_all_Button = QtWidgets.QPushButton(self.frame_6)
        self.guilty_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.guilty_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.guilty_all_Button.setObjectName("guilty_all_Button")
        self.gridLayout_2.addWidget(self.guilty_all_Button, 2, 2, 1, 1)
        self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.charges_gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
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
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setObjectName("label_5")
        self.charges_gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
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
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.charges_gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.gridLayout_2.addLayout(self.charges_gridLayout, 0, 0, 1, 3)
        self.gridLayout_6.addWidget(self.frame_6, 1, 0, 1, 2)
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_7)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_5.addWidget(self.create_entry_Button, 0, 0, 1, 2)
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_7)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(170, 58, 63);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_5.addWidget(self.close_dialog_Button, 1, 0, 1, 2)
        self.gridLayout_6.addWidget(self.frame_7, 2, 1, 1, 1)
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
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.appearance_reason_box = NoScrollComboBox(self.case_name_Frame)
        self.appearance_reason_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.appearance_reason_box.setObjectName("appearance_reason_box")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.gridLayout.addWidget(self.appearance_reason_box, 4, 1, 1, 1)
        self.defense_counsel_type_box = NoScrollComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.defense_counsel_name_box = DefenseCounselComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 2, 1, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 2, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.case_name_Frame)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 5)
        self.gridLayout_6.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 2)
        self.gridLayout_6.setRowStretch(2, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout.setStretch(0, 2)

        self.retranslateUi(LeapAdmissionPleaDialog)
        QtCore.QMetaObject.connectSlotsByName(LeapAdmissionPleaDialog)
        LeapAdmissionPleaDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        LeapAdmissionPleaDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        LeapAdmissionPleaDialog.setTabOrder(self.case_number_lineEdit, self.time_to_complete_box)
        LeapAdmissionPleaDialog.setTabOrder(self.time_to_complete_box, self.sentencing_date)
        LeapAdmissionPleaDialog.setTabOrder(self.sentencing_date, self.create_entry_Button)
        LeapAdmissionPleaDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, LeapAdmissionPleaDialog):
        _translate = QtCore.QCoreApplication.translate
        LeapAdmissionPleaDialog.setWindowTitle(_translate("LeapAdmissionPleaDialog", "LEAP Admission Plea Case Information"))
        self.label_10.setText(_translate("LeapAdmissionPleaDialog", "Time to Complete LEAP:"))
        self.time_to_complete_box.setItemText(0, _translate("LeapAdmissionPleaDialog", "120 days"))
        self.time_to_complete_box.setItemText(1, _translate("LeapAdmissionPleaDialog", "30 days"))
        self.time_to_complete_box.setItemText(2, _translate("LeapAdmissionPleaDialog", "forthwith"))
        self.label_19.setText(_translate("LeapAdmissionPleaDialog", "Sentencing Date:"))
        self.add_charge_Button.setText(_translate("LeapAdmissionPleaDialog", "Add Charge"))
        self.no_contest_all_Button.setText(_translate("LeapAdmissionPleaDialog", "No Contest All"))
        self.guilty_all_Button.setText(_translate("LeapAdmissionPleaDialog", "Guilty All"))
        self.offense_label_1.setText(_translate("LeapAdmissionPleaDialog", "Offense:"))
        self.label_5.setText(_translate("LeapAdmissionPleaDialog", "Dismissed:"))
        self.plea_label_1.setText(_translate("LeapAdmissionPleaDialog", "Plea:"))
        self.label_20.setText(_translate("LeapAdmissionPleaDialog", "Statute:"))
        self.label_21.setText(_translate("LeapAdmissionPleaDialog", "Degree:"))
        self.create_entry_Button.setText(_translate("LeapAdmissionPleaDialog", "Open Entry"))
        self.close_dialog_Button.setText(_translate("LeapAdmissionPleaDialog", "Close Dialog"))
        self.label_3.setText(_translate("LeapAdmissionPleaDialog", "Case Number:"))
        self.label_26.setText(_translate("LeapAdmissionPleaDialog", "Date:"))
        self.label_2.setText(_translate("LeapAdmissionPleaDialog", "Def. Last Name:"))
        self.clear_fields_case_Button.setText(_translate("LeapAdmissionPleaDialog", "Clear Fields"))
        self.cancel_Button.setText(_translate("LeapAdmissionPleaDialog", "Cancel"))
        self.label.setText(_translate("LeapAdmissionPleaDialog", "Def. First Name:"))
        self.appearance_reason_box.setItemText(0, _translate("LeapAdmissionPleaDialog", "arraignment"))
        self.appearance_reason_box.setItemText(1, _translate("LeapAdmissionPleaDialog", "change of plea"))
        self.defense_counsel_type_box.setItemText(0, _translate("LeapAdmissionPleaDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("LeapAdmissionPleaDialog", "Private Counsel"))
        self.label_7.setText(_translate("LeapAdmissionPleaDialog", "Appearance Reason:"))
        self.label_24.setText(_translate("LeapAdmissionPleaDialog", "Def. Counsel:"))
        self.defense_counsel_waived_checkBox.setText(_translate("LeapAdmissionPleaDialog", "Defendant waived right to counsel"))
from munientry.widgets.custom_widgets import DefenseCounselComboBox, NoScrollComboBox, NoScrollDateEdit
