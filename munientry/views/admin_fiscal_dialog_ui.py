# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'munientry/views/ui/AdminFiscalDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminFiscalDialog(object):
    def setupUi(self, AdminFiscalDialog):
        AdminFiscalDialog.setObjectName("AdminFiscalDialog")
        AdminFiscalDialog.setWindowModality(QtCore.Qt.NonModal)
        AdminFiscalDialog.resize(1144, 798)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AdminFiscalDialog.sizePolicy().hasHeightForWidth())
        AdminFiscalDialog.setSizePolicy(sizePolicy)
        AdminFiscalDialog.setMinimumSize(QtCore.QSize(0, 0))
        AdminFiscalDialog.setMaximumSize(QtCore.QSize(2500, 3500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        AdminFiscalDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        AdminFiscalDialog.setFont(font)
        AdminFiscalDialog.setToolTip("")
        AdminFiscalDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        AdminFiscalDialog.setSizeGripEnabled(True)
        AdminFiscalDialog.setModal(True)
        self.gridLayout_6 = QtWidgets.QGridLayout(AdminFiscalDialog)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_4 = QtWidgets.QFrame(AdminFiscalDialog)
        self.frame_4.setStyleSheet("background-color: rgb(29, 61, 102);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setStyleSheet("background-color: rgb(107, 107, 107);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1104, 758))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.close_dialog_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(255, 96, 82);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_2.addWidget(self.close_dialog_Button, 3, 1, 1, 1)
        self.case_name_Frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_name_Frame.sizePolicy().hasHeightForWidth())
        self.case_name_Frame.setSizePolicy(sizePolicy)
        self.case_name_Frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.case_name_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_name_Frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.case_name_Frame.setLineWidth(2)
        self.case_name_Frame.setObjectName("case_name_Frame")
        self.gridLayout = QtWidgets.QGridLayout(self.case_name_Frame)
        self.gridLayout.setVerticalSpacing(24)
        self.gridLayout.setObjectName("gridLayout")
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 2, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 1, 3, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 1, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.account_number_box = QtWidgets.QComboBox(self.case_name_Frame)
        self.account_number_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.account_number_box.setObjectName("account_number_box")
        self.account_number_box.addItem("")
        self.account_number_box.setItemText(0, "")
        self.account_number_box.addItem("")
        self.account_number_box.addItem("")
        self.account_number_box.addItem("")
        self.account_number_box.addItem("")
        self.account_number_box.addItem("")
        self.gridLayout.addWidget(self.account_number_box, 1, 1, 1, 1)
        self.subaccount_number_box = QtWidgets.QComboBox(self.case_name_Frame)
        self.subaccount_number_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.subaccount_number_box.setObjectName("subaccount_number_box")
        self.subaccount_number_box.addItem("")
        self.subaccount_number_box.setItemText(0, "")
        self.subaccount_number_box.addItem("")
        self.subaccount_number_box.addItem("")
        self.subaccount_number_box.addItem("")
        self.subaccount_number_box.addItem("")
        self.subaccount_number_box.addItem("")
        self.gridLayout.addWidget(self.subaccount_number_box, 2, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.create_entry_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_2.addWidget(self.create_entry_Button, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.disbursement_amount_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.disbursement_amount_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.disbursement_amount_lineEdit.setObjectName("disbursement_amount_lineEdit")
        self.gridLayout_3.addWidget(self.disbursement_amount_lineEdit, 2, 1, 1, 1)
        self.disbursement_vendor_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.disbursement_vendor_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.disbursement_vendor_lineEdit.setObjectName("disbursement_vendor_lineEdit")
        self.gridLayout_3.addWidget(self.disbursement_vendor_lineEdit, 3, 1, 1, 1)
        self.disbursement_reason_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.disbursement_reason_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.disbursement_reason_lineEdit.setObjectName("disbursement_reason_lineEdit")
        self.gridLayout_3.addWidget(self.disbursement_reason_lineEdit, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.invoice_number_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.invoice_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.invoice_number_lineEdit.setObjectName("invoice_number_lineEdit")
        self.gridLayout_3.addWidget(self.invoice_number_lineEdit, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 2)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(AdminFiscalDialog)
        QtCore.QMetaObject.connectSlotsByName(AdminFiscalDialog)
        AdminFiscalDialog.setTabOrder(self.account_number_box, self.subaccount_number_box)
        AdminFiscalDialog.setTabOrder(self.subaccount_number_box, self.disbursement_reason_lineEdit)
        AdminFiscalDialog.setTabOrder(self.disbursement_reason_lineEdit, self.disbursement_amount_lineEdit)
        AdminFiscalDialog.setTabOrder(self.disbursement_amount_lineEdit, self.disbursement_vendor_lineEdit)
        AdminFiscalDialog.setTabOrder(self.disbursement_vendor_lineEdit, self.invoice_number_lineEdit)
        AdminFiscalDialog.setTabOrder(self.invoice_number_lineEdit, self.create_entry_Button)
        AdminFiscalDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, AdminFiscalDialog):
        _translate = QtCore.QCoreApplication.translate
        AdminFiscalDialog.setWindowTitle(_translate("AdminFiscalDialog", "Admin Fiscal Information"))
        self.close_dialog_Button.setText(_translate("AdminFiscalDialog", "Close Dialog"))
        self.clear_fields_case_Button.setText(_translate("AdminFiscalDialog", "Clear Fields"))
        self.label_26.setText(_translate("AdminFiscalDialog", "Entry Date:"))
        self.label_3.setText(_translate("AdminFiscalDialog", "Account Number:"))
        self.cancel_Button.setText(_translate("AdminFiscalDialog", "Cancel"))
        self.label_6.setText(_translate("AdminFiscalDialog", "ACCOUNT INFORMATION"))
        self.label.setText(_translate("AdminFiscalDialog", "SubAccount Number:"))
        self.account_number_box.setItemText(1, _translate("AdminFiscalDialog", "Indigent Alcohol Monitoring - 24115000"))
        self.account_number_box.setItemText(2, _translate("AdminFiscalDialog", "Indigent Alcohol Treatment - 25115000"))
        self.account_number_box.setItemText(3, _translate("AdminFiscalDialog", "Computer Legal Research - 25615000"))
        self.account_number_box.setItemText(4, _translate("AdminFiscalDialog", "Special Projects - 25715000"))
        self.account_number_box.setItemText(5, _translate("AdminFiscalDialog", "Probation - 25915000"))
        self.subaccount_number_box.setItemText(1, _translate("AdminFiscalDialog", "Data Processing - 522200"))
        self.subaccount_number_box.setItemText(2, _translate("AdminFiscalDialog", "Professional Services - 523100"))
        self.subaccount_number_box.setItemText(3, _translate("AdminFiscalDialog", "IDAM - 523160"))
        self.subaccount_number_box.setItemText(4, _translate("AdminFiscalDialog", "Operating Supplies - 533000"))
        self.subaccount_number_box.setItemText(5, _translate("AdminFiscalDialog", "Capital Outlay - 550300"))
        self.create_entry_Button.setText(_translate("AdminFiscalDialog", "Open Entry"))
        self.label_4.setText(_translate("AdminFiscalDialog", "Disbursement Amount:"))
        self.label_5.setText(_translate("AdminFiscalDialog", "Disbursed To:"))
        self.label_7.setText(_translate("AdminFiscalDialog", "PAYMENT INFORMATION"))
        self.label_2.setText(_translate("AdminFiscalDialog", "Disbursement Reason:"))
        self.label_8.setText(_translate("AdminFiscalDialog", "Invoice Number:"))
from munientry.widgets.custom_widgets import NoScrollDateEdit
