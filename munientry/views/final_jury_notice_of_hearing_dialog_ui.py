# Form implementation generated from reading ui file 'munientry/views/ui/FinalJuryNoticeOfHearingDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FinalJuryNoticeOfHearingDialog(object):
    def setupUi(self, FinalJuryNoticeOfHearingDialog):
        FinalJuryNoticeOfHearingDialog.setObjectName("FinalJuryNoticeOfHearingDialog")
        FinalJuryNoticeOfHearingDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        FinalJuryNoticeOfHearingDialog.resize(1088, 737)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FinalJuryNoticeOfHearingDialog.sizePolicy().hasHeightForWidth())
        FinalJuryNoticeOfHearingDialog.setSizePolicy(sizePolicy)
        FinalJuryNoticeOfHearingDialog.setMinimumSize(QtCore.QSize(0, 0))
        FinalJuryNoticeOfHearingDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        FinalJuryNoticeOfHearingDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        FinalJuryNoticeOfHearingDialog.setFont(font)
        FinalJuryNoticeOfHearingDialog.setToolTip("")
        FinalJuryNoticeOfHearingDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        FinalJuryNoticeOfHearingDialog.setSizeGripEnabled(True)
        FinalJuryNoticeOfHearingDialog.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(FinalJuryNoticeOfHearingDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_4 = QtWidgets.QFrame(FinalJuryNoticeOfHearingDialog)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1027, 704))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        self.gridLayout_10.addWidget(self.close_dialog_Button, 2, 0, 1, 1)
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_8)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_10.addWidget(self.create_entry_Button, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_8, 2, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(24)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.final_pretrial_time_box = NoScrollComboBox(self.frame_5)
        self.final_pretrial_time_box.setEnabled(True)
        self.final_pretrial_time_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.final_pretrial_time_box.setObjectName("final_pretrial_time_box")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.final_pretrial_time_box.addItem("")
        self.gridLayout_3.addWidget(self.final_pretrial_time_box, 6, 1, 1, 1)
        self.final_pretrial_time_label = QtWidgets.QLabel(self.frame_5)
        self.final_pretrial_time_label.setObjectName("final_pretrial_time_label")
        self.gridLayout_3.addWidget(self.final_pretrial_time_label, 6, 0, 1, 1)
        self.jury_trial_only_yes_radioButton = QtWidgets.QRadioButton(self.frame_5)
        self.jury_trial_only_yes_radioButton.setObjectName("jury_trial_only_yes_radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(FinalJuryNoticeOfHearingDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.jury_trial_only_yes_radioButton)
        self.gridLayout_3.addWidget(self.jury_trial_only_yes_radioButton, 4, 0, 1, 1)
        self.final_pretrial_date_label = QtWidgets.QLabel(self.frame_5)
        self.final_pretrial_date_label.setObjectName("final_pretrial_date_label")
        self.gridLayout_3.addWidget(self.final_pretrial_date_label, 5, 0, 1, 1)
        self.trial_dateEdit = NoScrollDateEdit(self.frame_5)
        self.trial_dateEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.trial_dateEdit.setCalendarPopup(True)
        self.trial_dateEdit.setObjectName("trial_dateEdit")
        self.gridLayout_3.addWidget(self.trial_dateEdit, 7, 1, 1, 1)
        self.final_pretrial_dateEdit = NoScrollDateEdit(self.frame_5)
        self.final_pretrial_dateEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.final_pretrial_dateEdit.setCalendarPopup(True)
        self.final_pretrial_dateEdit.setObjectName("final_pretrial_dateEdit")
        self.gridLayout_3.addWidget(self.final_pretrial_dateEdit, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1)
        self.instructions_label = QtWidgets.QLabel(self.frame_5)
        self.instructions_label.setObjectName("instructions_label")
        self.gridLayout_3.addWidget(self.instructions_label, 1, 0, 1, 2)
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
        self.jury_trial_only_no_radioButton = QtWidgets.QRadioButton(self.frame_5)
        self.jury_trial_only_no_radioButton.setChecked(True)
        self.jury_trial_only_no_radioButton.setObjectName("jury_trial_only_no_radioButton")
        self.buttonGroup.addButton(self.jury_trial_only_no_radioButton)
        self.gridLayout_3.addWidget(self.jury_trial_only_no_radioButton, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 8, 0, 1, 1)
        self.hearing_location_box = NoScrollComboBox(self.frame_5)
        self.hearing_location_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hearing_location_box.setObjectName("hearing_location_box")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.setItemText(0, "")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.addItem("")
        self.gridLayout_3.addWidget(self.hearing_location_box, 8, 1, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 2)
        self.gridLayout_3.setRowStretch(2, 2)
        self.gridLayout_3.setRowStretch(3, 2)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 1)
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
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 1, 3, 1, 1)
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
        self.defense_counsel_name_box = QtWidgets.QComboBox(self.case_name_Frame)
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
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(FinalJuryNoticeOfHearingDialog)
        QtCore.QMetaObject.connectSlotsByName(FinalJuryNoticeOfHearingDialog)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.final_pretrial_dateEdit, self.final_pretrial_time_box)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.final_pretrial_time_box, self.trial_dateEdit)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.trial_dateEdit, self.hearing_location_box)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.hearing_location_box, self.defendant_first_name_lineEdit)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.defendant_last_name_lineEdit, self.defense_counsel_name_box)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.defense_counsel_name_box, self.case_number_lineEdit)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.case_number_lineEdit, self.jury_trial_only_no_radioButton)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.jury_trial_only_no_radioButton, self.jury_trial_only_yes_radioButton)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.jury_trial_only_yes_radioButton, self.create_entry_Button)
        FinalJuryNoticeOfHearingDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, FinalJuryNoticeOfHearingDialog):
        _translate = QtCore.QCoreApplication.translate
        FinalJuryNoticeOfHearingDialog.setWindowTitle(_translate("FinalJuryNoticeOfHearingDialog", "Final and Jury Notice of Hearing Information"))
        self.close_dialog_Button.setText(_translate("FinalJuryNoticeOfHearingDialog", "Close Dialog"))
        self.create_entry_Button.setText(_translate("FinalJuryNoticeOfHearingDialog", "Open Entry"))
        self.label_8.setText(_translate("FinalJuryNoticeOfHearingDialog", "Jury Trial Only:"))
        self.final_pretrial_time_box.setItemText(0, _translate("FinalJuryNoticeOfHearingDialog", "1:00 PM"))
        self.final_pretrial_time_box.setItemText(1, _translate("FinalJuryNoticeOfHearingDialog", "1:15 PM"))
        self.final_pretrial_time_box.setItemText(2, _translate("FinalJuryNoticeOfHearingDialog", "1:30 PM"))
        self.final_pretrial_time_box.setItemText(3, _translate("FinalJuryNoticeOfHearingDialog", "1:45 PM"))
        self.final_pretrial_time_box.setItemText(4, _translate("FinalJuryNoticeOfHearingDialog", "2:00 PM"))
        self.final_pretrial_time_box.setItemText(5, _translate("FinalJuryNoticeOfHearingDialog", "2:15 PM"))
        self.final_pretrial_time_box.setItemText(6, _translate("FinalJuryNoticeOfHearingDialog", "2:30 PM"))
        self.final_pretrial_time_box.setItemText(7, _translate("FinalJuryNoticeOfHearingDialog", "2:45 PM"))
        self.final_pretrial_time_box.setItemText(8, _translate("FinalJuryNoticeOfHearingDialog", "3:00 PM"))
        self.final_pretrial_time_box.setItemText(9, _translate("FinalJuryNoticeOfHearingDialog", "3:15 PM"))
        self.final_pretrial_time_box.setItemText(10, _translate("FinalJuryNoticeOfHearingDialog", "3:30 PM"))
        self.final_pretrial_time_box.setItemText(11, _translate("FinalJuryNoticeOfHearingDialog", "3:45 PM"))
        self.final_pretrial_time_box.setItemText(12, _translate("FinalJuryNoticeOfHearingDialog", "4:00 PM"))
        self.final_pretrial_time_box.setItemText(13, _translate("FinalJuryNoticeOfHearingDialog", "4:15 PM"))
        self.final_pretrial_time_label.setText(_translate("FinalJuryNoticeOfHearingDialog", "Final Pretrial Time:"))
        self.jury_trial_only_yes_radioButton.setText(_translate("FinalJuryNoticeOfHearingDialog", "Yes"))
        self.final_pretrial_date_label.setText(_translate("FinalJuryNoticeOfHearingDialog", "Final Pretrial Date:"))
        self.label_4.setText(_translate("FinalJuryNoticeOfHearingDialog", "Jury Trial Date:"))
        self.instructions_label.setText(_translate("FinalJuryNoticeOfHearingDialog", "INSTRUCTIONS:"))
        self.label_5.setText(_translate("FinalJuryNoticeOfHearingDialog", "SCHEDULING INFORMATION"))
        self.jury_trial_only_no_radioButton.setText(_translate("FinalJuryNoticeOfHearingDialog", "No"))
        self.label_7.setText(_translate("FinalJuryNoticeOfHearingDialog", "Trial / Final Pretrial Location:"))
        self.hearing_location_box.setItemText(1, _translate("FinalJuryNoticeOfHearingDialog", "Courtroom A"))
        self.hearing_location_box.setItemText(2, _translate("FinalJuryNoticeOfHearingDialog", "Courtroom B"))
        self.hearing_location_box.setItemText(3, _translate("FinalJuryNoticeOfHearingDialog", "Courtroom C"))
        self.label.setText(_translate("FinalJuryNoticeOfHearingDialog", "Def. First Name:"))
        self.label_26.setText(_translate("FinalJuryNoticeOfHearingDialog", "Date:"))
        self.cancel_Button.setText(_translate("FinalJuryNoticeOfHearingDialog", "Cancel"))
        self.label_2.setText(_translate("FinalJuryNoticeOfHearingDialog", "Def. Last Name:"))
        self.label_3.setText(_translate("FinalJuryNoticeOfHearingDialog", "Case Number:"))
        self.clear_fields_case_Button.setText(_translate("FinalJuryNoticeOfHearingDialog", "Clear Fields"))
        self.label_24.setText(_translate("FinalJuryNoticeOfHearingDialog", "Def. Counsel:"))
        self.label_6.setText(_translate("FinalJuryNoticeOfHearingDialog", "CASE INFORMATION"))
from munientry.widgets.combo_boxes import NoScrollComboBox
from munientry.widgets.custom_widgets import NoScrollDateEdit
