# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TrafficCaseInformationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrafficCaseInformationDialog(object):
    def setupUi(self, TrafficCaseInformationDialog):
        self.charge_list = [
            "Speeding - School Zone",
            "Speeding > 25 mph",
            "Speeding > 35 mph",
            "Driving in Marked Lanes",
            "Driving Under Suspension",
        ]
        TrafficCaseInformationDialog.setObjectName("TrafficCaseInformationDialog")
        TrafficCaseInformationDialog.setWindowModality(QtCore.Qt.NonModal)
        TrafficCaseInformationDialog.resize(1000, 867)
        TrafficCaseInformationDialog.setMinimumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        TrafficCaseInformationDialog.setFont(font)
        TrafficCaseInformationDialog.setToolTip("")
        self.frame = QtWidgets.QFrame(TrafficCaseInformationDialog)
        self.frame.setGeometry(QtCore.QRect(20, 230, 951, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 931, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.fines_amount = QtWidgets.QLineEdit(self.layoutWidget)
        self.fines_amount.setObjectName("fines_amount")
        self.gridLayout.addWidget(self.fines_amount, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.offense_choice_box = QtWidgets.QComboBox(self.layoutWidget)
        self.offense_choice_box.setEditable(True)
        self.offense_choice_box.setObjectName("offense_choice_box")
        self.offense_choice_box.addItems(self.charge_list)
        self.gridLayout.addWidget(self.offense_choice_box, 0, 1, 1, 1)
        self.court_costs_box = QtWidgets.QComboBox(self.layoutWidget)
        self.court_costs_box.setEditable(False)
        self.court_costs_box.setObjectName("court_costs_box")
        self.court_costs_box.addItem("")
        self.court_costs_box.addItem("")
        self.gridLayout.addWidget(self.court_costs_box, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)
        self.plea_choice_box = QtWidgets.QComboBox(self.layoutWidget)
        self.plea_choice_box.setEditable(True)
        self.plea_choice_box.setObjectName("plea_choice_box")
        self.plea_choice_box.addItem("")
        self.plea_choice_box.setItemText(0, "")
        self.plea_choice_box.addItem("")
        self.plea_choice_box.addItem("")
        self.plea_choice_box.addItem("")
        self.plea_choice_box.addItem("")
        self.gridLayout.addWidget(self.plea_choice_box, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.statute_choice_box = QtWidgets.QComboBox(self.layoutWidget)
        self.statute_choice_box.setEditable(True)
        self.statute_choice_box.setObjectName("statute_choice_box")
        self.statute_choice_box.addItem("")
        self.statute_choice_box.setItemText(0, "")
        self.statute_choice_box.addItem("")
        self.statute_choice_box.addItem("")
        self.statute_choice_box.addItem("")
        self.statute_choice_box.addItem("")
        self.statute_choice_box.addItem("")
        self.statute_choice_box.addItem("")
        self.gridLayout.addWidget(self.statute_choice_box, 0, 3, 1, 1)
        self.fines_suspended = QtWidgets.QLineEdit(self.layoutWidget)
        self.fines_suspended.setObjectName("fines_suspended")
        self.gridLayout.addWidget(self.fines_suspended, 2, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.finding_choice_box = QtWidgets.QComboBox(self.layoutWidget)
        self.finding_choice_box.setEditable(True)
        self.finding_choice_box.setObjectName("finding_choice_box")
        self.finding_choice_box.addItem("")
        self.finding_choice_box.setItemText(0, "")
        self.finding_choice_box.addItem("")
        self.finding_choice_box.addItem("")
        self.finding_choice_box.addItem("")
        self.finding_choice_box.addItem("")
        self.gridLayout.addWidget(self.finding_choice_box, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.addOffenseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addOffenseButton.setObjectName("addOffenseButton")
        self.gridLayout.addWidget(self.addOffenseButton, 1, 4, 1, 1)
        self.degree_choice_box = QtWidgets.QComboBox(self.layoutWidget)
        self.degree_choice_box.setObjectName("degree_choice_box")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.degree_choice_box.addItem("")
        self.gridLayout.addWidget(self.degree_choice_box, 0, 4, 1, 1)
        self.deleteOffenseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteOffenseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteOffenseButton.setObjectName("deleteOffenseButton")
        self.gridLayout.addWidget(self.deleteOffenseButton, 2, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 4, 1, 1)
        self.frame_2 = QtWidgets.QFrame(TrafficCaseInformationDialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 440, 951, 281))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 931, 260))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.charges_gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.charges_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.charges_gridLayout.setObjectName("charges_gridLayout")
        self.offense_label_1 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.offense_label_1.setFont(font)
        self.offense_label_1.setWordWrap(True)
        self.offense_label_1.setObjectName("offense_label_1")
        self.charges_gridLayout.addWidget(self.offense_label_1, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.charges_gridLayout.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.charges_gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.plea_label_1 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.plea_label_1.setFont(font)
        self.plea_label_1.setObjectName("plea_label_1")
        self.charges_gridLayout.addWidget(self.plea_label_1, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.charges_gridLayout.addWidget(self.label_16, 7, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.charges_gridLayout.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.charges_gridLayout.addWidget(self.label_17, 5, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.charges_gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(TrafficCaseInformationDialog)
        self.frame_3.setGeometry(QtCore.QRect(20, 10, 951, 211))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.widget = QtWidgets.QWidget(self.frame_3)
        self.widget.setGeometry(QtCore.QRect(11, 11, 931, 194))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.plea_trial_date = QtWidgets.QDateEdit(self.widget)
        self.plea_trial_date.setMinimumDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setCalendarPopup(True)
        self.plea_trial_date.setDate(QtCore.QDate(2021, 1, 1))
        self.plea_trial_date.setObjectName("plea_trial_date")
        self.gridLayout_3.addWidget(self.plea_trial_date, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.case_number = QtWidgets.QLineEdit(self.widget)
        self.case_number.setMaximumSize(QtCore.QSize(500, 16777215))
        self.case_number.setObjectName("case_number")
        self.gridLayout_3.addWidget(self.case_number, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.defendant_name = QtWidgets.QLineEdit(self.widget)
        self.defendant_name.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_name.setObjectName("defendant_name")
        self.gridLayout_3.addWidget(self.defendant_name, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setToolTip("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.defendant_attorney_name = QtWidgets.QLineEdit(self.widget)
        self.defendant_attorney_name.setMaximumSize(QtCore.QSize(500, 16777215))
        self.defendant_attorney_name.setObjectName("defendant_attorney_name")
        self.gridLayout_3.addWidget(self.defendant_attorney_name, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setToolTip("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setDateTime(
            QtCore.QDateTime(QtCore.QDate(1980, 1, 1), QtCore.QTime(0, 0, 0))
        )
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_3.addWidget(self.dateEdit, 4, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 4, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(TrafficCaseInformationDialog)
        self.frame_4.setGeometry(QtCore.QRect(20, 730, 951, 91))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.frame_4.setObjectName("frame_4")
        self.layoutWidget_3 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 731, 74))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.ability_to_pay_box = QtWidgets.QComboBox(self.layoutWidget_3)
        self.ability_to_pay_box.setObjectName("ability_to_pay_box")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.ability_to_pay_box.addItem("")
        self.gridLayout_2.addWidget(self.ability_to_pay_box, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)
        self.balance_due_date = QtWidgets.QDateEdit(self.layoutWidget_3)
        self.balance_due_date.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0))
        )
        self.balance_due_date.setCalendarPopup(True)
        self.balance_due_date.setObjectName("balance_due_date")
        self.gridLayout_2.addWidget(self.balance_due_date, 1, 1, 1, 1)
        self.createEntryButton = QtWidgets.QPushButton(TrafficCaseInformationDialog)
        self.createEntryButton.setGeometry(QtCore.QRect(780, 830, 191, 31))
        self.createEntryButton.setAutoDefault(False)
        self.createEntryButton.setObjectName("createEntryButton")

        self.retranslateUi(TrafficCaseInformationDialog)
        self.pushButton_2.clicked.connect(self.defendant_name.clear)
        self.pushButton_2.clicked.connect(self.defendant_attorney_name.clear)
        self.pushButton_2.clicked.connect(self.case_number.clear)
        self.addOffenseButton.clicked.connect(TrafficCaseInformationDialog.add_offense)
        self.createEntryButton.released.connect(
            TrafficCaseInformationDialog.close_window
        )
        self.createEntryButton.clicked.connect(
            TrafficCaseInformationDialog.create_entry
        )
        self.createEntryButton.pressed.connect(
            TrafficCaseInformationDialog.update_case_information
        )
        self.addOffenseButton.clicked.connect(self.offense_choice_box.clearEditText)
        self.addOffenseButton.clicked.connect(self.plea_choice_box.clearEditText)
        self.addOffenseButton.clicked.connect(self.fines_amount.clear)
        self.addOffenseButton.clicked.connect(self.statute_choice_box.clearEditText)
        self.addOffenseButton.clicked.connect(self.finding_choice_box.clearEditText)
        self.addOffenseButton.clicked.connect(self.fines_suspended.clear)
        self.offense_choice_box.currentTextChanged["QString"].connect(
            TrafficCaseInformationDialog.set_statute
        )
        QtCore.QMetaObject.connectSlotsByName(TrafficCaseInformationDialog)
        TrafficCaseInformationDialog.setTabOrder(self.case_number, self.defendant_name)
        TrafficCaseInformationDialog.setTabOrder(
            self.defendant_name, self.defendant_attorney_name
        )
        TrafficCaseInformationDialog.setTabOrder(
            self.defendant_attorney_name, self.dateEdit
        )
        TrafficCaseInformationDialog.setTabOrder(self.dateEdit, self.offense_choice_box)
        TrafficCaseInformationDialog.setTabOrder(
            self.offense_choice_box, self.statute_choice_box
        )
        TrafficCaseInformationDialog.setTabOrder(
            self.statute_choice_box, self.plea_choice_box
        )
        TrafficCaseInformationDialog.setTabOrder(
            self.plea_choice_box, self.finding_choice_box
        )
        TrafficCaseInformationDialog.setTabOrder(
            self.finding_choice_box, self.fines_amount
        )
        TrafficCaseInformationDialog.setTabOrder(
            self.fines_amount, self.fines_suspended
        )
        TrafficCaseInformationDialog.setTabOrder(
            self.fines_suspended, self.court_costs_box
        )
        TrafficCaseInformationDialog.setTabOrder(
            self.court_costs_box, self.ability_to_pay_box
        )
        TrafficCaseInformationDialog.setTabOrder(
            self.ability_to_pay_box, self.plea_trial_date
        )
        TrafficCaseInformationDialog.setTabOrder(
            self.plea_trial_date, self.createEntryButton
        )

    def retranslateUi(self, TrafficCaseInformationDialog):
        _translate = QtCore.QCoreApplication.translate
        TrafficCaseInformationDialog.setWindowTitle(
            _translate("TrafficCaseInformationDialog", "Case Information")
        )
        self.label_15.setText(_translate("TrafficCaseInformationDialog", "Offense:"))
        self.label_13.setText(_translate("TrafficCaseInformationDialog", "Plea:"))
        self.court_costs_box.setItemText(
            0, _translate("TrafficCaseInformationDialog", "Yes")
        )
        self.court_costs_box.setItemText(
            1, _translate("TrafficCaseInformationDialog", "No")
        )
        self.label_12.setText(_translate("TrafficCaseInformationDialog", "Finding:"))
        self.plea_choice_box.setItemText(
            1, _translate("TrafficCaseInformationDialog", "Not Guilty")
        )
        self.plea_choice_box.setItemText(
            2, _translate("TrafficCaseInformationDialog", "No Contest")
        )
        self.plea_choice_box.setItemText(
            3, _translate("TrafficCaseInformationDialog", "Guilty")
        )
        self.plea_choice_box.setItemText(
            4, _translate("TrafficCaseInformationDialog", "No Plea - Dismissed")
        )
        self.label_8.setText(_translate("TrafficCaseInformationDialog", "Court Costs:"))
        self.statute_choice_box.setItemText(
            1, _translate("TrafficCaseInformationDialog", "M1")
        )
        self.statute_choice_box.setItemText(
            2, _translate("TrafficCaseInformationDialog", "M2")
        )
        self.statute_choice_box.setItemText(
            3, _translate("TrafficCaseInformationDialog", "M3")
        )
        self.statute_choice_box.setItemText(
            4, _translate("TrafficCaseInformationDialog", "M4")
        )
        self.statute_choice_box.setItemText(
            5, _translate("TrafficCaseInformationDialog", "MM")
        )
        self.statute_choice_box.setItemText(
            6, _translate("TrafficCaseInformationDialog", "UCM")
        )
        self.label_7.setText(
            _translate("TrafficCaseInformationDialog", "Fines Suspended:")
        )
        self.finding_choice_box.setItemText(
            1, _translate("TrafficCaseInformationDialog", "Guilty")
        )
        self.finding_choice_box.setItemText(
            2, _translate("TrafficCaseInformationDialog", "Not Guilty")
        )
        self.finding_choice_box.setItemText(
            3, _translate("TrafficCaseInformationDialog", "Dismissed")
        )
        self.finding_choice_box.setItemText(
            4, _translate("TrafficCaseInformationDialog", "Dismissed with conditions")
        )
        self.label_6.setText(
            _translate("TrafficCaseInformationDialog", "Statute / Degree:")
        )
        self.label_11.setText(
            _translate("TrafficCaseInformationDialog", "Fines Amount:")
        )
        self.addOffenseButton.setText(
            _translate("TrafficCaseInformationDialog", "Add Offense")
        )
        self.degree_choice_box.setItemText(
            0, _translate("TrafficCaseInformationDialog", "MM")
        )
        self.degree_choice_box.setItemText(
            1, _translate("TrafficCaseInformationDialog", "M1")
        )
        self.degree_choice_box.setItemText(
            2, _translate("TrafficCaseInformationDialog", "M2")
        )
        self.degree_choice_box.setItemText(
            3, _translate("TrafficCaseInformationDialog", "M3")
        )
        self.degree_choice_box.setItemText(
            4, _translate("TrafficCaseInformationDialog", "M4")
        )
        self.deleteOffenseButton.setText(
            _translate("TrafficCaseInformationDialog", "Delete Offense")
        )
        self.pushButton_4.setText(
            _translate("TrafficCaseInformationDialog", "Clear Fields")
        )
        self.offense_label_1.setText(
            _translate("TrafficCaseInformationDialog", "Offense:")
        )
        self.label_19.setText(_translate("TrafficCaseInformationDialog", "Statute:"))
        self.label_10.setText(
            _translate("TrafficCaseInformationDialog", "Fines Suspended:")
        )
        self.plea_label_1.setText(_translate("TrafficCaseInformationDialog", "Plea:"))
        self.label_16.setText(
            _translate("TrafficCaseInformationDialog", "Court Costs:")
        )
        self.label_14.setText(_translate("TrafficCaseInformationDialog", "Finding:"))
        self.label_17.setText(_translate("TrafficCaseInformationDialog", "Fines:"))
        self.label_20.setText(_translate("TrafficCaseInformationDialog", "Degree:"))
        self.label_3.setText(_translate("TrafficCaseInformationDialog", "Date:"))
        self.label.setText(_translate("TrafficCaseInformationDialog", "Case Number:"))
        self.label_2.setText(
            _translate("TrafficCaseInformationDialog", "Defendant Name: ")
        )
        self.label_4.setText(
            _translate("TrafficCaseInformationDialog", "Operator License Number:")
        )
        self.label_5.setText(
            _translate("TrafficCaseInformationDialog", "Date of Birth:")
        )
        self.pushButton_2.setText(
            _translate("TrafficCaseInformationDialog", "Clear Fields")
        )
        self.label_9.setText(
            _translate(
                "TrafficCaseInformationDialog", "Defendant shall pay fines and costs:"
            )
        )
        self.ability_to_pay_box.setItemText(
            0, _translate("TrafficCaseInformationDialog", "forthwith")
        )
        self.ability_to_pay_box.setItemText(
            1, _translate("TrafficCaseInformationDialog", "within 30 days")
        )
        self.ability_to_pay_box.setItemText(
            2, _translate("TrafficCaseInformationDialog", "within 60 days")
        )
        self.ability_to_pay_box.setItemText(
            3, _translate("TrafficCaseInformationDialog", "within 90 days")
        )
        self.label_18.setText(
            _translate(
                "TrafficCaseInformationDialog", "Balance of fines and costs due by:"
            )
        )
        self.createEntryButton.setText(
            _translate("TrafficCaseInformationDialog", "Create Entry")
        )
