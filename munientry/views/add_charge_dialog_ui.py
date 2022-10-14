# Form implementation generated from reading ui file 'munientry/views/ui/AddChargeDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddChargeDialog(object):
    def setupUi(self, AddChargeDialog):
        AddChargeDialog.setObjectName("AddChargeDialog")
        AddChargeDialog.resize(1071, 474)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddChargeDialog.sizePolicy().hasHeightForWidth())
        AddChargeDialog.setSizePolicy(sizePolicy)
        AddChargeDialog.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        AddChargeDialog.setFont(font)
        AddChargeDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";")
        self.gridLayout = QtWidgets.QGridLayout(AddChargeDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(AddChargeDialog)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cancel_Button = QtWidgets.QPushButton(self.frame)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"font-weight: bold;")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout_4.addWidget(self.cancel_Button, 0, 0, 1, 1)
        self.add_charge_Button = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.add_charge_Button.setFont(font)
        self.add_charge_Button.setStyleSheet("background-color: rgb(62, 146, 255);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.add_charge_Button.setObjectName("add_charge_Button")
        self.gridLayout_4.addWidget(self.add_charge_Button, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.case_information_frame = QtWidgets.QFrame(AddChargeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_information_frame.sizePolicy().hasHeightForWidth())
        self.case_information_frame.setSizePolicy(sizePolicy)
        self.case_information_frame.setMaximumSize(QtCore.QSize(5000, 5000))
        self.case_information_frame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.case_information_frame.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font-weight: bold;")
        self.case_information_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.case_information_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
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
        self.gridLayout.addWidget(self.case_information_frame, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(AddChargeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font-weight: bold;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_23 = QtWidgets.QLabel(self.frame_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.offense_choice_box = QtWidgets.QComboBox(self.frame_3)
        self.offense_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.offense_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.offense_choice_box.setEditable(False)
        self.offense_choice_box.setObjectName("offense_choice_box")
        self.gridLayout_3.addWidget(self.offense_choice_box, 2, 1, 1, 1)
        self.statute_choice_box = QtWidgets.QComboBox(self.frame_3)
        self.statute_choice_box.setEnabled(True)
        self.statute_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.statute_choice_box.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.statute_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.statute_choice_box.setEditable(False)
        self.statute_choice_box.setObjectName("statute_choice_box")
        self.gridLayout_3.addWidget(self.statute_choice_box, 1, 1, 1, 1)
        self.degree_choice_box = QtWidgets.QComboBox(self.frame_3)
        self.degree_choice_box.setEnabled(True)
        self.degree_choice_box.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.degree_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.degree_choice_box.setObjectName("degree_choice_box")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.gridLayout_3.addWidget(self.degree_choice_box, 3, 1, 1, 1)
        self.clear_fields_Button = QtWidgets.QPushButton(self.frame_3)
        self.clear_fields_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.clear_fields_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_Button.setObjectName("clear_fields_Button")
        self.gridLayout_3.addWidget(self.clear_fields_Button, 3, 2, 1, 1)
        self.freeform_entry_checkBox = ConditionCheckbox(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.freeform_entry_checkBox.setFont(font)
        self.freeform_entry_checkBox.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.freeform_entry_checkBox.setStyleSheet("font: 75 9pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.freeform_entry_checkBox.setObjectName("freeform_entry_checkBox")
        self.gridLayout_3.addWidget(self.freeform_entry_checkBox, 1, 2, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(AddChargeDialog)
        QtCore.QMetaObject.connectSlotsByName(AddChargeDialog)
        AddChargeDialog.setTabOrder(self.statute_choice_box, self.offense_choice_box)
        AddChargeDialog.setTabOrder(self.offense_choice_box, self.add_charge_Button)
        AddChargeDialog.setTabOrder(self.add_charge_Button, self.cancel_Button)

    def retranslateUi(self, AddChargeDialog):
        _translate = QtCore.QCoreApplication.translate
        AddChargeDialog.setWindowTitle(_translate("AddChargeDialog", "Add Charge"))
        self.cancel_Button.setText(_translate("AddChargeDialog", "Cancel"))
        self.add_charge_Button.setText(_translate("AddChargeDialog", "Add Charge"))
        self.case_number_label.setText(_translate("AddChargeDialog", "TextLabel"))
        self.defendant_name_label.setText(_translate("AddChargeDialog", "TextLabel"))
        self.label_23.setText(_translate("AddChargeDialog", "Degree:"))
        self.label_15.setText(_translate("AddChargeDialog", "Offense:"))
        self.label_6.setText(_translate("AddChargeDialog", "Statute:"))
        self.degree_choice_box.setItemText(0, _translate("AddChargeDialog", "MM"))
        self.degree_choice_box.setItemText(1, _translate("AddChargeDialog", "M1"))
        self.degree_choice_box.setItemText(2, _translate("AddChargeDialog", "M2"))
        self.degree_choice_box.setItemText(3, _translate("AddChargeDialog", "M3"))
        self.degree_choice_box.setItemText(4, _translate("AddChargeDialog", "M4"))
        self.degree_choice_box.setItemText(5, _translate("AddChargeDialog", "UCM"))
        self.clear_fields_Button.setText(_translate("AddChargeDialog", "Clear Fields"))
        self.freeform_entry_checkBox.setText(_translate("AddChargeDialog", "Enable freeform entry for offense/statute"))
from .custom_widgets import ConditionCheckbox
