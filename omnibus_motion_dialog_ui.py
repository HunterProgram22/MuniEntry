# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/OmnibusMotionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OmnibusMotionDialog(object):
    def setupUi(self, OmnibusMotionDialog):
        OmnibusMotionDialog.setObjectName("OmnibusMotionDialog")
        OmnibusMotionDialog.resize(481, 617)
        self.layoutWidget = QtWidgets.QWidget(OmnibusMotionDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 48))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.CaseNo_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.CaseNo_lineEdit.setObjectName("CaseNo_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.CaseNo_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.DefendantName_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.DefendantName_lineEdit.setObjectName("DefendantName_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DefendantName_lineEdit)
        self.layoutWidget1 = QtWidgets.QWidget(OmnibusMotionDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(360, 10, 77, 147))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.line = QtWidgets.QFrame(OmnibusMotionDialog)
        self.line.setGeometry(QtCore.QRect(10, 260, 321, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(OmnibusMotionDialog)
        self.widget.setGeometry(QtCore.QRect(10, 70, 321, 262))
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.considerationDate_dateEdit = QtWidgets.QDateEdit(self.widget)
        self.considerationDate_dateEdit.setObjectName("considerationDate_dateEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.considerationDate_dateEdit)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.prosecutor_radioButton = QtWidgets.QRadioButton(self.widget)
        self.prosecutor_radioButton.setObjectName("prosecutor_radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(OmnibusMotionDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.prosecutor_radioButton)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.prosecutor_radioButton)
        self.defendant_radioButton = QtWidgets.QRadioButton(self.widget)
        self.defendant_radioButton.setObjectName("defendant_radioButton")
        self.buttonGroup.addButton(self.defendant_radioButton)
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.defendant_radioButton)
        self.widget1 = QtWidgets.QWidget(OmnibusMotionDialog)
        self.widget1.setGeometry(QtCore.QRect(10, 180, 321, 73))
        self.widget1.setObjectName("widget1")
        self.formLayout_3 = QtWidgets.QFormLayout(self.widget1)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.MotionDescription_textEdit = QtWidgets.QTextEdit(self.widget1)
        self.MotionDescription_textEdit.setObjectName("MotionDescription_textEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.MotionDescription_textEdit)
        self.widget2 = QtWidgets.QWidget(OmnibusMotionDialog)
        self.widget2.setGeometry(QtCore.QRect(10, 290, 321, 42))
        self.widget2.setObjectName("widget2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.widget2)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_6 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.motionGranted_radioButton = QtWidgets.QRadioButton(self.widget2)
        self.motionGranted_radioButton.setObjectName("motionGranted_radioButton")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(OmnibusMotionDialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.motionGranted_radioButton)
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.motionGranted_radioButton)
        self.motionDenied_radioButton = QtWidgets.QRadioButton(self.widget2)
        self.motionDenied_radioButton.setObjectName("motionDenied_radioButton")
        self.buttonGroup_2.addButton(self.motionDenied_radioButton)
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.motionDenied_radioButton)
        self.widget3 = QtWidgets.QWidget(OmnibusMotionDialog)
        self.widget3.setGeometry(QtCore.QRect(10, 350, 321, 131))
        self.widget3.setObjectName("widget3")
        self.formLayout_5 = QtWidgets.QFormLayout(self.widget3)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.widget3)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.DecisionReason_textEdit = QtWidgets.QTextEdit(self.widget3)
        self.DecisionReason_textEdit.setObjectName("DecisionReason_textEdit")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.DecisionReason_textEdit)

        self.retranslateUi(OmnibusMotionDialog)
        self.pushButton_3.clicked.connect(OmnibusMotionDialog.reject)
        self.pushButton_2.clicked.connect(self.CaseNo_lineEdit.clear)
        self.pushButton_2.clicked.connect(self.DefendantName_lineEdit.clear)
        self.pushButton.clicked.connect(OmnibusMotionDialog.createEntry)
        QtCore.QMetaObject.connectSlotsByName(OmnibusMotionDialog)
        OmnibusMotionDialog.setTabOrder(self.CaseNo_lineEdit, self.DefendantName_lineEdit)
        OmnibusMotionDialog.setTabOrder(self.DefendantName_lineEdit, self.considerationDate_dateEdit)
        OmnibusMotionDialog.setTabOrder(self.considerationDate_dateEdit, self.prosecutor_radioButton)
        OmnibusMotionDialog.setTabOrder(self.prosecutor_radioButton, self.defendant_radioButton)
        OmnibusMotionDialog.setTabOrder(self.defendant_radioButton, self.MotionDescription_textEdit)
        OmnibusMotionDialog.setTabOrder(self.MotionDescription_textEdit, self.motionGranted_radioButton)
        OmnibusMotionDialog.setTabOrder(self.motionGranted_radioButton, self.motionDenied_radioButton)
        OmnibusMotionDialog.setTabOrder(self.motionDenied_radioButton, self.checkBox)
        OmnibusMotionDialog.setTabOrder(self.checkBox, self.DecisionReason_textEdit)
        OmnibusMotionDialog.setTabOrder(self.DecisionReason_textEdit, self.pushButton)
        OmnibusMotionDialog.setTabOrder(self.pushButton, self.pushButton_2)
        OmnibusMotionDialog.setTabOrder(self.pushButton_2, self.pushButton_3)

    def retranslateUi(self, OmnibusMotionDialog):
        _translate = QtCore.QCoreApplication.translate
        OmnibusMotionDialog.setWindowTitle(_translate("OmnibusMotionDialog", "Omnibus Motion"))
        self.label.setText(_translate("OmnibusMotionDialog", "Case No."))
        self.label_2.setText(_translate("OmnibusMotionDialog", "Defendant Name: "))
        self.pushButton.setText(_translate("OmnibusMotionDialog", "Create Entry"))
        self.pushButton_2.setText(_translate("OmnibusMotionDialog", "Clear Fields"))
        self.pushButton_3.setText(_translate("OmnibusMotionDialog", "Cancel"))
        self.label_3.setText(_translate("OmnibusMotionDialog", "Consideration Date:"))
        self.label_4.setText(_translate("OmnibusMotionDialog", "Motion filed by:"))
        self.prosecutor_radioButton.setText(_translate("OmnibusMotionDialog", "Prosecutor"))
        self.defendant_radioButton.setText(_translate("OmnibusMotionDialog", "Defendant"))
        self.label_5.setText(_translate("OmnibusMotionDialog", "Motion description:"))
        self.label_6.setText(_translate("OmnibusMotionDialog", "Decision on Motion:"))
        self.motionGranted_radioButton.setText(_translate("OmnibusMotionDialog", "Granted"))
        self.motionDenied_radioButton.setText(_translate("OmnibusMotionDialog", "Denied"))
        self.checkBox.setText(_translate("OmnibusMotionDialog", "Include decision reason(s):"))
