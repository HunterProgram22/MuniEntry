# Form implementation generated from reading ui file 'munientry/views/ui/TermsCommControlDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TermsCommControlDialog(object):
    def setupUi(self, TermsCommControlDialog):
        TermsCommControlDialog.setObjectName("TermsCommControlDialog")
        TermsCommControlDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        TermsCommControlDialog.setEnabled(True)
        TermsCommControlDialog.resize(988, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TermsCommControlDialog.sizePolicy().hasHeightForWidth())
        TermsCommControlDialog.setSizePolicy(sizePolicy)
        TermsCommControlDialog.setMinimumSize(QtCore.QSize(0, 0))
        TermsCommControlDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        TermsCommControlDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        TermsCommControlDialog.setFont(font)
        TermsCommControlDialog.setToolTip("")
        TermsCommControlDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        TermsCommControlDialog.setSizeGripEnabled(True)
        TermsCommControlDialog.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(TermsCommControlDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_4 = QtWidgets.QFrame(TermsCommControlDialog)
        self.frame_4.setStyleSheet("background-color: rgb(29, 61, 102);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.scrollArea.setStyleSheet("\n"
"background-color: rgb(116, 116, 116);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 932, 755))
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
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.entry_date = NoScrollDateEdit(self.case_name_Frame)
        self.entry_date.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.entry_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.entry_date.setCalendarPopup(True)
        self.entry_date.setObjectName("entry_date")
        self.gridLayout.addWidget(self.entry_date, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setStyleSheet("background-color: rgb(116, 116, 116);")
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
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.community_control_frame = QtWidgets.QFrame(self.frame)
        self.community_control_frame.setEnabled(True)
        self.community_control_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.community_control_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.community_control_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.community_control_frame.setObjectName("community_control_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.community_control_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.interlock_vehicles_check_box = ConditionCheckbox(self.community_control_frame)
        self.interlock_vehicles_check_box.setObjectName("interlock_vehicles_check_box")
        self.gridLayout_3.addWidget(self.interlock_vehicles_check_box, 17, 0, 1, 1)
        self.no_alcohol_ordered_check_box = QtWidgets.QCheckBox(self.community_control_frame)
        self.no_alcohol_ordered_check_box.setObjectName("no_alcohol_ordered_check_box")
        self.gridLayout_3.addWidget(self.no_alcohol_ordered_check_box, 13, 0, 1, 1)
        self.report_frequency_box = NoScrollComboBox(self.community_control_frame)
        self.report_frequency_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.report_frequency_box.setEditable(True)
        self.report_frequency_box.setObjectName("report_frequency_box")
        self.report_frequency_box.addItem("")
        self.report_frequency_box.setItemText(0, "")
        self.report_frequency_box.addItem("")
        self.report_frequency_box.addItem("")
        self.report_frequency_box.addItem("")
        self.gridLayout_3.addWidget(self.report_frequency_box, 3, 2, 1, 1)
        self.scram_days_box = NoScrollComboBox(self.community_control_frame)
        self.scram_days_box.setMinimumSize(QtCore.QSize(200, 0))
        self.scram_days_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scram_days_box.setEditable(True)
        self.scram_days_box.setObjectName("scram_days_box")
        self.scram_days_box.addItem("")
        self.scram_days_box.addItem("")
        self.scram_days_box.addItem("")
        self.scram_days_box.addItem("")
        self.scram_days_box.addItem("")
        self.scram_days_box.addItem("")
        self.scram_days_box.addItem("")
        self.gridLayout_3.addWidget(self.scram_days_box, 16, 0, 1, 1)
        self.specialized_docket_box = NoScrollComboBox(self.community_control_frame)
        self.specialized_docket_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.specialized_docket_box.setObjectName("specialized_docket_box")
        self.specialized_docket_box.addItem("")
        self.specialized_docket_box.addItem("")
        self.specialized_docket_box.addItem("")
        self.gridLayout_3.addWidget(self.specialized_docket_box, 26, 0, 1, 1)
        self.specialized_docket_check_box = ConditionCheckbox(self.community_control_frame)
        self.specialized_docket_check_box.setObjectName("specialized_docket_check_box")
        self.gridLayout_3.addWidget(self.specialized_docket_check_box, 25, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.community_control_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(190, 195, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 16, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.community_control_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(190, 195, 255);")
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 22, 0, 1, 1)
        self.pay_restitution_check_box = ConditionCheckbox(self.community_control_frame)
        self.pay_restitution_check_box.setObjectName("pay_restitution_check_box")
        self.gridLayout_3.addWidget(self.pay_restitution_check_box, 17, 2, 1, 1)
        self.community_service_hours_box = NoScrollComboBox(self.community_control_frame)
        self.community_service_hours_box.setMinimumSize(QtCore.QSize(200, 0))
        self.community_service_hours_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.community_service_hours_box.setEditable(True)
        self.community_service_hours_box.setObjectName("community_service_hours_box")
        self.community_service_hours_box.addItem("")
        self.community_service_hours_box.addItem("")
        self.community_service_hours_box.addItem("")
        self.community_service_hours_box.addItem("")
        self.community_service_hours_box.addItem("")
        self.gridLayout_3.addWidget(self.community_service_hours_box, 26, 2, 1, 1)
        self.community_service_check_box = ConditionCheckbox(self.community_control_frame)
        self.community_service_check_box.setObjectName("community_service_check_box")
        self.gridLayout_3.addWidget(self.community_service_check_box, 25, 2, 1, 1)
        self.cs_label = QtWidgets.QLabel(self.community_control_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cs_label.setFont(font)
        self.cs_label.setStyleSheet("background-color: rgb(190, 195, 255);")
        self.cs_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cs_label.setObjectName("cs_label")
        self.gridLayout_3.addWidget(self.cs_label, 22, 2, 1, 1)
        self.gps_exclusion_check_box = ConditionCheckbox(self.community_control_frame)
        self.gps_exclusion_check_box.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gps_exclusion_check_box.setObjectName("gps_exclusion_check_box")
        self.gridLayout_3.addWidget(self.gps_exclusion_check_box, 11, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.community_control_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(190, 195, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 12, 0, 1, 1)
        self.no_contact_with_box = QtWidgets.QLineEdit(self.community_control_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_contact_with_box.sizePolicy().hasHeightForWidth())
        self.no_contact_with_box.setSizePolicy(sizePolicy)
        self.no_contact_with_box.setMinimumSize(QtCore.QSize(200, 0))
        self.no_contact_with_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.no_contact_with_box.setObjectName("no_contact_with_box")
        self.gridLayout_3.addWidget(self.no_contact_with_box, 10, 0, 1, 1)
        self.scram_ordered_check_box = ConditionCheckbox(self.community_control_frame)
        self.scram_ordered_check_box.setObjectName("scram_ordered_check_box")
        self.gridLayout_3.addWidget(self.scram_ordered_check_box, 14, 0, 1, 1)
        self.no_contact_check_box = ConditionCheckbox(self.community_control_frame)
        self.no_contact_check_box.setObjectName("no_contact_check_box")
        self.gridLayout_3.addWidget(self.no_contact_check_box, 9, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.community_control_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(190, 195, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 8, 2, 1, 1)
        self.line_19 = QtWidgets.QFrame(self.community_control_frame)
        self.line_19.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_19.setObjectName("line_19")
        self.gridLayout_3.addWidget(self.line_19, 21, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.community_control_frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 21, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.community_control_frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 28, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.community_control_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 0, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.community_control_frame)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 7, 0, 1, 3)
        self.line_4 = QtWidgets.QFrame(self.community_control_frame)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 28, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.community_control_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(190, 195, 255);")
        self.label_9.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 8, 0, 1, 1)
        self.antitheft_check_box = ConditionCheckbox(self.community_control_frame)
        self.antitheft_check_box.setObjectName("antitheft_check_box")
        self.gridLayout_3.addWidget(self.antitheft_check_box, 9, 2, 1, 1)
        self.alcohol_treatment_check_box = ConditionCheckbox(self.community_control_frame)
        self.alcohol_treatment_check_box.setObjectName("alcohol_treatment_check_box")
        self.gridLayout_3.addWidget(self.alcohol_treatment_check_box, 11, 2, 1, 1)
        self.domestic_violence_program_check_box = ConditionCheckbox(self.community_control_frame)
        self.domestic_violence_program_check_box.setObjectName("domestic_violence_program_check_box")
        self.gridLayout_3.addWidget(self.domestic_violence_program_check_box, 12, 2, 1, 1)
        self.anger_management_check_box = ConditionCheckbox(self.community_control_frame)
        self.anger_management_check_box.setObjectName("anger_management_check_box")
        self.gridLayout_3.addWidget(self.anger_management_check_box, 10, 2, 1, 1)
        self.term_of_control_box = NoScrollComboBox(self.community_control_frame)
        self.term_of_control_box.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.term_of_control_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.term_of_control_box.setEditable(False)
        self.term_of_control_box.setObjectName("term_of_control_box")
        self.term_of_control_box.addItem("")
        self.term_of_control_box.addItem("")
        self.term_of_control_box.addItem("")
        self.term_of_control_box.addItem("")
        self.term_of_control_box.addItem("")
        self.term_of_control_box.addItem("")
        self.term_of_control_box.addItem("")
        self.gridLayout_3.addWidget(self.term_of_control_box, 1, 2, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.community_control_frame)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_3.addWidget(self.line_6, 8, 1, 22, 1)
        self.mental_health_treatment_check_box = ConditionCheckbox(self.community_control_frame)
        self.mental_health_treatment_check_box.setObjectName("mental_health_treatment_check_box")
        self.gridLayout_3.addWidget(self.mental_health_treatment_check_box, 14, 2, 1, 1)
        self.driver_intervention_program_check_box = ConditionCheckbox(self.community_control_frame)
        self.driver_intervention_program_check_box.setObjectName("driver_intervention_program_check_box")
        self.gridLayout_3.addWidget(self.driver_intervention_program_check_box, 13, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.community_control_frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.test = QtWidgets.QLabel(self.community_control_frame)
        self.test.setObjectName("test")
        self.gridLayout_3.addWidget(self.test, 1, 0, 1, 1)
        self.jail_report_date_box = NoScrollDateEdit(self.community_control_frame)
        self.jail_report_date_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.jail_report_date_box.setCalendarPopup(True)
        self.jail_report_date_box.setObjectName("jail_report_date_box")
        self.gridLayout_3.addWidget(self.jail_report_date_box, 4, 2, 1, 1)
        self.report_to_jail_check_box = QtWidgets.QCheckBox(self.community_control_frame)
        self.report_to_jail_check_box.setObjectName("report_to_jail_check_box")
        self.gridLayout_3.addWidget(self.report_to_jail_check_box, 4, 0, 1, 1)
        self.jail_report_time_box = NoScrollTimeEdit(self.community_control_frame)
        self.jail_report_time_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.jail_report_time_box.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.jail_report_time_box.setCalendarPopup(True)
        self.jail_report_time_box.setObjectName("jail_report_time_box")
        self.gridLayout_3.addWidget(self.jail_report_time_box, 5, 2, 1, 1)
        self.jail_days_box = QtWidgets.QLineEdit(self.community_control_frame)
        self.jail_days_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jail_days_box.setObjectName("jail_days_box")
        self.gridLayout_3.addWidget(self.jail_days_box, 6, 2, 1, 1)
        self.jail_days_serve_label = QtWidgets.QLabel(self.community_control_frame)
        self.jail_days_serve_label.setObjectName("jail_days_serve_label")
        self.gridLayout_3.addWidget(self.jail_days_serve_label, 6, 0, 1, 1)
        self.jail_report_time_label = QtWidgets.QLabel(self.community_control_frame)
        self.jail_report_time_label.setObjectName("jail_report_time_label")
        self.gridLayout_3.addWidget(self.jail_report_time_label, 5, 0, 1, 1)
        self.gridLayout_5.addWidget(self.community_control_frame, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(TermsCommControlDialog)
        QtCore.QMetaObject.connectSlotsByName(TermsCommControlDialog)
        TermsCommControlDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        TermsCommControlDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        TermsCommControlDialog.setTabOrder(self.case_number_lineEdit, self.create_entry_Button)
        TermsCommControlDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, TermsCommControlDialog):
        _translate = QtCore.QCoreApplication.translate
        TermsCommControlDialog.setWindowTitle(_translate("TermsCommControlDialog", "Terms of Community Control Case Information"))
        self.clear_fields_case_Button.setText(_translate("TermsCommControlDialog", "Clear Fields"))
        self.label_26.setText(_translate("TermsCommControlDialog", "Date:"))
        self.label_2.setText(_translate("TermsCommControlDialog", "Def. Last Name:"))
        self.cancel_Button.setText(_translate("TermsCommControlDialog", "Cancel"))
        self.label.setText(_translate("TermsCommControlDialog", "Def. First Name:"))
        self.label_3.setText(_translate("TermsCommControlDialog", "Case Number:"))
        self.create_entry_Button.setText(_translate("TermsCommControlDialog", "Open Entry"))
        self.close_dialog_Button.setText(_translate("TermsCommControlDialog", "Close Dialog"))
        self.interlock_vehicles_check_box.setText(_translate("TermsCommControlDialog", "Only operate vehicles with certified ignition interlock"))
        self.no_alcohol_ordered_check_box.setText(_translate("TermsCommControlDialog", "No Alcohol Conditions"))
        self.report_frequency_box.setItemText(1, _translate("TermsCommControlDialog", "daily (Monday through Friday)"))
        self.report_frequency_box.setItemText(2, _translate("TermsCommControlDialog", "every Monday"))
        self.report_frequency_box.setItemText(3, _translate("TermsCommControlDialog", "once a week (as ordered)"))
        self.scram_days_box.setItemText(0, _translate("TermsCommControlDialog", "15 days"))
        self.scram_days_box.setItemText(1, _translate("TermsCommControlDialog", "30 days"))
        self.scram_days_box.setItemText(2, _translate("TermsCommControlDialog", "45 days"))
        self.scram_days_box.setItemText(3, _translate("TermsCommControlDialog", "60 days"))
        self.scram_days_box.setItemText(4, _translate("TermsCommControlDialog", "75 days"))
        self.scram_days_box.setItemText(5, _translate("TermsCommControlDialog", "90 days"))
        self.scram_days_box.setItemText(6, _translate("TermsCommControlDialog", "180 days"))
        self.specialized_docket_box.setItemText(0, _translate("TermsCommControlDialog", "OVI Docket"))
        self.specialized_docket_box.setItemText(1, _translate("TermsCommControlDialog", "Mental Health Docket"))
        self.specialized_docket_box.setItemText(2, _translate("TermsCommControlDialog", "Mission (Veteran\'s) Court"))
        self.specialized_docket_check_box.setText(_translate("TermsCommControlDialog", "Agree to comply with terms of specialized docket:"))
        self.label_5.setText(_translate("TermsCommControlDialog", "Restitution"))
        self.label_16.setText(_translate("TermsCommControlDialog", "Specialized Dockets"))
        self.pay_restitution_check_box.setText(_translate("TermsCommControlDialog", "Pay Restitution as ordered by the Court   "))
        self.community_service_hours_box.setItemText(0, _translate("TermsCommControlDialog", "25 hours"))
        self.community_service_hours_box.setItemText(1, _translate("TermsCommControlDialog", "50 hours"))
        self.community_service_hours_box.setItemText(2, _translate("TermsCommControlDialog", "100 hours"))
        self.community_service_hours_box.setItemText(3, _translate("TermsCommControlDialog", "200 hours"))
        self.community_service_hours_box.setItemText(4, _translate("TermsCommControlDialog", "500 hours"))
        self.community_service_check_box.setText(_translate("TermsCommControlDialog", "Community Service required                                       "))
        self.cs_label.setText(_translate("TermsCommControlDialog", "Community Service"))
        self.gps_exclusion_check_box.setText(_translate("TermsCommControlDialog", "Comply with court ordered GPS Exclusion Zone"))
        self.label_8.setText(_translate("TermsCommControlDialog", "Drug/Alcohol Conditions"))
        self.no_contact_with_box.setPlaceholderText(_translate("TermsCommControlDialog", "No Contact Person(s) Name(s)"))
        self.scram_ordered_check_box.setText(_translate("TermsCommControlDialog", "Submit to continuous alcohol monitoring (SCRAM) for:"))
        self.no_contact_check_box.setText(_translate("TermsCommControlDialog", "No Contact with:                                                                                             "))
        self.label_6.setText(_translate("TermsCommControlDialog", "Treatment/Education "))
        self.label_25.setText(_translate("TermsCommControlDialog", "TERMS OF COMMUNITY CONTROL"))
        self.label_9.setText(_translate("TermsCommControlDialog", "Restrictions on Movement"))
        self.antitheft_check_box.setText(_translate("TermsCommControlDialog", "Complete Anti-theft/Shoplifting Program"))
        self.alcohol_treatment_check_box.setText(_translate("TermsCommControlDialog", "Comply with Alcohol/Drug Dependency Counseling and Treatment"))
        self.domestic_violence_program_check_box.setText(_translate("TermsCommControlDialog", "Complete Domestic Violence Offender Program"))
        self.anger_management_check_box.setText(_translate("TermsCommControlDialog", "Complete Anger Management Class"))
        self.term_of_control_box.setItemText(0, _translate("TermsCommControlDialog", "1 year"))
        self.term_of_control_box.setItemText(1, _translate("TermsCommControlDialog", "6 months"))
        self.term_of_control_box.setItemText(2, _translate("TermsCommControlDialog", "18 months"))
        self.term_of_control_box.setItemText(3, _translate("TermsCommControlDialog", "2 years"))
        self.term_of_control_box.setItemText(4, _translate("TermsCommControlDialog", "3 years"))
        self.term_of_control_box.setItemText(5, _translate("TermsCommControlDialog", "4 years"))
        self.term_of_control_box.setItemText(6, _translate("TermsCommControlDialog", "5 years"))
        self.mental_health_treatment_check_box.setText(_translate("TermsCommControlDialog", "Comply with Mental Health Counseling and Treatment"))
        self.driver_intervention_program_check_box.setText(_translate("TermsCommControlDialog", "Complete Driver Intervention Program "))
        self.label_4.setText(_translate("TermsCommControlDialog", "Report to Community Control in Person:"))
        self.test.setText(_translate("TermsCommControlDialog", "Term of Control:"))
        self.report_to_jail_check_box.setText(_translate("TermsCommControlDialog", "Report to Jail on:"))
        self.jail_days_box.setPlaceholderText(_translate("TermsCommControlDialog", "Jail Days"))
        self.jail_days_serve_label.setText(_translate("TermsCommControlDialog", "Jail Days to Serve:"))
        self.jail_report_time_label.setText(_translate("TermsCommControlDialog", "Report Time:"))
from munientry.widgets.combo_boxes import NoScrollComboBox
from munientry.widgets.custom_widgets import ConditionCheckbox, NoScrollDateEdit, NoScrollTimeEdit
