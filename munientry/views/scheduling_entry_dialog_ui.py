# Form implementation generated from reading ui file 'munientry/views/ui/SchedulingEntryDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SchedulingEntryDialog(object):
    def setupUi(self, SchedulingEntryDialog):
        SchedulingEntryDialog.setObjectName("SchedulingEntryDialog")
        SchedulingEntryDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        SchedulingEntryDialog.setEnabled(True)
        SchedulingEntryDialog.resize(1088, 737)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SchedulingEntryDialog.sizePolicy().hasHeightForWidth())
        SchedulingEntryDialog.setSizePolicy(sizePolicy)
        SchedulingEntryDialog.setMinimumSize(QtCore.QSize(0, 0))
        SchedulingEntryDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        SchedulingEntryDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        SchedulingEntryDialog.setFont(font)
        SchedulingEntryDialog.setToolTip("")
        SchedulingEntryDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        SchedulingEntryDialog.setSizeGripEnabled(True)
        SchedulingEntryDialog.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(SchedulingEntryDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_4 = QtWidgets.QFrame(SchedulingEntryDialog)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1027, 700))
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
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 2, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 2, 1, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 2, 4, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 1, 1, 1, 1)
        self.entry_date = NoScrollDateEdit(self.case_name_Frame)
        self.entry_date.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.entry_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.entry_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.entry_date.setCalendarPopup(True)
        self.entry_date.setDate(QtCore.QDate(2021, 1, 1))
        self.entry_date.setObjectName("entry_date")
        self.gridLayout.addWidget(self.entry_date, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 2, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 3, 0, 1, 1)
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
        self.defense_counsel_name_box = DefenseCounselComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 3, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 1, 0, 1, 1)
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
        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 2)
        self.arrest_summons_date = NoScrollDateEdit(self.frame_6)
        self.arrest_summons_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.arrest_summons_date.setCalendarPopup(True)
        self.arrest_summons_date.setObjectName("arrest_summons_date")
        self.gridLayout_6.addWidget(self.arrest_summons_date, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 3, 0, 1, 1)
        self.highest_charge_box = NoScrollComboBox(self.frame_6)
        self.highest_charge_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.highest_charge_box.setObjectName("highest_charge_box")
        self.highest_charge_box.addItem("")
        self.highest_charge_box.addItem("")
        self.highest_charge_box.addItem("")
        self.highest_charge_box.addItem("")
        self.highest_charge_box.addItem("")
        self.highest_charge_box.addItem("")
        self.gridLayout_6.addWidget(self.highest_charge_box, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_6)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_6.addWidget(self.line, 5, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 6, 0, 1, 1)
        self.speedy_trial_date_label = QtWidgets.QLabel(self.frame_6)
        self.speedy_trial_date_label.setObjectName("speedy_trial_date_label")
        self.gridLayout_6.addWidget(self.speedy_trial_date_label, 6, 1, 1, 1)
        self.days_in_jail_line = QtWidgets.QLineEdit(self.frame_6)
        self.days_in_jail_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.days_in_jail_line.setObjectName("days_in_jail_line")
        self.gridLayout_6.addWidget(self.days_in_jail_line, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 4, 0, 1, 1)
        self.continuance_days_line = QtWidgets.QLineEdit(self.frame_6)
        self.continuance_days_line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.continuance_days_line.setObjectName("continuance_days_line")
        self.gridLayout_6.addWidget(self.continuance_days_line, 4, 1, 1, 1)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.four_week_pretrial_radio_btn = QtWidgets.QRadioButton(self.frame_5)
        self.four_week_pretrial_radio_btn.setChecked(True)
        self.four_week_pretrial_radio_btn.setObjectName("four_week_pretrial_radio_btn")
        self.buttonGroup = QtWidgets.QButtonGroup(SchedulingEntryDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.four_week_pretrial_radio_btn)
        self.gridLayout_5.addWidget(self.four_week_pretrial_radio_btn, 2, 0, 1, 1)
        self.trial_date = NoScrollDateEdit(self.frame_5)
        self.trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.trial_date.setCalendarPopup(True)
        self.trial_date.setObjectName("trial_date")
        self.gridLayout_5.addWidget(self.trial_date, 9, 1, 1, 1)
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
        self.gridLayout_5.addWidget(self.label_5, 4, 0, 1, 2)
        self.three_week_pretrial_radio_btn = QtWidgets.QRadioButton(self.frame_5)
        self.three_week_pretrial_radio_btn.setObjectName("three_week_pretrial_radio_btn")
        self.buttonGroup.addButton(self.three_week_pretrial_radio_btn)
        self.gridLayout_5.addWidget(self.three_week_pretrial_radio_btn, 3, 0, 1, 1)
        self.no_pretrial_radio_btn = QtWidgets.QRadioButton(self.frame_5)
        self.no_pretrial_radio_btn.setObjectName("no_pretrial_radio_btn")
        self.buttonGroup.addButton(self.no_pretrial_radio_btn)
        self.gridLayout_5.addWidget(self.no_pretrial_radio_btn, 3, 1, 1, 1)
        self.two_week_pretrial_radio_btn = QtWidgets.QRadioButton(self.frame_5)
        self.two_week_pretrial_radio_btn.setObjectName("two_week_pretrial_radio_btn")
        self.buttonGroup.addButton(self.two_week_pretrial_radio_btn)
        self.gridLayout_5.addWidget(self.two_week_pretrial_radio_btn, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 9, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 2)
        self.final_pretrial_date = NoScrollDateEdit(self.frame_5)
        self.final_pretrial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.final_pretrial_date.setCalendarPopup(True)
        self.final_pretrial_date.setObjectName("final_pretrial_date")
        self.gridLayout_5.addWidget(self.final_pretrial_date, 7, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 7, 0, 1, 1)
        self.pretrial_date_label = QtWidgets.QLabel(self.frame_5)
        self.pretrial_date_label.setObjectName("pretrial_date_label")
        self.gridLayout_5.addWidget(self.pretrial_date_label, 6, 0, 1, 1)
        self.pretrial_date = NoScrollDateEdit(self.frame_5)
        self.pretrial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pretrial_date.setCalendarPopup(True)
        self.pretrial_date.setObjectName("pretrial_date")
        self.gridLayout_5.addWidget(self.pretrial_date, 6, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 8, 0, 1, 1)
        self.final_pretrial_time = NoScrollComboBox(self.frame_5)
        self.final_pretrial_time.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.final_pretrial_time.setObjectName("final_pretrial_time")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.final_pretrial_time.addItem("")
        self.gridLayout_5.addWidget(self.final_pretrial_time, 8, 1, 1, 1)
        self.interpreter_check_box = QtWidgets.QCheckBox(self.frame_5)
        self.interpreter_check_box.setObjectName("interpreter_check_box")
        self.gridLayout_5.addWidget(self.interpreter_check_box, 5, 0, 1, 1)
        self.language_box = QtWidgets.QLineEdit(self.frame_5)
        self.language_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.language_box.setObjectName("language_box")
        self.gridLayout_5.addWidget(self.language_box, 5, 1, 1, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)
        self.gridLayout_2.addWidget(self.frame_5, 2, 0, 1, 1)
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
        self.gridLayout_2.addWidget(self.frame_8, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(SchedulingEntryDialog)
        QtCore.QMetaObject.connectSlotsByName(SchedulingEntryDialog)
        SchedulingEntryDialog.setTabOrder(self.pretrial_date, self.final_pretrial_date)
        SchedulingEntryDialog.setTabOrder(self.final_pretrial_date, self.final_pretrial_time)
        SchedulingEntryDialog.setTabOrder(self.final_pretrial_time, self.trial_date)
        SchedulingEntryDialog.setTabOrder(self.trial_date, self.defendant_first_name_lineEdit)
        SchedulingEntryDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        SchedulingEntryDialog.setTabOrder(self.defendant_last_name_lineEdit, self.defense_counsel_name_box)
        SchedulingEntryDialog.setTabOrder(self.defense_counsel_name_box, self.case_number_lineEdit)
        SchedulingEntryDialog.setTabOrder(self.case_number_lineEdit, self.arrest_summons_date)
        SchedulingEntryDialog.setTabOrder(self.arrest_summons_date, self.highest_charge_box)
        SchedulingEntryDialog.setTabOrder(self.highest_charge_box, self.days_in_jail_line)
        SchedulingEntryDialog.setTabOrder(self.days_in_jail_line, self.continuance_days_line)
        SchedulingEntryDialog.setTabOrder(self.continuance_days_line, self.four_week_pretrial_radio_btn)
        SchedulingEntryDialog.setTabOrder(self.four_week_pretrial_radio_btn, self.three_week_pretrial_radio_btn)
        SchedulingEntryDialog.setTabOrder(self.three_week_pretrial_radio_btn, self.two_week_pretrial_radio_btn)
        SchedulingEntryDialog.setTabOrder(self.two_week_pretrial_radio_btn, self.no_pretrial_radio_btn)
        SchedulingEntryDialog.setTabOrder(self.no_pretrial_radio_btn, self.create_entry_Button)
        SchedulingEntryDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, SchedulingEntryDialog):
        _translate = QtCore.QCoreApplication.translate
        SchedulingEntryDialog.setWindowTitle(_translate("SchedulingEntryDialog", "Scheduling Entry Information"))
        self.label.setText(_translate("SchedulingEntryDialog", "Def. First Name:"))
        self.label_26.setText(_translate("SchedulingEntryDialog", "Date:"))
        self.cancel_Button.setText(_translate("SchedulingEntryDialog", "Cancel"))
        self.label_3.setText(_translate("SchedulingEntryDialog", "Case Number:"))
        self.clear_fields_case_Button.setText(_translate("SchedulingEntryDialog", "Clear Fields"))
        self.label_2.setText(_translate("SchedulingEntryDialog", "Def. Last Name:"))
        self.label_24.setText(_translate("SchedulingEntryDialog", "Def. Counsel:"))
        self.label_6.setText(_translate("SchedulingEntryDialog", "CASE INFORMATION"))
        self.label_12.setText(_translate("SchedulingEntryDialog", "Arrest or Summons Date:"))
        self.label_11.setText(_translate("SchedulingEntryDialog", "SPEEDY TRIAL CALCULATOR"))
        self.label_10.setText(_translate("SchedulingEntryDialog", "Days Spent in Jail (reduces speedy trial date 3 days per day in jail):"))
        self.highest_charge_box.setItemText(0, _translate("SchedulingEntryDialog", "M1"))
        self.highest_charge_box.setItemText(1, _translate("SchedulingEntryDialog", "M2"))
        self.highest_charge_box.setItemText(2, _translate("SchedulingEntryDialog", "M3"))
        self.highest_charge_box.setItemText(3, _translate("SchedulingEntryDialog", "M4"))
        self.highest_charge_box.setItemText(4, _translate("SchedulingEntryDialog", "MM"))
        self.highest_charge_box.setItemText(5, _translate("SchedulingEntryDialog", "UCM"))
        self.label_14.setText(_translate("SchedulingEntryDialog", "Highest Charge Degree of Offense:"))
        self.label_13.setText(_translate("SchedulingEntryDialog", "Defendant must be brought to trial no later than:"))
        self.speedy_trial_date_label.setText(_translate("SchedulingEntryDialog", "Speedy Trial Date"))
        self.label_15.setText(_translate("SchedulingEntryDialog", "Continuance Days (increases speedy trial date 1 day per continuance day):"))
        self.four_week_pretrial_radio_btn.setText(_translate("SchedulingEntryDialog", "Pretrial 4 weeks before trial"))
        self.label_5.setText(_translate("SchedulingEntryDialog", "SCHEDULED DATES"))
        self.three_week_pretrial_radio_btn.setText(_translate("SchedulingEntryDialog", "Pretrial 3 weeks before trial"))
        self.no_pretrial_radio_btn.setText(_translate("SchedulingEntryDialog", "No Pretrial"))
        self.two_week_pretrial_radio_btn.setText(_translate("SchedulingEntryDialog", "Pretrial 2 weeks before trial"))
        self.label_4.setText(_translate("SchedulingEntryDialog", "Jury Trial Date"))
        self.label_16.setText(_translate("SchedulingEntryDialog", "PRETRIAL TIME"))
        self.label_9.setText(_translate("SchedulingEntryDialog", "Final Pretrial Date:"))
        self.pretrial_date_label.setText(_translate("SchedulingEntryDialog", "Telephonic Pretrial Date:"))
        self.label_7.setText(_translate("SchedulingEntryDialog", "Final Pretrial Time:"))
        self.final_pretrial_time.setItemText(0, _translate("SchedulingEntryDialog", "8:00 AM"))
        self.final_pretrial_time.setItemText(1, _translate("SchedulingEntryDialog", "8:15 AM"))
        self.final_pretrial_time.setItemText(2, _translate("SchedulingEntryDialog", "8:30 AM"))
        self.final_pretrial_time.setItemText(3, _translate("SchedulingEntryDialog", "8:45 AM"))
        self.final_pretrial_time.setItemText(4, _translate("SchedulingEntryDialog", "9:00 AM"))
        self.final_pretrial_time.setItemText(5, _translate("SchedulingEntryDialog", "9:15 AM"))
        self.final_pretrial_time.setItemText(6, _translate("SchedulingEntryDialog", "9:30 AM"))
        self.final_pretrial_time.setItemText(7, _translate("SchedulingEntryDialog", "9:45 AM"))
        self.final_pretrial_time.setItemText(8, _translate("SchedulingEntryDialog", "10:00 AM"))
        self.final_pretrial_time.setItemText(9, _translate("SchedulingEntryDialog", "10:15 AM"))
        self.final_pretrial_time.setItemText(10, _translate("SchedulingEntryDialog", "10:30 AM"))
        self.final_pretrial_time.setItemText(11, _translate("SchedulingEntryDialog", "10:45 AM"))
        self.final_pretrial_time.setItemText(12, _translate("SchedulingEntryDialog", "11:00 AM"))
        self.final_pretrial_time.setItemText(13, _translate("SchedulingEntryDialog", "11:15 AM"))
        self.final_pretrial_time.setItemText(14, _translate("SchedulingEntryDialog", "11:30 AM"))
        self.final_pretrial_time.setItemText(15, _translate("SchedulingEntryDialog", "1:00 PM"))
        self.final_pretrial_time.setItemText(16, _translate("SchedulingEntryDialog", "1:15 PM"))
        self.final_pretrial_time.setItemText(17, _translate("SchedulingEntryDialog", "1:30 PM"))
        self.final_pretrial_time.setItemText(18, _translate("SchedulingEntryDialog", "1:45 PM"))
        self.final_pretrial_time.setItemText(19, _translate("SchedulingEntryDialog", "2:00 PM"))
        self.final_pretrial_time.setItemText(20, _translate("SchedulingEntryDialog", "2:15 PM"))
        self.final_pretrial_time.setItemText(21, _translate("SchedulingEntryDialog", "2:30 PM"))
        self.final_pretrial_time.setItemText(22, _translate("SchedulingEntryDialog", "2:45 PM"))
        self.final_pretrial_time.setItemText(23, _translate("SchedulingEntryDialog", "3:00 PM"))
        self.final_pretrial_time.setItemText(24, _translate("SchedulingEntryDialog", "3:15 PM"))
        self.final_pretrial_time.setItemText(25, _translate("SchedulingEntryDialog", "3:30 PM"))
        self.final_pretrial_time.setItemText(26, _translate("SchedulingEntryDialog", "3:45 PM"))
        self.final_pretrial_time.setItemText(27, _translate("SchedulingEntryDialog", "4:00 PM"))
        self.final_pretrial_time.setItemText(28, _translate("SchedulingEntryDialog", "4:15 PM"))
        self.interpreter_check_box.setText(_translate("SchedulingEntryDialog", "Interpreter Required"))
        self.language_box.setPlaceholderText(_translate("SchedulingEntryDialog", "Language Required"))
        self.close_dialog_Button.setText(_translate("SchedulingEntryDialog", "Close Dialog"))
        self.create_entry_Button.setText(_translate("SchedulingEntryDialog", "Open Entry"))
from munientry.widgets.combo_boxes import DefenseCounselComboBox, NoScrollComboBox
from munientry.widgets.custom_widgets import NoScrollDateEdit
