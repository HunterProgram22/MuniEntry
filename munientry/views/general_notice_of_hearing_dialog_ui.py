# Form implementation generated from reading ui file 'munientry/views/ui/GeneralNoticeOfHearingDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GeneralNoticeOfHearingDialog(object):
    def setupUi(self, GeneralNoticeOfHearingDialog):
        GeneralNoticeOfHearingDialog.setObjectName("GeneralNoticeOfHearingDialog")
        GeneralNoticeOfHearingDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        GeneralNoticeOfHearingDialog.setEnabled(True)
        GeneralNoticeOfHearingDialog.resize(1088, 737)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GeneralNoticeOfHearingDialog.sizePolicy().hasHeightForWidth())
        GeneralNoticeOfHearingDialog.setSizePolicy(sizePolicy)
        GeneralNoticeOfHearingDialog.setMinimumSize(QtCore.QSize(0, 0))
        GeneralNoticeOfHearingDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        GeneralNoticeOfHearingDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        GeneralNoticeOfHearingDialog.setFont(font)
        GeneralNoticeOfHearingDialog.setToolTip("")
        GeneralNoticeOfHearingDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        GeneralNoticeOfHearingDialog.setSizeGripEnabled(True)
        GeneralNoticeOfHearingDialog.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(GeneralNoticeOfHearingDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_4 = QtWidgets.QFrame(GeneralNoticeOfHearingDialog)
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
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.hearing_date_label = QtWidgets.QLabel(self.frame_5)
        self.hearing_date_label.setObjectName("hearing_date_label")
        self.gridLayout_3.addWidget(self.hearing_date_label, 2, 0, 1, 1)
        self.hearing_dateEdit = NoScrollDateEdit(self.frame_5)
        self.hearing_dateEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.hearing_dateEdit.setCalendarPopup(True)
        self.hearing_dateEdit.setObjectName("hearing_dateEdit")
        self.gridLayout_3.addWidget(self.hearing_dateEdit, 2, 1, 1, 1)
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
        self.hearing_type_label = QtWidgets.QLabel(self.frame_5)
        self.hearing_type_label.setObjectName("hearing_type_label")
        self.gridLayout_3.addWidget(self.hearing_type_label, 1, 0, 1, 1)
        self.hearing_time_box = NoScrollComboBox(self.frame_5)
        self.hearing_time_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hearing_time_box.setObjectName("hearing_time_box")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.hearing_time_box.addItem("")
        self.gridLayout_3.addWidget(self.hearing_time_box, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)
        self.hearing_location_box = NoScrollComboBox(self.frame_5)
        self.hearing_location_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hearing_location_box.setObjectName("hearing_location_box")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.setItemText(0, "")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.addItem("")
        self.hearing_location_box.addItem("")
        self.gridLayout_3.addWidget(self.hearing_location_box, 4, 1, 1, 1)
        self.hearing_type_box = NoScrollComboBox(self.frame_5)
        self.hearing_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hearing_type_box.setEditable(False)
        self.hearing_type_box.setObjectName("hearing_type_box")
        self.hearing_type_box.addItem("")
        self.hearing_type_box.addItem("")
        self.hearing_type_box.addItem("")
        self.hearing_type_box.addItem("")
        self.hearing_type_box.addItem("")
        self.gridLayout_3.addWidget(self.hearing_type_box, 1, 1, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
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
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(GeneralNoticeOfHearingDialog)
        QtCore.QMetaObject.connectSlotsByName(GeneralNoticeOfHearingDialog)
        GeneralNoticeOfHearingDialog.setTabOrder(self.hearing_type_box, self.hearing_dateEdit)
        GeneralNoticeOfHearingDialog.setTabOrder(self.hearing_dateEdit, self.hearing_time_box)
        GeneralNoticeOfHearingDialog.setTabOrder(self.hearing_time_box, self.hearing_location_box)
        GeneralNoticeOfHearingDialog.setTabOrder(self.hearing_location_box, self.defendant_first_name_lineEdit)
        GeneralNoticeOfHearingDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        GeneralNoticeOfHearingDialog.setTabOrder(self.defendant_last_name_lineEdit, self.defense_counsel_name_box)
        GeneralNoticeOfHearingDialog.setTabOrder(self.defense_counsel_name_box, self.case_number_lineEdit)
        GeneralNoticeOfHearingDialog.setTabOrder(self.case_number_lineEdit, self.create_entry_Button)
        GeneralNoticeOfHearingDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, GeneralNoticeOfHearingDialog):
        _translate = QtCore.QCoreApplication.translate
        GeneralNoticeOfHearingDialog.setWindowTitle(_translate("GeneralNoticeOfHearingDialog", "General Notice of Hearing Information"))
        self.close_dialog_Button.setText(_translate("GeneralNoticeOfHearingDialog", "Close Dialog"))
        self.create_entry_Button.setText(_translate("GeneralNoticeOfHearingDialog", "Open Entry"))
        self.label_4.setText(_translate("GeneralNoticeOfHearingDialog", "Hearing Time:"))
        self.hearing_date_label.setText(_translate("GeneralNoticeOfHearingDialog", "Hearing Date:"))
        self.label_5.setText(_translate("GeneralNoticeOfHearingDialog", "SCHEDULING INFORMATION"))
        self.hearing_type_label.setText(_translate("GeneralNoticeOfHearingDialog", "Hearing Type:"))
        self.hearing_time_box.setItemText(0, _translate("GeneralNoticeOfHearingDialog", "8:00 AM"))
        self.hearing_time_box.setItemText(1, _translate("GeneralNoticeOfHearingDialog", "8:15 AM"))
        self.hearing_time_box.setItemText(2, _translate("GeneralNoticeOfHearingDialog", "8:30 AM"))
        self.hearing_time_box.setItemText(3, _translate("GeneralNoticeOfHearingDialog", "8:45 AM"))
        self.hearing_time_box.setItemText(4, _translate("GeneralNoticeOfHearingDialog", "9:00 AM"))
        self.hearing_time_box.setItemText(5, _translate("GeneralNoticeOfHearingDialog", "9:15 AM"))
        self.hearing_time_box.setItemText(6, _translate("GeneralNoticeOfHearingDialog", "9:30 AM"))
        self.hearing_time_box.setItemText(7, _translate("GeneralNoticeOfHearingDialog", "9:45 AM"))
        self.hearing_time_box.setItemText(8, _translate("GeneralNoticeOfHearingDialog", "10:00 AM"))
        self.hearing_time_box.setItemText(9, _translate("GeneralNoticeOfHearingDialog", "10:15 AM"))
        self.hearing_time_box.setItemText(10, _translate("GeneralNoticeOfHearingDialog", "10:30 AM"))
        self.hearing_time_box.setItemText(11, _translate("GeneralNoticeOfHearingDialog", "10:45 AM"))
        self.hearing_time_box.setItemText(12, _translate("GeneralNoticeOfHearingDialog", "11:00 AM"))
        self.hearing_time_box.setItemText(13, _translate("GeneralNoticeOfHearingDialog", "11:15 AM"))
        self.hearing_time_box.setItemText(14, _translate("GeneralNoticeOfHearingDialog", "11:30 AM"))
        self.hearing_time_box.setItemText(15, _translate("GeneralNoticeOfHearingDialog", "1:00 PM"))
        self.hearing_time_box.setItemText(16, _translate("GeneralNoticeOfHearingDialog", "1:15 PM"))
        self.hearing_time_box.setItemText(17, _translate("GeneralNoticeOfHearingDialog", "1:30 PM"))
        self.hearing_time_box.setItemText(18, _translate("GeneralNoticeOfHearingDialog", "1:45 PM"))
        self.hearing_time_box.setItemText(19, _translate("GeneralNoticeOfHearingDialog", "2:00 PM"))
        self.hearing_time_box.setItemText(20, _translate("GeneralNoticeOfHearingDialog", "2:15 PM"))
        self.hearing_time_box.setItemText(21, _translate("GeneralNoticeOfHearingDialog", "2:30 PM"))
        self.hearing_time_box.setItemText(22, _translate("GeneralNoticeOfHearingDialog", "2:45 PM"))
        self.hearing_time_box.setItemText(23, _translate("GeneralNoticeOfHearingDialog", "3:00 PM"))
        self.hearing_time_box.setItemText(24, _translate("GeneralNoticeOfHearingDialog", "3:15 PM"))
        self.hearing_time_box.setItemText(25, _translate("GeneralNoticeOfHearingDialog", "3:30 PM"))
        self.hearing_time_box.setItemText(26, _translate("GeneralNoticeOfHearingDialog", "3:45 PM"))
        self.hearing_time_box.setItemText(27, _translate("GeneralNoticeOfHearingDialog", "4:00 PM"))
        self.hearing_time_box.setItemText(28, _translate("GeneralNoticeOfHearingDialog", "4:15 PM"))
        self.label_7.setText(_translate("GeneralNoticeOfHearingDialog", "Hearing Location:"))
        self.hearing_location_box.setItemText(1, _translate("GeneralNoticeOfHearingDialog", "Courtroom A"))
        self.hearing_location_box.setItemText(2, _translate("GeneralNoticeOfHearingDialog", "Courtroom B"))
        self.hearing_location_box.setItemText(3, _translate("GeneralNoticeOfHearingDialog", "Courtroom C"))
        self.hearing_type_box.setItemText(0, _translate("GeneralNoticeOfHearingDialog", "Plea Hearing"))
        self.hearing_type_box.setItemText(1, _translate("GeneralNoticeOfHearingDialog", "Motion to Suppress Hearing"))
        self.hearing_type_box.setItemText(2, _translate("GeneralNoticeOfHearingDialog", "Oral Hearing"))
        self.hearing_type_box.setItemText(3, _translate("GeneralNoticeOfHearingDialog", "Seal Record"))
        self.hearing_type_box.setItemText(4, _translate("GeneralNoticeOfHearingDialog", "Motion Hearing"))
        self.label.setText(_translate("GeneralNoticeOfHearingDialog", "Def. First Name:"))
        self.label_26.setText(_translate("GeneralNoticeOfHearingDialog", "Date:"))
        self.cancel_Button.setText(_translate("GeneralNoticeOfHearingDialog", "Cancel"))
        self.label_2.setText(_translate("GeneralNoticeOfHearingDialog", "Def. Last Name:"))
        self.label_3.setText(_translate("GeneralNoticeOfHearingDialog", "Case Number:"))
        self.clear_fields_case_Button.setText(_translate("GeneralNoticeOfHearingDialog", "Clear Fields"))
        self.label_24.setText(_translate("GeneralNoticeOfHearingDialog", "Def. Counsel:"))
        self.label_6.setText(_translate("GeneralNoticeOfHearingDialog", "CASE INFORMATION"))
from munientry.widgets.combo_boxes import DefenseCounselComboBox, NoScrollComboBox
from munientry.widgets.custom_widgets import NoScrollDateEdit
