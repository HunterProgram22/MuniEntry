# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'munientry/views/ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1166, 871)
        MainWindow.setMinimumSize(QtCore.QSize(900, 720))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("font: 75 11pt \"Palatino Linotype\";\n"
"color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"font-weight: bold;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.judicial_officers_Stack = QtWidgets.QWidget()
        self.judicial_officers_Stack.setObjectName("judicial_officers_Stack")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.judicial_officers_Stack)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.judicial_officer_frame = QtWidgets.QFrame(self.judicial_officers_Stack)
        self.judicial_officer_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.judicial_officer_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.judicial_officer_frame.setLineWidth(2)
        self.judicial_officer_frame.setObjectName("judicial_officer_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.judicial_officer_frame)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.pelanda_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.pelanda_radioButton.setObjectName("pelanda_radioButton")
        self.gridLayout.addWidget(self.pelanda_radioButton, 6, 1, 1, 1)
        self.hemmeter_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.hemmeter_radioButton.setObjectName("hemmeter_radioButton")
        self.gridLayout.addWidget(self.hemmeter_radioButton, 5, 0, 1, 1)
        self.visiting_judge_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.visiting_judge_radioButton.setObjectName("visiting_judge_radioButton")
        self.gridLayout.addWidget(self.visiting_judge_radioButton, 5, 2, 1, 1)
        self.kudela_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.kudela_radioButton.setObjectName("kudela_radioButton")
        self.gridLayout.addWidget(self.kudela_radioButton, 6, 2, 1, 1)
        self.bunner_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.bunner_radioButton.setObjectName("bunner_radioButton")
        self.gridLayout.addWidget(self.bunner_radioButton, 6, 0, 1, 1)
        self.rohrer_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.rohrer_radioButton.setObjectName("rohrer_radioButton")
        self.gridLayout.addWidget(self.rohrer_radioButton, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.judicial_officer_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 3)
        self.gridLayout_6.addWidget(self.judicial_officer_frame, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.judicial_officers_Stack)
        self.assignment_commissioners_Stack = QtWidgets.QWidget()
        self.assignment_commissioners_Stack.setObjectName("assignment_commissioners_Stack")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.assignment_commissioners_Stack)
        self.gridLayout_7.setSpacing(12)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame = QtWidgets.QFrame(self.assignment_commissioners_Stack)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 24)
        self.gridLayout_3.setHorizontalSpacing(24)
        self.gridLayout_3.setVerticalSpacing(30)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.patterson_radioButton = QtWidgets.QRadioButton(self.frame)
        self.patterson_radioButton.setObjectName("patterson_radioButton")
        self.gridLayout_3.addWidget(self.patterson_radioButton, 1, 2, 1, 1)
        self.dattilo_radioButton = QtWidgets.QRadioButton(self.frame)
        self.dattilo_radioButton.setObjectName("dattilo_radioButton")
        self.gridLayout_3.addWidget(self.dattilo_radioButton, 1, 1, 1, 1)
        self.none_radioButton = QtWidgets.QRadioButton(self.frame)
        self.none_radioButton.setObjectName("none_radioButton")
        self.gridLayout_3.addWidget(self.none_radioButton, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 3)
        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.assignment_commissioners_Stack)
        self.gridLayout_9.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setVerticalSpacing(18)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.arraignments_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.arraignments_radioButton.setObjectName("arraignments_radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.arraignments_radioButton)
        self.gridLayout_8.addWidget(self.arraignments_radioButton, 1, 0, 1, 1)
        self.slated_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.slated_radioButton.setObjectName("slated_radioButton")
        self.buttonGroup.addButton(self.slated_radioButton)
        self.gridLayout_8.addWidget(self.slated_radioButton, 1, 1, 1, 1)
        self.final_pretrial_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.final_pretrial_radioButton.setObjectName("final_pretrial_radioButton")
        self.buttonGroup.addButton(self.final_pretrial_radioButton)
        self.gridLayout_8.addWidget(self.final_pretrial_radioButton, 1, 2, 1, 1)
        self.arraignments_cases_box = ExtendedComboBox(self.centralwidget)
        self.arraignments_cases_box.setObjectName("arraignments_cases_box")
        self.gridLayout_8.addWidget(self.arraignments_cases_box, 2, 0, 1, 1)
        self.slated_cases_box = ExtendedComboBox(self.centralwidget)
        self.slated_cases_box.setObjectName("slated_cases_box")
        self.gridLayout_8.addWidget(self.slated_cases_box, 2, 1, 1, 1)
        self.final_pretrial_cases_box = ExtendedComboBox(self.centralwidget)
        self.final_pretrial_cases_box.setObjectName("final_pretrial_cases_box")
        self.gridLayout_8.addWidget(self.final_pretrial_cases_box, 2, 2, 1, 1)
        self.pleas_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.pleas_radioButton.setObjectName("pleas_radioButton")
        self.buttonGroup.addButton(self.pleas_radioButton)
        self.gridLayout_8.addWidget(self.pleas_radioButton, 3, 0, 1, 1)
        self.trials_to_court_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.trials_to_court_radioButton.setObjectName("trials_to_court_radioButton")
        self.buttonGroup.addButton(self.trials_to_court_radioButton)
        self.gridLayout_8.addWidget(self.trials_to_court_radioButton, 3, 1, 1, 1)
        self.pcvh_fcvh_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.pcvh_fcvh_radioButton.setObjectName("pcvh_fcvh_radioButton")
        self.buttonGroup.addButton(self.pcvh_fcvh_radioButton)
        self.gridLayout_8.addWidget(self.pcvh_fcvh_radioButton, 3, 2, 1, 1)
        self.pleas_cases_box = ExtendedComboBox(self.centralwidget)
        self.pleas_cases_box.setObjectName("pleas_cases_box")
        self.gridLayout_8.addWidget(self.pleas_cases_box, 4, 0, 1, 1)
        self.trials_to_court_cases_box = ExtendedComboBox(self.centralwidget)
        self.trials_to_court_cases_box.setObjectName("trials_to_court_cases_box")
        self.gridLayout_8.addWidget(self.trials_to_court_cases_box, 4, 1, 1, 1)
        self.pcvh_fcvh_cases_box = ExtendedComboBox(self.centralwidget)
        self.pcvh_fcvh_cases_box.setObjectName("pcvh_fcvh_cases_box")
        self.gridLayout_8.addWidget(self.pcvh_fcvh_cases_box, 4, 2, 1, 1)
        self.reload_cases_Button = QtWidgets.QPushButton(self.centralwidget)
        self.reload_cases_Button.setMinimumSize(QtCore.QSize(120, 30))
        self.reload_cases_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.reload_cases_Button.setObjectName("reload_cases_Button")
        self.gridLayout_8.addWidget(self.reload_cases_Button, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 3)
        self.gridLayout_8.setRowStretch(0, 1)
        self.gridLayout_8.setRowStretch(1, 1)
        self.gridLayout_8.setRowStretch(2, 1)
        self.gridLayout_8.setRowStretch(3, 1)
        self.gridLayout_8.setRowStretch(4, 1)
        self.gridLayout_8.setRowStretch(5, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("\n"
"background-color: rgb(208, 208, 208);")
        self.tabWidget.setObjectName("tabWidget")
        self.crim_traffic_Tab = QtWidgets.QWidget()
        self.crim_traffic_Tab.setObjectName("crim_traffic_Tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.crim_traffic_Tab)
        self.gridLayout_2.setHorizontalSpacing(24)
        self.gridLayout_2.setVerticalSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.crim_traffic_Tab)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)
        self.FineOnlyPleaButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.FineOnlyPleaButton.setMinimumSize(QtCore.QSize(120, 30))
        self.FineOnlyPleaButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.FineOnlyPleaButton.setObjectName("FineOnlyPleaButton")
        self.gridLayout_2.addWidget(self.FineOnlyPleaButton, 4, 0, 1, 1)
        self.NoPleaBondButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.NoPleaBondButton.setMinimumSize(QtCore.QSize(120, 30))
        self.NoPleaBondButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.NoPleaBondButton.setObjectName("NoPleaBondButton")
        self.gridLayout_2.addWidget(self.NoPleaBondButton, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.crim_traffic_Tab)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.JailCCPleaButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.JailCCPleaButton.setMinimumSize(QtCore.QSize(120, 30))
        self.JailCCPleaButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.JailCCPleaButton.setObjectName("JailCCPleaButton")
        self.gridLayout_2.addWidget(self.JailCCPleaButton, 5, 0, 1, 1)
        self.NotGuiltyBondButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.NotGuiltyBondButton.setMinimumSize(QtCore.QSize(120, 30))
        self.NotGuiltyBondButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.NotGuiltyBondButton.setObjectName("NotGuiltyBondButton")
        self.gridLayout_2.addWidget(self.NotGuiltyBondButton, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.crim_traffic_Tab)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 2, 1, 1)
        self.BondHearingButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.BondHearingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.BondHearingButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.BondHearingButton.setObjectName("BondHearingButton")
        self.gridLayout_2.addWidget(self.BondHearingButton, 5, 2, 1, 1)
        self.PleaOnlyButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.PleaOnlyButton.setMinimumSize(QtCore.QSize(120, 30))
        self.PleaOnlyButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.PleaOnlyButton.setObjectName("PleaOnlyButton")
        self.gridLayout_2.addWidget(self.PleaOnlyButton, 5, 1, 1, 1)
        self.DiversionButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.DiversionButton.setMinimumSize(QtCore.QSize(120, 30))
        self.DiversionButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.DiversionButton.setObjectName("DiversionButton")
        self.gridLayout_2.addWidget(self.DiversionButton, 6, 0, 1, 1)
        self.ProbationViolationBondButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.ProbationViolationBondButton.setMinimumSize(QtCore.QSize(120, 30))
        self.ProbationViolationBondButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.ProbationViolationBondButton.setObjectName("ProbationViolationBondButton")
        self.gridLayout_2.addWidget(self.ProbationViolationBondButton, 6, 2, 1, 1)
        self.FailureToAppearButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.FailureToAppearButton.setMinimumSize(QtCore.QSize(120, 30))
        self.FailureToAppearButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.FailureToAppearButton.setObjectName("FailureToAppearButton")
        self.gridLayout_2.addWidget(self.FailureToAppearButton, 8, 2, 1, 1)
        self.LeapAdmissionButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.LeapAdmissionButton.setMinimumSize(QtCore.QSize(120, 30))
        self.LeapAdmissionButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.LeapAdmissionButton.setObjectName("LeapAdmissionButton")
        self.gridLayout_2.addWidget(self.LeapAdmissionButton, 8, 0, 1, 1)
        self.TrialSentencingButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.TrialSentencingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.TrialSentencingButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.TrialSentencingButton.setObjectName("TrialSentencingButton")
        self.gridLayout_2.addWidget(self.TrialSentencingButton, 8, 1, 1, 1)
        self.SentencingOnlyButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.SentencingOnlyButton.setMinimumSize(QtCore.QSize(120, 30))
        self.SentencingOnlyButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.SentencingOnlyButton.setObjectName("SentencingOnlyButton")
        self.gridLayout_2.addWidget(self.SentencingOnlyButton, 9, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.crim_traffic_Tab)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.crim_traffic_Tab)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 7, 1, 1, 1)
        self.FreeformEntryButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.FreeformEntryButton.setMinimumSize(QtCore.QSize(120, 30))
        self.FreeformEntryButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.FreeformEntryButton.setObjectName("FreeformEntryButton")
        self.gridLayout_2.addWidget(self.FreeformEntryButton, 9, 2, 1, 1)
        self.LeapSentencingButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.LeapSentencingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.LeapSentencingButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.LeapSentencingButton.setObjectName("LeapSentencingButton")
        self.gridLayout_2.addWidget(self.LeapSentencingButton, 10, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.crim_traffic_Tab)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 7, 2, 1, 1)
        self.LeapAdmissionValidButton = QtWidgets.QPushButton(self.crim_traffic_Tab)
        self.LeapAdmissionValidButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.LeapAdmissionValidButton.setObjectName("LeapAdmissionValidButton")
        self.gridLayout_2.addWidget(self.LeapAdmissionValidButton, 9, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.tabWidget.addTab(self.crim_traffic_Tab, "")
        self.scheduling_Tab = QtWidgets.QWidget()
        self.scheduling_Tab.setObjectName("scheduling_Tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scheduling_Tab)
        self.gridLayout_4.setHorizontalSpacing(30)
        self.gridLayout_4.setVerticalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.hemmeter_schedulingEntryButton = QtWidgets.QPushButton(self.scheduling_Tab)
        self.hemmeter_schedulingEntryButton.setMinimumSize(QtCore.QSize(120, 30))
        self.hemmeter_schedulingEntryButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.hemmeter_schedulingEntryButton.setObjectName("hemmeter_schedulingEntryButton")
        self.gridLayout_4.addWidget(self.hemmeter_schedulingEntryButton, 0, 0, 1, 1)
        self.rohrer_schedulingEntryButton = QtWidgets.QPushButton(self.scheduling_Tab)
        self.rohrer_schedulingEntryButton.setMinimumSize(QtCore.QSize(120, 30))
        self.rohrer_schedulingEntryButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.rohrer_schedulingEntryButton.setObjectName("rohrer_schedulingEntryButton")
        self.gridLayout_4.addWidget(self.rohrer_schedulingEntryButton, 0, 2, 1, 1)
        self.hemmeter_final_jury_hearingButton = QtWidgets.QPushButton(self.scheduling_Tab)
        self.hemmeter_final_jury_hearingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.hemmeter_final_jury_hearingButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.hemmeter_final_jury_hearingButton.setObjectName("hemmeter_final_jury_hearingButton")
        self.gridLayout_4.addWidget(self.hemmeter_final_jury_hearingButton, 1, 0, 1, 1)
        self.rohrer_final_jury_hearingButton = QtWidgets.QPushButton(self.scheduling_Tab)
        self.rohrer_final_jury_hearingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.rohrer_final_jury_hearingButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.rohrer_final_jury_hearingButton.setObjectName("rohrer_final_jury_hearingButton")
        self.gridLayout_4.addWidget(self.rohrer_final_jury_hearingButton, 1, 2, 1, 1)
        self.trial_to_court_hearingEntryButton = QtWidgets.QPushButton(self.scheduling_Tab)
        self.trial_to_court_hearingEntryButton.setMinimumSize(QtCore.QSize(120, 30))
        self.trial_to_court_hearingEntryButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.trial_to_court_hearingEntryButton.setObjectName("trial_to_court_hearingEntryButton")
        self.gridLayout_4.addWidget(self.trial_to_court_hearingEntryButton, 0, 1, 1, 1)
        self.hemmeter_general_hearingButton = QtWidgets.QPushButton(self.scheduling_Tab)
        self.hemmeter_general_hearingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.hemmeter_general_hearingButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.hemmeter_general_hearingButton.setObjectName("hemmeter_general_hearingButton")
        self.gridLayout_4.addWidget(self.hemmeter_general_hearingButton, 2, 0, 1, 1)
        self.rohrer_general_hearingButton = QtWidgets.QPushButton(self.scheduling_Tab)
        self.rohrer_general_hearingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.rohrer_general_hearingButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.rohrer_general_hearingButton.setObjectName("rohrer_general_hearingButton")
        self.gridLayout_4.addWidget(self.rohrer_general_hearingButton, 2, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.scheduling_Tab)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 3, 0, 1, 3)
        self.random_judge_Button = QtWidgets.QPushButton(self.scheduling_Tab)
        self.random_judge_Button.setMinimumSize(QtCore.QSize(120, 30))
        self.random_judge_Button.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.random_judge_Button.setObjectName("random_judge_Button")
        self.gridLayout_4.addWidget(self.random_judge_Button, 4, 0, 1, 1)
        self.last_judge_assigned_label = QtWidgets.QLabel(self.scheduling_Tab)
        self.last_judge_assigned_label.setMaximumSize(QtCore.QSize(16777215, 75))
        self.last_judge_assigned_label.setAlignment(QtCore.Qt.AlignCenter)
        self.last_judge_assigned_label.setObjectName("last_judge_assigned_label")
        self.gridLayout_4.addWidget(self.last_judge_assigned_label, 4, 2, 1, 1)
        self.assign_judge_label = QtWidgets.QLabel(self.scheduling_Tab)
        self.assign_judge_label.setMaximumSize(QtCore.QSize(16777215, 75))
        self.assign_judge_label.setAlignment(QtCore.Qt.AlignCenter)
        self.assign_judge_label.setObjectName("assign_judge_label")
        self.gridLayout_4.addWidget(self.assign_judge_label, 4, 1, 1, 1)
        self.tabWidget.addTab(self.scheduling_Tab, "")
        self.gridLayout_5.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)
        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_9.addLayout(self.gridLayout_5, 2, 0, 1, 2)
        self.gridLayout_10.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1166, 27))
        self.menubar.setObjectName("menubar")
        self.menuLogs = QtWidgets.QMenu(self.menubar)
        self.menuLogs.setObjectName("menuLogs")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Current_Log = QtWidgets.QAction(MainWindow)
        self.actionOpen_Current_Log.setObjectName("actionOpen_Current_Log")
        self.menuLogs.addAction(self.actionOpen_Current_Log)
        self.menubar.addAction(self.menuLogs.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MuniEntry - ver 0.24.0"))
        self.pelanda_radioButton.setText(_translate("MainWindow", "Magistrate Pelanda"))
        self.hemmeter_radioButton.setText(_translate("MainWindow", "Judge Hemmeter"))
        self.visiting_judge_radioButton.setText(_translate("MainWindow", "Visiting Judge"))
        self.kudela_radioButton.setText(_translate("MainWindow", "Magistrate Kudela"))
        self.bunner_radioButton.setText(_translate("MainWindow", "Magistrate Bunner"))
        self.rohrer_radioButton.setText(_translate("MainWindow", "Judge Rohrer"))
        self.label_9.setText(_translate("MainWindow", "JUDICIAL OFFICER"))
        self.patterson_radioButton.setText(_translate("MainWindow", "Kathryn Patterson"))
        self.dattilo_radioButton.setText(_translate("MainWindow", "Pat Dattilo"))
        self.none_radioButton.setText(_translate("MainWindow", "None"))
        self.label.setText(_translate("MainWindow", "ASSIGNMENT COMMISSIONER"))
        self.arraignments_radioButton.setText(_translate("MainWindow", "Arraignments"))
        self.slated_radioButton.setText(_translate("MainWindow", "Slated                                  "))
        self.final_pretrial_radioButton.setText(_translate("MainWindow", "Final Pre-trials"))
        self.pleas_radioButton.setText(_translate("MainWindow", "Pleas and Motion/Oral Hearings"))
        self.trials_to_court_radioButton.setText(_translate("MainWindow", "Trials to Court and Jury Trials"))
        self.pcvh_fcvh_radioButton.setText(_translate("MainWindow", "PCVH/FCVH"))
        self.reload_cases_Button.setText(_translate("MainWindow", "Reload Cases"))
        self.label_3.setText(_translate("MainWindow", "DAILY CASE LISTS"))
        self.label_4.setText(_translate("MainWindow", "Plea Only Entries"))
        self.FineOnlyPleaButton.setText(_translate("MainWindow", "Fine Only"))
        self.NoPleaBondButton.setText(_translate("MainWindow", "Appear on Warrant (No Plea) / Bond"))
        self.label_2.setText(_translate("MainWindow", "Plea and Sentence Entries"))
        self.JailCCPleaButton.setText(_translate("MainWindow", "Jail and/or Community Control"))
        self.NotGuiltyBondButton.setText(_translate("MainWindow", "Not Guilty Plea / Bond"))
        self.label_6.setText(_translate("MainWindow", "Bond Entries"))
        self.BondHearingButton.setText(_translate("MainWindow", "Bond Modification / Revocation"))
        self.PleaOnlyButton.setText(_translate("MainWindow", "Plea Only - Future Sentencing"))
        self.DiversionButton.setText(_translate("MainWindow", "Diversion"))
        self.ProbationViolationBondButton.setText(_translate("MainWindow", "Prelim. Probation Violation / Bond"))
        self.FailureToAppearButton.setText(_translate("MainWindow", "Failed to Appear / Issue Warrant"))
        self.LeapAdmissionButton.setText(_translate("MainWindow", "LEAP Admission Plea"))
        self.TrialSentencingButton.setText(_translate("MainWindow", "Jury Trial / Trial to Court Sentencing"))
        self.SentencingOnlyButton.setText(_translate("MainWindow", "Sentencing Only - Already Plead"))
        self.label_8.setText(_translate("MainWindow", "LEAP Entries"))
        self.label_5.setText(_translate("MainWindow", "Sentencing Only Entries"))
        self.FreeformEntryButton.setText(_translate("MainWindow", "Freeform Entry"))
        self.LeapSentencingButton.setText(_translate("MainWindow", "LEAP Sentencing"))
        self.label_7.setText(_translate("MainWindow", "General / Warrant Entries"))
        self.LeapAdmissionValidButton.setText(_translate("MainWindow", "LEAP Admission - Already Valid"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.crim_traffic_Tab), _translate("MainWindow", "Crim/Traffic"))
        self.hemmeter_schedulingEntryButton.setText(_translate("MainWindow", "Hemmeter - Scheduling Entry"))
        self.rohrer_schedulingEntryButton.setText(_translate("MainWindow", "Rohrer - Scheduling Entry"))
        self.hemmeter_final_jury_hearingButton.setText(_translate("MainWindow", "Hemmeter - Final/Jury Notice of Hearing"))
        self.rohrer_final_jury_hearingButton.setText(_translate("MainWindow", "Rohrer - Final/Jury Notice of Hearing"))
        self.trial_to_court_hearingEntryButton.setText(_translate("MainWindow", "Trial To Court Notice of Hearing"))
        self.hemmeter_general_hearingButton.setText(_translate("MainWindow", "Hemmeter - General Notice of Hearing"))
        self.rohrer_general_hearingButton.setText(_translate("MainWindow", "Rohrer - General Notice of Hearing"))
        self.random_judge_Button.setText(_translate("MainWindow", "Assign Random Judge"))
        self.last_judge_assigned_label.setText(_translate("MainWindow", "The Last Judge Assigned was None."))
        self.assign_judge_label.setText(_translate("MainWindow", "Assigned Judge Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scheduling_Tab), _translate("MainWindow", "Scheduling"))
        self.label_10.setText(_translate("MainWindow", "ENTRIES"))
        self.menuLogs.setTitle(_translate("MainWindow", "Logs"))
        self.actionOpen_Current_Log.setText(_translate("MainWindow", "Open Current Log"))
from .custom_widgets import ExtendedComboBox
