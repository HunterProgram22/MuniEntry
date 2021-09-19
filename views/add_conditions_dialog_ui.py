# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/AddConditionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddConditionsDialog(object):
    def setupUi(self, AddConditionsDialog):
        AddConditionsDialog.setObjectName("AddConditionsDialog")
        AddConditionsDialog.setWindowModality(QtCore.Qt.NonModal)
        AddConditionsDialog.resize(1000, 842)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddConditionsDialog.sizePolicy().hasHeightForWidth())
        AddConditionsDialog.setSizePolicy(sizePolicy)
        AddConditionsDialog.setMinimumSize(QtCore.QSize(1000, 800))
        AddConditionsDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        AddConditionsDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        AddConditionsDialog.setFont(font)
        AddConditionsDialog.setToolTip("")
        AddConditionsDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        AddConditionsDialog.setModal(True)
        self.frame_2 = QtWidgets.QFrame(AddConditionsDialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 981, 291))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 961, 266))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.charges_gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.charges_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.charges_gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.plea_label_1 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.plea_label_1.setFont(font)
        self.plea_label_1.setObjectName("plea_label_1")
        self.charges_gridLayout.addWidget(self.plea_label_1, 3, 0, 1, 1)
        self.offense_label_1 = QtWidgets.QLabel(self.layoutWidget_2)
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
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.charges_gridLayout.addWidget(self.label_16, 7, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.charges_gridLayout.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.charges_gridLayout.addWidget(self.label_17, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.charges_gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.charges_gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.charges_gridLayout.addWidget(self.label_25, 8, 0, 1, 1)
        self.createEntryButton_2 = QtWidgets.QPushButton(AddConditionsDialog)
        self.createEntryButton_2.setGeometry(QtCore.QRect(810, 800, 181, 31))
        self.createEntryButton_2.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.createEntryButton_2.setAutoDefault(False)
        self.createEntryButton_2.setObjectName("createEntryButton_2")
        self.frame_4 = QtWidgets.QFrame(AddConditionsDialog)
        self.frame_4.setGeometry(QtCore.QRect(10, 310, 981, 161))
        self.frame_4.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.frame_4.setObjectName("frame_4")
        self.label_24 = QtWidgets.QLabel(self.frame_4)
        self.label_24.setGeometry(QtCore.QRect(10, 10, 961, 21))
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
        self.remedial_driving_class_checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.remedial_driving_class_checkBox.setGeometry(QtCore.QRect(500, 114, 471, 31))
        self.remedial_driving_class_checkBox.setObjectName("remedial_driving_class_checkBox")
        self.layoutWidget = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 471, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.license_type_box = QtWidgets.QComboBox(self.layoutWidget)
        self.license_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.license_type_box.setObjectName("license_type_box")
        self.license_type_box.addItem("")
        self.license_type_box.addItem("")
        self.license_type_box.addItem("")
        self.license_type_box.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.license_type_box)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.license_suspension_date_box = QtWidgets.QDateEdit(self.layoutWidget)
        self.license_suspension_date_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.license_suspension_date_box.setObjectName("license_suspension_date_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.license_suspension_date_box)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.term_of_suspension_box = QtWidgets.QComboBox(self.layoutWidget)
        self.term_of_suspension_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.term_of_suspension_box.setObjectName("term_of_suspension_box")
        self.term_of_suspension_box.addItem("")
        self.term_of_suspension_box.addItem("")
        self.term_of_suspension_box.addItem("")
        self.term_of_suspension_box.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.term_of_suspension_box)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(500, 42, 471, 64))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.driving_privileges_type_box = QtWidgets.QComboBox(self.layoutWidget1)
        self.driving_privileges_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.driving_privileges_type_box.setObjectName("driving_privileges_type_box")
        self.driving_privileges_type_box.addItem("")
        self.driving_privileges_type_box.addItem("")
        self.driving_privileges_type_box.addItem("")
        self.driving_privileges_type_box.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.driving_privileges_type_box)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.term_of_privileges_box = QtWidgets.QComboBox(self.layoutWidget1)
        self.term_of_privileges_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.term_of_privileges_box.setObjectName("term_of_privileges_box")
        self.term_of_privileges_box.addItem("")
        self.term_of_privileges_box.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.term_of_privileges_box)
        self.frame_5 = QtWidgets.QFrame(AddConditionsDialog)
        self.frame_5.setGeometry(QtCore.QRect(10, 480, 981, 121))
        self.frame_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.label_26 = QtWidgets.QLabel(self.frame_5)
        self.label_26.setGeometry(QtCore.QRect(10, 10, 961, 21))
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
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_5)
        self.layoutWidget2.setGeometry(QtCore.QRect(310, 40, 451, 64))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.community_service_days_to_complete_box = QtWidgets.QComboBox(self.layoutWidget2)
        self.community_service_days_to_complete_box.setObjectName("community_service_days_to_complete_box")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.community_service_days_to_complete_box)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_22.setObjectName("label_22")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.community_service_date_to_complete_box = QtWidgets.QDateEdit(self.layoutWidget2)
        self.community_service_date_to_complete_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.community_service_date_to_complete_box.setObjectName("community_service_date_to_complete_box")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.community_service_date_to_complete_box)
        self.layoutWidget3 = QtWidgets.QWidget(self.frame_5)
        self.layoutWidget3.setGeometry(QtCore.QRect(12, 38, 261, 64))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.community_service_ordered_box = QtWidgets.QComboBox(self.layoutWidget3)
        self.community_service_ordered_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.community_service_ordered_box.setObjectName("community_service_ordered_box")
        self.community_service_ordered_box.addItem("")
        self.community_service_ordered_box.addItem("")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.community_service_ordered_box)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.community_service_hours_ordered_box = QtWidgets.QSpinBox(self.layoutWidget3)
        self.community_service_hours_ordered_box.setObjectName("community_service_hours_ordered_box")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.community_service_hours_ordered_box)
        self.frame_6 = QtWidgets.QFrame(AddConditionsDialog)
        self.frame_6.setGeometry(QtCore.QRect(10, 610, 981, 121))
        self.frame_6.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        self.label_27.setGeometry(QtCore.QRect(10, 10, 961, 21))
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
        self.layoutWidget_3 = QtWidgets.QWidget(self.frame_6)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 40, 471, 71))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.formLayout_5 = QtWidgets.QFormLayout(self.layoutWidget_3)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_23.setObjectName("label_23")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.type_of_community_control_box = QtWidgets.QComboBox(self.layoutWidget_3)
        self.type_of_community_control_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.type_of_community_control_box.setObjectName("type_of_community_control_box")
        self.type_of_community_control_box.addItem("")
        self.type_of_community_control_box.addItem("")
        self.type_of_community_control_box.addItem("")
        self.type_of_community_control_box.addItem("")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.type_of_community_control_box)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_29.setObjectName("label_29")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.term_of_community_control_box = QtWidgets.QComboBox(self.layoutWidget_3)
        self.term_of_community_control_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.term_of_community_control_box.setObjectName("term_of_community_control_box")
        self.term_of_community_control_box.addItem("")
        self.term_of_community_control_box.addItem("")
        self.term_of_community_control_box.addItem("")
        self.term_of_community_control_box.addItem("")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.term_of_community_control_box)
        self.createEntryButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.createEntryButton_3.setEnabled(False)
        self.createEntryButton_3.setGeometry(QtCore.QRect(790, 80, 181, 31))
        self.createEntryButton_3.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.createEntryButton_3.setAutoDefault(False)
        self.createEntryButton_3.setObjectName("createEntryButton_3")

        self.retranslateUi(AddConditionsDialog)
        self.createEntryButton_2.clicked.connect(AddConditionsDialog.add_conditions)
        self.createEntryButton_2.released.connect(AddConditionsDialog.close_window)
        QtCore.QMetaObject.connectSlotsByName(AddConditionsDialog)

    def retranslateUi(self, AddConditionsDialog):
        _translate = QtCore.QCoreApplication.translate
        AddConditionsDialog.setWindowTitle(_translate("AddConditionsDialog", "Additional Conditions"))
        self.label_20.setText(_translate("AddConditionsDialog", "Degree:"))
        self.plea_label_1.setText(_translate("AddConditionsDialog", "Plea:"))
        self.offense_label_1.setText(_translate("AddConditionsDialog", "Offense:"))
        self.label_16.setText(_translate("AddConditionsDialog", "Court Costs:"))
        self.label_14.setText(_translate("AddConditionsDialog", "Finding:"))
        self.label_17.setText(_translate("AddConditionsDialog", "Fines:"))
        self.label_10.setText(_translate("AddConditionsDialog", "Fines Suspended:"))
        self.label_19.setText(_translate("AddConditionsDialog", "Statute:"))
        self.createEntryButton_2.setText(_translate("AddConditionsDialog", "Continue"))
        self.label_24.setText(_translate("AddConditionsDialog", "License Suspension"))
        self.remedial_driving_class_checkBox.setText(_translate("AddConditionsDialog", "Remedial driving class required for OL return"))
        self.label_9.setText(_translate("AddConditionsDialog", "License type:"))
        self.license_type_box.setItemText(0, _translate("AddConditionsDialog", "None"))
        self.license_type_box.setItemText(1, _translate("AddConditionsDialog", "driving"))
        self.license_type_box.setItemText(2, _translate("AddConditionsDialog", "hunting"))
        self.license_type_box.setItemText(3, _translate("AddConditionsDialog", "concealed carry"))
        self.label_18.setText(_translate("AddConditionsDialog", "License suspended from:"))
        self.label_21.setText(_translate("AddConditionsDialog", "Term of suspension:"))
        self.term_of_suspension_box.setItemText(0, _translate("AddConditionsDialog", "6 months"))
        self.term_of_suspension_box.setItemText(1, _translate("AddConditionsDialog", "12 months"))
        self.term_of_suspension_box.setItemText(2, _translate("AddConditionsDialog", "18 months"))
        self.term_of_suspension_box.setItemText(3, _translate("AddConditionsDialog", "24 months"))
        self.label_11.setText(_translate("AddConditionsDialog", "Driving privileges:"))
        self.driving_privileges_type_box.setItemText(0, _translate("AddConditionsDialog", "None"))
        self.driving_privileges_type_box.setItemText(1, _translate("AddConditionsDialog", "Unlimited - CIID"))
        self.driving_privileges_type_box.setItemText(2, _translate("AddConditionsDialog", "Unlimited reduced-fee CIID"))
        self.driving_privileges_type_box.setItemText(3, _translate("AddConditionsDialog", "Limited"))
        self.label_12.setText(_translate("AddConditionsDialog", "Term of privileges:"))
        self.term_of_privileges_box.setItemText(0, _translate("AddConditionsDialog", "30 days"))
        self.term_of_privileges_box.setItemText(1, _translate("AddConditionsDialog", "Unlimited"))
        self.label_26.setText(_translate("AddConditionsDialog", "Community Service"))
        self.label.setText(_translate("AddConditionsDialog", "Days to Complete Service:"))
        self.community_service_days_to_complete_box.setItemText(0, _translate("AddConditionsDialog", "30"))
        self.community_service_days_to_complete_box.setItemText(1, _translate("AddConditionsDialog", "60"))
        self.community_service_days_to_complete_box.setItemText(2, _translate("AddConditionsDialog", "90"))
        self.community_service_days_to_complete_box.setItemText(3, _translate("AddConditionsDialog", "120"))
        self.community_service_days_to_complete_box.setItemText(4, _translate("AddConditionsDialog", "150"))
        self.community_service_days_to_complete_box.setItemText(5, _translate("AddConditionsDialog", "180"))
        self.label_22.setText(_translate("AddConditionsDialog", "Date to Complete Service:"))
        self.label_13.setText(_translate("AddConditionsDialog", "Community Service:"))
        self.community_service_ordered_box.setItemText(0, _translate("AddConditionsDialog", "No"))
        self.community_service_ordered_box.setItemText(1, _translate("AddConditionsDialog", "Yes"))
        self.label_15.setText(_translate("AddConditionsDialog", "Hours of Service:"))
        self.label_27.setText(_translate("AddConditionsDialog", "Community Control"))
        self.label_23.setText(_translate("AddConditionsDialog", "Community Control Type:"))
        self.type_of_community_control_box.setItemText(0, _translate("AddConditionsDialog", "None"))
        self.type_of_community_control_box.setItemText(1, _translate("AddConditionsDialog", "basic"))
        self.type_of_community_control_box.setItemText(2, _translate("AddConditionsDialog", "intensive"))
        self.type_of_community_control_box.setItemText(3, _translate("AddConditionsDialog", "monitored"))
        self.label_29.setText(_translate("AddConditionsDialog", "Term of Community Control:"))
        self.term_of_community_control_box.setItemText(0, _translate("AddConditionsDialog", "6 months"))
        self.term_of_community_control_box.setItemText(1, _translate("AddConditionsDialog", "12 months"))
        self.term_of_community_control_box.setItemText(2, _translate("AddConditionsDialog", "18 months"))
        self.term_of_community_control_box.setItemText(3, _translate("AddConditionsDialog", "24 months"))
        self.createEntryButton_3.setText(_translate("AddConditionsDialog", "Add CC Terms"))
