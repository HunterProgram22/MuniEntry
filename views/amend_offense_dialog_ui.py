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
        AmendOffenseDialog.resize(1071, 474)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AmendOffenseDialog.sizePolicy().hasHeightForWidth())
        AmendOffenseDialog.setSizePolicy(sizePolicy)
        AmendOffenseDialog.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        AmendOffenseDialog.setFont(font)
        AmendOffenseDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";")
        self.verticalLayout = QtWidgets.QVBoxLayout(AmendOffenseDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.case_information_frame = QtWidgets.QFrame(AmendOffenseDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_information_frame.sizePolicy().hasHeightForWidth())
        self.case_information_frame.setSizePolicy(sizePolicy)
        self.case_information_frame.setMaximumSize(QtCore.QSize(5000, 5000))
        self.case_information_frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.case_information_frame.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font-weight: bold;")
        self.case_information_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_information_frame.setLineWidth(2)
        self.case_information_frame.setObjectName("case_information_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.case_information_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.case_number_label = QtWidgets.QLabel(self.case_information_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.case_number_label.setFont(font)
        self.case_number_label.setObjectName("case_number_label")
        self.gridLayout_2.addWidget(self.case_number_label, 0, 0, 1, 1)
        self.defendant_name_label = QtWidgets.QLabel(self.case_information_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.defendant_name_label.setFont(font)
        self.defendant_name_label.setObjectName("defendant_name_label")
        self.gridLayout_2.addWidget(self.defendant_name_label, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.case_information_frame)
        self.frame_2 = QtWidgets.QFrame(AmendOffenseDialog)
        self.frame_2.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.motion_decision_box = QtWidgets.QComboBox(self.frame_2)
        self.motion_decision_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.motion_decision_box.setEditable(False)
        self.motion_decision_box.setObjectName("motion_decision_box")
        self.motion_decision_box.addItem("")
        self.motion_decision_box.addItem("")
        self.gridLayout.addWidget(self.motion_decision_box, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.original_charge_box = QtWidgets.QComboBox(self.frame_2)
        self.original_charge_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.original_charge_box.setEditable(True)
        self.original_charge_box.setObjectName("original_charge_box")
        self.gridLayout.addWidget(self.original_charge_box, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.amended_charge_box = QtWidgets.QComboBox(self.frame_2)
        self.amended_charge_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.amended_charge_box.setEditable(True)
        self.amended_charge_box.setObjectName("amended_charge_box")
        self.gridLayout.addWidget(self.amended_charge_box, 2, 1, 1, 1)
        self.clear_fields_Button = QtWidgets.QPushButton(self.frame_2)
        self.clear_fields_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_Button.setObjectName("clear_fields_Button")
        self.gridLayout.addWidget(self.clear_fields_Button, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(AmendOffenseDialog)
        self.frame.setStyleSheet("font: 75 11pt \"Palatino Linotype\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cancel_Button = QtWidgets.QPushButton(self.frame)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout_3.addWidget(self.cancel_Button, 0, 0, 1, 1)
        self.amend_offense_Button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.amend_offense_Button.setFont(font)
        self.amend_offense_Button.setStyleSheet("background-color: rgb(62, 146, 255);\n"
"font: 75 11pt \"Palatino Linotype\";")
        self.amend_offense_Button.setObjectName("amend_offense_Button")
        self.gridLayout_3.addWidget(self.amend_offense_Button, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(AmendOffenseDialog)
        QtCore.QMetaObject.connectSlotsByName(AmendOffenseDialog)
        AmendOffenseDialog.setTabOrder(self.motion_decision_box, self.original_charge_box)
        AmendOffenseDialog.setTabOrder(self.original_charge_box, self.amended_charge_box)

    def retranslateUi(self, AmendOffenseDialog):
        _translate = QtCore.QCoreApplication.translate
        AmendOffenseDialog.setWindowTitle(_translate("AmendOffenseDialog", "Amend Charge"))
        self.case_number_label.setText(_translate("AmendOffenseDialog", "TextLabel"))
        self.defendant_name_label.setText(_translate("AmendOffenseDialog", "TextLabel"))
        self.label.setText(_translate("AmendOffenseDialog", "Motion to amend is:"))
        self.motion_decision_box.setItemText(0, _translate("AmendOffenseDialog", "Granted"))
        self.motion_decision_box.setItemText(1, _translate("AmendOffenseDialog", "Denied"))
        self.label_2.setText(_translate("AmendOffenseDialog", "Original charge:"))
        self.label_3.setText(_translate("AmendOffenseDialog", "Amended charge:"))
        self.clear_fields_Button.setText(_translate("AmendOffenseDialog", "Clear Fields"))
        self.cancel_Button.setText(_translate("AmendOffenseDialog", "Cancel"))
        self.amend_offense_Button.setText(_translate("AmendOffenseDialog", "Amend Offense"))
