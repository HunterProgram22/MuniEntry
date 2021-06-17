# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AbilityToPayDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AbilityToPayDialog(object):
    def setupUi(self, AbilityToPayDialog):
        AbilityToPayDialog.setObjectName("AbilityToPayDialog")
        AbilityToPayDialog.resize(835, 609)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        AbilityToPayDialog.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(AbilityToPayDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 560, 191, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.case_information_frame = QtWidgets.QFrame(AbilityToPayDialog)
        self.case_information_frame.setGeometry(QtCore.QRect(10, 10, 661, 91))
        self.case_information_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_information_frame.setLineWidth(2)
        self.case_information_frame.setObjectName("case_information_frame")
        self.layoutWidget_2 = QtWidgets.QWidget(self.case_information_frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 641, 80))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.entry_name_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.entry_name_label.setFont(font)
        self.entry_name_label.setObjectName("entry_name_label")
        self.gridLayout_2.addWidget(self.entry_name_label, 0, 1, 1, 1)
        self.case_number_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.case_number_label.setFont(font)
        self.case_number_label.setObjectName("case_number_label")
        self.gridLayout_2.addWidget(self.case_number_label, 0, 0, 1, 1)
        self.defendant_name_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.defendant_name_label.setFont(font)
        self.defendant_name_label.setObjectName("defendant_name_label")
        self.gridLayout_2.addWidget(self.defendant_name_label, 1, 0, 1, 1)
        self.counsel_name_label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.counsel_name_label.setFont(font)
        self.counsel_name_label.setObjectName("counsel_name_label")
        self.gridLayout_2.addWidget(self.counsel_name_label, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(AbilityToPayDialog)
        self.frame.setGeometry(QtCore.QRect(10, 110, 781, 211))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 761, 196))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.offense_label_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.offense_label_1.setFont(font)
        self.offense_label_1.setWordWrap(True)
        self.offense_label_1.setObjectName("offense_label_1")
        self.gridLayout_3.addWidget(self.offense_label_1, 0, 0, 1, 1)
        self.plea_label_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.plea_label_1.setFont(font)
        self.plea_label_1.setObjectName("plea_label_1")
        self.gridLayout_3.addWidget(self.plea_label_1, 1, 0, 1, 1)
        self.finding_label_1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.finding_label_1.setFont(font)
        self.finding_label_1.setObjectName("finding_label_1")
        self.gridLayout_3.addWidget(self.finding_label_1, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 6, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.offense_1 = QtWidgets.QLabel(self.layoutWidget)
        self.offense_1.setText("")
        self.offense_1.setWordWrap(True)
        self.offense_1.setObjectName("offense_1")
        self.gridLayout_6.addWidget(self.offense_1, 0, 0, 1, 1)
        self.plea_1 = QtWidgets.QLabel(self.layoutWidget)
        self.plea_1.setText("")
        self.plea_1.setObjectName("plea_1")
        self.gridLayout_6.addWidget(self.plea_1, 1, 0, 1, 1)
        self.finding_1 = QtWidgets.QLabel(self.layoutWidget)
        self.finding_1.setText("")
        self.finding_1.setObjectName("finding_1")
        self.gridLayout_6.addWidget(self.finding_1, 2, 0, 1, 1)
        self.fines_1 = QtWidgets.QLabel(self.layoutWidget)
        self.fines_1.setText("")
        self.fines_1.setObjectName("fines_1")
        self.gridLayout_6.addWidget(self.fines_1, 3, 0, 1, 1)
        self.fines_suspended_1 = QtWidgets.QLabel(self.layoutWidget)
        self.fines_suspended_1.setText("")
        self.fines_suspended_1.setObjectName("fines_suspended_1")
        self.gridLayout_6.addWidget(self.fines_suspended_1, 4, 0, 1, 1)
        self.jail_days_1 = QtWidgets.QLabel(self.layoutWidget)
        self.jail_days_1.setText("")
        self.jail_days_1.setObjectName("jail_days_1")
        self.gridLayout_6.addWidget(self.jail_days_1, 5, 0, 1, 1)
        self.jail_days_suspended_1 = QtWidgets.QLabel(self.layoutWidget)
        self.jail_days_suspended_1.setText("")
        self.jail_days_suspended_1.setObjectName("jail_days_suspended_1")
        self.gridLayout_6.addWidget(self.jail_days_suspended_1, 6, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_6)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.offense_2 = QtWidgets.QLabel(self.layoutWidget)
        self.offense_2.setText("")
        self.offense_2.setWordWrap(True)
        self.offense_2.setObjectName("offense_2")
        self.gridLayout_7.addWidget(self.offense_2, 0, 0, 1, 1)
        self.plea_2 = QtWidgets.QLabel(self.layoutWidget)
        self.plea_2.setText("")
        self.plea_2.setObjectName("plea_2")
        self.gridLayout_7.addWidget(self.plea_2, 1, 0, 1, 1)
        self.finding_2 = QtWidgets.QLabel(self.layoutWidget)
        self.finding_2.setText("")
        self.finding_2.setObjectName("finding_2")
        self.gridLayout_7.addWidget(self.finding_2, 2, 0, 1, 1)
        self.fines_2 = QtWidgets.QLabel(self.layoutWidget)
        self.fines_2.setText("")
        self.fines_2.setObjectName("fines_2")
        self.gridLayout_7.addWidget(self.fines_2, 3, 0, 1, 1)
        self.fines_suspended_2 = QtWidgets.QLabel(self.layoutWidget)
        self.fines_suspended_2.setText("")
        self.fines_suspended_2.setObjectName("fines_suspended_2")
        self.gridLayout_7.addWidget(self.fines_suspended_2, 4, 0, 1, 1)
        self.jail_days_2 = QtWidgets.QLabel(self.layoutWidget)
        self.jail_days_2.setText("")
        self.jail_days_2.setObjectName("jail_days_2")
        self.gridLayout_7.addWidget(self.jail_days_2, 5, 0, 1, 1)
        self.jail_days_suspended_2 = QtWidgets.QLabel(self.layoutWidget)
        self.jail_days_suspended_2.setText("")
        self.jail_days_suspended_2.setObjectName("jail_days_suspended_2")
        self.gridLayout_7.addWidget(self.jail_days_suspended_2, 6, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_7)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.finding_3 = QtWidgets.QLabel(self.layoutWidget)
        self.finding_3.setText("")
        self.finding_3.setObjectName("finding_3")
        self.gridLayout_4.addWidget(self.finding_3, 2, 0, 1, 1)
        self.jail_days_suspended_3 = QtWidgets.QLabel(self.layoutWidget)
        self.jail_days_suspended_3.setText("")
        self.jail_days_suspended_3.setObjectName("jail_days_suspended_3")
        self.gridLayout_4.addWidget(self.jail_days_suspended_3, 6, 0, 1, 1)
        self.jail_days_3 = QtWidgets.QLabel(self.layoutWidget)
        self.jail_days_3.setText("")
        self.jail_days_3.setObjectName("jail_days_3")
        self.gridLayout_4.addWidget(self.jail_days_3, 5, 0, 1, 1)
        self.fines_suspended_3 = QtWidgets.QLabel(self.layoutWidget)
        self.fines_suspended_3.setText("")
        self.fines_suspended_3.setObjectName("fines_suspended_3")
        self.gridLayout_4.addWidget(self.fines_suspended_3, 4, 0, 1, 1)
        self.plea_3 = QtWidgets.QLabel(self.layoutWidget)
        self.plea_3.setText("")
        self.plea_3.setObjectName("plea_3")
        self.gridLayout_4.addWidget(self.plea_3, 1, 0, 1, 1)
        self.offense_3 = QtWidgets.QLabel(self.layoutWidget)
        self.offense_3.setText("")
        self.offense_3.setWordWrap(True)
        self.offense_3.setObjectName("offense_3")
        self.gridLayout_4.addWidget(self.offense_3, 0, 0, 1, 1)
        self.fines_3 = QtWidgets.QLabel(self.layoutWidget)
        self.fines_3.setText("")
        self.fines_3.setObjectName("fines_3")
        self.gridLayout_4.addWidget(self.fines_3, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.widget = QtWidgets.QWidget(AbilityToPayDialog)
        self.widget.setGeometry(QtCore.QRect(21, 350, 771, 126))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 3, 0, 1, 3)

        self.retranslateUi(AbilityToPayDialog)
        QtCore.QMetaObject.connectSlotsByName(AbilityToPayDialog)

    def retranslateUi(self, AbilityToPayDialog):
        _translate = QtCore.QCoreApplication.translate
        AbilityToPayDialog.setWindowTitle(_translate("AbilityToPayDialog", "Ability To Pay"))
        self.pushButton_2.setText(_translate("AbilityToPayDialog", "Continue"))
        self.entry_name_label.setText(_translate("AbilityToPayDialog", "TextLabel"))
        self.case_number_label.setText(_translate("AbilityToPayDialog", "TextLabel"))
        self.defendant_name_label.setText(_translate("AbilityToPayDialog", "TextLabel"))
        self.counsel_name_label.setText(_translate("AbilityToPayDialog", "TextLabel"))
        self.offense_label_1.setText(_translate("AbilityToPayDialog", "Offense:"))
        self.plea_label_1.setText(_translate("AbilityToPayDialog", "Plea:"))
        self.finding_label_1.setText(_translate("AbilityToPayDialog", "Finding:"))
        self.label_9.setText(_translate("AbilityToPayDialog", "Fines:"))
        self.label_10.setText(_translate("AbilityToPayDialog", "Fines Suspended:"))
        self.label_11.setText(_translate("AbilityToPayDialog", "Jail Days:"))
        self.label_12.setText(_translate("AbilityToPayDialog", "Jail Days Suspended:"))
        self.checkBox_3.setText(_translate("AbilityToPayDialog", "Community service approved for fines and costs."))
        self.comboBox.setItemText(1, _translate("AbilityToPayDialog", "30 Days"))
        self.comboBox.setItemText(2, _translate("AbilityToPayDialog", "60 Days"))
        self.comboBox.setItemText(3, _translate("AbilityToPayDialog", "90 Days"))
        self.checkBox.setText(_translate("AbilityToPayDialog", "Defendant claimed ability to pay in:"))
        self.checkBox_2.setText(_translate("AbilityToPayDialog", "All pretrial jail days served by Defendant not credited to jail sentence shall be applied to fines at $50/day."))
        self.checkBox_4.setText(_translate("AbilityToPayDialog", "Fines will be suspended contingent upon Defendant showing valid Operators License or Driving Privileges"))
