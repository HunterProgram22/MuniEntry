# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/TrafficCaseInformationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrafficCaseInformationDialog(object):
    def setupUi(self, TrafficCaseInformationDialog):
        TrafficCaseInformationDialog.setObjectName("TrafficCaseInformationDialog")
        TrafficCaseInformationDialog.setWindowModality(QtCore.Qt.NonModal)
        TrafficCaseInformationDialog.resize(1000, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TrafficCaseInformationDialog.sizePolicy().hasHeightForWidth())
        TrafficCaseInformationDialog.setSizePolicy(sizePolicy)
        TrafficCaseInformationDialog.setMinimumSize(QtCore.QSize(1000, 750))
        TrafficCaseInformationDialog.setMaximumSize(QtCore.QSize(2500, 3500))
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
        TrafficCaseInformationDialog.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        TrafficCaseInformationDialog.setFont(font)
        TrafficCaseInformationDialog.setToolTip("")
        TrafficCaseInformationDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        TrafficCaseInformationDialog.setModal(True)
        self.frame = QtWidgets.QFrame(TrafficCaseInformationDialog)
        self.frame.setGeometry(QtCore.QRect(10, 130, 981, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(833, 10, 141, 136))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.amendOffenseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.amendOffenseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.amendOffenseButton.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.amendOffenseButton.setObjectName("amendOffenseButton")
        self.gridLayout.addWidget(self.amendOffenseButton, 0, 0, 1, 1)
        self.addOffenseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addOffenseButton.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.addOffenseButton.setObjectName("addOffenseButton")
        self.gridLayout.addWidget(self.addOffenseButton, 1, 0, 1, 1)
        self.deleteOffenseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteOffenseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteOffenseButton.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.deleteOffenseButton.setObjectName("deleteOffenseButton")
        self.gridLayout.addWidget(self.deleteOffenseButton, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(11, 11, 811, 128))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.offense_choice_box = QtWidgets.QComboBox(self.widget)
        self.offense_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.offense_choice_box.setEditable(True)
        self.offense_choice_box.setObjectName("offense_choice_box")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.offense_choice_box)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.statute_choice_box = QtWidgets.QComboBox(self.widget)
        self.statute_choice_box.setEnabled(True)
        self.statute_choice_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.statute_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.statute_choice_box.setEditable(True)
        self.statute_choice_box.setObjectName("statute_choice_box")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.statute_choice_box)
        self.gridLayout_3.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setObjectName("label_23")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.degree_choice_box = QtWidgets.QComboBox(self.widget)
        self.degree_choice_box.setEnabled(True)
        self.degree_choice_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.degree_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.degree_choice_box.setObjectName("degree_choice_box")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.degree_choice_box)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.court_costs_box = QtWidgets.QComboBox(self.widget)
        self.court_costs_box.setMaximumSize(QtCore.QSize(16770, 16777215))
        self.court_costs_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.court_costs_box.setEditable(False)
        self.court_costs_box.setObjectName("court_costs_box")
        self.court_costs_box.addItem("")
        self.court_costs_box.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.court_costs_box)
        self.gridLayout_3.addLayout(self.formLayout, 0, 1, 1, 1)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.plea_choice_box = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plea_choice_box.sizePolicy().hasHeightForWidth())
        self.plea_choice_box.setSizePolicy(sizePolicy)
        self.plea_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.plea_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_choice_box.setEditable(False)
        self.plea_choice_box.setObjectName("plea_choice_box")
        self.plea_choice_box.addItem("")
        self.plea_choice_box.setItemText(0, "")
        self.plea_choice_box.addItem("")
        self.plea_choice_box.addItem("")
        self.plea_choice_box.addItem("")
        self.plea_choice_box.addItem("")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plea_choice_box)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.finding_choice_box = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finding_choice_box.sizePolicy().hasHeightForWidth())
        self.finding_choice_box.setSizePolicy(sizePolicy)
        self.finding_choice_box.setMinimumSize(QtCore.QSize(300, 0))
        self.finding_choice_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.finding_choice_box.setEditable(False)
        self.finding_choice_box.setObjectName("finding_choice_box")
        self.finding_choice_box.addItem("")
        self.finding_choice_box.setItemText(0, "")
        self.finding_choice_box.addItem("")
        self.finding_choice_box.addItem("")
        self.finding_choice_box.addItem("")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.finding_choice_box)
        self.gridLayout_3.addLayout(self.formLayout_6, 1, 0, 1, 1)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.fines_amount = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fines_amount.sizePolicy().hasHeightForWidth())
        self.fines_amount.setSizePolicy(sizePolicy)
        self.fines_amount.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fines_amount.setObjectName("fines_amount")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fines_amount)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.fines_suspended = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fines_suspended.sizePolicy().hasHeightForWidth())
        self.fines_suspended.setSizePolicy(sizePolicy)
        self.fines_suspended.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fines_suspended.setObjectName("fines_suspended")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fines_suspended)
        self.gridLayout_3.addLayout(self.formLayout_5, 1, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.frame_2 = QtWidgets.QFrame(TrafficCaseInformationDialog)
        self.frame_2.setGeometry(QtCore.QRect(10, 290, 981, 251))
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
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 961, 231))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.charges_gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.charges_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.charges_gridLayout.setObjectName("charges_gridLayout")
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
        self.frame_3 = QtWidgets.QFrame(TrafficCaseInformationDialog)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 981, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border-color: rgb(160, 48, 35);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 70, 121, 30))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 11, 471, 93))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.plea_trial_date = QtWidgets.QDateEdit(self.layoutWidget1)
        self.plea_trial_date.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plea_trial_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plea_trial_date)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.case_number = QtWidgets.QLineEdit(self.layoutWidget1)
        self.case_number.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.case_number.setObjectName("case_number")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.case_number)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.defendant_name = QtWidgets.QLineEdit(self.layoutWidget1)
        self.defendant_name.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_name.setObjectName("defendant_name")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.defendant_name)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(490, 12, 353, 60))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.defendant_attorney_name = QtWidgets.QLineEdit(self.layoutWidget2)
        self.defendant_attorney_name.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_attorney_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.defendant_attorney_name.setObjectName("defendant_attorney_name")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.defendant_attorney_name)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setToolTip("")
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget2)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1980, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.frame_4 = QtWidgets.QFrame(TrafficCaseInformationDialog)
        self.frame_4.setGeometry(QtCore.QRect(10, 550, 611, 91))
        self.frame_4.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.frame_4.setObjectName("frame_4")
        self.layoutWidget_3 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 591, 74))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ability_to_pay_box = QtWidgets.QComboBox(self.layoutWidget_3)
        self.ability_to_pay_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ability_to_pay_box.setObjectName("ability_to_pay_box")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.gridLayout_2.addWidget(self.ability_to_pay_box, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)
        self.balance_due_date = QtWidgets.QDateEdit(self.layoutWidget_3)
        self.balance_due_date.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.balance_due_date.setObjectName("balance_due_date")
        self.gridLayout_2.addWidget(self.balance_due_date, 1, 1, 1, 1)
        self.createEntryButton = QtWidgets.QPushButton(TrafficCaseInformationDialog)
        self.createEntryButton.setGeometry(QtCore.QRect(810, 700, 181, 31))
        self.createEntryButton.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"background-color: rgb(160, 160, 160);")
        self.createEntryButton.setAutoDefault(False)
        self.createEntryButton.setObjectName("createEntryButton")
        self.frame_5 = QtWidgets.QFrame(TrafficCaseInformationDialog)
        self.frame_5.setGeometry(QtCore.QRect(10, 650, 611, 91))
        self.frame_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.layoutWidget_4 = QtWidgets.QWidget(self.frame_5)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 10, 591, 74))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fra_in_file_box = QtWidgets.QComboBox(self.layoutWidget_4)
        self.fra_in_file_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_file_box.setObjectName("fra_in_file_box")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.fra_in_file_box.addItem("")
        self.gridLayout_4.addWidget(self.fra_in_file_box, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 1, 0, 1, 1)
        self.fra_in_court_box = QtWidgets.QComboBox(self.layoutWidget_4)
        self.fra_in_court_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fra_in_court_box.setObjectName("fra_in_court_box")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.fra_in_court_box.addItem("")
        self.gridLayout_4.addWidget(self.fra_in_court_box, 1, 1, 1, 1)
        self.createEntryButton_2 = QtWidgets.QPushButton(TrafficCaseInformationDialog)
        self.createEntryButton_2.setGeometry(QtCore.QRect(810, 550, 181, 31))
        self.createEntryButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.createEntryButton_2.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"background-color: rgb(160, 160, 160);")
        self.createEntryButton_2.setAutoDefault(False)
        self.createEntryButton_2.setObjectName("createEntryButton_2")

        self.retranslateUi(TrafficCaseInformationDialog)
        self.pushButton_2.clicked.connect(self.defendant_name.clear)
        self.pushButton_2.clicked.connect(self.defendant_attorney_name.clear)
        self.pushButton_2.clicked.connect(self.case_number.clear)
        self.addOffenseButton.pressed.connect(TrafficCaseInformationDialog.add_offense)
        self.createEntryButton.released.connect(TrafficCaseInformationDialog.close_window)
        self.createEntryButton.clicked.connect(TrafficCaseInformationDialog.create_entry)
        self.createEntryButton.pressed.connect(TrafficCaseInformationDialog.update_case_information)
        self.ability_to_pay_box.currentTextChanged['QString'].connect(TrafficCaseInformationDialog.set_pay_date)
        self.addOffenseButton.clicked.connect(self.finding_choice_box.clearEditText)
        self.addOffenseButton.clicked.connect(self.fines_suspended.clear)
        self.addOffenseButton.clicked.connect(self.fines_amount.clear)
        self.pushButton_4.clicked.connect(self.fines_amount.clear)
        self.offense_choice_box.currentTextChanged['QString'].connect(TrafficCaseInformationDialog.set_statute)
        self.pushButton_4.clicked.connect(self.finding_choice_box.clearEditText)
        self.pushButton_4.clicked.connect(self.plea_choice_box.clearEditText)
        self.addOffenseButton.clicked.connect(self.offense_choice_box.clearEditText)
        self.pushButton_4.clicked.connect(self.offense_choice_box.clearEditText)
        self.addOffenseButton.clicked.connect(self.plea_choice_box.clearEditText)
        self.pushButton_4.clicked.connect(self.fines_suspended.clear)
        self.amendOffenseButton.clicked.connect(TrafficCaseInformationDialog.amend_offense)
        self.addOffenseButton.clicked.connect(self.statute_choice_box.clearEditText)
        self.pushButton_4.clicked.connect(self.statute_choice_box.clearEditText)
        self.statute_choice_box.currentTextChanged['QString'].connect(TrafficCaseInformationDialog.set_offense)
        self.addOffenseButton.released.connect(TrafficCaseInformationDialog.add_offense_to_view)
        QtCore.QMetaObject.connectSlotsByName(TrafficCaseInformationDialog)
        TrafficCaseInformationDialog.setTabOrder(self.case_number, self.defendant_name)
        TrafficCaseInformationDialog.setTabOrder(self.defendant_name, self.defendant_attorney_name)
        TrafficCaseInformationDialog.setTabOrder(self.defendant_attorney_name, self.dateEdit)
        TrafficCaseInformationDialog.setTabOrder(self.dateEdit, self.offense_choice_box)
        TrafficCaseInformationDialog.setTabOrder(self.offense_choice_box, self.statute_choice_box)
        TrafficCaseInformationDialog.setTabOrder(self.statute_choice_box, self.plea_choice_box)
        TrafficCaseInformationDialog.setTabOrder(self.plea_choice_box, self.finding_choice_box)
        TrafficCaseInformationDialog.setTabOrder(self.finding_choice_box, self.court_costs_box)
        TrafficCaseInformationDialog.setTabOrder(self.court_costs_box, self.fines_amount)
        TrafficCaseInformationDialog.setTabOrder(self.fines_amount, self.fines_suspended)
        TrafficCaseInformationDialog.setTabOrder(self.fines_suspended, self.addOffenseButton)
        TrafficCaseInformationDialog.setTabOrder(self.addOffenseButton, self.ability_to_pay_box)
        TrafficCaseInformationDialog.setTabOrder(self.ability_to_pay_box, self.balance_due_date)
        TrafficCaseInformationDialog.setTabOrder(self.balance_due_date, self.fra_in_file_box)
        TrafficCaseInformationDialog.setTabOrder(self.fra_in_file_box, self.fra_in_court_box)
        TrafficCaseInformationDialog.setTabOrder(self.fra_in_court_box, self.createEntryButton)

    def retranslateUi(self, TrafficCaseInformationDialog):
        _translate = QtCore.QCoreApplication.translate
        TrafficCaseInformationDialog.setWindowTitle(_translate("TrafficCaseInformationDialog", "Case Information"))
        self.amendOffenseButton.setText(_translate("TrafficCaseInformationDialog", "Amend Offense"))
        self.addOffenseButton.setText(_translate("TrafficCaseInformationDialog", "Add Offense"))
        self.deleteOffenseButton.setText(_translate("TrafficCaseInformationDialog", "Delete Offense"))
        self.pushButton_4.setText(_translate("TrafficCaseInformationDialog", "Clear Fields"))
        self.label_15.setText(_translate("TrafficCaseInformationDialog", "Offense:"))
        self.label_6.setText(_translate("TrafficCaseInformationDialog", "Statute:"))
        self.label_23.setText(_translate("TrafficCaseInformationDialog", "Degree:"))
        self.degree_choice_box.setItemText(0, _translate("TrafficCaseInformationDialog", "MM"))
        self.degree_choice_box.setItemText(1, _translate("TrafficCaseInformationDialog", "M1"))
        self.degree_choice_box.setItemText(2, _translate("TrafficCaseInformationDialog", "M2"))
        self.degree_choice_box.setItemText(3, _translate("TrafficCaseInformationDialog", "M3"))
        self.degree_choice_box.setItemText(4, _translate("TrafficCaseInformationDialog", "M4"))
        self.degree_choice_box.setItemText(5, _translate("TrafficCaseInformationDialog", "UCM"))
        self.label_8.setText(_translate("TrafficCaseInformationDialog", "Court Costs:"))
        self.court_costs_box.setItemText(0, _translate("TrafficCaseInformationDialog", "No"))
        self.court_costs_box.setItemText(1, _translate("TrafficCaseInformationDialog", "Yes"))
        self.label_13.setText(_translate("TrafficCaseInformationDialog", "Plea:"))
        self.plea_choice_box.setItemText(1, _translate("TrafficCaseInformationDialog", "Guilty"))
        self.plea_choice_box.setItemText(2, _translate("TrafficCaseInformationDialog", "No Contest"))
        self.plea_choice_box.setItemText(3, _translate("TrafficCaseInformationDialog", "Not Guilty"))
        self.plea_choice_box.setItemText(4, _translate("TrafficCaseInformationDialog", "Dismissed"))
        self.label_12.setText(_translate("TrafficCaseInformationDialog", "Finding:"))
        self.finding_choice_box.setItemText(1, _translate("TrafficCaseInformationDialog", "Guilty"))
        self.finding_choice_box.setItemText(2, _translate("TrafficCaseInformationDialog", "Not Guilty"))
        self.finding_choice_box.setItemText(3, _translate("TrafficCaseInformationDialog", "Dismissed"))
        self.label_11.setText(_translate("TrafficCaseInformationDialog", "Fine:"))
        self.label_7.setText(_translate("TrafficCaseInformationDialog", "Fine Suspended:"))
        self.label_16.setText(_translate("TrafficCaseInformationDialog", "Court Costs:"))
        self.label_19.setText(_translate("TrafficCaseInformationDialog", "Statute:"))
        self.plea_label_1.setText(_translate("TrafficCaseInformationDialog", "Plea:"))
        self.offense_label_1.setText(_translate("TrafficCaseInformationDialog", "Offense:"))
        self.label_17.setText(_translate("TrafficCaseInformationDialog", "Fines:"))
        self.label_20.setText(_translate("TrafficCaseInformationDialog", "Degree:"))
        self.label_14.setText(_translate("TrafficCaseInformationDialog", "Finding:"))
        self.label_10.setText(_translate("TrafficCaseInformationDialog", "Fines Suspended:"))
        self.pushButton_2.setText(_translate("TrafficCaseInformationDialog", "Clear Fields"))
        self.label_3.setText(_translate("TrafficCaseInformationDialog", "Date:"))
        self.label.setText(_translate("TrafficCaseInformationDialog", "Case Number:"))
        self.label_2.setText(_translate("TrafficCaseInformationDialog", "Defendant Name: "))
        self.label_4.setText(_translate("TrafficCaseInformationDialog", "Operator License Number:"))
        self.label_5.setText(_translate("TrafficCaseInformationDialog", "Date of Birth:"))
        self.ability_to_pay_box.setItemText(0, _translate("TrafficCaseInformationDialog", "forthwith"))
        self.ability_to_pay_box.setItemText(1, _translate("TrafficCaseInformationDialog", "within 30 days"))
        self.ability_to_pay_box.setItemText(2, _translate("TrafficCaseInformationDialog", "within 60 days"))
        self.ability_to_pay_box.setItemText(3, _translate("TrafficCaseInformationDialog", "within 90 days"))
        self.label_9.setText(_translate("TrafficCaseInformationDialog", "Defendant shall pay fines and costs:"))
        self.label_18.setText(_translate("TrafficCaseInformationDialog", "Balance of fines and costs due by:"))
        self.createEntryButton.setText(_translate("TrafficCaseInformationDialog", "Create Entry"))
        self.fra_in_file_box.setItemText(0, _translate("TrafficCaseInformationDialog", "N/A"))
        self.fra_in_file_box.setItemText(1, _translate("TrafficCaseInformationDialog", "Yes"))
        self.fra_in_file_box.setItemText(2, _translate("TrafficCaseInformationDialog", "No"))
        self.label_21.setText(_translate("TrafficCaseInformationDialog", "FRA shown in complaint/file:"))
        self.label_22.setText(_translate("TrafficCaseInformationDialog", "FRA shown in court:"))
        self.fra_in_court_box.setItemText(0, _translate("TrafficCaseInformationDialog", "N/A"))
        self.fra_in_court_box.setItemText(1, _translate("TrafficCaseInformationDialog", "Yes"))
        self.fra_in_court_box.setItemText(2, _translate("TrafficCaseInformationDialog", "No"))
        self.createEntryButton_2.setText(_translate("TrafficCaseInformationDialog", "Add License Suspension"))
