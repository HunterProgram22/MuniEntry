# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/CaseInformationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CaseInformationDialog(object):
    def setupUi(self, CaseInformationDialog):
        CaseInformationDialog.setObjectName("CaseInformationDialog")
        CaseInformationDialog.setWindowModality(QtCore.Qt.NonModal)
        CaseInformationDialog.resize(1000, 800)
        CaseInformationDialog.setMinimumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        CaseInformationDialog.setFont(font)
        CaseInformationDialog.setToolTip("")
        self.continueButton = QtWidgets.QPushButton(CaseInformationDialog)
        self.continueButton.setGeometry(QtCore.QRect(820, 739, 158, 41))
        self.continueButton.setObjectName("continueButton")
        self.layoutWidget = QtWidgets.QWidget(CaseInformationDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(847, 10, 141, 80))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(CaseInformationDialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 471, 931, 103))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.offense_of_violence_gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.offense_of_violence_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.offense_of_violence_gridLayout.setObjectName("offense_of_violence_gridLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setToolTip("")
        self.label_7.setToolTipDuration(-2)
        self.label_7.setObjectName("label_7")
        self.offense_of_violence_gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.violence_no_firearm_checkbox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.violence_no_firearm_checkbox.setToolTipDuration(-1)
        self.violence_no_firearm_checkbox.setObjectName("violence_no_firearm_checkbox")
        self.offense_of_violence_gridLayout.addWidget(self.violence_no_firearm_checkbox, 1, 0, 1, 1)
        self.citizen_deportation_checkbox_2 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.citizen_deportation_checkbox_2.setObjectName("citizen_deportation_checkbox_2")
        self.offense_of_violence_gridLayout.addWidget(self.citizen_deportation_checkbox_2, 2, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(CaseInformationDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 337, 931, 103))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.citizenship_gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.citizenship_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.citizenship_gridLayout.setObjectName("citizenship_gridLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.citizenship_gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.is_citizen_checkbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.is_citizen_checkbox.setObjectName("is_citizen_checkbox")
        self.citizenship_gridLayout.addWidget(self.is_citizen_checkbox, 1, 0, 1, 1)
        self.citizen_deportation_checkbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.citizen_deportation_checkbox.setObjectName("citizen_deportation_checkbox")
        self.citizenship_gridLayout.addWidget(self.citizen_deportation_checkbox, 2, 0, 1, 1)
        self.continueButton_2 = QtWidgets.QPushButton(CaseInformationDialog)
        self.continueButton_2.setGeometry(QtCore.QRect(620, 740, 158, 41))
        self.continueButton_2.setObjectName("continueButton_2")
        self.layoutWidget2 = QtWidgets.QWidget(CaseInformationDialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(22, 13, 701, 161))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.caseinformation_gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.caseinformation_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.caseinformation_gridLayout.setObjectName("caseinformation_gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.caseinformation_gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.case_number = QtWidgets.QLineEdit(self.layoutWidget2)
        self.case_number.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number.setObjectName("case_number")
        self.caseinformation_gridLayout.addWidget(self.case_number, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.caseinformation_gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.defendant_name = QtWidgets.QLineEdit(self.layoutWidget2)
        self.defendant_name.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_name.setObjectName("defendant_name")
        self.caseinformation_gridLayout.addWidget(self.defendant_name, 1, 1, 1, 1)
        self.waived_counsel_checkbox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.waived_counsel_checkbox.setObjectName("waived_counsel_checkbox")
        self.caseinformation_gridLayout.addWidget(self.waived_counsel_checkbox, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.caseinformation_gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.defendant_attorney_name = QtWidgets.QLineEdit(self.layoutWidget2)
        self.defendant_attorney_name.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_attorney_name.setObjectName("defendant_attorney_name")
        self.caseinformation_gridLayout.addWidget(self.defendant_attorney_name, 3, 1, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(CaseInformationDialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(22, 202, 921, 101))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setToolTip("")
        self.label_8.setToolTipDuration(-2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.understood_rights_checkbox = QtWidgets.QCheckBox(self.layoutWidget3)
        self.understood_rights_checkbox.setChecked(True)
        self.understood_rights_checkbox.setObjectName("understood_rights_checkbox")
        self.gridLayout_2.addWidget(self.understood_rights_checkbox, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.plea_trial_date = QtWidgets.QDateEdit(self.layoutWidget3)
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout_2.addWidget(self.plea_trial_date, 1, 1, 1, 1)

        self.retranslateUi(CaseInformationDialog)
        self.pushButton_3.clicked.connect(CaseInformationDialog.reject)
        self.continueButton.released.connect(CaseInformationDialog.close_window)
        self.continueButton.pressed.connect(CaseInformationDialog.update_case_information)
        self.waived_counsel_checkbox.toggled['bool'].connect(CaseInformationDialog.set_dialog)
        self.pushButton_2.clicked.connect(self.defendant_name.clear)
        self.pushButton_2.clicked.connect(self.defendant_attorney_name.clear)
        self.pushButton_2.clicked.connect(self.case_number.clear)
        self.continueButton_2.pressed.connect(CaseInformationDialog.update_case_information)
        self.continueButton_2.released.connect(CaseInformationDialog.close_window)
        self.continueButton.clicked.connect(CaseInformationDialog.proceed_to_sentencing)
        self.continueButton_2.clicked.connect(CaseInformationDialog.proceed_to_ovi)
        QtCore.QMetaObject.connectSlotsByName(CaseInformationDialog)
        CaseInformationDialog.setTabOrder(self.case_number, self.defendant_name)
        CaseInformationDialog.setTabOrder(self.defendant_name, self.waived_counsel_checkbox)
        CaseInformationDialog.setTabOrder(self.waived_counsel_checkbox, self.defendant_attorney_name)
        CaseInformationDialog.setTabOrder(self.defendant_attorney_name, self.comboBox)
        CaseInformationDialog.setTabOrder(self.comboBox, self.is_citizen_checkbox)
        CaseInformationDialog.setTabOrder(self.is_citizen_checkbox, self.citizen_deportation_checkbox)
        CaseInformationDialog.setTabOrder(self.citizen_deportation_checkbox, self.violence_no_firearm_checkbox)
        CaseInformationDialog.setTabOrder(self.violence_no_firearm_checkbox, self.citizen_deportation_checkbox_2)
        CaseInformationDialog.setTabOrder(self.citizen_deportation_checkbox_2, self.continueButton)
        CaseInformationDialog.setTabOrder(self.continueButton, self.pushButton_2)
        CaseInformationDialog.setTabOrder(self.pushButton_2, self.pushButton_3)

    def retranslateUi(self, CaseInformationDialog):
        _translate = QtCore.QCoreApplication.translate
        CaseInformationDialog.setWindowTitle(_translate("CaseInformationDialog", "Case Information"))
        self.continueButton.setText(_translate("CaseInformationDialog", "Sentencing"))
        self.pushButton_2.setText(_translate("CaseInformationDialog", "Clear Fields"))
        self.pushButton_3.setText(_translate("CaseInformationDialog", "Cancel"))
        self.label_7.setText(_translate("CaseInformationDialog", "Offense of Violence"))
        self.violence_no_firearm_checkbox.setToolTip(_translate("CaseInformationDialog", "Defendant informed that convcition disallows Def. to ship/transport/purchase/possess firearms/ammo if victim is current/past spouse or person living as spouse, parent or child of spouse or parent or child of Defendant."))
        self.violence_no_firearm_checkbox.setText(_translate("CaseInformationDialog", "Conviction prohibits ship/transport/purchase/possess firearm/ammo "))
        self.citizen_deportation_checkbox_2.setText(_translate("CaseInformationDialog", "NCIC Mental Health Form shall issue"))
        self.label_6.setText(_translate("CaseInformationDialog", "Citizenship"))
        self.is_citizen_checkbox.setText(_translate("CaseInformationDialog", "Defendant stated that he/she is a U.S. Citizen"))
        self.citizen_deportation_checkbox.setText(_translate("CaseInformationDialog", "Def. advised that conviction may lead to deportation, exclusion from U.S. or denial of naturalization"))
        self.continueButton_2.setText(_translate("CaseInformationDialog", "OVI"))
        self.label.setText(_translate("CaseInformationDialog", "Case Number:"))
        self.label_2.setText(_translate("CaseInformationDialog", "Defendant Name: "))
        self.waived_counsel_checkbox.setText(_translate("CaseInformationDialog", "Defendant waived right to counsel"))
        self.label_4.setText(_translate("CaseInformationDialog", "Defendant Attorney:"))
        self.label_8.setText(_translate("CaseInformationDialog", "Type of Proceeding:"))
        self.comboBox.setItemText(0, _translate("CaseInformationDialog", "Plea"))
        self.comboBox.setItemText(1, _translate("CaseInformationDialog", "Trial"))
        self.comboBox.setItemText(2, _translate("CaseInformationDialog", "Plea in Abstentia"))
        self.label_9.setText(_translate("CaseInformationDialog", "Plea or Trial"))
        self.understood_rights_checkbox.setText(_translate("CaseInformationDialog", "Defendant understood the charges and effects of plea per Crim.R. 11 / Traf.R. 10"))
        self.label_3.setText(_translate("CaseInformationDialog", "Date:"))
