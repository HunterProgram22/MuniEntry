# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 803)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.FinalJudgmentEntryButton_14 = QtWidgets.QPushButton(self.tab)
        self.FinalJudgmentEntryButton_14.setMinimumSize(QtCore.QSize(120, 30))
        self.FinalJudgmentEntryButton_14.setObjectName("FinalJudgmentEntryButton_14")
        self.gridLayout_2.addWidget(self.FinalJudgmentEntryButton_14, 9, 2, 1, 2)
        self.hemmeter_radioButton = QtWidgets.QRadioButton(self.tab)
        self.hemmeter_radioButton.setObjectName("hemmeter_radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.hemmeter_radioButton)
        self.gridLayout_2.addWidget(self.hemmeter_radioButton, 0, 1, 1, 2)
        self.MinorMisdemeanorTrafficButton_3 = QtWidgets.QPushButton(self.tab)
        self.MinorMisdemeanorTrafficButton_3.setMinimumSize(QtCore.QSize(120, 30))
        self.MinorMisdemeanorTrafficButton_3.setObjectName("MinorMisdemeanorTrafficButton_3")
        self.gridLayout_2.addWidget(self.MinorMisdemeanorTrafficButton_3, 8, 4, 1, 2)
        self.FinalJudgmentEntryButton_12 = QtWidgets.QPushButton(self.tab)
        self.FinalJudgmentEntryButton_12.setMinimumSize(QtCore.QSize(120, 30))
        self.FinalJudgmentEntryButton_12.setObjectName("FinalJudgmentEntryButton_12")
        self.gridLayout_2.addWidget(self.FinalJudgmentEntryButton_12, 8, 2, 1, 2)
        self.FinalJudgmentEntryButton_15 = QtWidgets.QPushButton(self.tab)
        self.FinalJudgmentEntryButton_15.setMinimumSize(QtCore.QSize(120, 30))
        self.FinalJudgmentEntryButton_15.setObjectName("FinalJudgmentEntryButton_15")
        self.gridLayout_2.addWidget(self.FinalJudgmentEntryButton_15, 9, 4, 1, 2)
        self.FinalJudgmentEntryButton_4 = QtWidgets.QPushButton(self.tab)
        self.FinalJudgmentEntryButton_4.setMinimumSize(QtCore.QSize(120, 30))
        self.FinalJudgmentEntryButton_4.setObjectName("FinalJudgmentEntryButton_4")
        self.gridLayout_2.addWidget(self.FinalJudgmentEntryButton_4, 6, 4, 1, 2)
        self.LeapPleaLongButton = QtWidgets.QPushButton(self.tab)
        self.LeapPleaLongButton.setMinimumSize(QtCore.QSize(120, 30))
        self.LeapPleaLongButton.setObjectName("LeapPleaLongButton")
        self.gridLayout_2.addWidget(self.LeapPleaLongButton, 5, 2, 1, 2)
        self.NotGuiltyBondButton = QtWidgets.QPushButton(self.tab)
        self.NotGuiltyBondButton.setMinimumSize(QtCore.QSize(120, 30))
        self.NotGuiltyBondButton.setObjectName("NotGuiltyBondButton")
        self.gridLayout_2.addWidget(self.NotGuiltyBondButton, 6, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 1)
        self.FinalJudgmentEntryButton_11 = QtWidgets.QPushButton(self.tab)
        self.FinalJudgmentEntryButton_11.setMinimumSize(QtCore.QSize(120, 30))
        self.FinalJudgmentEntryButton_11.setObjectName("FinalJudgmentEntryButton_11")
        self.gridLayout_2.addWidget(self.FinalJudgmentEntryButton_11, 8, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.kudela_radioButton = QtWidgets.QRadioButton(self.tab)
        self.kudela_radioButton.setObjectName("kudela_radioButton")
        self.buttonGroup.addButton(self.kudela_radioButton)
        self.gridLayout_2.addWidget(self.kudela_radioButton, 0, 5, 1, 1)
        self.pelanda_radioButton = QtWidgets.QRadioButton(self.tab)
        self.pelanda_radioButton.setObjectName("pelanda_radioButton")
        self.buttonGroup.addButton(self.pelanda_radioButton)
        self.gridLayout_2.addWidget(self.pelanda_radioButton, 1, 3, 1, 2)
        self.LeapPleaShortButton = QtWidgets.QPushButton(self.tab)
        self.LeapPleaShortButton.setMinimumSize(QtCore.QSize(120, 30))
        self.LeapPleaShortButton.setObjectName("LeapPleaShortButton")
        self.gridLayout_2.addWidget(self.LeapPleaShortButton, 5, 4, 1, 2)
        self.NoJailPleaButton = QtWidgets.QPushButton(self.tab)
        self.NoJailPleaButton.setMinimumSize(QtCore.QSize(120, 30))
        self.NoJailPleaButton.setObjectName("NoJailPleaButton")
        self.gridLayout_2.addWidget(self.NoJailPleaButton, 5, 0, 1, 2)
        self.rohrer_radioButton = QtWidgets.QRadioButton(self.tab)
        self.rohrer_radioButton.setObjectName("rohrer_radioButton")
        self.buttonGroup.addButton(self.rohrer_radioButton)
        self.gridLayout_2.addWidget(self.rohrer_radioButton, 1, 1, 1, 2)
        self.bunner_radioButton = QtWidgets.QRadioButton(self.tab)
        self.bunner_radioButton.setObjectName("bunner_radioButton")
        self.buttonGroup.addButton(self.bunner_radioButton)
        self.gridLayout_2.addWidget(self.bunner_radioButton, 0, 3, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 2)
        self.FinalJudgmentEntryButton_13 = QtWidgets.QPushButton(self.tab)
        self.FinalJudgmentEntryButton_13.setMinimumSize(QtCore.QSize(120, 30))
        self.FinalJudgmentEntryButton_13.setObjectName("FinalJudgmentEntryButton_13")
        self.gridLayout_2.addWidget(self.FinalJudgmentEntryButton_13, 9, 0, 1, 2)
        self.arraignment_cases_box = QtWidgets.QComboBox(self.tab)
        self.arraignment_cases_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.arraignment_cases_box.setObjectName("arraignment_cases_box")
        self.gridLayout_2.addWidget(self.arraignment_cases_box, 3, 0, 1, 2)
        self.FTABondButton = QtWidgets.QPushButton(self.tab)
        self.FTABondButton.setMinimumSize(QtCore.QSize(120, 30))
        self.FTABondButton.setObjectName("FTABondButton")
        self.gridLayout_2.addWidget(self.FTABondButton, 6, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_3.addWidget(self.radioButton_4, 0, 1, 1, 2)
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_3.addWidget(self.radioButton, 0, 3, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_3.addWidget(self.radioButton_3, 1, 1, 1, 2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_3.addWidget(self.radioButton_2, 1, 3, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_3.addWidget(self.radioButton_5, 2, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 4, 0, 1, 2)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 4, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 4, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 5, 0, 1, 2)
        self.JurorPaymentButton = QtWidgets.QPushButton(self.tab_2)
        self.JurorPaymentButton.setObjectName("JurorPaymentButton")
        self.gridLayout_3.addWidget(self.JurorPaymentButton, 6, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 6, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 6, 3, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 29))
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MuniEntry - ver 0.3.1"))
        self.FinalJudgmentEntryButton_14.setText(_translate("MainWindow", "Entry"))
        self.hemmeter_radioButton.setText(_translate("MainWindow", "Judge Hemmeter"))
        self.MinorMisdemeanorTrafficButton_3.setText(_translate("MainWindow", "Entry"))
        self.FinalJudgmentEntryButton_12.setText(_translate("MainWindow", "Entry"))
        self.FinalJudgmentEntryButton_15.setText(_translate("MainWindow", "Entry"))
        self.FinalJudgmentEntryButton_4.setText(_translate("MainWindow", "Entry"))
        self.LeapPleaLongButton.setText(_translate("MainWindow", "LEAP Plea "))
        self.NotGuiltyBondButton.setText(_translate("MainWindow", "Not Guilty / Bond"))
        self.label_4.setText(_translate("MainWindow", "Civil Entries"))
        self.FinalJudgmentEntryButton_11.setText(_translate("MainWindow", "Entry"))
        self.label.setText(_translate("MainWindow", "Judicial Officer:"))
        self.kudela_radioButton.setText(_translate("MainWindow", "Magistrate Kudela"))
        self.pelanda_radioButton.setText(_translate("MainWindow", "Magistrate Pelanda"))
        self.LeapPleaShortButton.setText(_translate("MainWindow", "LEAP Plea Pre-Court Complete"))
        self.NoJailPleaButton.setText(_translate("MainWindow", "No Jail Plea"))
        self.rohrer_radioButton.setText(_translate("MainWindow", "Judge Rohrer"))
        self.bunner_radioButton.setText(_translate("MainWindow", "Magistrate Bunner"))
        self.label_2.setText(_translate("MainWindow", "Traffic and Criminal Entries"))
        self.label_3.setText(_translate("MainWindow", "Arraignment Cases List:"))
        self.FinalJudgmentEntryButton_13.setText(_translate("MainWindow", "Entry"))
        self.FTABondButton.setText(_translate("MainWindow", "FTA / Bond"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Judicial"))
        self.label_6.setText(_translate("MainWindow", "Staff Member:"))
        self.radioButton_4.setText(_translate("MainWindow", "Court Administrator Kudela"))
        self.radioButton.setText(_translate("MainWindow", "Assignment Commissioner Datillo"))
        self.radioButton_3.setText(_translate("MainWindow", "Assignment Commissioner Travis"))
        self.radioButton_2.setText(_translate("MainWindow", "Jury Commissioner Travis"))
        self.radioButton_5.setText(_translate("MainWindow", "No Signature"))
        self.label_7.setText(_translate("MainWindow", "Letters"))
        self.pushButton_4.setText(_translate("MainWindow", "Judge No Review"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.label_5.setText(_translate("MainWindow", "Administrative Entries"))
        self.JurorPaymentButton.setText(_translate("MainWindow", "Juror Payment"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Admin"))
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
