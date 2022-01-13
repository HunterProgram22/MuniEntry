# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views\ui\AddConditionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddConditionsDialog(object):
    def setupUi(self, AddConditionsDialog):
        AddConditionsDialog.setObjectName("AddConditionsDialog")
        AddConditionsDialog.setWindowModality(QtCore.Qt.NonModal)
        AddConditionsDialog.setEnabled(True)
        AddConditionsDialog.resize(1000, 842)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddConditionsDialog.sizePolicy().hasHeightForWidth())
        AddConditionsDialog.setSizePolicy(sizePolicy)
        AddConditionsDialog.setMinimumSize(QtCore.QSize(0, 0))
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
        AddConditionsDialog.setSizeGripEnabled(True)
        AddConditionsDialog.setModal(True)
        self.gridLayout_7 = QtWidgets.QGridLayout(AddConditionsDialog)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollArea = QtWidgets.QScrollArea(AddConditionsDialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 978, 792))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.offense_label_1 = QtWidgets.QLabel(self.frame_2)
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
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.charges_gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.charges_gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.charges_gridLayout, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_2, 0, 0, 1, 2)
        self.license_suspension_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.license_suspension_frame.setEnabled(False)
        self.license_suspension_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.license_suspension_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.license_suspension_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.license_suspension_frame.setLineWidth(2)
        self.license_suspension_frame.setObjectName("license_suspension_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.license_suspension_frame)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_24 = QtWidgets.QLabel(self.license_suspension_frame)
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
        self.gridLayout_2.addWidget(self.label_24, 0, 0, 1, 4)
        self.label_9 = QtWidgets.QLabel(self.license_suspension_frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.license_type_box = QtWidgets.QComboBox(self.license_suspension_frame)
        self.license_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.license_type_box.setObjectName("license_type_box")
        self.license_type_box.addItem("")
        self.license_type_box.addItem("")
        self.license_type_box.addItem("")
        self.gridLayout_2.addWidget(self.license_type_box, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.license_suspension_frame)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 2, 1, 1)
        self.license_suspension_date_box = QtWidgets.QDateEdit(self.license_suspension_frame)
        self.license_suspension_date_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.license_suspension_date_box.setCalendarPopup(True)
        self.license_suspension_date_box.setObjectName("license_suspension_date_box")
        self.gridLayout_2.addWidget(self.license_suspension_date_box, 1, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.license_suspension_frame)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 2, 0, 1, 1)
        self.term_of_suspension_box = QtWidgets.QComboBox(self.license_suspension_frame)
        self.term_of_suspension_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.term_of_suspension_box.setObjectName("term_of_suspension_box")
        self.term_of_suspension_box.addItem("")
        self.term_of_suspension_box.addItem("")
        self.term_of_suspension_box.addItem("")
        self.term_of_suspension_box.addItem("")
        self.gridLayout_2.addWidget(self.term_of_suspension_box, 2, 1, 1, 1)
        self.remedial_driving_class_checkBox = QtWidgets.QCheckBox(self.license_suspension_frame)
        self.remedial_driving_class_checkBox.setObjectName("remedial_driving_class_checkBox")
        self.gridLayout_2.addWidget(self.remedial_driving_class_checkBox, 2, 2, 1, 2)
        self.gridLayout_6.addWidget(self.license_suspension_frame, 1, 0, 1, 2)
        self.community_service_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.community_service_frame.setEnabled(False)
        self.community_service_frame.setMaximumSize(QtCore.QSize(16777215, 300))
        self.community_service_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.community_service_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.community_service_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.community_service_frame.setLineWidth(2)
        self.community_service_frame.setObjectName("community_service_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.community_service_frame)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_26 = QtWidgets.QLabel(self.community_service_frame)
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
        self.gridLayout.addWidget(self.label_26, 0, 0, 1, 6)
        self.label = QtWidgets.QLabel(self.community_service_frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.community_service_days_to_complete_box = QtWidgets.QComboBox(self.community_service_frame)
        self.community_service_days_to_complete_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.community_service_days_to_complete_box.setObjectName("community_service_days_to_complete_box")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.community_service_days_to_complete_box.addItem("")
        self.gridLayout.addWidget(self.community_service_days_to_complete_box, 1, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.community_service_frame)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 1, 4, 1, 1)
        self.community_service_date_to_complete_box = QtWidgets.QDateEdit(self.community_service_frame)
        self.community_service_date_to_complete_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.community_service_date_to_complete_box.setCalendarPopup(True)
        self.community_service_date_to_complete_box.setObjectName("community_service_date_to_complete_box")
        self.gridLayout.addWidget(self.community_service_date_to_complete_box, 1, 5, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.community_service_frame)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)
        self.community_service_hours_ordered_box = QtWidgets.QComboBox(self.community_service_frame)
        self.community_service_hours_ordered_box.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.community_service_hours_ordered_box.setEditable(True)
        self.community_service_hours_ordered_box.setObjectName("community_service_hours_ordered_box")
        self.community_service_hours_ordered_box.addItem("")
        self.community_service_hours_ordered_box.setItemText(0, "")
        self.community_service_hours_ordered_box.addItem("")
        self.community_service_hours_ordered_box.addItem("")
        self.community_service_hours_ordered_box.addItem("")
        self.community_service_hours_ordered_box.addItem("")
        self.community_service_hours_ordered_box.addItem("")
        self.gridLayout.addWidget(self.community_service_hours_ordered_box, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.community_service_frame, 2, 0, 1, 2)
        self.other_conditions_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.other_conditions_frame.setEnabled(False)
        self.other_conditions_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.other_conditions_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.other_conditions_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.other_conditions_frame.setObjectName("other_conditions_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.other_conditions_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.other_conditions_textEdit = QtWidgets.QTextEdit(self.other_conditions_frame)
        self.other_conditions_textEdit.setObjectName("other_conditions_textEdit")
        self.gridLayout_3.addWidget(self.other_conditions_textEdit, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.other_conditions_frame, 3, 0, 1, 2)
        self.cancel_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout_6.addWidget(self.cancel_Button, 4, 0, 1, 1)
        self.add_conditions_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.add_conditions_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_conditions_Button.setAutoDefault(False)
        self.add_conditions_Button.setObjectName("add_conditions_Button")
        self.gridLayout_6.addWidget(self.add_conditions_Button, 4, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_7.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(AddConditionsDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_7.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(AddConditionsDialog)
        QtCore.QMetaObject.connectSlotsByName(AddConditionsDialog)

    def retranslateUi(self, AddConditionsDialog):
        _translate = QtCore.QCoreApplication.translate
        AddConditionsDialog.setWindowTitle(_translate("AddConditionsDialog", "Additional Conditions"))
        self.offense_label_1.setText(_translate("AddConditionsDialog", "Offense:"))
        self.label_14.setText(_translate("AddConditionsDialog", "Finding:"))
        self.label_19.setText(_translate("AddConditionsDialog", "Statute:"))
        self.label_24.setText(_translate("AddConditionsDialog", "License Suspension"))
        self.label_9.setText(_translate("AddConditionsDialog", "License type:"))
        self.license_type_box.setItemText(0, _translate("AddConditionsDialog", "driving"))
        self.license_type_box.setItemText(1, _translate("AddConditionsDialog", "hunting"))
        self.license_type_box.setItemText(2, _translate("AddConditionsDialog", "concealed carry"))
        self.label_18.setText(_translate("AddConditionsDialog", "License suspended from:"))
        self.label_21.setText(_translate("AddConditionsDialog", "Term of suspension:"))
        self.term_of_suspension_box.setItemText(0, _translate("AddConditionsDialog", "6 months"))
        self.term_of_suspension_box.setItemText(1, _translate("AddConditionsDialog", "12 months"))
        self.term_of_suspension_box.setItemText(2, _translate("AddConditionsDialog", "18 months"))
        self.term_of_suspension_box.setItemText(3, _translate("AddConditionsDialog", "24 months"))
        self.remedial_driving_class_checkBox.setText(_translate("AddConditionsDialog", "Remedial driving class required for OL return"))
        self.label_26.setText(_translate("AddConditionsDialog", "Community Service"))
        self.label.setText(_translate("AddConditionsDialog", "Days to Complete:"))
        self.community_service_days_to_complete_box.setItemText(0, _translate("AddConditionsDialog", "0"))
        self.community_service_days_to_complete_box.setItemText(1, _translate("AddConditionsDialog", "30"))
        self.community_service_days_to_complete_box.setItemText(2, _translate("AddConditionsDialog", "60"))
        self.community_service_days_to_complete_box.setItemText(3, _translate("AddConditionsDialog", "90"))
        self.community_service_days_to_complete_box.setItemText(4, _translate("AddConditionsDialog", "120"))
        self.community_service_days_to_complete_box.setItemText(5, _translate("AddConditionsDialog", "150"))
        self.community_service_days_to_complete_box.setItemText(6, _translate("AddConditionsDialog", "180"))
        self.label_22.setText(_translate("AddConditionsDialog", "Date to Complete:"))
        self.label_15.setText(_translate("AddConditionsDialog", "Hours:"))
        self.community_service_hours_ordered_box.setItemText(1, _translate("AddConditionsDialog", "25"))
        self.community_service_hours_ordered_box.setItemText(2, _translate("AddConditionsDialog", "50"))
        self.community_service_hours_ordered_box.setItemText(3, _translate("AddConditionsDialog", "100"))
        self.community_service_hours_ordered_box.setItemText(4, _translate("AddConditionsDialog", "200"))
        self.community_service_hours_ordered_box.setItemText(5, _translate("AddConditionsDialog", "500"))
        self.label_28.setText(_translate("AddConditionsDialog", "Other Conditions"))
        self.cancel_Button.setText(_translate("AddConditionsDialog", "Cancel"))
        self.add_conditions_Button.setText(_translate("AddConditionsDialog", "Add Conditions"))
