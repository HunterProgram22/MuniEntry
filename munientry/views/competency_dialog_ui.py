# Form implementation generated from reading ui file 'munientry/views/ui/CompetencyDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CompetencyDialog(object):
    def setupUi(self, CompetencyDialog):
        CompetencyDialog.setObjectName("CompetencyDialog")
        CompetencyDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        CompetencyDialog.setEnabled(True)
        CompetencyDialog.resize(988, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CompetencyDialog.sizePolicy().hasHeightForWidth())
        CompetencyDialog.setSizePolicy(sizePolicy)
        CompetencyDialog.setMinimumSize(QtCore.QSize(0, 0))
        CompetencyDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        CompetencyDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        CompetencyDialog.setFont(font)
        CompetencyDialog.setToolTip("")
        CompetencyDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        CompetencyDialog.setSizeGripEnabled(True)
        CompetencyDialog.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(CompetencyDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_4 = QtWidgets.QFrame(CompetencyDialog)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 948, 685))
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 2)
        self.final_pretrial_time_label = QtWidgets.QLabel(self.frame)
        self.final_pretrial_time_label.setObjectName("final_pretrial_time_label")
        self.gridLayout_3.addWidget(self.final_pretrial_time_label, 3, 0, 1, 1)
        self.hearing_location_box = NoScrollComboBox(self.frame)
        self.hearing_location_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hearing_location_box.setObjectName("hearing_location_box")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.setItemText(0, "")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.addItem("")
        self.gridLayout_3.addWidget(self.hearing_location_box, 5, 1, 1, 1)
        self.trial_date = NoScrollDateEdit(self.frame)
        self.trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.trial_date.setCalendarPopup(True)
        self.trial_date.setObjectName("trial_date")
        self.gridLayout_3.addWidget(self.trial_date, 4, 1, 1, 1)
        self.hearing_location_label = QtWidgets.QLabel(self.frame)
        self.hearing_location_label.setObjectName("hearing_location_label")
        self.gridLayout_3.addWidget(self.hearing_location_label, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.competency_determination_box = NoScrollComboBox(self.frame)
        self.competency_determination_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.competency_determination_box.setObjectName("competency_determination_box")
        self.competency_determination_box.addItem("")
        self.competency_determination_box.addItem("")
        self.competency_determination_box.addItem("")
        self.competency_determination_box.addItem("")
        self.competency_determination_box.addItem("")
        self.gridLayout_3.addWidget(self.competency_determination_box, 1, 1, 1, 1)
        self.final_pretrial_date = NoScrollDateEdit(self.frame)
        self.final_pretrial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.final_pretrial_date.setCalendarPopup(True)
        self.final_pretrial_date.setObjectName("final_pretrial_date")
        self.gridLayout_3.addWidget(self.final_pretrial_date, 2, 1, 1, 1)
        self.final_pretrial_time_box = NoScrollComboBox(self.frame)
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
        self.final_pretrial_time_box.addItem("")
        self.gridLayout_3.addWidget(self.final_pretrial_time_box, 3, 1, 1, 1)
        self.trial_date_label = QtWidgets.QLabel(self.frame)
        self.trial_date_label.setObjectName("trial_date_label")
        self.gridLayout_3.addWidget(self.trial_date_label, 4, 0, 1, 1)
        self.final_pretrial_date_label = QtWidgets.QLabel(self.frame)
        self.final_pretrial_date_label.setObjectName("final_pretrial_date_label")
        self.gridLayout_3.addWidget(self.final_pretrial_date_label, 2, 0, 1, 1)
        self.treatment_type_label = QtWidgets.QLabel(self.frame)
        self.treatment_type_label.setObjectName("treatment_type_label")
        self.gridLayout_3.addWidget(self.treatment_type_label, 6, 0, 1, 1)
        self.treatment_type_box = NoScrollComboBox(self.frame)
        self.treatment_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.treatment_type_box.setObjectName("treatment_type_box")
        self.treatment_type_box.addItem("")
        self.treatment_type_box.addItem("")
        self.gridLayout_3.addWidget(self.treatment_type_box, 6, 1, 1, 1)
        self.in_jail_label = QtWidgets.QLabel(self.frame)
        self.in_jail_label.setObjectName("in_jail_label")
        self.gridLayout_3.addWidget(self.in_jail_label, 7, 0, 1, 1)
        self.in_jail_box = NoScrollComboBox(self.frame)
        self.in_jail_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.in_jail_box.setObjectName("in_jail_box")
        self.in_jail_box.addItem("")
        self.in_jail_box.addItem("")
        self.gridLayout_3.addWidget(self.in_jail_box, 7, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 2)
        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setRowStretch(1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(CompetencyDialog)
        QtCore.QMetaObject.connectSlotsByName(CompetencyDialog)
        CompetencyDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        CompetencyDialog.setTabOrder(self.defendant_last_name_lineEdit, self.defense_counsel_name_box)
        CompetencyDialog.setTabOrder(self.defense_counsel_name_box, self.defense_counsel_type_box)
        CompetencyDialog.setTabOrder(self.defense_counsel_type_box, self.defense_counsel_waived_checkBox)
        CompetencyDialog.setTabOrder(self.defense_counsel_waived_checkBox, self.case_number_lineEdit)
        CompetencyDialog.setTabOrder(self.case_number_lineEdit, self.create_entry_Button)
        CompetencyDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, CompetencyDialog):
        _translate = QtCore.QCoreApplication.translate
        CompetencyDialog.setWindowTitle(_translate("CompetencyDialog", "Competency Entry Case Information"))
        self.label.setText(_translate("CompetencyDialog", "Def. First Name:"))
        self.defense_counsel_type_box.setItemText(0, _translate("CompetencyDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("CompetencyDialog", "Private Counsel"))
        self.label_2.setText(_translate("CompetencyDialog", "Def. Last Name:"))
        self.defense_counsel_waived_checkBox.setText(_translate("CompetencyDialog", "Defendant appeared without counsel"))
        self.label_26.setText(_translate("CompetencyDialog", "Date:"))
        self.label_3.setText(_translate("CompetencyDialog", "Case Number:"))
        self.cancel_Button.setText(_translate("CompetencyDialog", "Cancel"))
        self.clear_fields_case_Button.setText(_translate("CompetencyDialog", "Clear Fields"))
        self.label_24.setText(_translate("CompetencyDialog", "Def. Counsel:"))
        self.create_entry_Button.setText(_translate("CompetencyDialog", "Open Entry"))
        self.close_dialog_Button.setText(_translate("CompetencyDialog", "Close Dialog"))
        self.label_4.setText(_translate("CompetencyDialog", "DECISION"))
        self.final_pretrial_time_label.setText(_translate("CompetencyDialog", "Final Pretrial Time:"))
        self.hearing_location_box.setItemText(1, _translate("CompetencyDialog", "Courtroom A"))
        self.hearing_location_box.setItemText(2, _translate("CompetencyDialog", "Courtroom B"))
        self.hearing_location_box.setItemText(3, _translate("CompetencyDialog", "Courtroom C"))
        self.hearing_location_label.setText(_translate("CompetencyDialog", "Trial / Final Pretrial Location:"))
        self.label_5.setText(_translate("CompetencyDialog", "Competency Determination:"))
        self.competency_determination_box.setItemText(0, _translate("CompetencyDialog", "Found Competent"))
        self.competency_determination_box.setItemText(1, _translate("CompetencyDialog", "Found Competent - Not Insane"))
        self.competency_determination_box.setItemText(2, _translate("CompetencyDialog", "Not Competent - Not Restorable"))
        self.competency_determination_box.setItemText(3, _translate("CompetencyDialog", "Not Competent - Restorable"))
        self.competency_determination_box.setItemText(4, _translate("CompetencyDialog", "Not Restored to Competency - Dismiss"))
        self.final_pretrial_time_box.setItemText(0, _translate("CompetencyDialog", "8:00 AM"))
        self.final_pretrial_time_box.setItemText(1, _translate("CompetencyDialog", "8:15 AM"))
        self.final_pretrial_time_box.setItemText(2, _translate("CompetencyDialog", "8:30 AM"))
        self.final_pretrial_time_box.setItemText(3, _translate("CompetencyDialog", "8:45 AM"))
        self.final_pretrial_time_box.setItemText(4, _translate("CompetencyDialog", "9:00 AM"))
        self.final_pretrial_time_box.setItemText(5, _translate("CompetencyDialog", "9:15 AM"))
        self.final_pretrial_time_box.setItemText(6, _translate("CompetencyDialog", "9:30 AM"))
        self.final_pretrial_time_box.setItemText(7, _translate("CompetencyDialog", "9:45 AM"))
        self.final_pretrial_time_box.setItemText(8, _translate("CompetencyDialog", "10:00 AM"))
        self.final_pretrial_time_box.setItemText(9, _translate("CompetencyDialog", "10:15 AM"))
        self.final_pretrial_time_box.setItemText(10, _translate("CompetencyDialog", "10:30 AM"))
        self.final_pretrial_time_box.setItemText(11, _translate("CompetencyDialog", "10:45 AM"))
        self.final_pretrial_time_box.setItemText(12, _translate("CompetencyDialog", "11:00 AM"))
        self.final_pretrial_time_box.setItemText(13, _translate("CompetencyDialog", "11:15 AM"))
        self.final_pretrial_time_box.setItemText(14, _translate("CompetencyDialog", "11:30 AM"))
        self.final_pretrial_time_box.setItemText(15, _translate("CompetencyDialog", "1:00 PM"))
        self.final_pretrial_time_box.setItemText(16, _translate("CompetencyDialog", "1:15 PM"))
        self.final_pretrial_time_box.setItemText(17, _translate("CompetencyDialog", "1:30 PM"))
        self.final_pretrial_time_box.setItemText(18, _translate("CompetencyDialog", "1:45 PM"))
        self.final_pretrial_time_box.setItemText(19, _translate("CompetencyDialog", "2:00 PM"))
        self.final_pretrial_time_box.setItemText(20, _translate("CompetencyDialog", "2:15 PM"))
        self.final_pretrial_time_box.setItemText(21, _translate("CompetencyDialog", "2:30 PM"))
        self.final_pretrial_time_box.setItemText(22, _translate("CompetencyDialog", "2:45 PM"))
        self.final_pretrial_time_box.setItemText(23, _translate("CompetencyDialog", "3:00 PM"))
        self.final_pretrial_time_box.setItemText(24, _translate("CompetencyDialog", "3:15 PM"))
        self.final_pretrial_time_box.setItemText(25, _translate("CompetencyDialog", "3:30 PM"))
        self.final_pretrial_time_box.setItemText(26, _translate("CompetencyDialog", "3:45 PM"))
        self.final_pretrial_time_box.setItemText(27, _translate("CompetencyDialog", "4:00 PM"))
        self.final_pretrial_time_box.setItemText(28, _translate("CompetencyDialog", "4:15 PM"))
        self.trial_date_label.setText(_translate("CompetencyDialog", "Jury Trial Date:"))
        self.final_pretrial_date_label.setText(_translate("CompetencyDialog", "Final Pretrial Date:"))
        self.treatment_type_label.setText(_translate("CompetencyDialog", "Treatment Type:"))
        self.treatment_type_box.setItemText(0, _translate("CompetencyDialog", "inpatient"))
        self.treatment_type_box.setItemText(1, _translate("CompetencyDialog", "outpatient"))
        self.in_jail_label.setText(_translate("CompetencyDialog", "Defendant in Jail:"))
        self.in_jail_box.setItemText(0, _translate("CompetencyDialog", "Yes"))
        self.in_jail_box.setItemText(1, _translate("CompetencyDialog", "No"))
from munientry.widgets.combo_boxes import DefenseCounselComboBox, NoScrollComboBox
from munientry.widgets.custom_widgets import NoScrollDateEdit
