# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'munientry/views/ui/DrivingPrivilegesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DrivingPrivilegesDialog(object):
    def setupUi(self, DrivingPrivilegesDialog):
        DrivingPrivilegesDialog.setObjectName("DrivingPrivilegesDialog")
        DrivingPrivilegesDialog.setWindowModality(QtCore.Qt.NonModal)
        DrivingPrivilegesDialog.resize(1144, 798)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DrivingPrivilegesDialog.sizePolicy().hasHeightForWidth())
        DrivingPrivilegesDialog.setSizePolicy(sizePolicy)
        DrivingPrivilegesDialog.setMinimumSize(QtCore.QSize(0, 0))
        DrivingPrivilegesDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        DrivingPrivilegesDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        DrivingPrivilegesDialog.setFont(font)
        DrivingPrivilegesDialog.setToolTip("")
        DrivingPrivilegesDialog.setStyleSheet("background-color: rgb(29, 61, 102);\n"
"font: 75 10pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        DrivingPrivilegesDialog.setSizeGripEnabled(True)
        DrivingPrivilegesDialog.setModal(True)
        self.gridLayout_6 = QtWidgets.QGridLayout(DrivingPrivilegesDialog)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_4 = QtWidgets.QFrame(DrivingPrivilegesDialog)
        self.frame_4.setStyleSheet("background-color: rgb(29, 61, 102);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setStyleSheet("background-color: rgb(107, 107, 107);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1104, 758))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.close_dialog_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(255, 96, 82);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_2.addWidget(self.close_dialog_Button, 5, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setObjectName("label_23")
        self.gridLayout_7.addWidget(self.label_23, 14, 0, 1, 1)
        self.employer_name_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.employer_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.employer_name_lineEdit.setObjectName("employer_name_lineEdit")
        self.gridLayout_7.addWidget(self.employer_name_lineEdit, 10, 1, 2, 3)
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 12, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 10, 0, 1, 1)
        self.employer_city_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.employer_city_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.employer_city_lineEdit.setObjectName("employer_city_lineEdit")
        self.gridLayout_7.addWidget(self.employer_city_lineEdit, 13, 1, 1, 3)
        self.employer_address_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.employer_address_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.employer_address_lineEdit.setObjectName("employer_address_lineEdit")
        self.gridLayout_7.addWidget(self.employer_address_lineEdit, 12, 1, 1, 3)
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 13, 0, 1, 1)
        self.employer_state_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.employer_state_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.employer_state_lineEdit.setObjectName("employer_state_lineEdit")
        self.gridLayout_7.addWidget(self.employer_state_lineEdit, 14, 1, 1, 3)
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setObjectName("label_22")
        self.gridLayout_7.addWidget(self.label_22, 15, 0, 1, 1)
        self.employer_zipcode_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.employer_zipcode_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.employer_zipcode_lineEdit.setObjectName("employer_zipcode_lineEdit")
        self.gridLayout_7.addWidget(self.employer_zipcode_lineEdit, 15, 1, 1, 3)
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 0, 0, 1, 9)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setObjectName("label_28")
        self.gridLayout_7.addWidget(self.label_28, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 2, 0, 1, 1)
        self.occupational_checkBox = QtWidgets.QCheckBox(self.frame)
        self.occupational_checkBox.setObjectName("occupational_checkBox")
        self.gridLayout_7.addWidget(self.occupational_checkBox, 1, 1, 1, 1)
        self.sunday_checkBox = QtWidgets.QCheckBox(self.frame)
        self.sunday_checkBox.setObjectName("sunday_checkBox")
        self.gridLayout_7.addWidget(self.sunday_checkBox, 2, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 3, 1, 1, 1)
        self.varied_hours_checkBox = QtWidgets.QCheckBox(self.frame)
        self.varied_hours_checkBox.setObjectName("varied_hours_checkBox")
        self.gridLayout_7.addWidget(self.varied_hours_checkBox, 5, 1, 1, 1)
        self.monday_checkBox = QtWidgets.QCheckBox(self.frame)
        self.monday_checkBox.setObjectName("monday_checkBox")
        self.gridLayout_7.addWidget(self.monday_checkBox, 2, 2, 1, 1)
        self.tuesday_checkBox = QtWidgets.QCheckBox(self.frame)
        self.tuesday_checkBox.setObjectName("tuesday_checkBox")
        self.gridLayout_7.addWidget(self.tuesday_checkBox, 2, 3, 1, 1)
        self.wednesday_checkBox = QtWidgets.QCheckBox(self.frame)
        self.wednesday_checkBox.setObjectName("wednesday_checkBox")
        self.gridLayout_7.addWidget(self.wednesday_checkBox, 2, 4, 1, 1)
        self.thursday_checkBox = QtWidgets.QCheckBox(self.frame)
        self.thursday_checkBox.setObjectName("thursday_checkBox")
        self.gridLayout_7.addWidget(self.thursday_checkBox, 2, 5, 1, 1)
        self.friday_checkBox = QtWidgets.QCheckBox(self.frame)
        self.friday_checkBox.setObjectName("friday_checkBox")
        self.gridLayout_7.addWidget(self.friday_checkBox, 2, 6, 1, 1)
        self.saturday_checkBox = QtWidgets.QCheckBox(self.frame)
        self.saturday_checkBox.setObjectName("saturday_checkBox")
        self.gridLayout_7.addWidget(self.saturday_checkBox, 2, 7, 1, 1)
        self.other_conditions_checkBox = QtWidgets.QCheckBox(self.frame)
        self.other_conditions_checkBox.setObjectName("other_conditions_checkBox")
        self.gridLayout_7.addWidget(self.other_conditions_checkBox, 5, 2, 1, 1)
        self.from_hours_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.from_hours_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.from_hours_lineEdit.setObjectName("from_hours_lineEdit")
        self.gridLayout_7.addWidget(self.from_hours_lineEdit, 3, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 3, 3, 1, 1)
        self.to_hours_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.to_hours_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.to_hours_lineEdit.setObjectName("to_hours_lineEdit")
        self.gridLayout_7.addWidget(self.to_hours_lineEdit, 3, 4, 1, 1)
        self.other_conditions_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.other_conditions_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.other_conditions_lineEdit.setObjectName("other_conditions_lineEdit")
        self.gridLayout_7.addWidget(self.other_conditions_lineEdit, 5, 3, 1, 5)
        self.vocational_checkBox = QtWidgets.QCheckBox(self.frame)
        self.vocational_checkBox.setObjectName("vocational_checkBox")
        self.gridLayout_7.addWidget(self.vocational_checkBox, 1, 5, 1, 2)
        self.educational_checkBox = QtWidgets.QCheckBox(self.frame)
        self.educational_checkBox.setObjectName("educational_checkBox")
        self.gridLayout_7.addWidget(self.educational_checkBox, 1, 3, 1, 2)
        self.add_employer_school_Button = QtWidgets.QPushButton(self.frame)
        self.add_employer_school_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.add_employer_school_Button.setObjectName("add_employer_school_Button")
        self.gridLayout_7.addWidget(self.add_employer_school_Button, 10, 4, 1, 4)
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_7.addWidget(self.label_30, 12, 4, 1, 4)
        self.employer_school_label = QtWidgets.QLabel(self.frame)
        self.employer_school_label.setObjectName("employer_school_label")
        self.gridLayout_7.addWidget(self.employer_school_label, 14, 4, 1, 4)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.gridLayout_7.setColumnStretch(1, 1)
        self.gridLayout_7.setColumnStretch(2, 1)
        self.gridLayout_7.setColumnStretch(3, 1)
        self.gridLayout_7.setColumnStretch(4, 1)
        self.gridLayout_7.setColumnStretch(5, 1)
        self.gridLayout_7.setColumnStretch(6, 1)
        self.gridLayout_7.setColumnStretch(7, 1)
        self.label_23.raise_()
        self.label_20.raise_()
        self.label_19.raise_()
        self.employer_city_lineEdit.raise_()
        self.employer_address_lineEdit.raise_()
        self.label_21.raise_()
        self.employer_state_lineEdit.raise_()
        self.label_22.raise_()
        self.employer_zipcode_lineEdit.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_10.raise_()
        self.label_28.raise_()
        self.label_7.raise_()
        self.occupational_checkBox.raise_()
        self.sunday_checkBox.raise_()
        self.label_24.raise_()
        self.varied_hours_checkBox.raise_()
        self.monday_checkBox.raise_()
        self.tuesday_checkBox.raise_()
        self.wednesday_checkBox.raise_()
        self.thursday_checkBox.raise_()
        self.friday_checkBox.raise_()
        self.saturday_checkBox.raise_()
        self.other_conditions_checkBox.raise_()
        self.from_hours_lineEdit.raise_()
        self.label_25.raise_()
        self.to_hours_lineEdit.raise_()
        self.other_conditions_lineEdit.raise_()
        self.vocational_checkBox.raise_()
        self.educational_checkBox.raise_()
        self.add_employer_school_Button.raise_()
        self.label_30.raise_()
        self.employer_school_label.raise_()
        self.employer_name_lineEdit.raise_()
        self.gridLayout_2.addWidget(self.frame, 3, 0, 1, 2)
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
        self.label_3 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.case_number_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.case_number_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number_lineEdit.setObjectName("case_number_lineEdit")
        self.gridLayout.addWidget(self.case_number_lineEdit, 1, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 2, 1, 1)
        self.plea_trial_date = NoScrollDateEdit(self.case_name_Frame)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout.addWidget(self.plea_trial_date, 1, 3, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.case_name_Frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.defendant_first_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_first_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_first_name_lineEdit.setObjectName("defendant_first_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_first_name_lineEdit, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 2, 1, 1)
        self.defendant_dob_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_dob_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_dob_lineEdit.setObjectName("defendant_dob_lineEdit")
        self.gridLayout.addWidget(self.defendant_dob_lineEdit, 2, 3, 1, 1)
        self.clear_fields_case_Button = QtWidgets.QPushButton(self.case_name_Frame)
        self.clear_fields_case_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_fields_case_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.clear_fields_case_Button.setObjectName("clear_fields_case_Button")
        self.gridLayout.addWidget(self.clear_fields_case_Button, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.defendant_last_name_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_last_name_lineEdit.setEnabled(True)
        self.defendant_last_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_last_name_lineEdit.setObjectName("defendant_last_name_lineEdit")
        self.gridLayout.addWidget(self.defendant_last_name_lineEdit, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)
        self.defendant_driver_license_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_driver_license_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_driver_license_lineEdit.setText("")
        self.defendant_driver_license_lineEdit.setObjectName("defendant_driver_license_lineEdit")
        self.gridLayout.addWidget(self.defendant_driver_license_lineEdit, 3, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.defendant_address_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_address_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_address_lineEdit.setObjectName("defendant_address_lineEdit")
        self.gridLayout.addWidget(self.defendant_address_lineEdit, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 2, 1, 1)
        self.defendant_state_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_state_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_state_lineEdit.setObjectName("defendant_state_lineEdit")
        self.gridLayout.addWidget(self.defendant_state_lineEdit, 4, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.defendant_city_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_city_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_city_lineEdit.setObjectName("defendant_city_lineEdit")
        self.gridLayout.addWidget(self.defendant_city_lineEdit, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.case_name_Frame)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 2, 1, 1)
        self.defendant_zipcode_lineEdit = QtWidgets.QLineEdit(self.case_name_Frame)
        self.defendant_zipcode_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_zipcode_lineEdit.setObjectName("defendant_zipcode_lineEdit")
        self.gridLayout.addWidget(self.defendant_zipcode_lineEdit, 5, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.case_name_Frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout_2.addWidget(self.case_name_Frame, 0, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setHorizontalSpacing(12)
        self.gridLayout_3.setVerticalSpacing(18)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_5)
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
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 6)
        self.suspension_start_date = NoScrollDateEdit(self.frame_5)
        self.suspension_start_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.suspension_start_date.setCalendarPopup(True)
        self.suspension_start_date.setObjectName("suspension_start_date")
        self.gridLayout_3.addWidget(self.suspension_start_date, 2, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.frame_5)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 4, 1, 1)
        self.suspension_end_date = NoScrollDateEdit(self.frame_5)
        self.suspension_end_date.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.suspension_end_date.setCalendarPopup(True)
        self.suspension_end_date.setObjectName("suspension_end_date")
        self.gridLayout_3.addWidget(self.suspension_end_date, 2, 5, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame_5)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 2, 2, 1, 1)
        self.suspension_term_box = QtWidgets.QComboBox(self.frame_5)
        self.suspension_term_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.suspension_term_box.setObjectName("suspension_term_box")
        self.suspension_term_box.addItem("")
        self.suspension_term_box.setItemText(0, "")
        self.suspension_term_box.addItem("")
        self.suspension_term_box.addItem("")
        self.suspension_term_box.addItem("")
        self.suspension_term_box.addItem("")
        self.suspension_term_box.addItem("")
        self.suspension_term_box.addItem("")
        self.suspension_term_box.addItem("")
        self.suspension_term_box.addItem("")
        self.gridLayout_3.addWidget(self.suspension_term_box, 2, 3, 1, 1)
        self.court_suspension_radioButton = QtWidgets.QRadioButton(self.frame_5)
        self.court_suspension_radioButton.setChecked(True)
        self.court_suspension_radioButton.setObjectName("court_suspension_radioButton")
        self.gridLayout_3.addWidget(self.court_suspension_radioButton, 1, 1, 1, 2)
        self.als_suspension_radioButton = QtWidgets.QRadioButton(self.frame_5)
        self.als_suspension_radioButton.setObjectName("als_suspension_radioButton")
        self.gridLayout_3.addWidget(self.als_suspension_radioButton, 1, 3, 1, 2)
        self.restricted_tags_checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.restricted_tags_checkBox.setObjectName("restricted_tags_checkBox")
        self.gridLayout_3.addWidget(self.restricted_tags_checkBox, 4, 1, 1, 2)
        self.ignition_interlock_checkBox = QtWidgets.QCheckBox(self.frame_5)
        self.ignition_interlock_checkBox.setObjectName("ignition_interlock_checkBox")
        self.gridLayout_3.addWidget(self.ignition_interlock_checkBox, 4, 3, 1, 2)
        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 2)
        self.create_entry_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.create_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.create_entry_Button.setAutoDefault(False)
        self.create_entry_Button.setObjectName("create_entry_Button")
        self.gridLayout_2.addWidget(self.create_entry_Button, 4, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_4, 0, 0, 1, 1)

        self.retranslateUi(DrivingPrivilegesDialog)
        QtCore.QMetaObject.connectSlotsByName(DrivingPrivilegesDialog)
        DrivingPrivilegesDialog.setTabOrder(self.case_number_lineEdit, self.defendant_first_name_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.defendant_first_name_lineEdit, self.defendant_last_name_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.defendant_last_name_lineEdit, self.defendant_address_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.defendant_address_lineEdit, self.defendant_city_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.defendant_city_lineEdit, self.defendant_state_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.defendant_state_lineEdit, self.defendant_zipcode_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.defendant_zipcode_lineEdit, self.court_suspension_radioButton)
        DrivingPrivilegesDialog.setTabOrder(self.court_suspension_radioButton, self.als_suspension_radioButton)
        DrivingPrivilegesDialog.setTabOrder(self.als_suspension_radioButton, self.suspension_start_date)
        DrivingPrivilegesDialog.setTabOrder(self.suspension_start_date, self.suspension_term_box)
        DrivingPrivilegesDialog.setTabOrder(self.suspension_term_box, self.suspension_end_date)
        DrivingPrivilegesDialog.setTabOrder(self.suspension_end_date, self.restricted_tags_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.restricted_tags_checkBox, self.ignition_interlock_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.ignition_interlock_checkBox, self.occupational_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.occupational_checkBox, self.educational_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.educational_checkBox, self.vocational_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.vocational_checkBox, self.sunday_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.sunday_checkBox, self.monday_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.monday_checkBox, self.tuesday_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.tuesday_checkBox, self.wednesday_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.wednesday_checkBox, self.thursday_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.thursday_checkBox, self.friday_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.friday_checkBox, self.saturday_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.saturday_checkBox, self.from_hours_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.from_hours_lineEdit, self.to_hours_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.to_hours_lineEdit, self.varied_hours_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.varied_hours_checkBox, self.other_conditions_checkBox)
        DrivingPrivilegesDialog.setTabOrder(self.other_conditions_checkBox, self.other_conditions_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.other_conditions_lineEdit, self.employer_name_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.employer_name_lineEdit, self.employer_address_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.employer_address_lineEdit, self.employer_city_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.employer_city_lineEdit, self.employer_state_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.employer_state_lineEdit, self.employer_zipcode_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.employer_zipcode_lineEdit, self.add_employer_school_Button)
        DrivingPrivilegesDialog.setTabOrder(self.add_employer_school_Button, self.create_entry_Button)
        DrivingPrivilegesDialog.setTabOrder(self.create_entry_Button, self.close_dialog_Button)
        DrivingPrivilegesDialog.setTabOrder(self.close_dialog_Button, self.defendant_dob_lineEdit)
        DrivingPrivilegesDialog.setTabOrder(self.defendant_dob_lineEdit, self.defendant_driver_license_lineEdit)

    def retranslateUi(self, DrivingPrivilegesDialog):
        _translate = QtCore.QCoreApplication.translate
        DrivingPrivilegesDialog.setWindowTitle(_translate("DrivingPrivilegesDialog", "Driving Privileges Information"))
        self.close_dialog_Button.setText(_translate("DrivingPrivilegesDialog", "Close Dialog"))
        self.label_23.setText(_translate("DrivingPrivilegesDialog", "State:"))
        self.label_20.setText(_translate("DrivingPrivilegesDialog", "Address:"))
        self.label_19.setText(_translate("DrivingPrivilegesDialog", "Name: "))
        self.label_21.setText(_translate("DrivingPrivilegesDialog", "City:"))
        self.label_22.setText(_translate("DrivingPrivilegesDialog", "ZIP Code:"))
        self.label_17.setText(_translate("DrivingPrivilegesDialog", "Type of Privileges:"))
        self.label_18.setText(_translate("DrivingPrivilegesDialog", "EMPLOYER / SCHOOL INFORMATION"))
        self.label_10.setText(_translate("DrivingPrivilegesDialog", "Hours for Privileges:"))
        self.label_28.setText(_translate("DrivingPrivilegesDialog", "Conditions:"))
        self.label_7.setText(_translate("DrivingPrivilegesDialog", "Days for Privileges:"))
        self.occupational_checkBox.setText(_translate("DrivingPrivilegesDialog", "Occupational"))
        self.sunday_checkBox.setText(_translate("DrivingPrivilegesDialog", "Sunday"))
        self.label_24.setText(_translate("DrivingPrivilegesDialog", "From:"))
        self.varied_hours_checkBox.setText(_translate("DrivingPrivilegesDialog", "Days / Hours may vary"))
        self.monday_checkBox.setText(_translate("DrivingPrivilegesDialog", "Monday"))
        self.tuesday_checkBox.setText(_translate("DrivingPrivilegesDialog", "Tuesday"))
        self.wednesday_checkBox.setText(_translate("DrivingPrivilegesDialog", "Wednesday"))
        self.thursday_checkBox.setText(_translate("DrivingPrivilegesDialog", "Thursday"))
        self.friday_checkBox.setText(_translate("DrivingPrivilegesDialog", "Friday"))
        self.saturday_checkBox.setText(_translate("DrivingPrivilegesDialog", "Saturday"))
        self.other_conditions_checkBox.setText(_translate("DrivingPrivilegesDialog", "Other"))
        self.label_25.setText(_translate("DrivingPrivilegesDialog", "To:"))
        self.other_conditions_lineEdit.setPlaceholderText(_translate("DrivingPrivilegesDialog", "List other conditions here."))
        self.vocational_checkBox.setText(_translate("DrivingPrivilegesDialog", "Vocational"))
        self.educational_checkBox.setText(_translate("DrivingPrivilegesDialog", "Educational"))
        self.add_employer_school_Button.setText(_translate("DrivingPrivilegesDialog", "Add Another Employer/School"))
        self.label_30.setText(_translate("DrivingPrivilegesDialog", "Employers and Schools for Privileges"))
        self.employer_school_label.setText(_translate("DrivingPrivilegesDialog", "None."))
        self.label_3.setText(_translate("DrivingPrivilegesDialog", "Case Number:"))
        self.label_26.setText(_translate("DrivingPrivilegesDialog", "Entry Date:"))
        self.cancel_Button.setText(_translate("DrivingPrivilegesDialog", "Cancel"))
        self.label.setText(_translate("DrivingPrivilegesDialog", "Def. First Name:"))
        self.label_8.setText(_translate("DrivingPrivilegesDialog", "Def. DOB:"))
        self.clear_fields_case_Button.setText(_translate("DrivingPrivilegesDialog", "Clear Fields"))
        self.label_2.setText(_translate("DrivingPrivilegesDialog", "Def. Last Name:"))
        self.label_9.setText(_translate("DrivingPrivilegesDialog", "Def. Driver License Number:"))
        self.label_11.setText(_translate("DrivingPrivilegesDialog", "Address:"))
        self.label_13.setText(_translate("DrivingPrivilegesDialog", "State:"))
        self.label_12.setText(_translate("DrivingPrivilegesDialog", "City:"))
        self.label_14.setText(_translate("DrivingPrivilegesDialog", "ZIP Code:"))
        self.label_6.setText(_translate("DrivingPrivilegesDialog", "CASE INFORMATION"))
        self.label_15.setText(_translate("DrivingPrivilegesDialog", "Begin Suspension Date:"))
        self.label_5.setText(_translate("DrivingPrivilegesDialog", "GENERAL PRIVILEGES INFORMATION"))
        self.label_27.setText(_translate("DrivingPrivilegesDialog", "Additional Requirements:"))
        self.label_4.setText(_translate("DrivingPrivilegesDialog", "Suspension Type:"))
        self.label_16.setText(_translate("DrivingPrivilegesDialog", "End Suspension Date:"))
        self.label_29.setText(_translate("DrivingPrivilegesDialog", "Term of Suspension:"))
        self.suspension_term_box.setItemText(1, _translate("DrivingPrivilegesDialog", "90 Days"))
        self.suspension_term_box.setItemText(2, _translate("DrivingPrivilegesDialog", "1 Year"))
        self.suspension_term_box.setItemText(3, _translate("DrivingPrivilegesDialog", "2 Years"))
        self.suspension_term_box.setItemText(4, _translate("DrivingPrivilegesDialog", "3 Years"))
        self.suspension_term_box.setItemText(5, _translate("DrivingPrivilegesDialog", "4 Years"))
        self.suspension_term_box.setItemText(6, _translate("DrivingPrivilegesDialog", "5 Years"))
        self.suspension_term_box.setItemText(7, _translate("DrivingPrivilegesDialog", "6 Years"))
        self.suspension_term_box.setItemText(8, _translate("DrivingPrivilegesDialog", "7 Years"))
        self.court_suspension_radioButton.setText(_translate("DrivingPrivilegesDialog", "Court"))
        self.als_suspension_radioButton.setText(_translate("DrivingPrivilegesDialog", "ALS"))
        self.restricted_tags_checkBox.setText(_translate("DrivingPrivilegesDialog", "Restricted Vehicle ID Tags"))
        self.ignition_interlock_checkBox.setText(_translate("DrivingPrivilegesDialog", "Certified Ignition Interlock Device"))
        self.create_entry_Button.setText(_translate("DrivingPrivilegesDialog", "Open Entry"))
from munientry.widgets.custom_widgets import NoScrollDateEdit
