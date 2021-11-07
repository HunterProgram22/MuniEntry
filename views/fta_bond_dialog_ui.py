# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/FTABondDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FTABondDialog(object):
    def setupUi(self, FTABondDialog):
        FTABondDialog.setObjectName("FTABondDialog")
        FTABondDialog.setWindowModality(QtCore.Qt.NonModal)
        FTABondDialog.resize(997, 775)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FTABondDialog.sizePolicy().hasHeightForWidth())
        FTABondDialog.setSizePolicy(sizePolicy)
        FTABondDialog.setMinimumSize(QtCore.QSize(0, 0))
        FTABondDialog.setMaximumSize(QtCore.QSize(2500, 3500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        FTABondDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        FTABondDialog.setFont(font)
        FTABondDialog.setToolTip("")
        FTABondDialog.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        FTABondDialog.setSizeGripEnabled(True)
        FTABondDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(FTABondDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(FTABondDialog)
        self.frame.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_26 = QtWidgets.QLabel(self.frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 0, 0, 1, 1)
        self.plea_trial_date = QtWidgets.QDateEdit(self.frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout_2.addWidget(self.plea_trial_date, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.defendant_first_name_lineEdit.setMaximumSize(QtCore.QSize(5000, 16777215))
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout_2.addWidget(self.defendant_first_name_lineEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout_2.addWidget(self.defendant_last_name_lineEdit, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(5000, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout_2.addWidget(self.case_number_lineEdit, 3, 1, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout_2.addWidget(self.clear_fields_case_Button, 3, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 6)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(FTABondDialog)
        self.frame_2.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_6, 4, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_3, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_7, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(FTABondDialog)
        self.frame_4.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setEditable(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_5, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(FTABondDialog)
        self.frame_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 2)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_5.addWidget(self.checkBox_5, 7, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_5.addWidget(self.checkBox_3, 5, 0, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_9, 7, 1, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_8, 5, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_5.addWidget(self.checkBox_6, 4, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_5.addWidget(self.checkBox_2, 3, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_5.addWidget(self.checkBox_4, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(FTABondDialog)
        self.frame_3.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_3)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout.addWidget(self.create_entry_Button, 0, 1, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.frame_3)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout.setStretch(4, 1)

        self.retranslateUi(FTABondDialog)
        QtCore.QMetaObject.connectSlotsByName(FTABondDialog)
        FTABondDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        FTABondDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        FTABondDialog.setTabOrder(self.case_number_lineEdit, self.comboBox)
        FTABondDialog.setTabOrder(self.comboBox, self.comboBox_7)
        FTABondDialog.setTabOrder(self.comboBox_7, self.comboBox_2)
        FTABondDialog.setTabOrder(self.comboBox_2, self.comboBox_3)
        FTABondDialog.setTabOrder(self.comboBox_3, self.comboBox_6)
        FTABondDialog.setTabOrder(self.comboBox_6, self.comboBox_4)
        FTABondDialog.setTabOrder(self.comboBox_4, self.comboBox_5)
        FTABondDialog.setTabOrder(self.comboBox_5, self.checkBox)
        FTABondDialog.setTabOrder(self.checkBox, self.checkBox_4)
        FTABondDialog.setTabOrder(self.checkBox_4, self.checkBox_2)
        FTABondDialog.setTabOrder(self.checkBox_2, self.checkBox_6)
        FTABondDialog.setTabOrder(self.checkBox_6, self.checkBox_3)
        FTABondDialog.setTabOrder(self.checkBox_3, self.comboBox_8)
        FTABondDialog.setTabOrder(self.comboBox_8, self.checkBox_5)
        FTABondDialog.setTabOrder(self.checkBox_5, self.comboBox_9)
        FTABondDialog.setTabOrder(self.comboBox_9, self.create_entry_Button)

    def retranslateUi(self, FTABondDialog):
        _translate = QtCore.QCoreApplication.translate
        FTABondDialog.setWindowTitle(_translate("FTABondDialog", "FTA Bond Case Information"))
        self.label_26.setText(_translate("FTABondDialog", "Date:"))
        self.label.setText(_translate("FTABondDialog", "Def. First Name:"))
        self.label_2.setText(_translate("FTABondDialog", "Def. Last Name:"))
        self.label_3.setText(_translate("FTABondDialog", "Case Number:"))
        self.clear_fields_case_Button.setText(_translate("FTABondDialog", "Clear Fields"))
        self.label_10.setText(_translate("FTABondDialog", "Vehicle Registration Block:"))
        self.comboBox_6.setItemText(0, _translate("FTABondDialog", "No"))
        self.comboBox_6.setItemText(1, _translate("FTABondDialog", "Yes"))
        self.comboBox.setItemText(0, _translate("FTABondDialog", "Arraignment"))
        self.comboBox.setItemText(1, _translate("FTABondDialog", "Motion Hearing"))
        self.comboBox.setItemText(2, _translate("FTABondDialog", "Final Pre-trial"))
        self.comboBox.setItemText(3, _translate("FTABondDialog", "Trial"))
        self.comboBox_3.setItemText(0, _translate("FTABondDialog", "No"))
        self.comboBox_3.setItemText(1, _translate("FTABondDialog", "Yes"))
        self.label_5.setText(_translate("FTABondDialog", "Issue Warrant:"))
        self.comboBox_2.setItemText(0, _translate("FTABondDialog", "No"))
        self.comboBox_2.setItemText(1, _translate("FTABondDialog", "Yes"))
        self.label_4.setText(_translate("FTABondDialog", "Appearance Reason:"))
        self.label_6.setText(_translate("FTABondDialog", "Forfeit OL/CDL/Permit:"))
        self.label_11.setText(_translate("FTABondDialog", "Forfeit Bond:"))
        self.comboBox_7.setItemText(0, _translate("FTABondDialog", "Yes"))
        self.comboBox_7.setItemText(1, _translate("FTABondDialog", "No"))
        self.label_9.setText(_translate("FTABondDialog", "Bond Amount:"))
        self.comboBox_4.setItemText(0, _translate("FTABondDialog", "Recognizance (OR Bond)"))
        self.comboBox_4.setItemText(1, _translate("FTABondDialog", "10% Deposit, Cash or Surety"))
        self.comboBox_4.setItemText(2, _translate("FTABondDialog", "Cash or Surety"))
        self.label_8.setText(_translate("FTABondDialog", "Bond Type:"))
        self.comboBox_5.setItemText(0, _translate("FTABondDialog", "None (OR Bond)"))
        self.comboBox_5.setItemText(1, _translate("FTABondDialog", "$1,500"))
        self.comboBox_5.setItemText(2, _translate("FTABondDialog", "$2,000"))
        self.comboBox_5.setItemText(3, _translate("FTABondDialog", "$2,500"))
        self.comboBox_5.setItemText(4, _translate("FTABondDialog", "$3,000"))
        self.comboBox_5.setItemText(5, _translate("FTABondDialog", "$3,500"))
        self.comboBox_5.setItemText(6, _translate("FTABondDialog", "$5,000"))
        self.comboBox_5.setItemText(7, _translate("FTABondDialog", "$10,000"))
        self.checkBox.setText(_translate("FTABondDialog", "Have no contact with complaining witness(es) / persons as listed."))
        self.label_7.setText(_translate("FTABondDialog", "Bond Conditions"))
        self.checkBox_5.setText(_translate("FTABondDialog", "Report prior to release/forthwith to Office of Community Control for:"))
        self.checkBox_3.setText(_translate("FTABondDialog", "Report to Specialized Docket Coordinator for screening for:"))
        self.comboBox_9.setItemText(0, _translate("FTABondDialog", "GPS Monitoring"))
        self.comboBox_9.setItemText(1, _translate("FTABondDialog", "SCRAM Monitoring"))
        self.comboBox_9.setItemText(2, _translate("FTABondDialog", "Smart Start Monitoring"))
        self.comboBox_8.setItemText(0, _translate("FTABondDialog", "OVI Docket"))
        self.comboBox_8.setItemText(1, _translate("FTABondDialog", "Mission (Veteran\'s) Court"))
        self.comboBox_8.setItemText(2, _translate("FTABondDialog", "Mental Health Docket"))
        self.checkBox_6.setText(_translate("FTABondDialog", "Report to Office of Community Control: Set schedule for AB (Alcohol) Kiosk testing."))
        self.checkBox_2.setText(_translate("FTABondDialog", "Report to Office of Community Control: Obtain alcohol/drug assessment. "))
        self.checkBox_4.setText(_translate("FTABondDialog", "Not consume, possess, or purchase alcohol or drugs of abuse."))
        self.create_entry_Button.setText(_translate("FTABondDialog", "Create Entry"))
        self.cancel_Button.setText(_translate("FTABondDialog", "Cancel"))
