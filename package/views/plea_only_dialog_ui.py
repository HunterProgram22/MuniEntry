# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package\views\ui\PleaOnlyDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PleaOnlyDialog(object):
    def setupUi(self, PleaOnlyDialog):
        PleaOnlyDialog.setObjectName("PleaOnlyDialog")
        PleaOnlyDialog.setWindowModality(QtCore.Qt.NonModal)
        PleaOnlyDialog.resize(964, 791)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PleaOnlyDialog.sizePolicy().hasHeightForWidth())
        PleaOnlyDialog.setSizePolicy(sizePolicy)
        PleaOnlyDialog.setMinimumSize(QtCore.QSize(0, 0))
        PleaOnlyDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        PleaOnlyDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        PleaOnlyDialog.setFont(font)
        PleaOnlyDialog.setToolTip("")
        PleaOnlyDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        PleaOnlyDialog.setSizeGripEnabled(True)
        PleaOnlyDialog.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(PleaOnlyDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_4 = QtWidgets.QFrame(PleaOnlyDialog)
        self.frame_4.setStyleSheet("background-color: rgb(29, 61, 102);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 924, 751))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.create_entry_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_8.addWidget(self.create_entry_Button, 2, 1, 1, 1)
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
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.defense_counsel_name_box = DefenseCounselComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 2, 1, 1, 1)
        self.defense_counsel_type_box = NoScrollComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 2, 2, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 2, 3, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.appearance_reason_box = NoScrollComboBox(self.case_name_Frame)
        self.appearance_reason_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.appearance_reason_box.setEditable(True)
        self.appearance_reason_box.setObjectName("appearance_reason_box")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.gridLayout.addWidget(self.appearance_reason_box, 4, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.case_name_Frame)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_8.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setSpacing(16)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.plea_only_bond_type_box = NoScrollComboBox(self.frame_2)
        self.plea_only_bond_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_only_bond_type_box.setObjectName("plea_only_bond_type_box")
        self.plea_only_bond_type_box.addItem("")
        self.plea_only_bond_type_box.addItem("")
        self.gridLayout_7.addWidget(self.plea_only_bond_type_box, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 250))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 2)
        self.gridLayout_8.addWidget(self.frame_2, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.no_contest_all_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_contest_all_Button.sizePolicy().hasHeightForWidth())
        self.no_contest_all_Button.setSizePolicy(sizePolicy)
        self.no_contest_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.no_contest_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.no_contest_all_Button.setObjectName("no_contest_all_Button")
        self.gridLayout_3.addWidget(self.no_contest_all_Button, 2, 1, 1, 1)
        self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.offense_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.offense_label.setFont(font)
        self.offense_label.setWordWrap(True)
        self.offense_label.setObjectName("offense_label")
        self.charges_gridLayout.addWidget(self.offense_label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.charges_gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.amend_row_label = QtWidgets.QLabel(self.frame)
        self.amend_row_label.setText("")
        self.amend_row_label.setObjectName("amend_row_label")
        self.charges_gridLayout.addWidget(self.amend_row_label, 7, 0, 1, 1)
        self.dismissed_label = QtWidgets.QLabel(self.frame)
        self.dismissed_label.setObjectName("dismissed_label")
        self.charges_gridLayout.addWidget(self.dismissed_label, 3, 0, 1, 1)
        self.degree_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.degree_label.setFont(font)
        self.degree_label.setObjectName("degree_label")
        self.charges_gridLayout.addWidget(self.degree_label, 2, 0, 1, 1)
        self.finding_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.finding_label.setFont(font)
        self.finding_label.setObjectName("finding_label")
        self.charges_gridLayout.addWidget(self.finding_label, 6, 0, 1, 1)
        self.statute_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.statute_label.setFont(font)
        self.statute_label.setObjectName("statute_label")
        self.charges_gridLayout.addWidget(self.statute_label, 1, 0, 1, 1)
        self.plea_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plea_label.setFont(font)
        self.plea_label.setObjectName("plea_label")
        self.charges_gridLayout.addWidget(self.plea_label, 5, 0, 1, 1)
        self.allied_label = QtWidgets.QLabel(self.frame)
        self.allied_label.setObjectName("allied_label")
        self.charges_gridLayout.addWidget(self.allied_label, 4, 0, 1, 1)
        self.gridLayout_3.addLayout(self.charges_gridLayout, 0, 0, 1, 3)
        self.guilty_all_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guilty_all_Button.sizePolicy().hasHeightForWidth())
        self.guilty_all_Button.setSizePolicy(sizePolicy)
        self.guilty_all_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.guilty_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.guilty_all_Button.setObjectName("guilty_all_Button")
        self.gridLayout_3.addWidget(self.guilty_all_Button, 2, 2, 1, 1)
        self.add_charge_Button = QtWidgets.QPushButton(self.frame)
        self.add_charge_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_charge_Button.setObjectName("add_charge_Button")
        self.gridLayout_3.addWidget(self.add_charge_Button, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_8.addWidget(self.frame, 1, 0, 1, 2)
        self.close_dialog_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(255, 96, 82);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_8.addWidget(self.close_dialog_Button, 3, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.set_restitution_checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.set_restitution_checkBox.setObjectName("set_restitution_checkBox")
        self.gridLayout_5.addWidget(self.set_restitution_checkBox, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 2)
        self.prepare_psi_checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.prepare_psi_checkBox.setObjectName("prepare_psi_checkBox")
        self.gridLayout_5.addWidget(self.prepare_psi_checkBox, 1, 0, 1, 1)
        self.victim_appearance_checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.victim_appearance_checkBox.setObjectName("victim_appearance_checkBox")
        self.gridLayout_5.addWidget(self.victim_appearance_checkBox, 3, 0, 1, 1)
        self.gridLayout_8.addWidget(self.frame_5, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(PleaOnlyDialog)
        QtCore.QMetaObject.connectSlotsByName(PleaOnlyDialog)
        PleaOnlyDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        PleaOnlyDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)

    def retranslateUi(self, PleaOnlyDialog):
        _translate = QtCore.QCoreApplication.translate
        PleaOnlyDialog.setWindowTitle(_translate("PleaOnlyDialog", "Plea Future Sentencing Case Information"))
        self.create_entry_Button.setText(_translate("PleaOnlyDialog", "Open Entry"))
        self.label.setText(_translate("PleaOnlyDialog", "Def. First Name:"))
        self.defense_counsel_type_box.setItemText(0, _translate("PleaOnlyDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("PleaOnlyDialog", "Private Counsel"))
        self.defense_counsel_waived_checkBox.setText(_translate("PleaOnlyDialog", "Defendant appeared without counsel"))
        self.cancel_Button.setText(_translate("PleaOnlyDialog", "Cancel"))
        self.label_26.setText(_translate("PleaOnlyDialog", "Date:"))
        self.label_3.setText(_translate("PleaOnlyDialog", "Case Number:"))
        self.clear_fields_case_Button.setText(_translate("PleaOnlyDialog", "Clear Fields"))
        self.label_2.setText(_translate("PleaOnlyDialog", "Def. Last Name:"))
        self.label_11.setText(_translate("PleaOnlyDialog", "Appearance Reason:"))
        self.label_24.setText(_translate("PleaOnlyDialog", "Def. Counsel:"))
        self.appearance_reason_box.setItemText(0, _translate("PleaOnlyDialog", "arraignment"))
        self.appearance_reason_box.setItemText(1, _translate("PleaOnlyDialog", "a change of plea"))
        self.appearance_reason_box.setItemText(2, _translate("PleaOnlyDialog", "motion hearing"))
        self.appearance_reason_box.setItemText(3, _translate("PleaOnlyDialog", "warrant for failure to appear"))
        self.plea_only_bond_type_box.setItemText(0, _translate("PleaOnlyDialog", "OR Bond"))
        self.plea_only_bond_type_box.setItemText(1, _translate("PleaOnlyDialog", "Continue Existing Bond"))
        self.label_7.setText(_translate("PleaOnlyDialog", "Bond:"))
        self.label_4.setText(_translate("PleaOnlyDialog", "BOND PENDING SENTENCING"))
        self.no_contest_all_Button.setText(_translate("PleaOnlyDialog", "No Contest All"))
        self.offense_label.setText(_translate("PleaOnlyDialog", "Offense:"))
        self.dismissed_label.setText(_translate("PleaOnlyDialog", "Dismissed:"))
        self.degree_label.setText(_translate("PleaOnlyDialog", "Degree:"))
        self.finding_label.setText(_translate("PleaOnlyDialog", "Finding:"))
        self.statute_label.setText(_translate("PleaOnlyDialog", "Statute:"))
        self.plea_label.setText(_translate("PleaOnlyDialog", "Plea:"))
        self.allied_label.setText(_translate("PleaOnlyDialog", "Allied:"))
        self.guilty_all_Button.setText(_translate("PleaOnlyDialog", "Guilty All"))
        self.add_charge_Button.setText(_translate("PleaOnlyDialog", "Add Charge"))
        self.close_dialog_Button.setText(_translate("PleaOnlyDialog", "Close Dialog"))
        self.set_restitution_checkBox.setText(_translate("PleaOnlyDialog", "Set for Restitution Hearing with Sentencing"))
        self.label_5.setText(_translate("PleaOnlyDialog", "FUTURE SENTENCING REASONS"))
        self.prepare_psi_checkBox.setText(_translate("PleaOnlyDialog", "Prepare Presentence Investigation Report"))
        self.victim_appearance_checkBox.setText(_translate("PleaOnlyDialog", "Set for Future Sentencing to Allow for Appearance of the Victim at Sentencing"))
from .custom_widgets import DefenseCounselComboBox, NoScrollComboBox, NoScrollDateEdit
