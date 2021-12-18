# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/AddSpecialBondConditionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddSpecialBondConditionsDialog(object):
    def setupUi(self, AddSpecialBondConditionsDialog):
        AddSpecialBondConditionsDialog.setObjectName("AddSpecialBondConditionsDialog")
        AddSpecialBondConditionsDialog.setWindowModality(QtCore.Qt.NonModal)
        AddSpecialBondConditionsDialog.setEnabled(True)
        AddSpecialBondConditionsDialog.resize(1217, 873)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddSpecialBondConditionsDialog.sizePolicy().hasHeightForWidth())
        AddSpecialBondConditionsDialog.setSizePolicy(sizePolicy)
        AddSpecialBondConditionsDialog.setMinimumSize(QtCore.QSize(0, 0))
        AddSpecialBondConditionsDialog.setMaximumSize(QtCore.QSize(2500, 3500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 49, 91))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        AddSpecialBondConditionsDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        AddSpecialBondConditionsDialog.setFont(font)
        AddSpecialBondConditionsDialog.setToolTip("")
        AddSpecialBondConditionsDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        AddSpecialBondConditionsDialog.setSizeGripEnabled(True)
        AddSpecialBondConditionsDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(AddSpecialBondConditionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(AddSpecialBondConditionsDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1152, 842))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.banner_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.banner_frame.setFont(font)
        self.banner_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.banner_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.banner_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.banner_frame.setLineWidth(2)
        self.banner_frame.setObjectName("banner_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.banner_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.label_19 = QtWidgets.QLabel(self.banner_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.charges_gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.offense_label_1 = QtWidgets.QLabel(self.banner_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.offense_label_1.setFont(font)
        self.offense_label_1.setWordWrap(True)
        self.offense_label_1.setObjectName("offense_label_1")
        self.charges_gridLayout.addWidget(self.offense_label_1, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.charges_gridLayout, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.banner_frame, 0, 0, 1, 2)
        self.admin_license_suspension_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.admin_license_suspension_frame.setEnabled(False)
        self.admin_license_suspension_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.admin_license_suspension_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.admin_license_suspension_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.admin_license_suspension_frame.setLineWidth(2)
        self.admin_license_suspension_frame.setObjectName("admin_license_suspension_frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.admin_license_suspension_frame)
        self.gridLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_24 = QtWidgets.QLabel(self.admin_license_suspension_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 0, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.admin_license_suspension_frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)
        self.admin_license_suspension_objection_box = QtWidgets.QComboBox(self.admin_license_suspension_frame)
        self.admin_license_suspension_objection_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.admin_license_suspension_objection_box.setObjectName("admin_license_suspension_objection_box")
        self.admin_license_suspension_objection_box.addItem("")
        self.admin_license_suspension_objection_box.addItem("")
        self.gridLayout_7.addWidget(self.admin_license_suspension_objection_box, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.admin_license_suspension_frame)
        self.label_21.setObjectName("label_21")
        self.gridLayout_7.addWidget(self.label_21, 2, 0, 1, 1)
        self.admin_license_suspension_disposition_box = QtWidgets.QComboBox(self.admin_license_suspension_frame)
        self.admin_license_suspension_disposition_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.admin_license_suspension_disposition_box.setObjectName("admin_license_suspension_disposition_box")
        self.admin_license_suspension_disposition_box.addItem("")
        self.admin_license_suspension_disposition_box.addItem("")
        self.gridLayout_7.addWidget(self.admin_license_suspension_disposition_box, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.admin_license_suspension_frame)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 3, 0, 1, 1)
        self.admin_license_suspension_explanation_box = QtWidgets.QLineEdit(self.admin_license_suspension_frame)
        self.admin_license_suspension_explanation_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.admin_license_suspension_explanation_box.setObjectName("admin_license_suspension_explanation_box")
        self.gridLayout_7.addWidget(self.admin_license_suspension_explanation_box, 3, 1, 1, 1)
        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_7.setRowStretch(1, 1)
        self.gridLayout_7.setRowStretch(2, 1)
        self.gridLayout_7.setRowStretch(3, 1)
        self.gridLayout_11.addWidget(self.admin_license_suspension_frame, 1, 0, 1, 2)
        self.domestic_violence_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.domestic_violence_frame.setEnabled(False)
        self.domestic_violence_frame.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.domestic_violence_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.domestic_violence_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.domestic_violence_frame.setObjectName("domestic_violence_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.domestic_violence_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_26 = QtWidgets.QLabel(self.domestic_violence_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 0, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(self.domestic_violence_frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.domestic_violence_exclusive_possession_to_box = QtWidgets.QLineEdit(self.domestic_violence_frame)
        self.domestic_violence_exclusive_possession_to_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.domestic_violence_exclusive_possession_to_box.setObjectName("domestic_violence_exclusive_possession_to_box")
        self.gridLayout_2.addWidget(self.domestic_violence_exclusive_possession_to_box, 2, 1, 1, 2)
        self.domestic_violence_surrender_weapons_checkBox = QtWidgets.QCheckBox(self.domestic_violence_frame)
        self.domestic_violence_surrender_weapons_checkBox.setObjectName("domestic_violence_surrender_weapons_checkBox")
        self.gridLayout_2.addWidget(self.domestic_violence_surrender_weapons_checkBox, 2, 3, 1, 1)
        self.domestic_violence_surrender_weapons_dateBox = QtWidgets.QDateEdit(self.domestic_violence_frame)
        self.domestic_violence_surrender_weapons_dateBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.domestic_violence_surrender_weapons_dateBox.setCalendarPopup(True)
        self.domestic_violence_surrender_weapons_dateBox.setObjectName("domestic_violence_surrender_weapons_dateBox")
        self.gridLayout_2.addWidget(self.domestic_violence_surrender_weapons_dateBox, 2, 4, 1, 1)
        self.domestic_violence_vacate_checkBox = QtWidgets.QCheckBox(self.domestic_violence_frame)
        self.domestic_violence_vacate_checkBox.setObjectName("domestic_violence_vacate_checkBox")
        self.gridLayout_2.addWidget(self.domestic_violence_vacate_checkBox, 1, 0, 1, 1)
        self.domestic_violence_residence_box = QtWidgets.QLineEdit(self.domestic_violence_frame)
        self.domestic_violence_residence_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.domestic_violence_residence_box.setObjectName("domestic_violence_residence_box")
        self.gridLayout_2.addWidget(self.domestic_violence_residence_box, 1, 1, 1, 4)
        self.gridLayout_11.addWidget(self.domestic_violence_frame, 2, 0, 1, 2)
        self.no_contact_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.no_contact_frame.setEnabled(False)
        self.no_contact_frame.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.no_contact_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.no_contact_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.no_contact_frame.setObjectName("no_contact_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.no_contact_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_5 = QtWidgets.QLabel(self.no_contact_frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)
        self.no_contact_name_box = QtWidgets.QLineEdit(self.no_contact_frame)
        self.no_contact_name_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.no_contact_name_box.setObjectName("no_contact_name_box")
        self.gridLayout_6.addWidget(self.no_contact_name_box, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.no_contact_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 0, 0, 1, 2)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 2)
        self.gridLayout_11.addWidget(self.no_contact_frame, 3, 0, 1, 2)
        self.vehicle_seizure_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.vehicle_seizure_frame.setEnabled(False)
        self.vehicle_seizure_frame.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.vehicle_seizure_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vehicle_seizure_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vehicle_seizure_frame.setObjectName("vehicle_seizure_frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.vehicle_seizure_frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_4 = QtWidgets.QLabel(self.vehicle_seizure_frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 1)
        self.vehicle_make_model_box = QtWidgets.QLineEdit(self.vehicle_seizure_frame)
        self.vehicle_make_model_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vehicle_make_model_box.setObjectName("vehicle_make_model_box")
        self.gridLayout_8.addWidget(self.vehicle_make_model_box, 1, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.vehicle_seizure_frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 1, 4, 1, 2)
        self.vehicle_license_plate_box = QtWidgets.QLineEdit(self.vehicle_seizure_frame)
        self.vehicle_license_plate_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vehicle_license_plate_box.setObjectName("vehicle_license_plate_box")
        self.gridLayout_8.addWidget(self.vehicle_license_plate_box, 1, 6, 1, 2)
        self.tow_to_residence_checkBox = QtWidgets.QCheckBox(self.vehicle_seizure_frame)
        self.tow_to_residence_checkBox.setObjectName("tow_to_residence_checkBox")
        self.gridLayout_8.addWidget(self.tow_to_residence_checkBox, 2, 0, 1, 4)
        self.motion_to_return_vehicle_checkBox = QtWidgets.QCheckBox(self.vehicle_seizure_frame)
        self.motion_to_return_vehicle_checkBox.setObjectName("motion_to_return_vehicle_checkBox")
        self.gridLayout_8.addWidget(self.motion_to_return_vehicle_checkBox, 3, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.vehicle_seizure_frame)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 3, 2, 1, 1)
        self.state_opposes_box = QtWidgets.QComboBox(self.vehicle_seizure_frame)
        self.state_opposes_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.state_opposes_box.setObjectName("state_opposes_box")
        self.state_opposes_box.addItem("")
        self.state_opposes_box.addItem("")
        self.gridLayout_8.addWidget(self.state_opposes_box, 3, 3, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.vehicle_seizure_frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 3, 5, 1, 2)
        self.disposition_motion_to_return_box = QtWidgets.QComboBox(self.vehicle_seizure_frame)
        self.disposition_motion_to_return_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.disposition_motion_to_return_box.setObjectName("disposition_motion_to_return_box")
        self.disposition_motion_to_return_box.addItem("")
        self.disposition_motion_to_return_box.addItem("")
        self.gridLayout_8.addWidget(self.disposition_motion_to_return_box, 3, 7, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.vehicle_seizure_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_8.addWidget(self.label_27, 0, 0, 1, 8)
        self.gridLayout_11.addWidget(self.vehicle_seizure_frame, 4, 0, 1, 2)
        self.other_conditions_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.other_conditions_frame.setEnabled(False)
        self.other_conditions_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.other_conditions_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.other_conditions_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.other_conditions_frame.setObjectName("other_conditions_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.other_conditions_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.other_conditions_plainTextEdit = QtWidgets.QPlainTextEdit(self.other_conditions_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.other_conditions_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.other_conditions_plainTextEdit.setSizePolicy(sizePolicy)
        self.other_conditions_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.other_conditions_plainTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.other_conditions_plainTextEdit.setObjectName("other_conditions_plainTextEdit")
        self.gridLayout_3.addWidget(self.other_conditions_plainTextEdit, 1, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.other_conditions_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 0, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 1)
        self.gridLayout_11.addWidget(self.other_conditions_frame, 5, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.cancel_Button = QtWidgets.QPushButton(self.frame_7)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout_10.addWidget(self.cancel_Button, 0, 0, 1, 1)
        self.add_special_conditions_Button = QtWidgets.QPushButton(self.frame_7)
        self.add_special_conditions_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_special_conditions_Button.setAutoDefault(False)
        self.add_special_conditions_Button.setObjectName("add_special_conditions_Button")
        self.gridLayout_10.addWidget(self.add_special_conditions_Button, 1, 0, 1, 1)
        self.gridLayout_11.addWidget(self.frame_7, 5, 1, 2, 1)
        self.custodial_supervision_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.custodial_supervision_frame.setEnabled(False)
        self.custodial_supervision_frame.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.custodial_supervision_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.custodial_supervision_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.custodial_supervision_frame.setObjectName("custodial_supervision_frame")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.custodial_supervision_frame)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_29 = QtWidgets.QLabel(self.custodial_supervision_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_9.addWidget(self.label_29, 0, 0, 1, 2)
        self.custodial_supervision_supervisor_box = QtWidgets.QLineEdit(self.custodial_supervision_frame)
        self.custodial_supervision_supervisor_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.custodial_supervision_supervisor_box.setObjectName("custodial_supervision_supervisor_box")
        self.gridLayout_9.addWidget(self.custodial_supervision_supervisor_box, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.custodial_supervision_frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 1)
        self.gridLayout_11.addWidget(self.custodial_supervision_frame, 6, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(AddSpecialBondConditionsDialog)
        QtCore.QMetaObject.connectSlotsByName(AddSpecialBondConditionsDialog)
        AddSpecialBondConditionsDialog.setTabOrder(self.admin_license_suspension_objection_box, self.admin_license_suspension_disposition_box)
        AddSpecialBondConditionsDialog.setTabOrder(self.admin_license_suspension_disposition_box, self.admin_license_suspension_explanation_box)
        AddSpecialBondConditionsDialog.setTabOrder(self.admin_license_suspension_explanation_box, self.domestic_violence_vacate_checkBox)
        AddSpecialBondConditionsDialog.setTabOrder(self.domestic_violence_vacate_checkBox, self.domestic_violence_residence_box)
        AddSpecialBondConditionsDialog.setTabOrder(self.domestic_violence_residence_box, self.domestic_violence_exclusive_possession_to_box)
        AddSpecialBondConditionsDialog.setTabOrder(self.domestic_violence_exclusive_possession_to_box, self.domestic_violence_surrender_weapons_checkBox)
        AddSpecialBondConditionsDialog.setTabOrder(self.domestic_violence_surrender_weapons_checkBox, self.domestic_violence_surrender_weapons_dateBox)
        AddSpecialBondConditionsDialog.setTabOrder(self.domestic_violence_surrender_weapons_dateBox, self.no_contact_name_box)
        AddSpecialBondConditionsDialog.setTabOrder(self.no_contact_name_box, self.vehicle_make_model_box)
        AddSpecialBondConditionsDialog.setTabOrder(self.vehicle_make_model_box, self.vehicle_license_plate_box)
        AddSpecialBondConditionsDialog.setTabOrder(self.vehicle_license_plate_box, self.tow_to_residence_checkBox)
        AddSpecialBondConditionsDialog.setTabOrder(self.tow_to_residence_checkBox, self.motion_to_return_vehicle_checkBox)
        AddSpecialBondConditionsDialog.setTabOrder(self.motion_to_return_vehicle_checkBox, self.state_opposes_box)
        AddSpecialBondConditionsDialog.setTabOrder(self.state_opposes_box, self.disposition_motion_to_return_box)
        AddSpecialBondConditionsDialog.setTabOrder(self.disposition_motion_to_return_box, self.other_conditions_plainTextEdit)
        AddSpecialBondConditionsDialog.setTabOrder(self.other_conditions_plainTextEdit, self.custodial_supervision_supervisor_box)
        AddSpecialBondConditionsDialog.setTabOrder(self.custodial_supervision_supervisor_box, self.add_special_conditions_Button)
        AddSpecialBondConditionsDialog.setTabOrder(self.add_special_conditions_Button, self.scrollArea)

    def retranslateUi(self, AddSpecialBondConditionsDialog):
        _translate = QtCore.QCoreApplication.translate
        AddSpecialBondConditionsDialog.setWindowTitle(_translate("AddSpecialBondConditionsDialog", "Special Bond Conditions"))
        self.label_19.setText(_translate("AddSpecialBondConditionsDialog", "Statute:"))
        self.offense_label_1.setText(_translate("AddSpecialBondConditionsDialog", "Offense:"))
        self.label_24.setText(_translate("AddSpecialBondConditionsDialog", "Administrative License Suspension"))
        self.label_9.setText(_translate("AddSpecialBondConditionsDialog", "State Objects to Administrative License Suspension:"))
        self.admin_license_suspension_objection_box.setItemText(0, _translate("AddSpecialBondConditionsDialog", "No"))
        self.admin_license_suspension_objection_box.setItemText(1, _translate("AddSpecialBondConditionsDialog", "Yes"))
        self.label_21.setText(_translate("AddSpecialBondConditionsDialog", "Administrative License Suspension:"))
        self.admin_license_suspension_disposition_box.setItemText(0, _translate("AddSpecialBondConditionsDialog", "Granted"))
        self.admin_license_suspension_disposition_box.setItemText(1, _translate("AddSpecialBondConditionsDialog", "Denied"))
        self.label.setText(_translate("AddSpecialBondConditionsDialog", "Explanation of Decision:"))
        self.label_26.setText(_translate("AddSpecialBondConditionsDialog", "Domestic Violence Restrictions"))
        self.label_2.setText(_translate("AddSpecialBondConditionsDialog", "Exclusive possesion to:"))
        self.domestic_violence_surrender_weapons_checkBox.setText(_translate("AddSpecialBondConditionsDialog", "Surrender deadly weapons no later than:"))
        self.domestic_violence_vacate_checkBox.setText(_translate("AddSpecialBondConditionsDialog", "Vacate Residence located at:"))
        self.label_5.setText(_translate("AddSpecialBondConditionsDialog", "No Contact with the Following:"))
        self.label_25.setText(_translate("AddSpecialBondConditionsDialog", "No Contact Restrictions"))
        self.label_4.setText(_translate("AddSpecialBondConditionsDialog", "Vehicle Year/Make/Model:"))
        self.label_3.setText(_translate("AddSpecialBondConditionsDialog", "License Plate Number:"))
        self.tow_to_residence_checkBox.setText(_translate("AddSpecialBondConditionsDialog", "Permit Tow and Immobilization at Defendant\'s Residence"))
        self.motion_to_return_vehicle_checkBox.setText(_translate("AddSpecialBondConditionsDialog", "Motion for return of vehicle Filed."))
        self.label_8.setText(_translate("AddSpecialBondConditionsDialog", "The State:"))
        self.state_opposes_box.setItemText(0, _translate("AddSpecialBondConditionsDialog", "objects"))
        self.state_opposes_box.setItemText(1, _translate("AddSpecialBondConditionsDialog", "does not object"))
        self.label_7.setText(_translate("AddSpecialBondConditionsDialog", "Motion to Return Disposition:"))
        self.disposition_motion_to_return_box.setItemText(0, _translate("AddSpecialBondConditionsDialog", "Denied"))
        self.disposition_motion_to_return_box.setItemText(1, _translate("AddSpecialBondConditionsDialog", "Granted"))
        self.label_27.setText(_translate("AddSpecialBondConditionsDialog", "Vehicle Seizure / Immobilization"))
        self.label_28.setText(_translate("AddSpecialBondConditionsDialog", "Other Conditions"))
        self.cancel_Button.setText(_translate("AddSpecialBondConditionsDialog", "Cancel"))
        self.add_special_conditions_Button.setText(_translate("AddSpecialBondConditionsDialog", "Add Special Bond Conditions"))
        self.label_29.setText(_translate("AddSpecialBondConditionsDialog", "Custodial Supervision"))
        self.label_6.setText(_translate("AddSpecialBondConditionsDialog", "Shall submit to the custody of:"))
