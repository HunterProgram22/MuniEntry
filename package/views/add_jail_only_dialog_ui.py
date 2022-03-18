# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package\views\ui\AddJailOnlyDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddJailOnly(object):
    def setupUi(self, AddJailOnly):
        AddJailOnly.setObjectName("AddJailOnly")
        AddJailOnly.setWindowModality(QtCore.Qt.NonModal)
        AddJailOnly.setEnabled(True)
        AddJailOnly.resize(1000, 627)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddJailOnly.sizePolicy().hasHeightForWidth())
        AddJailOnly.setSizePolicy(sizePolicy)
        AddJailOnly.setMinimumSize(QtCore.QSize(0, 0))
        AddJailOnly.setMaximumSize(QtCore.QSize(2500, 3500))
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
        AddJailOnly.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        AddJailOnly.setFont(font)
        AddJailOnly.setToolTip("")
        AddJailOnly.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        AddJailOnly.setSizeGripEnabled(True)
        AddJailOnly.setModal(True)
        self.gridLayout_7 = QtWidgets.QGridLayout(AddJailOnly)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollArea = QtWidgets.QScrollArea(AddJailOnly)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 980, 607))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.case_banner_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.case_banner_frame.setMaximumSize(QtCore.QSize(16777215, 110))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.case_banner_frame.setFont(font)
        self.case_banner_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.case_banner_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_banner_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.case_banner_frame.setLineWidth(2)
        self.case_banner_frame.setObjectName("case_banner_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.case_banner_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.charges_gridLayout = QtWidgets.QGridLayout()
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.offense_label_1 = QtWidgets.QLabel(self.case_banner_frame)
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
        self.label_14 = QtWidgets.QLabel(self.case_banner_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.charges_gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.case_banner_frame)
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
        self.gridLayout_5.addWidget(self.case_banner_frame, 0, 0, 1, 1)
        self.jail_commitment_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.jail_commitment_frame.setEnabled(True)
        self.jail_commitment_frame.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.jail_commitment_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.jail_commitment_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.jail_commitment_frame.setLineWidth(2)
        self.jail_commitment_frame.setObjectName("jail_commitment_frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.jail_commitment_frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_10 = QtWidgets.QLabel(self.jail_commitment_frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 2, 0, 1, 1)
        self.jail_report_days_notes_box = QtWidgets.QLineEdit(self.jail_commitment_frame)
        self.jail_report_days_notes_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jail_report_days_notes_box.setObjectName("jail_report_days_notes_box")
        self.gridLayout_6.addWidget(self.jail_report_days_notes_box, 6, 1, 1, 1)
        self.report_date_label = QtWidgets.QLabel(self.jail_commitment_frame)
        self.report_date_label.setObjectName("report_date_label")
        self.gridLayout_6.addWidget(self.report_date_label, 3, 0, 1, 1)
        self.report_date_box = QtWidgets.QDateEdit(self.jail_commitment_frame)
        self.report_date_box.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.report_date_box.setCalendarPopup(True)
        self.report_date_box.setObjectName("report_date_box")
        self.gridLayout_6.addWidget(self.report_date_box, 3, 1, 1, 1)
        self.report_type_box = QtWidgets.QComboBox(self.jail_commitment_frame)
        self.report_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.report_type_box.setObjectName("report_type_box")
        self.report_type_box.addItem("")
        self.report_type_box.addItem("")
        self.report_type_box.addItem("")
        self.gridLayout_6.addWidget(self.report_type_box, 2, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.jail_commitment_frame)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_6.addWidget(self.line_5, 7, 0, 1, 2)
        self.report_time_label = QtWidgets.QLabel(self.jail_commitment_frame)
        self.report_time_label.setObjectName("report_time_label")
        self.gridLayout_6.addWidget(self.report_time_label, 4, 0, 1, 1)
        self.report_time_box = QtWidgets.QTimeEdit(self.jail_commitment_frame)
        self.report_time_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.report_time_box.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 30, 0)))
        self.report_time_box.setObjectName("report_time_box")
        self.gridLayout_6.addWidget(self.report_time_box, 4, 1, 1, 1)
        self.jail_sentence_execution_type_box = QtWidgets.QComboBox(self.jail_commitment_frame)
        self.jail_sentence_execution_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jail_sentence_execution_type_box.setObjectName("jail_sentence_execution_type_box")
        self.jail_sentence_execution_type_box.addItem("")
        self.jail_sentence_execution_type_box.addItem("")
        self.jail_sentence_execution_type_box.addItem("")
        self.gridLayout_6.addWidget(self.jail_sentence_execution_type_box, 5, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.jail_commitment_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 100))
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
        self.gridLayout_6.addWidget(self.label_27, 0, 0, 1, 4)
        self.jail_term_type_box = QtWidgets.QComboBox(self.jail_commitment_frame)
        self.jail_term_type_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.jail_term_type_box.setObjectName("jail_term_type_box")
        self.jail_term_type_box.addItem("")
        self.jail_term_type_box.addItem("")
        self.gridLayout_6.addWidget(self.jail_term_type_box, 9, 1, 1, 1)
        self.consecutive_jail_days_label = QtWidgets.QLabel(self.jail_commitment_frame)
        self.consecutive_jail_days_label.setObjectName("consecutive_jail_days_label")
        self.gridLayout_6.addWidget(self.consecutive_jail_days_label, 9, 0, 1, 1)
        self.companion_cases_checkBox = QtWidgets.QCheckBox(self.jail_commitment_frame)
        self.companion_cases_checkBox.setObjectName("companion_cases_checkBox")
        self.gridLayout_6.addWidget(self.companion_cases_checkBox, 8, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.jail_commitment_frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 5, 0, 1, 1)
        self.companion_cases_box = QtWidgets.QLineEdit(self.jail_commitment_frame)
        self.companion_cases_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.companion_cases_box.setObjectName("companion_cases_box")
        self.gridLayout_6.addWidget(self.companion_cases_box, 8, 1, 1, 1)
        self.gridLayout_6.setColumnStretch(0, 2)
        self.gridLayout_6.setRowStretch(0, 2)
        self.gridLayout_5.addWidget(self.jail_commitment_frame, 1, 0, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.cancel_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout_5.addWidget(self.cancel_Button, 3, 0, 1, 1)
        self.add_conditions_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.add_conditions_Button.setStyleSheet("background-color: rgb(62, 146, 255)")
        self.add_conditions_Button.setAutoDefault(False)
        self.add_conditions_Button.setObjectName("add_conditions_Button")
        self.gridLayout_5.addWidget(self.add_conditions_Button, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_7.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(AddJailOnly)
        QtCore.QMetaObject.connectSlotsByName(AddJailOnly)
        AddJailOnly.setTabOrder(self.report_type_box, self.report_date_box)
        AddJailOnly.setTabOrder(self.report_date_box, self.jail_sentence_execution_type_box)
        AddJailOnly.setTabOrder(self.jail_sentence_execution_type_box, self.jail_term_type_box)

    def retranslateUi(self, AddJailOnly):
        _translate = QtCore.QCoreApplication.translate
        AddJailOnly.setWindowTitle(_translate("AddJailOnly", "Jail Reporting Terms"))
        self.offense_label_1.setText(_translate("AddJailOnly", "Offense:"))
        self.label_14.setText(_translate("AddJailOnly", "Finding:"))
        self.label_19.setText(_translate("AddJailOnly", "Statute:"))
        self.label_10.setText(_translate("AddJailOnly", "Report Type:"))
        self.jail_report_days_notes_box.setPlaceholderText(_translate("AddJailOnly", "Jail report days if not consecutive"))
        self.report_date_label.setText(_translate("AddJailOnly", "Report Date:"))
        self.report_type_box.setItemText(0, _translate("AddJailOnly", "future date"))
        self.report_type_box.setItemText(1, _translate("AddJailOnly", "forthwith"))
        self.report_type_box.setItemText(2, _translate("AddJailOnly", "date set by Office of Community Control"))
        self.report_time_label.setText(_translate("AddJailOnly", "Report Time:"))
        self.jail_sentence_execution_type_box.setItemText(0, _translate("AddJailOnly", "consecutive days"))
        self.jail_sentence_execution_type_box.setItemText(1, _translate("AddJailOnly", "intermittent days"))
        self.jail_sentence_execution_type_box.setItemText(2, _translate("AddJailOnly", "weekends (Friday evening to Monday morning)"))
        self.label_27.setText(_translate("AddJailOnly", "JAIL COMMITMENT"))
        self.jail_term_type_box.setItemText(0, _translate("AddJailOnly", "concurrently"))
        self.jail_term_type_box.setItemText(1, _translate("AddJailOnly", "consecutively"))
        self.consecutive_jail_days_label.setText(_translate("AddJailOnly", "Jail Days in this Case to be Served Concurrent / Consecutive w/ Companion Cases:"))
        self.companion_cases_checkBox.setText(_translate("AddJailOnly", "Companion Cases (Check only if applicable)"))
        self.label_11.setText(_translate("AddJailOnly", "Type of Sentence Execution:"))
        self.companion_cases_box.setPlaceholderText(_translate("AddJailOnly", "Companion Case Nos."))
        self.cancel_Button.setText(_translate("AddJailOnly", "Cancel"))
        self.add_conditions_Button.setText(_translate("AddJailOnly", "Add Jail Reporting Terms"))
