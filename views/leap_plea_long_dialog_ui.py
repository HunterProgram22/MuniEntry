# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/LeapPleaLongDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LeapPleaLongDialog(object):
    def setupUi(self, LeapPleaLongDialog):
        LeapPleaLongDialog.setObjectName("LeapPleaLongDialog")
        LeapPleaLongDialog.setWindowModality(QtCore.Qt.NonModal)
        LeapPleaLongDialog.resize(923, 762)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LeapPleaLongDialog.sizePolicy().hasHeightForWidth())
        LeapPleaLongDialog.setSizePolicy(sizePolicy)
        LeapPleaLongDialog.setMinimumSize(QtCore.QSize(0, 0))
        LeapPleaLongDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        LeapPleaLongDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        LeapPleaLongDialog.setFont(font)
        LeapPleaLongDialog.setToolTip("")
        LeapPleaLongDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        LeapPleaLongDialog.setSizeGripEnabled(True)
        LeapPleaLongDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(LeapPleaLongDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(LeapPleaLongDialog)
        self.frame_4.setStyleSheet("background-color: rgb(25, 49, 91);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 883, 722))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMinimumSize(QtCore.QSize(141, 0))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.defendant_first_name_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame_3)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.plea_trial_date = QtWidgets.QDateEdit(self.frame_3)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.frame_3)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMinimumSize(QtCore.QSize(141, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMinimumSize(QtCore.QSize(131, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.frame_3)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.gridLayout_5.addWidget(self.frame_3, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.statute_choice_box = QtWidgets.QComboBox(self.frame)
        self.statute_choice_box.setEnabled(True)
        self.statute_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.statute_choice_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.statute_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.statute_choice_box.setEditable(True)
        self.statute_choice_box.setObjectName("statute_choice_box")
        self.gridLayout_2.addWidget(self.statute_choice_box, 0, 1, 1, 1)
        self.freeform_entry_checkBox = QtWidgets.QCheckBox(self.frame)
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
        self.clear_fields_charge_Button = QtWidgets.QPushButton(self.frame)
        self.clear_fields_charge_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_charge_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_charge_Button.setObjectName("clear_fields_charge_Button")
        self.gridLayout_2.addWidget(self.clear_fields_charge_Button, 0, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.offense_choice_box = QtWidgets.QComboBox(self.frame)
        self.offense_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.offense_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.offense_choice_box.setEditable(True)
        self.offense_choice_box.setObjectName("offense_choice_box")
        self.gridLayout_2.addWidget(self.offense_choice_box, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 1, 2, 1, 1)
        self.degree_choice_box = QtWidgets.QComboBox(self.frame)
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
        self.add_charge_Button = QtWidgets.QPushButton(self.frame)
        self.add_charge_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.add_charge_Button.setObjectName("add_charge_Button")
        self.gridLayout_2.addWidget(self.add_charge_Button, 1, 4, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 2, 0, 1, 2)
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
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
        self.plea_label_1 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plea_label_1.setFont(font)
        self.plea_label_1.setObjectName("plea_label_1")
        self.charges_gridLayout.addWidget(self.plea_label_1, 3, 0, 1, 1)
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
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.charges_gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.gridLayout_3.addLayout(self.charges_gridLayout, 0, 0, 1, 1)
        self.guilty_all_Button = QtWidgets.QPushButton(self.frame_6)
        self.guilty_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.guilty_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.guilty_all_Button.setObjectName("guilty_all_Button")
        self.gridLayout_3.addWidget(self.guilty_all_Button, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_6, 3, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.formLayout = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.time_to_complete_box = QtWidgets.QComboBox(self.frame_5)
        self.time_to_complete_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.time_to_complete_box.setObjectName("time_to_complete_box")
        self.time_to_complete_box.addItem("")
        self.time_to_complete_box.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.time_to_complete_box)
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.sentencing_date = QtWidgets.QDateEdit(self.frame_5)
        self.sentencing_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sentencing_date.setObjectName("sentencing_date")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sentencing_date)
        self.gridLayout_5.addWidget(self.frame_5, 4, 0, 1, 1)
        self.create_entry_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_5.addWidget(self.create_entry_Button, 4, 1, 1, 1)
        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 2)
        self.gridLayout_5.setRowStretch(2, 2)
        self.gridLayout_5.setRowStretch(3, 4)
        self.gridLayout_5.setRowStretch(4, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout.setStretch(0, 2)

        self.retranslateUi(LeapPleaLongDialog)
        QtCore.QMetaObject.connectSlotsByName(LeapPleaLongDialog)
        LeapPleaLongDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        LeapPleaLongDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        LeapPleaLongDialog.setTabOrder(self.case_number_lineEdit, self.statute_choice_box)
        LeapPleaLongDialog.setTabOrder(self.statute_choice_box, self.offense_choice_box)
        LeapPleaLongDialog.setTabOrder(self.offense_choice_box, self.add_charge_Button)
        LeapPleaLongDialog.setTabOrder(self.add_charge_Button, self.time_to_complete_box)
        LeapPleaLongDialog.setTabOrder(self.time_to_complete_box, self.sentencing_date)
        LeapPleaLongDialog.setTabOrder(self.sentencing_date, self.create_entry_Button)
        LeapPleaLongDialog.setTabOrder(self.create_entry_Button, self.textBrowser)
        LeapPleaLongDialog.setTabOrder(self.textBrowser, self.scrollArea)

    def retranslateUi(self, LeapPleaLongDialog):
        _translate = QtCore.QCoreApplication.translate
        LeapPleaLongDialog.setWindowTitle(_translate("LeapPleaLongDialog", "Leap Plea Case Information"))
        self.textBrowser.setHtml(_translate("LeapPleaLongDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Palatino Linotype\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">INSTRUCTIONS: </span><span style=\" font-size:11pt; font-weight:400;\">Must have completed LEAP eligibility checklist and LEAP Participation agreement that is signed by Defendant, LEAP Coordinator and Prosecutor. Defendant must plead guilty to all charges. May enter program even if Prosecutor doesn\'t agree to dismiss companion charges, but Defendant must understand and be made aware that companion charges will not be dismissed and that he will be sentenced separately on companion charge(s) at completion of LEAP Program.</span></p></body></html>"))
        self.label.setText(_translate("LeapPleaLongDialog", "Def. First Name:"))
        self.label_26.setText(_translate("LeapPleaLongDialog", "Date:"))
        self.cancel_Button.setText(_translate("LeapPleaLongDialog", "Cancel"))
        self.label_2.setText(_translate("LeapPleaLongDialog", "Def. Last Name:"))
        self.label_3.setText(_translate("LeapPleaLongDialog", "Case Number:"))
        self.clear_fields_case_Button.setText(_translate("LeapPleaLongDialog", "Clear Fields"))
        self.label_6.setText(_translate("LeapPleaLongDialog", "Statute:"))
        self.freeform_entry_checkBox.setText(_translate("LeapPleaLongDialog", "Enable freeform entry for offense/statute"))
        self.clear_fields_charge_Button.setText(_translate("LeapPleaLongDialog", "Clear Fields"))
        self.label_15.setText(_translate("LeapPleaLongDialog", "Offense:"))
        self.label_23.setText(_translate("LeapPleaLongDialog", "Degree:"))
        self.degree_choice_box.setItemText(0, _translate("LeapPleaLongDialog", "Minor Misdemeanor"))
        self.degree_choice_box.setItemText(1, _translate("LeapPleaLongDialog", "M1"))
        self.degree_choice_box.setItemText(2, _translate("LeapPleaLongDialog", "M2"))
        self.degree_choice_box.setItemText(3, _translate("LeapPleaLongDialog", "M3"))
        self.degree_choice_box.setItemText(4, _translate("LeapPleaLongDialog", "M4"))
        self.degree_choice_box.setItemText(5, _translate("LeapPleaLongDialog", "Unclassified Misdemeanor"))
        self.add_charge_Button.setText(_translate("LeapPleaLongDialog", "Add Charge"))
        self.label_20.setText(_translate("LeapPleaLongDialog", "Statute:"))
        self.label_21.setText(_translate("LeapPleaLongDialog", "Degree:"))
        self.plea_label_1.setText(_translate("LeapPleaLongDialog", "Plea:"))
        self.offense_label_1.setText(_translate("LeapPleaLongDialog", "Offense:"))
        self.guilty_all_Button.setText(_translate("LeapPleaLongDialog", "Guilty All"))
        self.label_10.setText(_translate("LeapPleaLongDialog", "Time to Complete LEAP:"))
        self.time_to_complete_box.setItemText(0, _translate("LeapPleaLongDialog", "120 days"))
        self.time_to_complete_box.setItemText(1, _translate("LeapPleaLongDialog", "forthwith"))
        self.label_19.setText(_translate("LeapPleaLongDialog", "Sentencing Date:"))
        self.create_entry_Button.setText(_translate("LeapPleaLongDialog", "Create Entry"))
