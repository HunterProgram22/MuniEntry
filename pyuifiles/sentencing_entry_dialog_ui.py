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
        SentencingDialog.resize(709, 556)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SentencingDialog.sizePolicy().hasHeightForWidth())
        SentencingDialog.setSizePolicy(sizePolicy)
        self.pushButton = QtWidgets.QPushButton(SentencingDialog)
        self.pushButton.setGeometry(QtCore.QRect(9, 519, 128, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(SentencingDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(358, 519, 147, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(SentencingDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 347, 280, 108))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.layoutWidget1 = QtWidgets.QWidget(SentencingDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(9, 461, 492, 52))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.case_information_frame = QtWidgets.QFrame(SentencingDialog)
        self.case_information_frame.setGeometry(QtCore.QRect(9, 9, 691, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_information_frame.sizePolicy().hasHeightForWidth())
        self.case_information_frame.setSizePolicy(sizePolicy)
        self.case_information_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_information_frame.setLineWidth(2)
        self.case_information_frame.setObjectName("case_information_frame")
        self.widget = QtWidgets.QWidget(self.case_information_frame)
        self.widget.setGeometry(QtCore.QRect(13, 12, 671, 116))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(5, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.defendant_name_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.defendant_name_label.setFont(font)
        self.defendant_name_label.setObjectName("defendant_name_label")
        self.gridLayout_2.addWidget(self.defendant_name_label, 1, 0, 1, 1)
        self.counsel_name_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.counsel_name_label.setFont(font)
        self.counsel_name_label.setObjectName("counsel_name_label")
        self.gridLayout_2.addWidget(self.counsel_name_label, 2, 0, 1, 1)
        self.case_no_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.case_no_label.setFont(font)
        self.case_no_label.setObjectName("case_no_label")
        self.gridLayout_2.addWidget(self.case_no_label, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(SentencingDialog)
        self.frame.setGeometry(QtCore.QRect(10, 180, 691, 141))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(11, 11, 671, 121))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.offense_label = QtWidgets.QLabel(self.widget1)
        self.offense_label.setObjectName("offense_label")
        self.verticalLayout.addWidget(self.offense_label)
        self.plea_label = QtWidgets.QLabel(self.widget1)
        self.plea_label.setObjectName("plea_label")
        self.verticalLayout.addWidget(self.plea_label)
        self.finding_label = QtWidgets.QLabel(self.widget1)
        self.finding_label.setObjectName("finding_label")
        self.verticalLayout.addWidget(self.finding_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.offense_label_2 = QtWidgets.QLabel(self.widget1)
        self.offense_label_2.setObjectName("offense_label_2")
        self.verticalLayout_2.addWidget(self.offense_label_2)
        self.plea_label_2 = QtWidgets.QLabel(self.widget1)
        self.plea_label_2.setObjectName("plea_label_2")
        self.verticalLayout_2.addWidget(self.plea_label_2)
        self.finding_label_2 = QtWidgets.QLabel(self.widget1)
        self.finding_label_2.setObjectName("finding_label_2")
        self.verticalLayout_2.addWidget(self.finding_label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.offense_label_3 = QtWidgets.QLabel(self.widget1)
        self.offense_label_3.setObjectName("offense_label_3")
        self.verticalLayout_3.addWidget(self.offense_label_3)
        self.plea_label_3 = QtWidgets.QLabel(self.widget1)
        self.plea_label_3.setObjectName("plea_label_3")
        self.verticalLayout_3.addWidget(self.plea_label_3)
        self.finding_label_3 = QtWidgets.QLabel(self.widget1)
        self.finding_label_3.setObjectName("finding_label_3")
        self.verticalLayout_3.addWidget(self.finding_label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.offense_label_4 = QtWidgets.QLabel(self.widget1)
        self.offense_label_4.setObjectName("offense_label_4")
        self.verticalLayout_4.addWidget(self.offense_label_4)
        self.plea_label_4 = QtWidgets.QLabel(self.widget1)
        self.plea_label_4.setObjectName("plea_label_4")
        self.verticalLayout_4.addWidget(self.plea_label_4)
        self.finding_label_4 = QtWidgets.QLabel(self.widget1)
        self.finding_label_4.setObjectName("finding_label_4")
        self.verticalLayout_4.addWidget(self.finding_label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.offense_label_5 = QtWidgets.QLabel(self.widget1)
        self.offense_label_5.setObjectName("offense_label_5")
        self.verticalLayout_5.addWidget(self.offense_label_5)
        self.plea_label_5 = QtWidgets.QLabel(self.widget1)
        self.plea_label_5.setObjectName("plea_label_5")
        self.verticalLayout_5.addWidget(self.plea_label_5)
        self.finding_label_5 = QtWidgets.QLabel(self.widget1)
        self.finding_label_5.setObjectName("finding_label_5")
        self.verticalLayout_5.addWidget(self.finding_label_5)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.offense_label_6 = QtWidgets.QLabel(self.widget1)
        self.offense_label_6.setObjectName("offense_label_6")
        self.verticalLayout_6.addWidget(self.offense_label_6)
        self.plea_label_6 = QtWidgets.QLabel(self.widget1)
        self.plea_label_6.setObjectName("plea_label_6")
        self.verticalLayout_6.addWidget(self.plea_label_6)
        self.finding_label_6 = QtWidgets.QLabel(self.widget1)
        self.finding_label_6.setObjectName("finding_label_6")
        self.verticalLayout_6.addWidget(self.finding_label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.retranslateUi(SentencingDialog)
        self.pushButton_2.clicked.connect(SentencingDialog.proceed_to_ability_to_pay)
        self.pushButton_2.released.connect(SentencingDialog.close_window)
        QtCore.QMetaObject.connectSlotsByName(SentencingDialog)

    def retranslateUi(self, SentencingDialog):
        _translate = QtCore.QCoreApplication.translate
        SentencingDialog.setWindowTitle(_translate("SentencingDialog", "Sentencing"))
        self.pushButton.setText(_translate("SentencingDialog", "Add Another Offense"))
        self.pushButton_2.setText(_translate("SentencingDialog", "Proceed to Ability to Pay"))
        self.label.setText(_translate("SentencingDialog", "Offense:"))
        self.comboBox.setItemText(1, _translate("SentencingDialog", "OVI - R.C. 4511.19(A)(1)(a)"))
        self.comboBox.setItemText(2, _translate("SentencingDialog", "OVI - R.C. 4511.19(A)(1)(b)"))
        self.comboBox.setItemText(3, _translate("SentencingDialog", "Failure to Control - R.C. 4511.202"))
        self.label_2.setText(_translate("SentencingDialog", "Degree:"))
        self.comboBox_2.setItemText(0, _translate("SentencingDialog", "M1"))
        self.comboBox_2.setItemText(1, _translate("SentencingDialog", "M2"))
        self.comboBox_2.setItemText(2, _translate("SentencingDialog", "M3"))
        self.comboBox_2.setItemText(3, _translate("SentencingDialog", "M4"))
        self.comboBox_2.setItemText(4, _translate("SentencingDialog", "MM"))
        self.comboBox_2.setItemText(5, _translate("SentencingDialog", "UCM"))
        self.label_3.setText(_translate("SentencingDialog", "Plea:"))
        self.comboBox_3.setItemText(0, _translate("SentencingDialog", "Not Guilty"))
        self.comboBox_3.setItemText(1, _translate("SentencingDialog", "No Contest"))
        self.comboBox_3.setItemText(2, _translate("SentencingDialog", "Guilty"))
        self.label_4.setText(_translate("SentencingDialog", "Finding:"))
        self.comboBox_4.setItemText(0, _translate("SentencingDialog", "Guilty"))
        self.comboBox_4.setItemText(1, _translate("SentencingDialog", "Not Guilty"))
        self.label_8.setText(_translate("SentencingDialog", "Jail Days Suspended:"))
        self.label_7.setText(_translate("SentencingDialog", "Jail Days:"))
        self.label_6.setText(_translate("SentencingDialog", "Fines Suspended:"))
        self.label_5.setText(_translate("SentencingDialog", "Fine Amount:"))
        self.defendant_name_label.setText(_translate("SentencingDialog", "TextLabel"))
        self.counsel_name_label.setText(_translate("SentencingDialog", "TextLabel"))
        self.case_no_label.setText(_translate("SentencingDialog", "TextLabel"))
        self.offense_label.setText(_translate("SentencingDialog", "Offense"))
        self.plea_label.setText(_translate("SentencingDialog", "Plea"))
        self.finding_label.setText(_translate("SentencingDialog", "Finding"))
        self.offense_label_2.setText(_translate("SentencingDialog", "Offense"))
        self.plea_label_2.setText(_translate("SentencingDialog", "Plea"))
        self.finding_label_2.setText(_translate("SentencingDialog", "Finding"))
        self.offense_label_3.setText(_translate("SentencingDialog", "Offense"))
        self.plea_label_3.setText(_translate("SentencingDialog", "Plea"))
        self.finding_label_3.setText(_translate("SentencingDialog", "Finding"))
        self.offense_label_4.setText(_translate("SentencingDialog", "Offense"))
        self.plea_label_4.setText(_translate("SentencingDialog", "Plea"))
        self.finding_label_4.setText(_translate("SentencingDialog", "Finding"))
        self.offense_label_5.setText(_translate("SentencingDialog", "Offense"))
        self.plea_label_5.setText(_translate("SentencingDialog", "Plea"))
        self.finding_label_5.setText(_translate("SentencingDialog", "Finding"))
        self.offense_label_6.setText(_translate("SentencingDialog", "Offense"))
        self.plea_label_6.setText(_translate("SentencingDialog", "Plea"))
        self.finding_label_6.setText(_translate("SentencingDialog", "Finding"))
