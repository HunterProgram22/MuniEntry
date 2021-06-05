# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\MotionEntryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MotionEntryDialog(object):
    def setupUi(self, MotionEntryDialog):
        MotionEntryDialog.setObjectName("MotionEntryDialog")
        MotionEntryDialog.resize(593, 522)
        self.layoutWidget_2 = QtWidgets.QWidget(MotionEntryDialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(470, 20, 95, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.layoutWidget = QtWidgets.QWidget(MotionEntryDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 390, 431, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.motion_decision_reasons = QtWidgets.QTextEdit(self.layoutWidget)
        self.motion_decision_reasons.setObjectName("motion_decision_reasons")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.motion_decision_reasons)
        self.layoutWidget1 = QtWidgets.QWidget(MotionEntryDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 431, 362))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.defendant_name = QtWidgets.QLineEdit(self.layoutWidget1)
        self.defendant_name.setObjectName("defendant_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.defendant_name)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.case_no = QtWidgets.QLineEdit(self.layoutWidget1)
        self.case_no.setObjectName("case_no")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.case_no)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.assigned_judge = QtWidgets.QComboBox(self.layoutWidget1)
        self.assigned_judge.setObjectName("assigned_judge")
        self.assigned_judge.addItem("")
        self.assigned_judge.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.assigned_judge)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.motion_filed_date = QtWidgets.QDateEdit(self.layoutWidget1)
        self.motion_filed_date.setCalendarPopup(True)
        self.motion_filed_date.setDate(QtCore.QDate(2021, 1, 1))
        self.motion_filed_date.setObjectName("motion_filed_date")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.motion_filed_date)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.motion_filed_by = QtWidgets.QComboBox(self.layoutWidget1)
        self.motion_filed_by.setObjectName("motion_filed_by")
        self.motion_filed_by.addItem("")
        self.motion_filed_by.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.motion_filed_by)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.motion_description = QtWidgets.QTextEdit(self.layoutWidget1)
        self.motion_description.setObjectName("motion_description")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.motion_description)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.motion_decision = QtWidgets.QComboBox(self.layoutWidget1)
        self.motion_decision.setObjectName("motion_decision")
        self.motion_decision.addItem("")
        self.motion_decision.addItem("")
        self.motion_decision.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.motion_decision)

        self.retranslateUi(MotionEntryDialog)
        self.pushButton.clicked.connect(MotionEntryDialog.create_entry)
        self.pushButton_2.clicked.connect(self.defendant_name.clear)
        self.pushButton_2.clicked.connect(self.case_no.clear)
        self.pushButton_3.clicked.connect(MotionEntryDialog.reject)
        self.pushButton_2.clicked.connect(self.motion_description.clear)
        self.pushButton_2.clicked.connect(self.motion_decision_reasons.clear)
        QtCore.QMetaObject.connectSlotsByName(MotionEntryDialog)
        MotionEntryDialog.setTabOrder(self.defendant_name, self.case_no)
        MotionEntryDialog.setTabOrder(self.case_no, self.motion_filed_date)
        MotionEntryDialog.setTabOrder(self.motion_filed_date, self.motion_filed_by)
        MotionEntryDialog.setTabOrder(self.motion_filed_by, self.motion_description)
        MotionEntryDialog.setTabOrder(self.motion_description, self.motion_decision)
        MotionEntryDialog.setTabOrder(self.motion_decision, self.pushButton)
        MotionEntryDialog.setTabOrder(self.pushButton, self.pushButton_2)
        MotionEntryDialog.setTabOrder(self.pushButton_2, self.pushButton_3)

    def retranslateUi(self, MotionEntryDialog):
        _translate = QtCore.QCoreApplication.translate
        MotionEntryDialog.setWindowTitle(_translate("MotionEntryDialog", "Dialog"))
        self.pushButton.setText(_translate("MotionEntryDialog", "Create Entry"))
        self.pushButton_2.setText(_translate("MotionEntryDialog", "Clear Fields"))
        self.pushButton_3.setText(_translate("MotionEntryDialog", "Cancel"))
        self.label_7.setText(_translate("MotionEntryDialog", "Reasons for Decision:"))
        self.label.setText(_translate("MotionEntryDialog", "Defendant Name:"))
        self.label_2.setText(_translate("MotionEntryDialog", "Case No.:"))
        self.label_8.setText(_translate("MotionEntryDialog", "Assigned Judge:"))
        self.assigned_judge.setItemText(0, _translate("MotionEntryDialog", "Judge Marianne Hemmeter"))
        self.assigned_judge.setItemText(1, _translate("MotionEntryDialog", "Judge Kyle Rohrer"))
        self.label_3.setText(_translate("MotionEntryDialog", "Motion filed date:"))
        self.label_4.setText(_translate("MotionEntryDialog", "Motion filed by:"))
        self.motion_filed_by.setItemText(0, _translate("MotionEntryDialog", "Prosecutor"))
        self.motion_filed_by.setItemText(1, _translate("MotionEntryDialog", "Defendant"))
        self.label_5.setText(_translate("MotionEntryDialog", "Motion description:"))
        self.label_6.setText(_translate("MotionEntryDialog", "Decision on Motion:"))
        self.motion_decision.setItemText(0, _translate("MotionEntryDialog", "Granted"))
        self.motion_decision.setItemText(1, _translate("MotionEntryDialog", "Denied"))
        self.motion_decision.setItemText(2, _translate("MotionEntryDialog", "Denied as moot"))
