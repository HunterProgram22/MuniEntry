# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package\views\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 700)
        MainWindow.setMinimumSize(QtCore.QSize(860, 700))
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
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.reload_cases_Button = QtWidgets.QPushButton(self.centralwidget)
        self.reload_cases_Button.setMinimumSize(QtCore.QSize(120, 30))
        self.reload_cases_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.reload_cases_Button.setObjectName("reload_cases_Button")
        self.gridLayout_3.addWidget(self.reload_cases_Button, 5, 2, 1, 1)
        self.final_pretrial_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.final_pretrial_radioButton.setObjectName("final_pretrial_radioButton")
        self.gridLayout_3.addWidget(self.final_pretrial_radioButton, 1, 2, 1, 1)
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
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 3)
        self.pleas_cases_box = ExtendedComboBox(self.centralwidget)
        self.pleas_cases_box.setEnabled(False)
        self.pleas_cases_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pleas_cases_box.setObjectName("pleas_cases_box")
        self.gridLayout_3.addWidget(self.pleas_cases_box, 4, 0, 1, 1)
        self.pcvh_fcvh_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.pcvh_fcvh_radioButton.setObjectName("pcvh_fcvh_radioButton")
        self.gridLayout_3.addWidget(self.pcvh_fcvh_radioButton, 3, 2, 1, 1)
        self.slated_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.slated_radioButton.setObjectName("slated_radioButton")
        self.gridLayout_3.addWidget(self.slated_radioButton, 1, 1, 1, 1)
        self.trials_to_court_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.trials_to_court_radioButton.setObjectName("trials_to_court_radioButton")
        self.gridLayout_3.addWidget(self.trials_to_court_radioButton, 3, 1, 1, 1)
        self.trials_to_court_cases_box = ExtendedComboBox(self.centralwidget)
        self.trials_to_court_cases_box.setEnabled(False)
        self.trials_to_court_cases_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.trials_to_court_cases_box.setObjectName("trials_to_court_cases_box")
        self.gridLayout_3.addWidget(self.trials_to_court_cases_box, 4, 1, 1, 1)
        self.pcvh_fcvh_cases_box = ExtendedComboBox(self.centralwidget)
        self.pcvh_fcvh_cases_box.setEnabled(False)
        self.pcvh_fcvh_cases_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pcvh_fcvh_cases_box.setObjectName("pcvh_fcvh_cases_box")
        self.gridLayout_3.addWidget(self.pcvh_fcvh_cases_box, 4, 2, 1, 1)
        self.arraignments_cases_box = ExtendedComboBox(self.centralwidget)
        self.arraignments_cases_box.setEnabled(False)
        self.arraignments_cases_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.arraignments_cases_box.setEditable(False)
        self.arraignments_cases_box.setObjectName("arraignments_cases_box")
        self.gridLayout_3.addWidget(self.arraignments_cases_box, 2, 0, 1, 1)
        self.arraignments_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.arraignments_radioButton.setObjectName("arraignments_radioButton")
        self.gridLayout_3.addWidget(self.arraignments_radioButton, 1, 0, 1, 1)
        self.slated_cases_box = ExtendedComboBox(self.centralwidget)
        self.slated_cases_box.setEnabled(False)
        self.slated_cases_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.slated_cases_box.setEditable(False)
        self.slated_cases_box.setObjectName("slated_cases_box")
        self.gridLayout_3.addWidget(self.slated_cases_box, 2, 1, 1, 1)
        self.final_pretrial_cases_box = ExtendedComboBox(self.centralwidget)
        self.final_pretrial_cases_box.setEnabled(False)
        self.final_pretrial_cases_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.final_pretrial_cases_box.setEditable(False)
        self.final_pretrial_cases_box.setObjectName("final_pretrial_cases_box")
        self.gridLayout_3.addWidget(self.final_pretrial_cases_box, 2, 2, 1, 1)
        self.pleas_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.pleas_radioButton.setObjectName("pleas_radioButton")
        self.gridLayout_3.addWidget(self.pleas_radioButton, 3, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.judicial_officer_gridLayout = QtWidgets.QGridLayout()
        self.judicial_officer_gridLayout.setObjectName("judicial_officer_gridLayout")
        self.judicial_officer_frame = QtWidgets.QFrame(self.centralwidget)
        self.judicial_officer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.judicial_officer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.judicial_officer_frame.setObjectName("judicial_officer_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.judicial_officer_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pelanda_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.pelanda_radioButton.setObjectName("pelanda_radioButton")
        self.gridLayout.addWidget(self.pelanda_radioButton, 4, 1, 1, 1)
        self.bunner_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.bunner_radioButton.setObjectName("bunner_radioButton")
        self.gridLayout.addWidget(self.bunner_radioButton, 4, 0, 1, 1)
        self.kudela_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.kudela_radioButton.setObjectName("kudela_radioButton")
        self.gridLayout.addWidget(self.kudela_radioButton, 4, 2, 1, 1)
        self.judicial_officer_label = QtWidgets.QLabel(self.judicial_officer_frame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.judicial_officer_label.setFont(font)
        self.judicial_officer_label.setObjectName("judicial_officer_label")
        self.gridLayout.addWidget(self.judicial_officer_label, 3, 0, 1, 1)
        self.hemmeter_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.hemmeter_radioButton.setObjectName("hemmeter_radioButton")
        self.gridLayout.addWidget(self.hemmeter_radioButton, 3, 1, 1, 1)
        self.rohrer_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.rohrer_radioButton.setObjectName("rohrer_radioButton")
        self.gridLayout.addWidget(self.rohrer_radioButton, 3, 2, 1, 1)
        self.judicial_officer_gridLayout.addWidget(self.judicial_officer_frame, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.judicial_officer_gridLayout, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.crimTab = QtWidgets.QWidget()
        self.crimTab.setObjectName("crimTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.crimTab)
        self.gridLayout_2.setHorizontalSpacing(18)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.FineOnlyPleaButton = QtWidgets.QPushButton(self.crimTab)
        self.FineOnlyPleaButton.setMinimumSize(QtCore.QSize(120, 30))
        self.FineOnlyPleaButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.FineOnlyPleaButton.setObjectName("FineOnlyPleaButton")
        self.gridLayout_2.addWidget(self.FineOnlyPleaButton, 0, 0, 1, 1)
        self.FailureToAppearButton = QtWidgets.QPushButton(self.crimTab)
        self.FailureToAppearButton.setMinimumSize(QtCore.QSize(120, 30))
        self.FailureToAppearButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.FailureToAppearButton.setObjectName("FailureToAppearButton")
        self.gridLayout_2.addWidget(self.FailureToAppearButton, 0, 1, 1, 1)
        self.NotGuiltyBondButton = QtWidgets.QPushButton(self.crimTab)
        self.NotGuiltyBondButton.setMinimumSize(QtCore.QSize(120, 30))
        self.NotGuiltyBondButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.NotGuiltyBondButton.setObjectName("NotGuiltyBondButton")
        self.gridLayout_2.addWidget(self.NotGuiltyBondButton, 0, 2, 1, 1)
        self.JailCCPleaButton = QtWidgets.QPushButton(self.crimTab)
        self.JailCCPleaButton.setMinimumSize(QtCore.QSize(120, 30))
        self.JailCCPleaButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.JailCCPleaButton.setObjectName("JailCCPleaButton")
        self.gridLayout_2.addWidget(self.JailCCPleaButton, 1, 0, 1, 1)
        self.NoPleaBondButton = QtWidgets.QPushButton(self.crimTab)
        self.NoPleaBondButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.NoPleaBondButton.setObjectName("NoPleaBondButton")
        self.gridLayout_2.addWidget(self.NoPleaBondButton, 1, 2, 1, 1)
        self.BondHearingButton = QtWidgets.QPushButton(self.crimTab)
        self.BondHearingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.BondHearingButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.BondHearingButton.setObjectName("BondHearingButton")
        self.gridLayout_2.addWidget(self.BondHearingButton, 1, 1, 1, 1)
        self.DiversionButton = QtWidgets.QPushButton(self.crimTab)
        self.DiversionButton.setMinimumSize(QtCore.QSize(120, 30))
        self.DiversionButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.DiversionButton.setObjectName("DiversionButton")
        self.gridLayout_2.addWidget(self.DiversionButton, 2, 0, 1, 1)
        self.PleaOnlyButton = QtWidgets.QPushButton(self.crimTab)
        self.PleaOnlyButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.PleaOnlyButton.setObjectName("PleaOnlyButton")
        self.gridLayout_2.addWidget(self.PleaOnlyButton, 2, 1, 1, 1)
        self.ProbationViolationBondButton = QtWidgets.QPushButton(self.crimTab)
        self.ProbationViolationBondButton.setMinimumSize(QtCore.QSize(120, 30))
        self.ProbationViolationBondButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.ProbationViolationBondButton.setObjectName("ProbationViolationBondButton")
        self.gridLayout_2.addWidget(self.ProbationViolationBondButton, 2, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.tabWidget.addTab(self.crimTab, "")
        self.schedulingTab = QtWidgets.QWidget()
        self.schedulingTab.setObjectName("schedulingTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.schedulingTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.schedulingTab)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_4.addWidget(self.pushButton_12, 1, 2, 1, 1)
        self.rohrer_schedulingEntryButton = QtWidgets.QPushButton(self.schedulingTab)
        self.rohrer_schedulingEntryButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.rohrer_schedulingEntryButton.setObjectName("rohrer_schedulingEntryButton")
        self.gridLayout_4.addWidget(self.rohrer_schedulingEntryButton, 1, 0, 1, 1)
        self.hemmeter_schedulingEntryButton = QtWidgets.QPushButton(self.schedulingTab)
        self.hemmeter_schedulingEntryButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.hemmeter_schedulingEntryButton.setObjectName("hemmeter_schedulingEntryButton")
        self.gridLayout_4.addWidget(self.hemmeter_schedulingEntryButton, 1, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.tabWidget.addTab(self.schedulingTab, "")
        self.gridLayout_5.addWidget(self.tabWidget, 5, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_5.addWidget(self.line_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 250))
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
        self.gridLayout_5.addWidget(self.label, 4, 0, 1, 1)
        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 1)
        self.gridLayout_5.setRowStretch(2, 1)
        self.gridLayout_5.setRowStretch(3, 1)
        self.gridLayout_5.setRowStretch(5, 2)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu_file_exit = QtWidgets.QAction(MainWindow)
        self.menu_file_exit.setObjectName("menu_file_exit")
        self.actionGeneral_Motion_Entry = QtWidgets.QAction(MainWindow)
        self.actionGeneral_Motion_Entry.setObjectName("actionGeneral_Motion_Entry")
        self.actionFail_to_Appear_Minor_Traffic_Offense = QtWidgets.QAction(MainWindow)
        self.actionFail_to_Appear_Minor_Traffic_Offense.setObjectName("actionFail_to_Appear_Minor_Traffic_Offense")
        self.actionOmnibus_Motion_Form = QtWidgets.QAction(MainWindow)
        self.actionOmnibus_Motion_Form.setObjectName("actionOmnibus_Motion_Form")
        self.actionJury_Instructions = QtWidgets.QAction(MainWindow)
        self.actionJury_Instructions.setObjectName("actionJury_Instructions")
        self.actioncontrollers = QtWidgets.QAction(MainWindow)
        self.actioncontrollers.setObjectName("actioncontrollers")
        self.actionTemplates = QtWidgets.QAction(MainWindow)
        self.actionTemplates.setObjectName("actionTemplates")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOptions)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu_file_exit)
        self.menuSettings.addAction(self.actioncontrollers)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.FineOnlyPleaButton, self.FailureToAppearButton)
        MainWindow.setTabOrder(self.FailureToAppearButton, self.NotGuiltyBondButton)
        MainWindow.setTabOrder(self.NotGuiltyBondButton, self.JailCCPleaButton)
        MainWindow.setTabOrder(self.JailCCPleaButton, self.DiversionButton)
        MainWindow.setTabOrder(self.DiversionButton, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MuniEntry - ver 0.21.1"))
        self.reload_cases_Button.setText(_translate("MainWindow", "Reload Cases"))
        self.final_pretrial_radioButton.setText(_translate("MainWindow", "Final Pre-trials"))
        self.label_3.setText(_translate("MainWindow", "DAILY CASE LISTS"))
        self.pcvh_fcvh_radioButton.setText(_translate("MainWindow", "PCVH/FCVH"))
        self.slated_radioButton.setText(_translate("MainWindow", "Slated                                  "))
        self.trials_to_court_radioButton.setText(_translate("MainWindow", "Trials to Court and Jury Trials"))
        self.arraignments_radioButton.setText(_translate("MainWindow", "Arraignments"))
        self.pleas_radioButton.setText(_translate("MainWindow", "Pleas and Motion/Oral Hearings"))
        self.pelanda_radioButton.setText(_translate("MainWindow", "Magistrate Pelanda"))
        self.bunner_radioButton.setText(_translate("MainWindow", "Magistrate Bunner"))
        self.kudela_radioButton.setText(_translate("MainWindow", "Magistrate Kudela"))
        self.judicial_officer_label.setText(_translate("MainWindow", "JUDICIAL OFFICER:"))
        self.hemmeter_radioButton.setText(_translate("MainWindow", "Judge Hemmeter"))
        self.rohrer_radioButton.setText(_translate("MainWindow", "Judge Rohrer"))
        self.FineOnlyPleaButton.setText(_translate("MainWindow", "Fine Only Plea"))
        self.FailureToAppearButton.setText(_translate("MainWindow", "Failed to Appear / Issue Warrant"))
        self.NotGuiltyBondButton.setText(_translate("MainWindow", "Not Guilty / Bond"))
        self.JailCCPleaButton.setText(_translate("MainWindow", "Jail and Comm. Control Plea"))
        self.NoPleaBondButton.setText(_translate("MainWindow", "Appear on Warrant (No Plea) / Bond"))
        self.BondHearingButton.setText(_translate("MainWindow", "Bond Modification / Revocation"))
        self.DiversionButton.setText(_translate("MainWindow", "Diversion Plea"))
        self.PleaOnlyButton.setText(_translate("MainWindow", "Plea Future Sentence Date"))
        self.ProbationViolationBondButton.setText(_translate("MainWindow", "Prelim. Probation Violation / Bond"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.crimTab), _translate("MainWindow", "Crim/Traffic"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.rohrer_schedulingEntryButton.setText(_translate("MainWindow", "Rohrer Scheduling Entry"))
        self.hemmeter_schedulingEntryButton.setText(_translate("MainWindow", "Hemmeter Scheduling Entry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.schedulingTab), _translate("MainWindow", "Scheduling"))
        self.label.setText(_translate("MainWindow", "ENTRIES"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionExit.setText(_translate("MainWindow", "Templates"))
        self.menu_file_exit.setText(_translate("MainWindow", "Exit"))
        self.actionGeneral_Motion_Entry.setText(_translate("MainWindow", "General Motion Entry"))
        self.actionFail_to_Appear_Minor_Traffic_Offense.setText(_translate("MainWindow", "Fail to Appear - Minor Traffic Offense"))
        self.actionOmnibus_Motion_Form.setText(_translate("MainWindow", "Omnibus Motion Form"))
        self.actionJury_Instructions.setText(_translate("MainWindow", "Jury Instructions"))
        self.actioncontrollers.setText(_translate("MainWindow", "controllers"))
        self.actionTemplates.setText(_translate("MainWindow", "Templates"))
from .custom_widgets import ExtendedComboBox
