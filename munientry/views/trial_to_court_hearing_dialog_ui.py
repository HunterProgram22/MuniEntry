# Form implementation generated from reading ui file 'munientry/views/ui/TrialToCourtHearingDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TrialToCourtHearingDialog(object):
    def setupUi(self, TrialToCourtHearingDialog):
        TrialToCourtHearingDialog.setObjectName("TrialToCourtHearingDialog")
        TrialToCourtHearingDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        TrialToCourtHearingDialog.setEnabled(True)
        TrialToCourtHearingDialog.resize(1088, 737)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TrialToCourtHearingDialog.sizePolicy().hasHeightForWidth())
        TrialToCourtHearingDialog.setSizePolicy(sizePolicy)
        TrialToCourtHearingDialog.setMinimumSize(QtCore.QSize(0, 0))
        TrialToCourtHearingDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        TrialToCourtHearingDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        TrialToCourtHearingDialog.setFont(font)
        TrialToCourtHearingDialog.setToolTip("")
        TrialToCourtHearingDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        TrialToCourtHearingDialog.setSizeGripEnabled(True)
        TrialToCourtHearingDialog.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(TrialToCourtHearingDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_4 = QtWidgets.QFrame(TrialToCourtHearingDialog)
        self.frame_4.setStyleSheet("background-color: rgb(29, 61, 102);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.scrollArea.setStyleSheet("background-color: rgb(12, 117, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1048, 697))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.days_in_jail_lineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.days_in_jail_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.days_in_jail_lineEdit.setObjectName("days_in_jail_lineEdit")
        self.gridLayout_7.addWidget(self.days_in_jail_lineEdit, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 4, 0, 1, 1)
        self.continuance_days_lineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.continuance_days_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.continuance_days_lineEdit.setObjectName("continuance_days_lineEdit")
        self.gridLayout_7.addWidget(self.continuance_days_lineEdit, 4, 1, 1, 1)
        self.arrest_summons_date_box = NoScrollDateEdit(self.frame_6)
        self.arrest_summons_date_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.arrest_summons_date_box.setCalendarPopup(True)
        self.arrest_summons_date_box.setObjectName("arrest_summons_date_box")
        self.gridLayout_7.addWidget(self.arrest_summons_date_box, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 3, 0, 1, 1)
        self.highest_charge_box = NoScrollComboBox(self.frame_6)
        self.highest_charge_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.highest_charge_box.setObjectName("highest_charge_box")
        self.highest_charge_box.addItem("")
        self.highest_charge_box.addItem("")
        self.gridLayout_7.addWidget(self.highest_charge_box, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 2, 0, 1, 1)
        self.speedy_trial_date_label = QtWidgets.QLabel(self.frame_6)
        self.speedy_trial_date_label.setObjectName("speedy_trial_date_label")
        self.gridLayout_7.addWidget(self.speedy_trial_date_label, 6, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_6)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_7.addWidget(self.line, 5, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 0, 0, 1, 2)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.gridLayout_2.addWidget(self.frame_6, 1, 0, 1, 2)
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
        self.gridLayout_5 = QtWidgets.QGridLayout(self.case_name_Frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(24)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 1, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 2, 1, 1)
        self.entry_date = NoScrollDateEdit(self.case_name_Frame)
        self.entry_date.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.entry_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.entry_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.entry_date.setCalendarPopup(True)
        self.entry_date.setDate(QtCore.QDate(2021, 1, 1))
        self.entry_date.setObjectName("entry_date")
        self.gridLayout.addWidget(self.entry_date, 1, 3, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 2, 3, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 2, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 3, 0, 1, 1)
        self.defense_counsel_name_box = DefenseCounselComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.case_name_Frame)
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
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.gridLayout_3.setVerticalSpacing(36)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.trial_dateEdit = NoScrollDateEdit(self.frame_5)
        self.trial_dateEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.trial_dateEdit.setCalendarPopup(True)
        self.trial_dateEdit.setObjectName("trial_dateEdit")
        self.gridLayout_3.addWidget(self.trial_dateEdit, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.trial_time_box = NoScrollComboBox(self.frame_5)
        self.trial_time_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.trial_time_box.setObjectName("trial_time_box")
        self.trial_time_box.addItem("")
        self.trial_time_box.addItem("")
        self.trial_time_box.addItem("")
        self.trial_time_box.addItem("")
        self.trial_time_box.addItem("")
        self.trial_time_box.addItem("")
        self.trial_time_box.addItem("")
        self.trial_time_box.addItem("")
        self.trial_time_box.addItem("")
        self.trial_time_box.addItem("")
        self.gridLayout_3.addWidget(self.trial_time_box, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.hearing_location_box = NoScrollComboBox(self.frame_5)
        self.hearing_location_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hearing_location_box.setObjectName("hearing_location_box")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.addItem("")
        self.gridLayout_3.addWidget(self.hearing_location_box, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 2)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 2)
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setStyleSheet("background-color: rgb(12, 117, 255);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_8)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(255, 96, 82);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_10.addWidget(self.close_dialog_Button, 1, 0, 1, 1)
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_8)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_10.addWidget(self.create_entry_Button, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_8, 3, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(TrialToCourtHearingDialog)
        QtCore.QMetaObject.connectSlotsByName(TrialToCourtHearingDialog)
        TrialToCourtHearingDialog.setTabOrder(self.trial_dateEdit, self.trial_time_box)
        TrialToCourtHearingDialog.setTabOrder(self.trial_time_box, self.hearing_location_box)
        TrialToCourtHearingDialog.setTabOrder(self.hearing_location_box, self.defendant_first_name_lineEdit)
        TrialToCourtHearingDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        TrialToCourtHearingDialog.setTabOrder(self.defendant_last_name_lineEdit, self.defense_counsel_name_box)
        TrialToCourtHearingDialog.setTabOrder(self.defense_counsel_name_box, self.case_number_lineEdit)

    def retranslateUi(self, TrialToCourtHearingDialog):
        _translate = QtCore.QCoreApplication.translate
        TrialToCourtHearingDialog.setWindowTitle(_translate("TrialToCourtHearingDialog", "Trial To Court Hearing Notice Information"))
        self.label_15.setText(_translate("TrialToCourtHearingDialog", "Continuance Days (increases speedy trial date 1 day per continuance day):"))
        self.label_10.setText(_translate("TrialToCourtHearingDialog", "Days Spent in Jail (reduces speedy trial date 3 days per day in jail):"))
        self.highest_charge_box.setItemText(0, _translate("TrialToCourtHearingDialog", "MM"))
        self.highest_charge_box.setItemText(1, _translate("TrialToCourtHearingDialog", "UCM"))
        self.label_14.setText(_translate("TrialToCourtHearingDialog", "Highest Charge Degree of Offense:"))
        self.speedy_trial_date_label.setText(_translate("TrialToCourtHearingDialog", "Speedy Trial Date"))
        self.label_13.setText(_translate("TrialToCourtHearingDialog", "Defendant must be brought to trial no later than:"))
        self.label_12.setText(_translate("TrialToCourtHearingDialog", "Arrest or Summons Date:"))
        self.label_11.setText(_translate("TrialToCourtHearingDialog", "SPEEDY TRIAL CALCULATOR"))
        self.label.setText(_translate("TrialToCourtHearingDialog", "Def. First Name:"))
        self.label_26.setText(_translate("TrialToCourtHearingDialog", "Date:"))
        self.cancel_Button.setText(_translate("TrialToCourtHearingDialog", "Cancel"))
        self.label_2.setText(_translate("TrialToCourtHearingDialog", "Def. Last Name:"))
        self.label_3.setText(_translate("TrialToCourtHearingDialog", "Case Number:"))
        self.clear_fields_case_Button.setText(_translate("TrialToCourtHearingDialog", "Clear Fields"))
        self.label_24.setText(_translate("TrialToCourtHearingDialog", "Def. Counsel:"))
        self.label_6.setText(_translate("TrialToCourtHearingDialog", "CASE INFORMATION"))
        self.label_4.setText(_translate("TrialToCourtHearingDialog", "Trial To Court Date:"))
        self.label_7.setText(_translate("TrialToCourtHearingDialog", "Trial To Court Time:"))
        self.trial_time_box.setItemText(0, _translate("TrialToCourtHearingDialog", "9:30 AM"))
        self.trial_time_box.setItemText(1, _translate("TrialToCourtHearingDialog", "10:00 AM"))
        self.trial_time_box.setItemText(2, _translate("TrialToCourtHearingDialog", "10:30 AM"))
        self.trial_time_box.setItemText(3, _translate("TrialToCourtHearingDialog", "11:00 AM"))
        self.trial_time_box.setItemText(4, _translate("TrialToCourtHearingDialog", "11:30 AM"))
        self.trial_time_box.setItemText(5, _translate("TrialToCourtHearingDialog", "1:00 PM"))
        self.trial_time_box.setItemText(6, _translate("TrialToCourtHearingDialog", "1:30 PM"))
        self.trial_time_box.setItemText(7, _translate("TrialToCourtHearingDialog", "2:00 PM"))
        self.trial_time_box.setItemText(8, _translate("TrialToCourtHearingDialog", "2:30 PM"))
        self.trial_time_box.setItemText(9, _translate("TrialToCourtHearingDialog", "3:00 PM"))
        self.label_8.setText(_translate("TrialToCourtHearingDialog", "Assigned Courtroom:"))
        self.hearing_location_box.setItemText(0, _translate("TrialToCourtHearingDialog", "Courtroom C"))
        self.hearing_location_box.setItemText(1, _translate("TrialToCourtHearingDialog", "Courtroom B"))
        self.hearing_location_box.setItemText(2, _translate("TrialToCourtHearingDialog", "Courtroom A"))
        self.label_5.setText(_translate("TrialToCourtHearingDialog", "SCHEDULED DATES"))
        self.close_dialog_Button.setText(_translate("TrialToCourtHearingDialog", "Close Dialog"))
        self.create_entry_Button.setText(_translate("TrialToCourtHearingDialog", "Open Entry"))
from munientry.widgets.combo_boxes import DefenseCounselComboBox, NoScrollComboBox
from munientry.widgets.custom_widgets import NoScrollDateEdit
