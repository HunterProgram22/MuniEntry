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
        AmendOffenseDialog.resize(1000, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AmendOffenseDialog.sizePolicy().hasHeightForWidth())
        AmendOffenseDialog.setSizePolicy(sizePolicy)
        AmendOffenseDialog.setMinimumSize(QtCore.QSize(1000, 300))
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
        self.cancel_Button = QtWidgets.QPushButton(self.case_information_frame)
        self.cancel_Button.setGeometry(QtCore.QRect(832, 10, 141, 33))
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.frame_2 = QtWidgets.QFrame(AmendOffenseDialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 150, 981, 141))
        self.frame_2.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(830, 14, 141, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.clear_fields_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.clear_fields_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_Button.setObjectName("clear_fields_Button")
        self.gridLayout.addWidget(self.clear_fields_Button, 0, 0, 1, 1)
        self.continue_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.continue_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.continue_Button.setObjectName("continue_Button")
        self.gridLayout.addWidget(self.continue_Button, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(13, 10, 791, 121))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.motion_decision_box = QtWidgets.QComboBox(self.widget)
        self.motion_decision_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.motion_decision_box.setEditable(False)
        self.motion_decision_box.setObjectName("motion_decision_box")
        self.motion_decision_box.addItem("")
        self.motion_decision_box.addItem("")
        self.gridLayout_2.addWidget(self.motion_decision_box, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.original_charge_box = QtWidgets.QComboBox(self.widget)
        self.original_charge_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.original_charge_box.setEditable(True)
        self.original_charge_box.setObjectName("original_charge_box")
        self.gridLayout_2.addWidget(self.original_charge_box, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.amended_charge_box = QtWidgets.QComboBox(self.widget)
        self.amended_charge_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.amended_charge_box.setEditable(True)
        self.amended_charge_box.setObjectName("amended_charge_box")
        self.gridLayout_2.addWidget(self.amended_charge_box, 2, 1, 1, 1)

        self.retranslateUi(AmendOffenseDialog)
        self.continue_Button.released.connect(AmendOffenseDialog.close_window)
        self.cancel_Button.clicked.connect(AmendOffenseDialog.close_window)
        self.clear_fields_Button.clicked.connect(self.original_charge_box.clearEditText)
        self.clear_fields_Button.clicked.connect(self.amended_charge_box.clearEditText)
        self.continue_Button.pressed.connect(AmendOffenseDialog.amend_offense)
        QtCore.QMetaObject.connectSlotsByName(AmendOffenseDialog)
        AmendOffenseDialog.setTabOrder(self.motion_decision_box, self.original_charge_box)
        AmendOffenseDialog.setTabOrder(self.original_charge_box, self.amended_charge_box)
        AmendOffenseDialog.setTabOrder(self.amended_charge_box, self.continue_Button)
        AmendOffenseDialog.setTabOrder(self.continue_Button, self.clear_fields_Button)
        AmendOffenseDialog.setTabOrder(self.clear_fields_Button, self.cancel_Button)

    def retranslateUi(self, AmendOffenseDialog):
        _translate = QtCore.QCoreApplication.translate
        AmendOffenseDialog.setWindowTitle(_translate("AmendOffenseDialog", "Amend Charge"))
        self.defendant_name_label.setText(_translate("AmendOffenseDialog", "TextLabel"))
        self.case_number_label.setText(_translate("AmendOffenseDialog", "TextLabel"))
        self.defendant_attorney_name_label.setText(_translate("AmendOffenseDialog", "TextLabel"))
        self.cancel_Button.setText(_translate("AmendOffenseDialog", "Cancel"))
        self.clear_fields_Button.setText(_translate("AmendOffenseDialog", "Clear Fields"))
        self.continue_Button.setText(_translate("AmendOffenseDialog", "Continue"))
        self.label.setText(_translate("AmendOffenseDialog", "Motion to amend is:"))
        self.motion_decision_box.setItemText(0, _translate("AmendOffenseDialog", "Granted"))
        self.motion_decision_box.setItemText(1, _translate("AmendOffenseDialog", "Denied"))
        self.label_2.setText(_translate("AmendOffenseDialog", "Original charge:"))
        self.label_3.setText(_translate("AmendOffenseDialog", "Amended charge:"))
