# Form implementation generated from reading ui file './views/ui/BondHearingDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BondHearingDialog(object):
    def setupUi(self, BondHearingDialog):
        BondHearingDialog.setObjectName("BondHearingDialog")
        BondHearingDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        BondHearingDialog.resize(1045, 791)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BondHearingDialog.sizePolicy().hasHeightForWidth())
        BondHearingDialog.setSizePolicy(sizePolicy)
        BondHearingDialog.setMinimumSize(QtCore.QSize(0, 0))
        BondHearingDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        BondHearingDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        BondHearingDialog.setFont(font)
        BondHearingDialog.setToolTip("")
        BondHearingDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        BondHearingDialog.setSizeGripEnabled(True)
        BondHearingDialog.setModal(True)
        self.gridLayout_8 = QtWidgets.QGridLayout(BondHearingDialog)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_4 = QtWidgets.QFrame(BondHearingDialog)
        self.frame_4.setStyleSheet("background-color: rgb(29, 61, 102);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1005, 751))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.bond_conditions_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.bond_conditions_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.bond_conditions_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.bond_conditions_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.bond_conditions_frame.setLineWidth(2)
        self.bond_conditions_frame.setObjectName("bond_conditions_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.bond_conditions_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.bond_conditions_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 2)
        self.alcohol_drugs_assessment_checkBox = ConditionCheckbox(self.bond_conditions_frame)
        self.alcohol_drugs_assessment_checkBox.setObjectName("alcohol_drugs_assessment_checkBox")
        self.gridLayout_2.addWidget(self.alcohol_drugs_assessment_checkBox, 3, 0, 1, 1)
        self.no_alcohol_drugs_checkBox = ConditionCheckbox(self.bond_conditions_frame)
        self.no_alcohol_drugs_checkBox.setObjectName("no_alcohol_drugs_checkBox")
        self.gridLayout_2.addWidget(self.no_alcohol_drugs_checkBox, 2, 0, 1, 1)
        self.monitoring_type_box = NoScrollComboBox(self.bond_conditions_frame)
        self.monitoring_type_box.setEnabled(True)
        self.monitoring_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.monitoring_type_box.setObjectName("monitoring_type_box")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.monitoring_type_box.addItem("")
        self.gridLayout_2.addWidget(self.monitoring_type_box, 7, 0, 1, 1)
        self.specialized_docket_type_box = NoScrollComboBox(self.bond_conditions_frame)
        self.specialized_docket_type_box.setEnabled(True)
        self.specialized_docket_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.specialized_docket_type_box.setObjectName("specialized_docket_type_box")
        self.specialized_docket_type_box.addItem("")
        self.specialized_docket_type_box.addItem("")
        self.specialized_docket_type_box.addItem("")
        self.gridLayout_2.addWidget(self.specialized_docket_type_box, 7, 1, 1, 1)
        self.specialized_docket_checkBox = ConditionCheckbox(self.bond_conditions_frame)
        self.specialized_docket_checkBox.setObjectName("specialized_docket_checkBox")
        self.gridLayout_2.addWidget(self.specialized_docket_checkBox, 6, 1, 1, 1)
        self.monitoring_checkBox = ConditionCheckbox(self.bond_conditions_frame)
        self.monitoring_checkBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.monitoring_checkBox.setObjectName("monitoring_checkBox")
        self.gridLayout_2.addWidget(self.monitoring_checkBox, 6, 0, 1, 1)
        self.mental_health_assessment_checkBox = ConditionCheckbox(self.bond_conditions_frame)
        self.mental_health_assessment_checkBox.setObjectName("mental_health_assessment_checkBox")
        self.gridLayout_2.addWidget(self.mental_health_assessment_checkBox, 3, 1, 1, 1)
        self.fingerprint_in_court_checkBox = ConditionCheckbox(self.bond_conditions_frame)
        self.fingerprint_in_court_checkBox.setObjectName("fingerprint_in_court_checkBox")
        self.gridLayout_2.addWidget(self.fingerprint_in_court_checkBox, 2, 1, 1, 1)
        self.comply_protection_order_checkBox = ConditionCheckbox(self.bond_conditions_frame)
        self.comply_protection_order_checkBox.setObjectName("comply_protection_order_checkBox")
        self.gridLayout_2.addWidget(self.comply_protection_order_checkBox, 8, 0, 1, 1)
        self.public_safety_suspension_checkBox = ConditionCheckbox(self.bond_conditions_frame)
        self.public_safety_suspension_checkBox.setObjectName("public_safety_suspension_checkBox")
        self.gridLayout_2.addWidget(self.public_safety_suspension_checkBox, 8, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_9.addWidget(self.bond_conditions_frame, 2, 0, 1, 2)
        self.bond_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.bond_frame.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.bond_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.bond_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.bond_frame.setLineWidth(2)
        self.bond_frame.setObjectName("bond_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.bond_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_8 = QtWidgets.QLabel(self.bond_frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)
        self.bond_amount_box = NoScrollComboBox(self.bond_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bond_amount_box.setFont(font)
        self.bond_amount_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bond_amount_box.setEditable(True)
        self.bond_amount_box.setObjectName("bond_amount_box")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.bond_amount_box.addItem("")
        self.gridLayout_5.addWidget(self.bond_amount_box, 2, 1, 1, 1)
        self.bond_type_box = NoScrollComboBox(self.bond_frame)
        self.bond_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bond_type_box.setObjectName("bond_type_box")
        self.bond_type_box.addItem("")
        self.bond_type_box.addItem("")
        self.bond_type_box.addItem("")
        self.gridLayout_5.addWidget(self.bond_type_box, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.bond_frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.bond_frame)
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
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 2)
        self.gridLayout_9.addWidget(self.bond_frame, 1, 0, 1, 2)
        self.special_bond_conditions_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.special_bond_conditions_frame.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-color: rgb(0, 0, 0);")
        self.special_bond_conditions_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.special_bond_conditions_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.special_bond_conditions_frame.setLineWidth(2)
        self.special_bond_conditions_frame.setObjectName("special_bond_conditions_frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.special_bond_conditions_frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.vehicle_seizure_checkBox = ConditionCheckbox(self.special_bond_conditions_frame)
        self.vehicle_seizure_checkBox.setObjectName("vehicle_seizure_checkBox")
        self.gridLayout_7.addWidget(self.vehicle_seizure_checkBox, 1, 1, 1, 1)
        self.admin_license_suspension_checkBox = ConditionCheckbox(self.special_bond_conditions_frame)
        self.admin_license_suspension_checkBox.setObjectName("admin_license_suspension_checkBox")
        self.gridLayout_7.addWidget(self.admin_license_suspension_checkBox, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.special_bond_conditions_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 2)
        self.domestic_violence_checkBox = ConditionCheckbox(self.special_bond_conditions_frame)
        self.domestic_violence_checkBox.setObjectName("domestic_violence_checkBox")
        self.gridLayout_7.addWidget(self.domestic_violence_checkBox, 1, 0, 1, 1)
        self.custodial_supervision_checkBox = ConditionCheckbox(self.special_bond_conditions_frame)
        self.custodial_supervision_checkBox.setObjectName("custodial_supervision_checkBox")
        self.gridLayout_7.addWidget(self.custodial_supervision_checkBox, 3, 0, 1, 1)
        self.no_contact_checkBox = ConditionCheckbox(self.special_bond_conditions_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_contact_checkBox.sizePolicy().hasHeightForWidth())
        self.no_contact_checkBox.setSizePolicy(sizePolicy)
        self.no_contact_checkBox.setObjectName("no_contact_checkBox")
        self.gridLayout_7.addWidget(self.no_contact_checkBox, 2, 1, 1, 1)
        self.other_conditions_checkBox = ConditionCheckbox(self.special_bond_conditions_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.other_conditions_checkBox.sizePolicy().hasHeightForWidth())
        self.other_conditions_checkBox.setSizePolicy(sizePolicy)
        self.other_conditions_checkBox.setObjectName("other_conditions_checkBox")
        self.gridLayout_7.addWidget(self.other_conditions_checkBox, 3, 1, 1, 1)
        self.add_special_conditions_Button = QtWidgets.QPushButton(self.special_bond_conditions_frame)
        self.add_special_conditions_Button.setStyleSheet("background-color: rgb(62, 146, 255);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.add_special_conditions_Button.setAutoDefault(False)
        self.add_special_conditions_Button.setObjectName("add_special_conditions_Button")
        self.gridLayout_7.addWidget(self.add_special_conditions_Button, 4, 0, 1, 2)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.gridLayout_7.setColumnStretch(1, 1)
        self.gridLayout_9.addWidget(self.special_bond_conditions_frame, 3, 0, 1, 1)
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
        self.appearance_reason_box = NoScrollComboBox(self.case_name_Frame)
        self.appearance_reason_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.appearance_reason_box.setEditable(True)
        self.appearance_reason_box.setObjectName("appearance_reason_box")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.gridLayout.addWidget(self.appearance_reason_box, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.bond_modification_decision_box = NoScrollComboBox(self.case_name_Frame)
        self.bond_modification_decision_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bond_modification_decision_box.setObjectName("bond_modification_decision_box")
        self.bond_modification_decision_box.addItem("")
        self.bond_modification_decision_box.setItemText(0, "")
        self.bond_modification_decision_box.addItem("")
        self.bond_modification_decision_box.addItem("")
        self.bond_modification_decision_box.addItem("")
        self.bond_modification_decision_box.addItem("")
        self.gridLayout.addWidget(self.bond_modification_decision_box, 5, 1, 1, 1)
        self.defense_counsel_type_box = NoScrollComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 2, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.defense_counsel_name_box = DefenseCounselComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setEnabled(True)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 2, 1, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 2, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.case_name_Frame)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 5)
        self.gridLayout_9.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setStyleSheet("\n"
"background-color: rgb(255, 255, 127);")
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
        self.gridLayout_9.addWidget(self.frame_8, 3, 1, 1, 1)
        self.gridLayout_9.setColumnStretch(0, 2)
        self.gridLayout_9.setColumnStretch(1, 1)
        self.gridLayout_9.setRowStretch(0, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(BondHearingDialog)
        QtCore.QMetaObject.connectSlotsByName(BondHearingDialog)
        BondHearingDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        BondHearingDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        BondHearingDialog.setTabOrder(self.case_number_lineEdit, self.bond_type_box)
        BondHearingDialog.setTabOrder(self.bond_type_box, self.bond_amount_box)
        BondHearingDialog.setTabOrder(self.bond_amount_box, self.domestic_violence_checkBox)
        BondHearingDialog.setTabOrder(self.domestic_violence_checkBox, self.admin_license_suspension_checkBox)
        BondHearingDialog.setTabOrder(self.admin_license_suspension_checkBox, self.custodial_supervision_checkBox)
        BondHearingDialog.setTabOrder(self.custodial_supervision_checkBox, self.vehicle_seizure_checkBox)
        BondHearingDialog.setTabOrder(self.vehicle_seizure_checkBox, self.no_contact_checkBox)
        BondHearingDialog.setTabOrder(self.no_contact_checkBox, self.other_conditions_checkBox)
        BondHearingDialog.setTabOrder(self.other_conditions_checkBox, self.add_special_conditions_Button)
        BondHearingDialog.setTabOrder(self.add_special_conditions_Button, self.create_entry_Button)
        BondHearingDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)

    def retranslateUi(self, BondHearingDialog):
        _translate = QtCore.QCoreApplication.translate
        BondHearingDialog.setWindowTitle(_translate("BondHearingDialog", "Bond Hearing Case Information"))
        self.label_7.setText(_translate("BondHearingDialog", "BOND CONDITIONS"))
        self.alcohol_drugs_assessment_checkBox.setText(_translate("BondHearingDialog", " Obtain alcohol/drug assessment                             "))
        self.no_alcohol_drugs_checkBox.setText(_translate("BondHearingDialog", " No alcohol/drugs of abuse                                   "))
        self.monitoring_type_box.setItemText(0, _translate("BondHearingDialog", "SCRAM - Court Pay"))
        self.monitoring_type_box.setItemText(1, _translate("BondHearingDialog", "SCRAM"))
        self.monitoring_type_box.setItemText(2, _translate("BondHearingDialog", "GPS"))
        self.monitoring_type_box.setItemText(3, _translate("BondHearingDialog", "Smart Start"))
        self.monitoring_type_box.setItemText(4, _translate("BondHearingDialog", "GPS and SCRAM"))
        self.monitoring_type_box.setItemText(5, _translate("BondHearingDialog", "GPS and Smart Start"))
        self.monitoring_type_box.setItemText(6, _translate("BondHearingDialog", "SCRAM and Smart Start"))
        self.monitoring_type_box.setItemText(7, _translate("BondHearingDialog", "GPS, SCRAM and Smart Start"))
        self.specialized_docket_type_box.setItemText(0, _translate("BondHearingDialog", "OVI Docket"))
        self.specialized_docket_type_box.setItemText(1, _translate("BondHearingDialog", "Mission (Veteran\'s) Court"))
        self.specialized_docket_type_box.setItemText(2, _translate("BondHearingDialog", "Mental Health Docket"))
        self.specialized_docket_checkBox.setText(_translate("BondHearingDialog", "Screen for Specialized Dockets:                           "))
        self.monitoring_checkBox.setText(_translate("BondHearingDialog", "Monitoring (GPS/Scram/Smart Start):                    "))
        self.mental_health_assessment_checkBox.setText(_translate("BondHearingDialog", " Obtain mental health assessment                         "))
        self.fingerprint_in_court_checkBox.setText(_translate("BondHearingDialog", "Fingerprinted by court staff prior to leaving                          "))
        self.comply_protection_order_checkBox.setText(_translate("BondHearingDialog", " Comply with Terms of Protection Order"))
        self.public_safety_suspension_checkBox.setText(_translate("BondHearingDialog", "Public Safety Suspension imposed pursuant to R.C. 4511.196(B)"))
        self.label_8.setText(_translate("BondHearingDialog", "Bond Type:"))
        self.bond_amount_box.setItemText(0, _translate("BondHearingDialog", "None"))
        self.bond_amount_box.setItemText(1, _translate("BondHearingDialog", "$1,000"))
        self.bond_amount_box.setItemText(2, _translate("BondHearingDialog", "$1,500"))
        self.bond_amount_box.setItemText(3, _translate("BondHearingDialog", "$2,000"))
        self.bond_amount_box.setItemText(4, _translate("BondHearingDialog", "$2,500"))
        self.bond_amount_box.setItemText(5, _translate("BondHearingDialog", "$3,000"))
        self.bond_amount_box.setItemText(6, _translate("BondHearingDialog", "$3,500"))
        self.bond_amount_box.setItemText(7, _translate("BondHearingDialog", "$5,000"))
        self.bond_amount_box.setItemText(8, _translate("BondHearingDialog", "$7,500"))
        self.bond_amount_box.setItemText(9, _translate("BondHearingDialog", "$10,000"))
        self.bond_type_box.setItemText(0, _translate("BondHearingDialog", "Recognizance (OR) Bond"))
        self.bond_type_box.setItemText(1, _translate("BondHearingDialog", "10% Deposit, Cash or Surety Bond"))
        self.bond_type_box.setItemText(2, _translate("BondHearingDialog", "Cash or Surety Bond"))
        self.label_9.setText(_translate("BondHearingDialog", "Bond Amount:"))
        self.label_5.setText(_translate("BondHearingDialog", "BOND"))
        self.vehicle_seizure_checkBox.setText(_translate("BondHearingDialog", "Vehicle Seizure / Immobilization"))
        self.admin_license_suspension_checkBox.setText(_translate("BondHearingDialog", "Administrative License Suspension"))
        self.label_10.setText(_translate("BondHearingDialog", "SPECIAL BOND CONDITIONS"))
        self.domestic_violence_checkBox.setText(_translate("BondHearingDialog", "Domestic Violence Restrictions"))
        self.custodial_supervision_checkBox.setText(_translate("BondHearingDialog", "Custodial Supervision                          "))
        self.no_contact_checkBox.setText(_translate("BondHearingDialog", "No Contact Restrictions                         "))
        self.other_conditions_checkBox.setText(_translate("BondHearingDialog", "Other Conditions                          "))
        self.add_special_conditions_Button.setText(_translate("BondHearingDialog", "Add Special Conditions"))
        self.appearance_reason_box.setItemText(0, _translate("BondHearingDialog", "bond modification hearing"))
        self.appearance_reason_box.setItemText(1, _translate("BondHearingDialog", "bond revocation hearing"))
        self.label_11.setText(_translate("BondHearingDialog", "Appearance Reason:"))
        self.label_4.setText(_translate("BondHearingDialog", "Decision on Bond:"))
        self.bond_modification_decision_box.setItemText(1, _translate("BondHearingDialog", "request to modify bond is granted"))
        self.bond_modification_decision_box.setItemText(2, _translate("BondHearingDialog", "request to modify bond is denied"))
        self.bond_modification_decision_box.setItemText(3, _translate("BondHearingDialog", "request to revoke bond is granted"))
        self.bond_modification_decision_box.setItemText(4, _translate("BondHearingDialog", "request to revoke bond is denied"))
        self.defense_counsel_type_box.setItemText(0, _translate("BondHearingDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("BondHearingDialog", "Private Counsel"))
        self.label_26.setText(_translate("BondHearingDialog", "Date:"))
        self.cancel_Button.setText(_translate("BondHearingDialog", "Cancel"))
        self.label_2.setText(_translate("BondHearingDialog", "Def. Last Name:"))
        self.label.setText(_translate("BondHearingDialog", "Def. First Name:"))
        self.label_3.setText(_translate("BondHearingDialog", "Case Number:"))
        self.clear_fields_case_Button.setText(_translate("BondHearingDialog", "Clear Fields"))
        self.label_24.setText(_translate("BondHearingDialog", "Def. Counsel:"))
        self.defense_counsel_waived_checkBox.setText(_translate("BondHearingDialog", "Defendant appeared without counsel"))
        self.close_dialog_Button.setText(_translate("BondHearingDialog", "Close Dialog"))
        self.create_entry_Button.setText(_translate("BondHearingDialog", "Open Entry"))
from munientry.widgets.combo_boxes import DefenseCounselComboBox, NoScrollComboBox
from munientry.widgets.custom_widgets import ConditionCheckbox, NoScrollDateEdit
