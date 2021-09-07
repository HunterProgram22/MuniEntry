# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/AmendOffenseDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AmendOffenseDialog(object):
    def setupUi(self, AmendOffenseDialog):
        AmendOffenseDialog.setObjectName("AmendOffenseDialog")
        AmendOffenseDialog.resize(1000, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AmendOffenseDialog.sizePolicy().hasHeightForWidth())
        AmendOffenseDialog.setSizePolicy(sizePolicy)
        AmendOffenseDialog.setMinimumSize(QtCore.QSize(1000, 350))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        AmendOffenseDialog.setFont(font)
        AmendOffenseDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";")
        self.case_information_frame = QtWidgets.QFrame(AmendOffenseDialog)
        self.case_information_frame.setGeometry(QtCore.QRect(9, 9, 981, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_information_frame.sizePolicy().hasHeightForWidth())
        self.case_information_frame.setSizePolicy(sizePolicy)
        self.case_information_frame.setMaximumSize(QtCore.QSize(1000, 800))
        self.case_information_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.case_information_frame.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font-weight: bold;")
        self.case_information_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_information_frame.setLineWidth(2)
        self.case_information_frame.setObjectName("case_information_frame")
        self.defendant_name_label = QtWidgets.QLabel(self.case_information_frame)
        self.defendant_name_label.setGeometry(QtCore.QRect(18, 53, 831, 27))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.defendant_name_label.setFont(font)
        self.defendant_name_label.setObjectName("defendant_name_label")
        self.case_number_label = QtWidgets.QLabel(self.case_information_frame)
        self.case_number_label.setGeometry(QtCore.QRect(18, 13, 831, 27))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.case_number_label.setFont(font)
        self.case_number_label.setObjectName("case_number_label")
        self.defendant_attorney_name_label = QtWidgets.QLabel(self.case_information_frame)
        self.defendant_attorney_name_label.setGeometry(QtCore.QRect(18, 93, 821, 27))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.defendant_attorney_name_label.setFont(font)
        self.defendant_attorney_name_label.setObjectName("defendant_attorney_name_label")
        self.frame_2 = QtWidgets.QFrame(AmendOffenseDialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 150, 981, 191))
        self.frame_2.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(801, 21, 161, 151))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.continueButton = QtWidgets.QPushButton(self.widget)
        self.continueButton.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.continueButton.setObjectName("continueButton")
        self.gridLayout.addWidget(self.continueButton, 2, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(11, 21, 781, 151))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.motion_decision_box = QtWidgets.QComboBox(self.widget1)
        self.motion_decision_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.motion_decision_box.setEditable(False)
        self.motion_decision_box.setObjectName("motion_decision_box")
        self.motion_decision_box.addItem("")
        self.motion_decision_box.addItem("")
        self.motion_decision_box.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.motion_decision_box)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.original_charge_box = QtWidgets.QComboBox(self.widget1)
        self.original_charge_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.original_charge_box.setEditable(True)
        self.original_charge_box.setObjectName("original_charge_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.original_charge_box)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.amended_charge_box = QtWidgets.QComboBox(self.widget1)
        self.amended_charge_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.amended_charge_box.setEditable(True)
        self.amended_charge_box.setObjectName("amended_charge_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.amended_charge_box)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pursuant_to_box = QtWidgets.QComboBox(self.widget1)
        self.pursuant_to_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pursuant_to_box.setEditable(True)
        self.pursuant_to_box.setObjectName("pursuant_to_box")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pursuant_to_box)

        self.retranslateUi(AmendOffenseDialog)
        self.continueButton.released.connect(AmendOffenseDialog.close_window)
        self.pushButton_3.clicked.connect(AmendOffenseDialog.close_window)
        self.pushButton_2.clicked.connect(self.original_charge_box.clearEditText)
        self.pushButton_2.clicked.connect(self.amended_charge_box.clearEditText)
        self.pushButton_2.clicked.connect(self.pursuant_to_box.clearEditText)
        self.continueButton.pressed.connect(AmendOffenseDialog.amend_offense)
        QtCore.QMetaObject.connectSlotsByName(AmendOffenseDialog)
        AmendOffenseDialog.setTabOrder(self.motion_decision_box, self.original_charge_box)
        AmendOffenseDialog.setTabOrder(self.original_charge_box, self.amended_charge_box)
        AmendOffenseDialog.setTabOrder(self.amended_charge_box, self.pursuant_to_box)
        AmendOffenseDialog.setTabOrder(self.pursuant_to_box, self.continueButton)
        AmendOffenseDialog.setTabOrder(self.continueButton, self.pushButton_2)
        AmendOffenseDialog.setTabOrder(self.pushButton_2, self.pushButton_3)

    def retranslateUi(self, AmendOffenseDialog):
        _translate = QtCore.QCoreApplication.translate
        AmendOffenseDialog.setWindowTitle(_translate("AmendOffenseDialog", "Amend Charge"))
        self.defendant_name_label.setText(_translate("AmendOffenseDialog", "TextLabel"))
        self.case_number_label.setText(_translate("AmendOffenseDialog", "TextLabel"))
        self.defendant_attorney_name_label.setText(_translate("AmendOffenseDialog", "TextLabel"))
        self.pushButton_3.setText(_translate("AmendOffenseDialog", "Cancel"))
        self.pushButton_2.setText(_translate("AmendOffenseDialog", "Clear Fields"))
        self.continueButton.setText(_translate("AmendOffenseDialog", "Continue"))
        self.label.setText(_translate("AmendOffenseDialog", "Prosecutor motion to amend is "))
        self.motion_decision_box.setItemText(0, _translate("AmendOffenseDialog", "Granted"))
        self.motion_decision_box.setItemText(1, _translate("AmendOffenseDialog", "Denied"))
        self.motion_decision_box.setItemText(2, _translate("AmendOffenseDialog", "Denied as moot"))
        self.label_2.setText(_translate("AmendOffenseDialog", "The charge of "))
        self.label_3.setText(_translate("AmendOffenseDialog", "is amended to"))
        self.label_4.setText(_translate("AmendOffenseDialog", "pursuant to"))
