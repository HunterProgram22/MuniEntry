# Form implementation generated from reading ui file './munientry/views/ui/DenyPrivilegesDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DenyPrivilegesDialog(object):
    def setupUi(self, DenyPrivilegesDialog):
        DenyPrivilegesDialog.setObjectName("DenyPrivilegesDialog")
        DenyPrivilegesDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        DenyPrivilegesDialog.resize(1209, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DenyPrivilegesDialog.sizePolicy().hasHeightForWidth())
        DenyPrivilegesDialog.setSizePolicy(sizePolicy)
        DenyPrivilegesDialog.setMinimumSize(QtCore.QSize(0, 0))
        DenyPrivilegesDialog.setMaximumSize(QtCore.QSize(2500, 3500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 61, 102))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        DenyPrivilegesDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        DenyPrivilegesDialog.setFont(font)
        DenyPrivilegesDialog.setToolTip("")
        DenyPrivilegesDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        DenyPrivilegesDialog.setSizeGripEnabled(True)
        DenyPrivilegesDialog.setModal(True)
        self.gridLayout_6 = QtWidgets.QGridLayout(DenyPrivilegesDialog)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_4 = QtWidgets.QFrame(DenyPrivilegesDialog)
        self.frame_4.setStyleSheet("background-color: rgb(29, 61, 102);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.scrollArea.setStyleSheet("background-color: rgb(107, 107, 107);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1169, 685))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.deny_privileges_radio_btn = QtWidgets.QRadioButton(self.frame)
        self.deny_privileges_radio_btn.setObjectName("deny_privileges_radio_btn")
        self.gridLayout_3.addWidget(self.deny_privileges_radio_btn, 1, 0, 1, 1)
        self.permit_test_radio_btn = QtWidgets.QRadioButton(self.frame)
        self.permit_test_radio_btn.setObjectName("permit_test_radio_btn")
        self.gridLayout_3.addWidget(self.permit_test_radio_btn, 5, 0, 1, 1)
        self.permit_renew_radio_btn = QtWidgets.QRadioButton(self.frame)
        self.permit_renew_radio_btn.setObjectName("permit_renew_radio_btn")
        self.gridLayout_3.addWidget(self.permit_renew_radio_btn, 6, 0, 1, 1)
        self.hard_time_check_box = QtWidgets.QCheckBox(self.frame)
        self.hard_time_check_box.setObjectName("hard_time_check_box")
        self.gridLayout_3.addWidget(self.hard_time_check_box, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)
        self.petition_incomplete_check_box = QtWidgets.QCheckBox(self.frame)
        self.petition_incomplete_check_box.setObjectName("petition_incomplete_check_box")
        self.gridLayout_3.addWidget(self.petition_incomplete_check_box, 4, 0, 1, 1)
        self.no_employer_info_check_box = QtWidgets.QCheckBox(self.frame)
        self.no_employer_info_check_box.setObjectName("no_employer_info_check_box")
        self.gridLayout_3.addWidget(self.no_employer_info_check_box, 3, 1, 1, 1)
        self.no_insurance_check_box = QtWidgets.QCheckBox(self.frame)
        self.no_insurance_check_box.setObjectName("no_insurance_check_box")
        self.gridLayout_3.addWidget(self.no_insurance_check_box, 3, 0, 1, 1)
        self.no_jurisdiction_check_box = QtWidgets.QCheckBox(self.frame)
        self.no_jurisdiction_check_box.setObjectName("no_jurisdiction_check_box")
        self.gridLayout_3.addWidget(self.no_jurisdiction_check_box, 2, 1, 1, 1)
        self.prohibited_activities_check_box = QtWidgets.QCheckBox(self.frame)
        self.prohibited_activities_check_box.setObjectName("prohibited_activities_check_box")
        self.gridLayout_3.addWidget(self.prohibited_activities_check_box, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 2)
        self.close_dialog_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(255, 96, 82);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_2.addWidget(self.close_dialog_Button, 3, 0, 1, 1)
        self.create_entry_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_2.addWidget(self.create_entry_Button, 3, 1, 1, 1)
        self.case_name_Frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.case_name_Frame.sizePolicy().hasHeightForWidth())
        self.case_name_Frame.setSizePolicy(sizePolicy)
        self.case_name_Frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.case_name_Frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.case_name_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.case_name_Frame.setLineWidth(2)
        self.case_name_Frame.setObjectName("case_name_Frame")
        self.gridLayout = QtWidgets.QGridLayout(self.case_name_Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 4, 4, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 4, 1, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 5)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 5, 4, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 3, 4, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(750, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 3, 2, 1, 2)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(DenyPrivilegesDialog)
        QtCore.QMetaObject.connectSlotsByName(DenyPrivilegesDialog)
        DenyPrivilegesDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)

    def retranslateUi(self, DenyPrivilegesDialog):
        _translate = QtCore.QCoreApplication.translate
        DenyPrivilegesDialog.setWindowTitle(_translate("DenyPrivilegesDialog", "Driving Privileges Information"))
        self.deny_privileges_radio_btn.setText(_translate("DenyPrivilegesDialog", "Deny Driving Privileges"))
        self.permit_test_radio_btn.setText(_translate("DenyPrivilegesDialog", "Permit Defendant to Test and/or Renew"))
        self.permit_renew_radio_btn.setText(_translate("DenyPrivilegesDialog", "Permit Defendant to Renew upon Expiration"))
        self.hard_time_check_box.setText(_translate("DenyPrivilegesDialog", "Not Eligible - Hard Time has not passed"))
        self.label_4.setText(_translate("DenyPrivilegesDialog", "DRIVING PRIVILEGES ENTRY TYPE"))
        self.petition_incomplete_check_box.setText(_translate("DenyPrivilegesDialog", "Petition is Incomplete and/or Illegible"))
        self.no_employer_info_check_box.setText(_translate("DenyPrivilegesDialog", "Court could not verify employer information"))
        self.no_insurance_check_box.setText(_translate("DenyPrivilegesDialog", "Failed to Provide Proof of Insurance"))
        self.no_jurisdiction_check_box.setText(_translate("DenyPrivilegesDialog", "License not subject to suspension for which this court may grant privileges"))
        self.prohibited_activities_check_box.setText(_translate("DenyPrivilegesDialog", "Petition requests privileges for activities not permitted by this Court"))
        self.close_dialog_Button.setText(_translate("DenyPrivilegesDialog", "Close Dialog"))
        self.create_entry_Button.setText(_translate("DenyPrivilegesDialog", "Open Entry"))
        self.label.setText(_translate("DenyPrivilegesDialog", "Def. First Name:"))
        self.clear_fields_case_Button.setText(_translate("DenyPrivilegesDialog", "Clear Fields"))
        self.label_2.setText(_translate("DenyPrivilegesDialog", "Def. Last Name:"))
        self.label_6.setText(_translate("DenyPrivilegesDialog", "CASE INFORMATION"))
        self.cancel_Button.setText(_translate("DenyPrivilegesDialog", "Cancel"))
        self.label_3.setText(_translate("DenyPrivilegesDialog", "Case Number:"))
        self.label_26.setText(_translate("DenyPrivilegesDialog", "Entry Date:"))
from munientry.widgets.custom_widgets import NoScrollDateEdit
