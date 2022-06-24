# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'package/views/ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 807)
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
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.judicial_officer_gridLayout = QtWidgets.QGridLayout()
        self.judicial_officer_gridLayout.setObjectName("judicial_officer_gridLayout")
        self.judicial_officer_frame = QtWidgets.QFrame(self.centralwidget)
        self.judicial_officer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.judicial_officer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.judicial_officer_frame.setObjectName("judicial_officer_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.judicial_officer_frame)
        self.gridLayout.setObjectName("gridLayout")
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
        self.kudela_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.kudela_radioButton.setObjectName("kudela_radioButton")
        self.gridLayout.addWidget(self.kudela_radioButton, 4, 2, 1, 1)
        self.bunner_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.bunner_radioButton.setObjectName("bunner_radioButton")
        self.gridLayout.addWidget(self.bunner_radioButton, 4, 0, 1, 1)
        self.pelanda_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.pelanda_radioButton.setObjectName("pelanda_radioButton")
        self.gridLayout.addWidget(self.pelanda_radioButton, 4, 1, 1, 1)
        self.rohrer_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.rohrer_radioButton.setObjectName("rohrer_radioButton")
        self.gridLayout.addWidget(self.rohrer_radioButton, 3, 2, 1, 1)
        self.hemmeter_radioButton = QtWidgets.QRadioButton(self.judicial_officer_frame)
        self.hemmeter_radioButton.setObjectName("hemmeter_radioButton")
        self.gridLayout.addWidget(self.hemmeter_radioButton, 3, 1, 1, 1)
        self.judicial_officer_gridLayout.addWidget(self.judicial_officer_frame, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.judicial_officer_gridLayout, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.reload_cases_Button = QtWidgets.QPushButton(self.centralwidget)
        self.reload_cases_Button.setMinimumSize(QtCore.QSize(120, 30))
        self.reload_cases_Button.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.reload_cases_Button.setObjectName("reload_cases_Button")
        self.gridLayout_3.addWidget(self.reload_cases_Button, 5, 2, 1, 1)
        self.final_pretrial_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.final_pretrial_radioButton.setObjectName("final_pretrial_radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.final_pretrial_radioButton)
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
        self.pleas_cases_box.setEditable(False)
        self.pleas_cases_box.setObjectName("pleas_cases_box")
        self.gridLayout_3.addWidget(self.pleas_cases_box, 4, 0, 1, 1)
        self.pcvh_fcvh_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.pcvh_fcvh_radioButton.setObjectName("pcvh_fcvh_radioButton")
        self.buttonGroup.addButton(self.pcvh_fcvh_radioButton)
        self.gridLayout_3.addWidget(self.pcvh_fcvh_radioButton, 3, 2, 1, 1)
        self.slated_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.slated_radioButton.setObjectName("slated_radioButton")
        self.buttonGroup.addButton(self.slated_radioButton)
        self.gridLayout_3.addWidget(self.slated_radioButton, 1, 1, 1, 1)
        self.trials_to_court_radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.trials_to_court_radioButton.setObjectName("trials_to_court_radioButton")
        self.buttonGroup.addButton(self.trials_to_court_radioButton)
        self.gridLayout_3.addWidget(self.trials_to_court_radioButton, 3, 1, 1, 1)
        self.trials_to_court_cases_box = ExtendedComboBox(self.centralwidget)
        self.trials_to_court_cases_box.setEnabled(False)
        self.trials_to_court_cases_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.trials_to_court_cases_box.setEditable(False)
        self.trials_to_court_cases_box.setObjectName("trials_to_court_cases_box")
        self.gridLayout_3.addWidget(self.trials_to_court_cases_box, 4, 1, 1, 1)
        self.pcvh_fcvh_cases_box = ExtendedComboBox(self.centralwidget)
        self.pcvh_fcvh_cases_box.setEnabled(False)
        self.pcvh_fcvh_cases_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pcvh_fcvh_cases_box.setEditable(False)
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
        self.buttonGroup.addButton(self.arraignments_radioButton)
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
        self.buttonGroup.addButton(self.pleas_radioButton)
        self.gridLayout_3.addWidget(self.pleas_radioButton, 3, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.crimTab = QtWidgets.QWidget()
        self.crimTab.setObjectName("crimTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.crimTab)
        self.gridLayout_2.setHorizontalSpacing(24)
        self.gridLayout_2.setVerticalSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LeapAdmissionButton = QtWidgets.QPushButton(self.crimTab)
        self.LeapAdmissionButton.setMinimumSize(QtCore.QSize(120, 30))
        self.LeapAdmissionButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.LeapAdmissionButton.setObjectName("LeapAdmissionButton")
        self.gridLayout_2.addWidget(self.LeapAdmissionButton, 3, 1, 1, 1)
        self.DiversionButton = QtWidgets.QPushButton(self.crimTab)
        self.DiversionButton.setMinimumSize(QtCore.QSize(120, 30))
        self.DiversionButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.DiversionButton.setObjectName("DiversionButton")
        self.gridLayout_2.addWidget(self.DiversionButton, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.crimTab)
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
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.ProbationViolationBondButton = QtWidgets.QPushButton(self.crimTab)
        self.ProbationViolationBondButton.setMinimumSize(QtCore.QSize(120, 30))
        self.ProbationViolationBondButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.ProbationViolationBondButton.setObjectName("ProbationViolationBondButton")
        self.gridLayout_2.addWidget(self.ProbationViolationBondButton, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.crimTab)
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
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.JailCCPleaButton = QtWidgets.QPushButton(self.crimTab)
        self.JailCCPleaButton.setMinimumSize(QtCore.QSize(120, 30))
        self.JailCCPleaButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.JailCCPleaButton.setObjectName("JailCCPleaButton")
        self.gridLayout_2.addWidget(self.JailCCPleaButton, 2, 0, 1, 1)
        self.PleaOnlyButton = QtWidgets.QPushButton(self.crimTab)
        self.PleaOnlyButton.setMinimumSize(QtCore.QSize(120, 30))
        self.PleaOnlyButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.PleaOnlyButton.setObjectName("PleaOnlyButton")
        self.gridLayout_2.addWidget(self.PleaOnlyButton, 2, 1, 1, 1)
        self.NotGuiltyBondButton = QtWidgets.QPushButton(self.crimTab)
        self.NotGuiltyBondButton.setMinimumSize(QtCore.QSize(120, 30))
        self.NotGuiltyBondButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.NotGuiltyBondButton.setObjectName("NotGuiltyBondButton")
        self.gridLayout_2.addWidget(self.NotGuiltyBondButton, 1, 1, 1, 1)
        self.FineOnlyPleaButton = QtWidgets.QPushButton(self.crimTab)
        self.FineOnlyPleaButton.setMinimumSize(QtCore.QSize(120, 30))
        self.FineOnlyPleaButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.FineOnlyPleaButton.setObjectName("FineOnlyPleaButton")
        self.gridLayout_2.addWidget(self.FineOnlyPleaButton, 1, 0, 1, 1)
        self.LeapSentencingButton = QtWidgets.QPushButton(self.crimTab)
        self.LeapSentencingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.LeapSentencingButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.LeapSentencingButton.setObjectName("LeapSentencingButton")
        self.gridLayout_2.addWidget(self.LeapSentencingButton, 7, 1, 1, 1)
        self.NoPleaBondButton = QtWidgets.QPushButton(self.crimTab)
        self.NoPleaBondButton.setMinimumSize(QtCore.QSize(120, 30))
        self.NoPleaBondButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.NoPleaBondButton.setObjectName("NoPleaBondButton")
        self.gridLayout_2.addWidget(self.NoPleaBondButton, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.crimTab)
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
        self.gridLayout_2.addWidget(self.label_5, 4, 1, 1, 1)
        self.TrialSentencingButton = QtWidgets.QPushButton(self.crimTab)
        self.TrialSentencingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.TrialSentencingButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.TrialSentencingButton.setObjectName("TrialSentencingButton")
        self.gridLayout_2.addWidget(self.TrialSentencingButton, 5, 1, 1, 1)
        self.FailureToAppearButton = QtWidgets.QPushButton(self.crimTab)
        self.FailureToAppearButton.setMinimumSize(QtCore.QSize(120, 30))
        self.FailureToAppearButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.FailureToAppearButton.setObjectName("FailureToAppearButton")
        self.gridLayout_2.addWidget(self.FailureToAppearButton, 5, 2, 1, 1)
        self.BondHearingButton = QtWidgets.QPushButton(self.crimTab)
        self.BondHearingButton.setMinimumSize(QtCore.QSize(120, 30))
        self.BondHearingButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.BondHearingButton.setObjectName("BondHearingButton")
        self.gridLayout_2.addWidget(self.BondHearingButton, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.crimTab)
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
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.crimTab)
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
        self.gridLayout_2.addWidget(self.label_7, 4, 2, 1, 1)
        self.SentencingOnlyButton = QtWidgets.QPushButton(self.crimTab)
        self.SentencingOnlyButton.setMinimumSize(QtCore.QSize(120, 30))
        self.SentencingOnlyButton.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.SentencingOnlyButton.setObjectName("SentencingOnlyButton")
        self.gridLayout_2.addWidget(self.SentencingOnlyButton, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.crimTab)
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
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.FreeformEntryButton = QtWidgets.QPushButton(self.crimTab)
        self.FreeformEntryButton.setMinimumSize(QtCore.QSize(120, 30))
        self.FreeformEntryButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.FreeformEntryButton.setObjectName("FreeformEntryButton")
        self.gridLayout_2.addWidget(self.FreeformEntryButton, 5, 0, 1, 1)
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
        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 1)
        self.gridLayout_5.setRowStretch(2, 1)
        self.gridLayout_5.setRowStretch(3, 1)
        self.gridLayout_5.setRowStretch(5, 2)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1103, 27))
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
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MuniEntry - ver 0.24.0"))
        self.judicial_officer_label.setText(_translate("MainWindow", "JUDICIAL OFFICER:"))
        self.kudela_radioButton.setText(_translate("MainWindow", "Magistrate Kudela"))
        self.bunner_radioButton.setText(_translate("MainWindow", "Magistrate Bunner"))
        self.pelanda_radioButton.setText(_translate("MainWindow", "Magistrate Pelanda"))
        self.rohrer_radioButton.setText(_translate("MainWindow", "Judge Rohrer"))
        self.hemmeter_radioButton.setText(_translate("MainWindow", "Judge Hemmeter"))
        self.reload_cases_Button.setText(_translate("MainWindow", "Reload Cases"))
        self.final_pretrial_radioButton.setText(_translate("MainWindow", "Final Pre-trials"))
        self.label_3.setText(_translate("MainWindow", "DAILY CASE LISTS"))
        self.pcvh_fcvh_radioButton.setText(_translate("MainWindow", "PCVH/FCVH"))
        self.slated_radioButton.setText(_translate("MainWindow", "Slated                                  "))
        self.trials_to_court_radioButton.setText(_translate("MainWindow", "Trials to Court and Jury Trials"))
        self.arraignments_radioButton.setText(_translate("MainWindow", "Arraignments"))
        self.pleas_radioButton.setText(_translate("MainWindow", "Pleas and Motion/Oral Hearings"))
        self.label.setText(_translate("MainWindow", "ENTRIES"))
        self.LeapAdmissionButton.setText(_translate("MainWindow", "LEAP Admission Plea"))
        self.DiversionButton.setText(_translate("MainWindow", "Diversion"))
        self.label_2.setText(_translate("MainWindow", "Plea and Sentence Entries"))
        self.ProbationViolationBondButton.setText(_translate("MainWindow", "Prelim. Probation Violation / Bond"))
        self.label_4.setText(_translate("MainWindow", "Plea Only Entries"))
        self.JailCCPleaButton.setText(_translate("MainWindow", "Jail and/or Community Control"))
        self.PleaOnlyButton.setText(_translate("MainWindow", "Plea Only - Future Sentencing"))
        self.NotGuiltyBondButton.setText(_translate("MainWindow", "Not Guilty Plea / Bond"))
        self.FineOnlyPleaButton.setText(_translate("MainWindow", "Fine Only"))
        self.LeapSentencingButton.setText(_translate("MainWindow", "LEAP Sentencing"))
        self.NoPleaBondButton.setText(_translate("MainWindow", "Appear on Warrant (No Plea) / Bond"))
        self.label_5.setText(_translate("MainWindow", "Sentencing Only Entries"))
        self.TrialSentencingButton.setText(_translate("MainWindow", "Jury Trial / Trial to Court Sentencing"))
        self.FailureToAppearButton.setText(_translate("MainWindow", "Failed to Appear / Issue Warrant"))
        self.BondHearingButton.setText(_translate("MainWindow", "Bond Modification / Revocation"))
        self.label_6.setText(_translate("MainWindow", "Bond Entries"))
        self.label_7.setText(_translate("MainWindow", "Warrant Entries"))
        self.SentencingOnlyButton.setText(_translate("MainWindow", "Sentencing Only - Already Plead"))
        self.label_8.setText(_translate("MainWindow", "General Entries"))
        self.FreeformEntryButton.setText(_translate("MainWindow", "Freeform Entry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.crimTab), _translate("MainWindow", "Crim/Traffic"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.rohrer_schedulingEntryButton.setText(_translate("MainWindow", "Rohrer Scheduling Entry"))
        self.hemmeter_schedulingEntryButton.setText(_translate("MainWindow", "Hemmeter Scheduling Entry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.schedulingTab), _translate("MainWindow", "Scheduling"))
        self.menuLogs.setTitle(_translate("MainWindow", "Logs"))
        self.actionOpen_Current_Log.setText(_translate("MainWindow", "Open Current Log"))
from .custom_widgets import ExtendedComboBox
