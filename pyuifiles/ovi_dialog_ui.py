# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/OviDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OviDialog(object):
    def setupUi(self, OviDialog):
        OviDialog.setObjectName("OviDialog")
        OviDialog.resize(830, 564)
        OviDialog.setMinimumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        OviDialog.setFont(font)
        self.layoutWidget_2 = QtWidgets.QWidget(OviDialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(490, 10, 118, 80))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.continueButton = QtWidgets.QPushButton(OviDialog)
        self.continueButton.setGeometry(QtCore.QRect(450, 350, 121, 28))
        self.continueButton.setObjectName("continueButton")
        self.case_information_frame = QtWidgets.QFrame(OviDialog)
        self.case_information_frame.setGeometry(QtCore.QRect(10, 10, 381, 101))
        self.case_information_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_information_frame.setLineWidth(2)
        self.case_information_frame.setObjectName("case_information_frame")
        self.layoutWidget_3 = QtWidgets.QWidget(self.case_information_frame)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 361, 95))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.defendant_attorney_name_label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.defendant_attorney_name_label.setFont(font)
        self.defendant_attorney_name_label.setObjectName("defendant_attorney_name_label")
        self.gridLayout_2.addWidget(self.defendant_attorney_name_label, 2, 0, 1, 1)
        self.defendant_name_label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.defendant_name_label.setFont(font)
        self.defendant_name_label.setObjectName("defendant_name_label")
        self.gridLayout_2.addWidget(self.defendant_name_label, 1, 0, 1, 1)
        self.case_number_label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.case_number_label.setFont(font)
        self.case_number_label.setObjectName("case_number_label")
        self.gridLayout_2.addWidget(self.case_number_label, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(OviDialog)
        self.label_8.setGeometry(QtCore.QRect(20, 140, 87, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(OviDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 170, 528, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.refused_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.refused_checkbox.setObjectName("refused_checkbox")
        self.gridLayout.addWidget(self.refused_checkbox, 2, 0, 1, 2)
        self.ovi_in_20_years = QtWidgets.QComboBox(self.layoutWidget)
        self.ovi_in_20_years.setEnabled(False)
        self.ovi_in_20_years.setObjectName("ovi_in_20_years")
        self.ovi_in_20_years.addItem("")
        self.ovi_in_20_years.addItem("")
        self.ovi_in_20_years.addItem("")
        self.ovi_in_20_years.addItem("")
        self.ovi_in_20_years.addItem("")
        self.ovi_in_20_years.addItem("")
        self.ovi_in_20_years.addItem("")
        self.ovi_in_20_years.addItem("")
        self.ovi_in_20_years.addItem("")
        self.ovi_in_20_years.addItem("")
        self.gridLayout.addWidget(self.ovi_in_20_years, 2, 2, 1, 1)

        self.retranslateUi(OviDialog)
        self.pushButton_3.clicked.connect(OviDialog.reject)
        self.refused_checkbox.toggled['bool'].connect(OviDialog.set_dialog)
        self.continueButton.clicked.connect(OviDialog.proceed_to_sentencing)
        self.continueButton.released.connect(OviDialog.close_window)
        QtCore.QMetaObject.connectSlotsByName(OviDialog)
        OviDialog.setTabOrder(self.comboBox, self.checkBox)
        OviDialog.setTabOrder(self.checkBox, self.refused_checkbox)
        OviDialog.setTabOrder(self.refused_checkbox, self.ovi_in_20_years)
        OviDialog.setTabOrder(self.ovi_in_20_years, self.continueButton)
        OviDialog.setTabOrder(self.continueButton, self.pushButton_2)
        OviDialog.setTabOrder(self.pushButton_2, self.pushButton_3)

    def retranslateUi(self, OviDialog):
        _translate = QtCore.QCoreApplication.translate
        OviDialog.setWindowTitle(_translate("OviDialog", "Operating a Vehicle Impaired"))
        self.pushButton_2.setText(_translate("OviDialog", "Clear Fields"))
        self.pushButton_3.setText(_translate("OviDialog", "Cancel"))
        self.continueButton.setText(_translate("OviDialog", "Continue"))
        self.defendant_attorney_name_label.setText(_translate("OviDialog", "TextLabel"))
        self.defendant_name_label.setText(_translate("OviDialog", "TextLabel"))
        self.case_number_label.setText(_translate("OviDialog", "TextLabel"))
        self.label_8.setText(_translate("OviDialog", "OVI Details"))
        self.label_9.setText(_translate("OviDialog", "OVI Offenses in Past 10 Years: "))
        self.comboBox.setItemText(0, _translate("OviDialog", "1st"))
        self.comboBox.setItemText(1, _translate("OviDialog", "2nd"))
        self.comboBox.setItemText(2, _translate("OviDialog", "3rd"))
        self.comboBox.setItemText(3, _translate("OviDialog", "4th"))
        self.comboBox.setItemText(4, _translate("OviDialog", "5th"))
        self.comboBox.setItemText(5, _translate("OviDialog", "6th"))
        self.comboBox.setItemText(6, _translate("OviDialog", "7th"))
        self.comboBox.setItemText(7, _translate("OviDialog", "8th"))
        self.checkBox.setText(_translate("OviDialog", "High BAC Test"))
        self.refused_checkbox.setText(_translate("OviDialog", "Refused Breathylizer. Offenses in Past 20 Years:"))
        self.ovi_in_20_years.setItemText(0, _translate("OviDialog", "1st"))
        self.ovi_in_20_years.setItemText(1, _translate("OviDialog", "2nd"))
        self.ovi_in_20_years.setItemText(2, _translate("OviDialog", "3rd"))
        self.ovi_in_20_years.setItemText(3, _translate("OviDialog", "4th"))
        self.ovi_in_20_years.setItemText(4, _translate("OviDialog", "5th"))
        self.ovi_in_20_years.setItemText(5, _translate("OviDialog", "6th"))
        self.ovi_in_20_years.setItemText(6, _translate("OviDialog", "7th"))
        self.ovi_in_20_years.setItemText(7, _translate("OviDialog", "8th"))
        self.ovi_in_20_years.setItemText(8, _translate("OviDialog", "9th"))
        self.ovi_in_20_years.setItemText(9, _translate("OviDialog", "10th"))
