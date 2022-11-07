# Form implementation generated from reading ui file 'munientry/views/ui/DiversionPleaDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from munientry.widgets.combo_boxes import DefenseCounselComboBox, NoScrollComboBox
from munientry.widgets.custom_widgets import NoScrollDateEdit
from munientry.widgets.charges_grids import JailChargesGrid


class Ui_DiversionPleaDialog(object):
    def setupUi(self, DiversionPleaDialog):
        DiversionPleaDialog.setObjectName("DiversionPleaDialog")
        DiversionPleaDialog.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        DiversionPleaDialog.resize(1010, 782)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DiversionPleaDialog.sizePolicy().hasHeightForWidth())
        DiversionPleaDialog.setSizePolicy(sizePolicy)
        DiversionPleaDialog.setMinimumSize(QtCore.QSize(0, 0))
        DiversionPleaDialog.setMaximumSize(QtCore.QSize(2500, 3500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        DiversionPleaDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        DiversionPleaDialog.setFont(font)
        DiversionPleaDialog.setToolTip("")
        DiversionPleaDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        DiversionPleaDialog.setSizeGripEnabled(True)
        DiversionPleaDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(DiversionPleaDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(DiversionPleaDialog)
        self.scrollArea.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 969, 1073))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.diversion_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.diversion_frame.setEnabled(True)
        self.diversion_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.diversion_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.diversion_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.diversion_frame.setLineWidth(2)
        self.diversion_frame.setObjectName("diversion_frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.diversion_frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.diversion_fine_pay_date_box = NoScrollDateEdit(self.diversion_frame)
        self.diversion_fine_pay_date_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.diversion_fine_pay_date_box.setCalendarPopup(True)
        self.diversion_fine_pay_date_box.setObjectName("diversion_fine_pay_date_box")
        self.gridLayout_8.addWidget(self.diversion_fine_pay_date_box, 1, 3, 1, 1)
        self.theft_diversion_radioButton = QtWidgets.QRadioButton(self.diversion_frame)
        self.theft_diversion_radioButton.setObjectName("theft_diversion_radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(DiversionPleaDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.theft_diversion_radioButton)
        self.gridLayout_8.addWidget(self.theft_diversion_radioButton, 2, 0, 1, 1)
        self.jail_report_date_note_label = QtWidgets.QLabel(self.diversion_frame)
        self.jail_report_date_note_label.setObjectName("jail_report_date_note_label")
        self.gridLayout_8.addWidget(self.jail_report_date_note_label, 5, 2, 1, 2)
        self.other_conditions_textEdit = QtWidgets.QTextEdit(self.diversion_frame)
        self.other_conditions_textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.other_conditions_textEdit.setObjectName("other_conditions_textEdit")
        self.gridLayout_8.addWidget(self.other_conditions_textEdit, 10, 2, 1, 2)
        self.other_conditions_checkBox = QtWidgets.QCheckBox(self.diversion_frame)
        self.other_conditions_checkBox.setObjectName("other_conditions_checkBox")
        self.gridLayout_8.addWidget(self.other_conditions_checkBox, 10, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.diversion_frame)
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_8.addWidget(self.line_7, 1, 1, 5, 1)
        self.other_diversion_radioButton = QtWidgets.QRadioButton(self.diversion_frame)
        self.other_diversion_radioButton.setObjectName("other_diversion_radioButton")
        self.buttonGroup.addButton(self.other_diversion_radioButton)
        self.gridLayout_8.addWidget(self.other_diversion_radioButton, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.diversion_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 4)
        self.label_23 = QtWidgets.QLabel(self.diversion_frame)
        self.label_23.setObjectName("label_23")
        self.gridLayout_8.addWidget(self.label_23, 1, 2, 1, 1)
        self.diversion_jail_report_date_box = NoScrollDateEdit(self.diversion_frame)
        self.diversion_jail_report_date_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.diversion_jail_report_date_box.setCalendarPopup(True)
        self.diversion_jail_report_date_box.setObjectName("diversion_jail_report_date_box")
        self.gridLayout_8.addWidget(self.diversion_jail_report_date_box, 4, 3, 1, 1)
        self.diversion_jail_report_date_label = QtWidgets.QLabel(self.diversion_frame)
        self.diversion_jail_report_date_label.setObjectName("diversion_jail_report_date_label")
        self.gridLayout_8.addWidget(self.diversion_jail_report_date_label, 4, 2, 1, 1)
        self.pay_restitution_checkBox = QtWidgets.QCheckBox(self.diversion_frame)
        self.pay_restitution_checkBox.setObjectName("pay_restitution_checkBox")
        self.gridLayout_8.addWidget(self.pay_restitution_checkBox, 8, 0, 1, 1)
        self.marijuana_diversion_radioButton = QtWidgets.QRadioButton(self.diversion_frame)
        self.marijuana_diversion_radioButton.setObjectName("marijuana_diversion_radioButton")
        self.buttonGroup.addButton(self.marijuana_diversion_radioButton)
        self.gridLayout_8.addWidget(self.marijuana_diversion_radioButton, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.diversion_frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 2, 2, 1, 2)
        self.line_2 = QtWidgets.QFrame(self.diversion_frame)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_8.addWidget(self.line_2, 7, 0, 1, 4)
        self.diversion_jail_imposed_checkBox = QtWidgets.QCheckBox(self.diversion_frame)
        self.diversion_jail_imposed_checkBox.setObjectName("diversion_jail_imposed_checkBox")
        self.gridLayout_8.addWidget(self.diversion_jail_imposed_checkBox, 3, 2, 1, 1)
        self.pay_restitution_to_box = QtWidgets.QLineEdit(self.diversion_frame)
        self.pay_restitution_to_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pay_restitution_to_box.setObjectName("pay_restitution_to_box")
        self.gridLayout_8.addWidget(self.pay_restitution_to_box, 8, 3, 1, 1)
        self.pay_restitution_amount_box = QtWidgets.QLineEdit(self.diversion_frame)
        self.pay_restitution_amount_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pay_restitution_amount_box.setObjectName("pay_restitution_amount_box")
        self.gridLayout_8.addWidget(self.pay_restitution_amount_box, 9, 3, 1, 1)
        self.pay_restitution_to_label = QtWidgets.QLabel(self.diversion_frame)
        self.pay_restitution_to_label.setObjectName("pay_restitution_to_label")
        self.gridLayout_8.addWidget(self.pay_restitution_to_label, 8, 2, 1, 1)
        self.pay_restitution_amount_label = QtWidgets.QLabel(self.diversion_frame)
        self.pay_restitution_amount_label.setObjectName("pay_restitution_amount_label")
        self.gridLayout_8.addWidget(self.pay_restitution_amount_label, 9, 2, 1, 1)
        self.gridLayout_8.setRowStretch(0, 1)
        self.gridLayout_8.setRowStretch(1, 1)
        self.gridLayout_8.setRowStretch(2, 1)
        self.gridLayout_8.setRowStretch(3, 1)
        self.gridLayout_8.setRowStretch(4, 1)
        self.gridLayout_2.addWidget(self.diversion_frame, 1, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.no_contest_all_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no_contest_all_Button.sizePolicy().hasHeightForWidth())
        self.no_contest_all_Button.setSizePolicy(sizePolicy)
        self.no_contest_all_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.no_contest_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.no_contest_all_Button.setObjectName("no_contest_all_Button")
        self.gridLayout_3.addWidget(self.no_contest_all_Button, 2, 1, 1, 1)
        self.guilty_all_Button = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guilty_all_Button.sizePolicy().hasHeightForWidth())
        self.guilty_all_Button.setSizePolicy(sizePolicy)
        self.guilty_all_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.guilty_all_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.guilty_all_Button.setObjectName("guilty_all_Button")
        self.gridLayout_3.addWidget(self.guilty_all_Button, 2, 2, 1, 1)
        self.add_charge_Button = QtWidgets.QPushButton(self.frame)
        self.add_charge_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_charge_Button.setObjectName("add_charge_Button")
        self.gridLayout_3.addWidget(self.add_charge_Button, 2, 0, 1, 1)
        # self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout = JailChargesGrid()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.charges_gridLayout.addWidget(self.label_5, 12, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.charges_gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.charges_gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.charges_gridLayout.addWidget(self.label_14, 6, 0, 1, 1)
        self.plea_label_1 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plea_label_1.setFont(font)
        self.plea_label_1.setObjectName("plea_label_1")
        self.charges_gridLayout.addWidget(self.plea_label_1, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.charges_gridLayout.addWidget(self.label_12, 10, 0, 1, 1)
        self.offense_label_1 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.offense_label_1.setFont(font)
        self.offense_label_1.setWordWrap(True)
        self.offense_label_1.setObjectName("offense_label_1")
        self.charges_gridLayout.addWidget(self.offense_label_1, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.charges_gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.charges_gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.charges_gridLayout.addWidget(self.label_17, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.charges_gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.charges_gridLayout.addWidget(self.label_4, 11, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setObjectName("label_25")
        self.charges_gridLayout.addWidget(self.label_25, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.charges_gridLayout, 0, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 2)
        self.case_name_Frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
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
        self.appearance_reason_box.setObjectName("appearance_reason_box")
        self.appearance_reason_box.addItem("")
        self.appearance_reason_box.addItem("")
        self.gridLayout.addWidget(self.appearance_reason_box, 4, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.defense_counsel_type_box = NoScrollComboBox(self.case_name_Frame)
        self.defense_counsel_type_box.setEnabled(True)
        self.defense_counsel_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_type_box.setObjectName("defense_counsel_type_box")
        self.defense_counsel_type_box.addItem("")
        self.defense_counsel_type_box.addItem("")
        self.gridLayout.addWidget(self.defense_counsel_type_box, 2, 2, 1, 1)
        self.defense_counsel_name_box = DefenseCounselComboBox(self.case_name_Frame)
        self.defense_counsel_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defense_counsel_name_box.setEditable(True)
        self.defense_counsel_name_box.setObjectName("defense_counsel_name_box")
        self.gridLayout.addWidget(self.defense_counsel_name_box, 2, 1, 1, 1)
        self.defense_counsel_waived_checkBox = QtWidgets.QCheckBox(self.case_name_Frame)
        self.defense_counsel_waived_checkBox.setObjectName("defense_counsel_waived_checkBox")
        self.gridLayout.addWidget(self.defense_counsel_waived_checkBox, 2, 3, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 1, 4, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 3, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 0, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 1, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 4, 0, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 0, 1, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.case_name_Frame)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.fra_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fra_frame.sizePolicy().hasHeightForWidth())
        self.fra_frame.setSizePolicy(sizePolicy)
        self.fra_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.fra_frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.fra_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.fra_frame.setLineWidth(2)
        self.fra_frame.setObjectName("fra_frame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.fra_frame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_21 = QtWidgets.QLabel(self.fra_frame)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_21)
        self.fra_in_file_box = NoScrollComboBox(self.fra_frame)
        self.fra_in_file_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_file_box.setObjectName("fra_in_file_box")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fra_in_file_box)
        self.label_22 = QtWidgets.QLabel(self.fra_frame)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_22)
        self.fra_in_court_box = NoScrollComboBox(self.fra_frame)
        self.fra_in_court_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_court_box.setObjectName("fra_in_court_box")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fra_in_court_box)
        self.gridLayout_2.addWidget(self.fra_frame, 3, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.create_entry_Button = QtWidgets.QPushButton(self.frame_3)
        self.create_entry_Button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_4.addWidget(self.create_entry_Button, 0, 0, 1, 1)
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_3)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(255, 96, 82);")
        self.close_dialog_Button.setAutoDefault(False)
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_4.addWidget(self.close_dialog_Button, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 3, 1, 1, 1)
        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 4)
        self.gridLayout_2.setRowStretch(3, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(DiversionPleaDialog)
        QtCore.QMetaObject.connectSlotsByName(DiversionPleaDialog)
        DiversionPleaDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        DiversionPleaDialog.setTabOrder(self.defendant_last_name_lineEdit, self.case_number_lineEdit)
        DiversionPleaDialog.setTabOrder(self.case_number_lineEdit, self.appearance_reason_box)
        DiversionPleaDialog.setTabOrder(self.appearance_reason_box, self.fra_in_file_box)
        DiversionPleaDialog.setTabOrder(self.fra_in_file_box, self.fra_in_court_box)
        DiversionPleaDialog.setTabOrder(self.fra_in_court_box, self.add_charge_Button)

    def retranslateUi(self, DiversionPleaDialog):
        _translate = QtCore.QCoreApplication.translate
        DiversionPleaDialog.setWindowTitle(_translate("DiversionPleaDialog", "Diversion Plea Case Information"))
        self.theft_diversion_radioButton.setText(_translate("DiversionPleaDialog", "Theft Diversion Program"))
        self.jail_report_date_note_label.setText(_translate("DiversionPleaDialog", "Jail report date is set to first Friday after 97 days from today."))
        self.other_conditions_checkBox.setText(_translate("DiversionPleaDialog", "Add Other Conditions"))
        self.other_diversion_radioButton.setText(_translate("DiversionPleaDialog", "Other Diversion Program"))
        self.label_9.setText(_translate("DiversionPleaDialog", "DIVERSION DETAILS"))
        self.label_23.setText(_translate("DiversionPleaDialog", "Fine Pay Date:"))
        self.diversion_jail_report_date_label.setText(_translate("DiversionPleaDialog", "Jail Report Date:"))
        self.pay_restitution_checkBox.setText(_translate("DiversionPleaDialog", "Restitution Ordered"))
        self.marijuana_diversion_radioButton.setText(_translate("DiversionPleaDialog", "Marijuana Diversion Program"))
        self.label_6.setText(_translate("DiversionPleaDialog", "Fine pay date is set to first Tuesday after 97 days from today."))
        self.diversion_jail_imposed_checkBox.setText(_translate("DiversionPleaDialog", "Jail Time Imposed"))
        self.pay_restitution_to_label.setText(_translate("DiversionPleaDialog", "Pay Restitution To:"))
        self.pay_restitution_amount_label.setText(_translate("DiversionPleaDialog", "Pay Restitution in Amount of:"))
        self.no_contest_all_Button.setText(_translate("DiversionPleaDialog", "No Contest All"))
        self.guilty_all_Button.setText(_translate("DiversionPleaDialog", "Guilty All"))
        self.add_charge_Button.setText(_translate("DiversionPleaDialog", "Add Charge"))
        self.label_10.setText(_translate("DiversionPleaDialog", "Fines Suspended:"))
        self.label_20.setText(_translate("DiversionPleaDialog", "Degree:"))
        self.label_14.setText(_translate("DiversionPleaDialog", "Finding:"))
        self.plea_label_1.setText(_translate("DiversionPleaDialog", "Plea:"))
        self.label_12.setText(_translate("DiversionPleaDialog", "Jail Days Suspended:"))
        self.offense_label_1.setText(_translate("DiversionPleaDialog", "Offense:"))
        self.label_19.setText(_translate("DiversionPleaDialog", "Statute:"))
        self.label_8.setText(_translate("DiversionPleaDialog", "Jail Days:"))
        self.label_17.setText(_translate("DiversionPleaDialog", "Fines:"))
        self.label_7.setText(_translate("DiversionPleaDialog", "Allied:"))
        self.label_25.setText(_translate("DiversionPleaDialog", "Dismissed:"))
        self.appearance_reason_box.setItemText(0, _translate("DiversionPleaDialog", "arraignment"))
        self.appearance_reason_box.setItemText(1, _translate("DiversionPleaDialog", "change of plea"))
        self.label_24.setText(_translate("DiversionPleaDialog", "Def. Counsel:"))
        self.label_3.setText(_translate("DiversionPleaDialog", "Case Number:"))
        self.defense_counsel_type_box.setItemText(0, _translate("DiversionPleaDialog", "Public Defender"))
        self.defense_counsel_type_box.setItemText(1, _translate("DiversionPleaDialog", "Private Counsel"))
        self.defense_counsel_waived_checkBox.setText(_translate("DiversionPleaDialog", "Defendant waived right to counsel"))
        self.clear_fields_case_Button.setText(_translate("DiversionPleaDialog", "Clear Fields"))
        self.cancel_Button.setText(_translate("DiversionPleaDialog", "Cancel"))
        self.label_26.setText(_translate("DiversionPleaDialog", "Date:"))
        self.label_27.setText(_translate("DiversionPleaDialog", "Appearance Reason:"))
        self.label.setText(_translate("DiversionPleaDialog", "Def. First Name:"))
        self.label_2.setText(_translate("DiversionPleaDialog", "Def. Last Name:"))
        self.label_21.setText(_translate("DiversionPleaDialog", "FRA shown in complaint:"))
        self.fra_in_file_box.setItemText(0, _translate("DiversionPleaDialog", "N/A"))
        self.fra_in_file_box.setItemText(1, _translate("DiversionPleaDialog", "Yes"))
        self.fra_in_file_box.setItemText(2, _translate("DiversionPleaDialog", "No"))
        self.label_22.setText(_translate("DiversionPleaDialog", "FRA shown in court:"))
        self.fra_in_court_box.setItemText(0, _translate("DiversionPleaDialog", "N/A"))
        self.fra_in_court_box.setItemText(1, _translate("DiversionPleaDialog", "Yes"))
        self.fra_in_court_box.setItemText(2, _translate("DiversionPleaDialog", "No"))
        self.create_entry_Button.setText(_translate("DiversionPleaDialog", "Open Entry"))
        self.close_dialog_Button.setText(_translate("DiversionPleaDialog", "Close Dialog"))
