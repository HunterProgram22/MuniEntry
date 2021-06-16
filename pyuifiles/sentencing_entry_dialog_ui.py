# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SentencingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SentencingDialog(object):
    def setupUi(self, SentencingDialog):
        SentencingDialog.setObjectName("SentencingDialog")
        SentencingDialog.resize(739, 671)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SentencingDialog.sizePolicy().hasHeightForWidth())
        SentencingDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        SentencingDialog.setFont(font)
        self.case_information_frame = QtWidgets.QFrame(SentencingDialog)
        self.case_information_frame.setGeometry(QtCore.QRect(9, 9, 721, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_information_frame.sizePolicy().hasHeightForWidth())
        self.case_information_frame.setSizePolicy(sizePolicy)
        self.case_information_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_information_frame.setLineWidth(2)
        self.case_information_frame.setObjectName("case_information_frame")
        self.layoutWidget = QtWidgets.QWidget(self.case_information_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(13, 12, 691, 116))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(5, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.defendant_name_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.defendant_name_label.setFont(font)
        self.defendant_name_label.setObjectName("defendant_name_label")
        self.gridLayout_2.addWidget(self.defendant_name_label, 1, 0, 1, 1)
        self.counsel_name_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.counsel_name_label.setFont(font)
        self.counsel_name_label.setObjectName("counsel_name_label")
        self.gridLayout_2.addWidget(self.counsel_name_label, 2, 0, 1, 1)
        self.case_number_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.case_number_label.setFont(font)
        self.case_number_label.setObjectName("case_number_label")
        self.gridLayout_2.addWidget(self.case_number_label, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(SentencingDialog)
        self.frame.setGeometry(QtCore.QRect(10, 490, 372, 102))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.offense_label_1 = QtWidgets.QLabel(self.frame)
        self.offense_label_1.setObjectName("offense_label_1")
        self.gridLayout_3.addWidget(self.offense_label_1, 0, 0, 1, 1)
        self.offense_label_2 = QtWidgets.QLabel(self.frame)
        self.offense_label_2.setObjectName("offense_label_2")
        self.gridLayout_3.addWidget(self.offense_label_2, 0, 1, 1, 1)
        self.offense_label_3 = QtWidgets.QLabel(self.frame)
        self.offense_label_3.setObjectName("offense_label_3")
        self.gridLayout_3.addWidget(self.offense_label_3, 0, 2, 1, 1)
        self.offense_label_4 = QtWidgets.QLabel(self.frame)
        self.offense_label_4.setObjectName("offense_label_4")
        self.gridLayout_3.addWidget(self.offense_label_4, 0, 3, 1, 1)
        self.offense_label_5 = QtWidgets.QLabel(self.frame)
        self.offense_label_5.setObjectName("offense_label_5")
        self.gridLayout_3.addWidget(self.offense_label_5, 0, 4, 1, 1)
        self.offense_label_6 = QtWidgets.QLabel(self.frame)
        self.offense_label_6.setObjectName("offense_label_6")
        self.gridLayout_3.addWidget(self.offense_label_6, 0, 5, 1, 1)
        self.plea_label_1 = QtWidgets.QLabel(self.frame)
        self.plea_label_1.setObjectName("plea_label_1")
        self.gridLayout_3.addWidget(self.plea_label_1, 1, 0, 1, 1)
        self.plea_label_2 = QtWidgets.QLabel(self.frame)
        self.plea_label_2.setObjectName("plea_label_2")
        self.gridLayout_3.addWidget(self.plea_label_2, 1, 1, 1, 1)
        self.plea_label_3 = QtWidgets.QLabel(self.frame)
        self.plea_label_3.setObjectName("plea_label_3")
        self.gridLayout_3.addWidget(self.plea_label_3, 1, 2, 1, 1)
        self.plea_label_4 = QtWidgets.QLabel(self.frame)
        self.plea_label_4.setObjectName("plea_label_4")
        self.gridLayout_3.addWidget(self.plea_label_4, 1, 3, 1, 1)
        self.plea_label_5 = QtWidgets.QLabel(self.frame)
        self.plea_label_5.setObjectName("plea_label_5")
        self.gridLayout_3.addWidget(self.plea_label_5, 1, 4, 1, 1)
        self.plea_label_6 = QtWidgets.QLabel(self.frame)
        self.plea_label_6.setObjectName("plea_label_6")
        self.gridLayout_3.addWidget(self.plea_label_6, 1, 5, 1, 1)
        self.finding_label_1 = QtWidgets.QLabel(self.frame)
        self.finding_label_1.setObjectName("finding_label_1")
        self.gridLayout_3.addWidget(self.finding_label_1, 2, 0, 1, 1)
        self.finding_label_2 = QtWidgets.QLabel(self.frame)
        self.finding_label_2.setObjectName("finding_label_2")
        self.gridLayout_3.addWidget(self.finding_label_2, 2, 1, 1, 1)
        self.finding_label_3 = QtWidgets.QLabel(self.frame)
        self.finding_label_3.setObjectName("finding_label_3")
        self.gridLayout_3.addWidget(self.finding_label_3, 2, 2, 1, 1)
        self.finding_label_4 = QtWidgets.QLabel(self.frame)
        self.finding_label_4.setObjectName("finding_label_4")
        self.gridLayout_3.addWidget(self.finding_label_4, 2, 3, 1, 1)
        self.finding_label_5 = QtWidgets.QLabel(self.frame)
        self.finding_label_5.setObjectName("finding_label_5")
        self.gridLayout_3.addWidget(self.finding_label_5, 2, 4, 1, 1)
        self.finding_label_6 = QtWidgets.QLabel(self.frame)
        self.finding_label_6.setObjectName("finding_label_6")
        self.gridLayout_3.addWidget(self.finding_label_6, 2, 5, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(SentencingDialog)
        self.pushButton.setGeometry(QtCore.QRect(9, 596, 151, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SentencingDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(9, 632, 175, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(SentencingDialog)
        self.label.setGeometry(QtCore.QRect(17, 168, 56, 22))
        self.label.setObjectName("label")
        self.offense_choice_box = QtWidgets.QComboBox(SentencingDialog)
        self.offense_choice_box.setGeometry(QtCore.QRect(80, 168, 252, 28))
        self.offense_choice_box.setEditable(True)
        self.offense_choice_box.setObjectName("offense_choice_box")
        self.offense_choice_box.addItem("")
        self.offense_choice_box.setItemText(0, "")
        self.offense_choice_box.addItem("")
        self.offense_choice_box.addItem("")
        self.offense_choice_box.addItem("")
        self.label_2 = QtWidgets.QLabel(SentencingDialog)
        self.label_2.setGeometry(QtCore.QRect(17, 202, 52, 22))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(SentencingDialog)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 202, 65, 28))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(SentencingDialog)
        self.label_3.setGeometry(QtCore.QRect(17, 236, 32, 22))
        self.label_3.setObjectName("label_3")
        self.plea_choice_box = QtWidgets.QComboBox(SentencingDialog)
        self.plea_choice_box.setGeometry(QtCore.QRect(80, 236, 102, 28))
        self.plea_choice_box.setObjectName("plea_choice_box")
        self.plea_choice_box.addItem("")
        self.plea_choice_box.addItem("")
        self.plea_choice_box.addItem("")
        self.label_4 = QtWidgets.QLabel(SentencingDialog)
        self.label_4.setGeometry(QtCore.QRect(17, 270, 57, 22))
        self.label_4.setObjectName("label_4")
        self.finding_choice_box = QtWidgets.QComboBox(SentencingDialog)
        self.finding_choice_box.setGeometry(QtCore.QRect(80, 270, 99, 28))
        self.finding_choice_box.setObjectName("finding_choice_box")
        self.finding_choice_box.addItem("")
        self.finding_choice_box.addItem("")
        self.layoutWidget1 = QtWidgets.QWidget(SentencingDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 310, 588, 64))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.jail_days_suspended = QtWidgets.QSpinBox(self.layoutWidget1)
        self.jail_days_suspended.setObjectName("jail_days_suspended")
        self.gridLayout.addWidget(self.jail_days_suspended, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.fine_amount = QtWidgets.QLineEdit(self.layoutWidget1)
        self.fine_amount.setObjectName("fine_amount")
        self.gridLayout.addWidget(self.fine_amount, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.fine_suspended = QtWidgets.QLineEdit(self.layoutWidget1)
        self.fine_suspended.setObjectName("fine_suspended")
        self.gridLayout.addWidget(self.fine_suspended, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.jail_days = QtWidgets.QComboBox(self.layoutWidget1)
        self.jail_days.setEditable(True)
        self.jail_days.setObjectName("jail_days")
        self.jail_days.addItem("")
        self.jail_days.addItem("")
        self.jail_days.addItem("")
        self.jail_days.addItem("")
        self.jail_days.addItem("")
        self.jail_days.addItem("")
        self.gridLayout.addWidget(self.jail_days, 1, 1, 1, 1)

        self.retranslateUi(SentencingDialog)
        self.pushButton_2.clicked.connect(SentencingDialog.proceed_to_ability_to_pay)
        self.pushButton_2.released.connect(SentencingDialog.close_window)
        self.pushButton.clicked.connect(SentencingDialog.add_offense)
        QtCore.QMetaObject.connectSlotsByName(SentencingDialog)
        SentencingDialog.setTabOrder(self.offense_choice_box, self.comboBox_2)
        SentencingDialog.setTabOrder(self.comboBox_2, self.plea_choice_box)
        SentencingDialog.setTabOrder(self.plea_choice_box, self.finding_choice_box)
        SentencingDialog.setTabOrder(self.finding_choice_box, self.fine_amount)
        SentencingDialog.setTabOrder(self.fine_amount, self.fine_suspended)
        SentencingDialog.setTabOrder(self.fine_suspended, self.jail_days)
        SentencingDialog.setTabOrder(self.jail_days, self.jail_days_suspended)
        SentencingDialog.setTabOrder(self.jail_days_suspended, self.pushButton)
        SentencingDialog.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, SentencingDialog):
        _translate = QtCore.QCoreApplication.translate
        SentencingDialog.setWindowTitle(_translate("SentencingDialog", "Sentencing"))
        self.defendant_name_label.setText(_translate("SentencingDialog", "TextLabel"))
        self.counsel_name_label.setText(_translate("SentencingDialog", "TextLabel"))
        self.case_number_label.setText(_translate("SentencingDialog", "TextLabel"))
        self.offense_label_1.setText(_translate("SentencingDialog", "Offense"))
        self.offense_label_2.setText(_translate("SentencingDialog", "Offense"))
        self.offense_label_3.setText(_translate("SentencingDialog", "Offense"))
        self.offense_label_4.setText(_translate("SentencingDialog", "Offense"))
        self.offense_label_5.setText(_translate("SentencingDialog", "Offense"))
        self.offense_label_6.setText(_translate("SentencingDialog", "Offense"))
        self.plea_label_1.setText(_translate("SentencingDialog", "Plea"))
        self.plea_label_2.setText(_translate("SentencingDialog", "Plea"))
        self.plea_label_3.setText(_translate("SentencingDialog", "Plea"))
        self.plea_label_4.setText(_translate("SentencingDialog", "Plea"))
        self.plea_label_5.setText(_translate("SentencingDialog", "Plea"))
        self.plea_label_6.setText(_translate("SentencingDialog", "Plea"))
        self.finding_label_1.setText(_translate("SentencingDialog", "Finding"))
        self.finding_label_2.setText(_translate("SentencingDialog", "Finding"))
        self.finding_label_3.setText(_translate("SentencingDialog", "Finding"))
        self.finding_label_4.setText(_translate("SentencingDialog", "Finding"))
        self.finding_label_5.setText(_translate("SentencingDialog", "Finding"))
        self.finding_label_6.setText(_translate("SentencingDialog", "Finding"))
        self.pushButton.setText(_translate("SentencingDialog", "Add Another Offense"))
        self.pushButton_2.setText(_translate("SentencingDialog", "Proceed to Ability to Pay"))
        self.label.setText(_translate("SentencingDialog", "Offense:"))
        self.offense_choice_box.setItemText(1, _translate("SentencingDialog", "OVI - R.C. 4511.19(A)(1)(a)"))
        self.offense_choice_box.setItemText(2, _translate("SentencingDialog", "OVI - R.C. 4511.19(A)(1)(b)"))
        self.offense_choice_box.setItemText(3, _translate("SentencingDialog", "Failure to Control - R.C. 4511.202"))
        self.label_2.setText(_translate("SentencingDialog", "Degree:"))
        self.comboBox_2.setItemText(0, _translate("SentencingDialog", "M1"))
        self.comboBox_2.setItemText(1, _translate("SentencingDialog", "M2"))
        self.comboBox_2.setItemText(2, _translate("SentencingDialog", "M3"))
        self.comboBox_2.setItemText(3, _translate("SentencingDialog", "M4"))
        self.comboBox_2.setItemText(4, _translate("SentencingDialog", "MM"))
        self.comboBox_2.setItemText(5, _translate("SentencingDialog", "UCM"))
        self.label_3.setText(_translate("SentencingDialog", "Plea:"))
        self.plea_choice_box.setItemText(0, _translate("SentencingDialog", "Not Guilty"))
        self.plea_choice_box.setItemText(1, _translate("SentencingDialog", "No Contest"))
        self.plea_choice_box.setItemText(2, _translate("SentencingDialog", "Guilty"))
        self.label_4.setText(_translate("SentencingDialog", "Finding:"))
        self.finding_choice_box.setItemText(0, _translate("SentencingDialog", "Guilty"))
        self.finding_choice_box.setItemText(1, _translate("SentencingDialog", "Not Guilty"))
        self.label_8.setText(_translate("SentencingDialog", "Jail Days Suspended:"))
        self.label_7.setText(_translate("SentencingDialog", "Jail Days:"))
        self.label_6.setText(_translate("SentencingDialog", "Fines Suspended:"))
        self.label_5.setText(_translate("SentencingDialog", "Fine Amount:"))
        self.jail_days.setItemText(0, _translate("SentencingDialog", "30"))
        self.jail_days.setItemText(1, _translate("SentencingDialog", "60"))
        self.jail_days.setItemText(2, _translate("SentencingDialog", "90"))
        self.jail_days.setItemText(3, _translate("SentencingDialog", "120"))
        self.jail_days.setItemText(4, _translate("SentencingDialog", "150"))
        self.jail_days.setItemText(5, _translate("SentencingDialog", "180"))
