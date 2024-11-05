# Form implementation generated from reading ui file './views/ui/CriminalSealingDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CriminalSealingEntryDialog(object):
    def setupUi(self, CriminalSealingEntryDialog):
        CriminalSealingEntryDialog.setObjectName("CriminalSealingEntryDialog")
        CriminalSealingEntryDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        CriminalSealingEntryDialog.setEnabled(True)
        CriminalSealingEntryDialog.resize(1149, 835)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CriminalSealingEntryDialog.sizePolicy().hasHeightForWidth())
        CriminalSealingEntryDialog.setSizePolicy(sizePolicy)
        CriminalSealingEntryDialog.setMinimumSize(QtCore.QSize(0, 0))
        CriminalSealingEntryDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        CriminalSealingEntryDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        CriminalSealingEntryDialog.setFont(font)
        CriminalSealingEntryDialog.setToolTip("")
        CriminalSealingEntryDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        CriminalSealingEntryDialog.setSizeGripEnabled(True)
        CriminalSealingEntryDialog.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(CriminalSealingEntryDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_4 = QtWidgets.QFrame(CriminalSealingEntryDialog)
        self.frame_4.setStyleSheet("background-color: rgb(29, 61, 102);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.scrollArea.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1109, 795))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.defense_counsel_type_box = NoScrollComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 2, 3, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.defense_counsel_name_box = DefenseCounselComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 2, 1, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_8)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_10.addWidget(self.create_entry_Button, 0, 0, 1, 1)
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_8)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(255, 96, 82);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_10.addWidget(self.close_dialog_Button, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_8, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame)
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
        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 4)
        self.offense_line_edit = QtWidgets.QLineEdit(self.frame)
        self.offense_line_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.offense_line_edit.setObjectName("offense_line_edit")
        self.gridLayout_6.addWidget(self.offense_line_edit, 2, 1, 1, 3)
        self.fbi_number_line_edit = QtWidgets.QLineEdit(self.frame)
        self.fbi_number_line_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fbi_number_line_edit.setObjectName("fbi_number_line_edit")
        self.gridLayout_6.addWidget(self.fbi_number_line_edit, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 7, 0, 1, 1)
        self.state_response_box = NoScrollComboBox(self.frame)
        self.state_response_box.setMinimumSize(QtCore.QSize(0, 25))
        self.state_response_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.state_response_box.setObjectName("state_response_box")
        self.state_response_box.addItem("")
        self.state_response_box.addItem("")
        self.gridLayout_6.addWidget(self.state_response_box, 7, 1, 1, 1)
        self.seal_decision_box = NoScrollComboBox(self.frame)
        self.seal_decision_box.setMinimumSize(QtCore.QSize(0, 25))
        self.seal_decision_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.seal_decision_box.setObjectName("seal_decision_box")
        self.seal_decision_box.addItem("")
        self.seal_decision_box.addItem("")
        self.seal_decision_box.addItem("")
        self.gridLayout_6.addWidget(self.seal_decision_box, 8, 1, 1, 1)
        self.offense_date = NoScrollDateEdit(self.frame)
        self.offense_date.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.offense_date.setCalendarPopup(True)
        self.offense_date.setObjectName("offense_date")
        self.gridLayout_6.addWidget(self.offense_date, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 3, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 2, 0, 1, 1)
        self.bci_number_line_edit = QtWidgets.QLineEdit(self.frame)
        self.bci_number_line_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bci_number_line_edit.setObjectName("bci_number_line_edit")
        self.gridLayout_6.addWidget(self.bci_number_line_edit, 3, 1, 1, 1)
        self.sealing_type_box = NoScrollComboBox(self.frame)
        self.sealing_type_box.setMinimumSize(QtCore.QSize(0, 30))
        self.sealing_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sealing_type_box.setObjectName("sealing_type_box")
        self.sealing_type_box.addItem("")
        self.sealing_type_box.addItem("")
        self.sealing_type_box.addItem("")
        self.sealing_type_box.addItem("")
        self.sealing_type_box.addItem("")
        self.gridLayout_6.addWidget(self.sealing_type_box, 6, 1, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.gridLayout_6.addWidget(self.line, 5, 0, 1, 4)
        self.denial_reasons_label = QtWidgets.QLabel(self.frame)
        self.denial_reasons_label.setObjectName("denial_reasons_label")
        self.gridLayout_6.addWidget(self.denial_reasons_label, 9, 0, 1, 1)
        self.denial_reasons_text_box = QtWidgets.QPlainTextEdit(self.frame)
        self.denial_reasons_text_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.denial_reasons_text_box.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.denial_reasons_text_box.setLineWidth(2)
        self.denial_reasons_text_box.setObjectName("denial_reasons_text_box")
        self.gridLayout_6.addWidget(self.denial_reasons_text_box, 9, 1, 1, 3)
        self.date_of_birth = NoScrollDateEdit(self.frame)
        self.date_of_birth.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.date_of_birth.setCalendarPopup(True)
        self.date_of_birth.setObjectName("date_of_birth")
        self.gridLayout_6.addWidget(self.date_of_birth, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(CriminalSealingEntryDialog)
        QtCore.QMetaObject.connectSlotsByName(CriminalSealingEntryDialog)
        CriminalSealingEntryDialog.setTabOrder(self.bci_number_line_edit, self.fbi_number_line_edit)
        CriminalSealingEntryDialog.setTabOrder(self.fbi_number_line_edit, self.sealing_type_box)
        CriminalSealingEntryDialog.setTabOrder(self.sealing_type_box, self.state_response_box)
        CriminalSealingEntryDialog.setTabOrder(self.state_response_box, self.seal_decision_box)
        CriminalSealingEntryDialog.setTabOrder(self.seal_decision_box, self.denial_reasons_text_box)
        CriminalSealingEntryDialog.setTabOrder(self.denial_reasons_text_box, self.defendant_first_name_lineEdit)
        CriminalSealingEntryDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        CriminalSealingEntryDialog.setTabOrder(self.defendant_last_name_lineEdit, self.defense_counsel_name_box)
        CriminalSealingEntryDialog.setTabOrder(self.defense_counsel_name_box, self.defense_counsel_type_box)
        CriminalSealingEntryDialog.setTabOrder(self.defense_counsel_type_box, self.defense_counsel_waived_checkBox)
        CriminalSealingEntryDialog.setTabOrder(self.defense_counsel_waived_checkBox, self.offense_date)
        CriminalSealingEntryDialog.setTabOrder(self.offense_date, self.offense_line_edit)
        CriminalSealingEntryDialog.setTabOrder(self.offense_line_edit, self.case_number_lineEdit)
        CriminalSealingEntryDialog.setTabOrder(self.case_number_lineEdit, self.create_entry_Button)
        CriminalSealingEntryDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, CriminalSealingEntryDialog):
        _translate = QtCore.QCoreApplication.translate
        CriminalSealingEntryDialog.setWindowTitle(_translate("CriminalSealingEntryDialog", "Criminal Sealing Entry Case Information"))
        self.label.setText(_translate("CriminalSealingEntryDialog", "Def. First Name:"))
        self.defense_counsel_type_box.setItemText(0, _translate("CriminalSealingEntryDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("CriminalSealingEntryDialog", "Private Counsel"))
        self.label_2.setText(_translate("CriminalSealingEntryDialog", "Def. Last Name:"))
        self.defense_counsel_waived_checkBox.setText(_translate("CriminalSealingEntryDialog", "Defendant appeared without counsel"))
        self.label_26.setText(_translate("CriminalSealingEntryDialog", "Date:"))
        self.label_3.setText(_translate("CriminalSealingEntryDialog", "Case Number:"))
        self.cancel_Button.setText(_translate("CriminalSealingEntryDialog", "Cancel"))
        self.clear_fields_case_Button.setText(_translate("CriminalSealingEntryDialog", "Clear Fields"))
        self.label_24.setText(_translate("CriminalSealingEntryDialog", "Def. Counsel:"))
        self.create_entry_Button.setText(_translate("CriminalSealingEntryDialog", "Open Entry"))
        self.close_dialog_Button.setText(_translate("CriminalSealingEntryDialog", "Close Dialog"))
        self.label_4.setText(_translate("CriminalSealingEntryDialog", "DECISION"))
        self.label_5.setText(_translate("CriminalSealingEntryDialog", "Motion is:"))
        self.label_8.setText(_translate("CriminalSealingEntryDialog", "Offense Date:"))
        self.label_6.setText(_translate("CriminalSealingEntryDialog", "State of Ohio response to motion:"))
        self.state_response_box.setItemText(0, _translate("CriminalSealingEntryDialog", "did not oppose"))
        self.state_response_box.setItemText(1, _translate("CriminalSealingEntryDialog", "opposed"))
        self.seal_decision_box.setItemText(0, _translate("CriminalSealingEntryDialog", "Granted"))
        self.seal_decision_box.setItemText(1, _translate("CriminalSealingEntryDialog", "Denied - with reason"))
        self.seal_decision_box.setItemText(2, _translate("CriminalSealingEntryDialog", "Denied - ineligible"))
        self.label_10.setText(_translate("CriminalSealingEntryDialog", "FBI Number:"))
        self.label_9.setText(_translate("CriminalSealingEntryDialog", "BCI Number:"))
        self.label_7.setText(_translate("CriminalSealingEntryDialog", "Offenses:"))
        self.sealing_type_box.setItemText(0, _translate("CriminalSealingEntryDialog", "sealing of a conviction or bail forfeiture record pursuant to R.C. 2953.32"))
        self.sealing_type_box.setItemText(1, _translate("CriminalSealingEntryDialog", "sealing after a not guilty finding or dismissal pursuant to R.C. 2953.33"))
        self.sealing_type_box.setItemText(2, _translate("CriminalSealingEntryDialog", "expungement of firearms conviction pursuant to R.C. 2953.35"))
        self.sealing_type_box.setItemText(3, _translate("CriminalSealingEntryDialog", "expungement of conviction by victim of human trafficking pursuant to R.C. 2953.36"))
        self.sealing_type_box.setItemText(4, _translate("CriminalSealingEntryDialog", "expungement of record of not guilty finding or dismissed charges by vicitim of human trafficking pursuant to R.C. 2953.521"))
        self.label_11.setText(_translate("CriminalSealingEntryDialog", "Motion type:"))
        self.denial_reasons_label.setText(_translate("CriminalSealingEntryDialog", "Denial reasons:"))
        self.label_12.setText(_translate("CriminalSealingEntryDialog", "Date of Birth:"))
from munientry.widgets.combo_boxes import DefenseCounselComboBox, NoScrollComboBox
from munientry.widgets.custom_widgets import NoScrollDateEdit
