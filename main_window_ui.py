# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWIndow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 181, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.TransferEntryDialog = QtWidgets.QPushButton(self.layoutWidget)
        self.TransferEntryDialog.setObjectName("TransferEntryDialog")
        self.gridLayout.addWidget(self.TransferEntryDialog, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)
        self.VerdictForm_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.VerdictForm_pushButton.setObjectName("VerdictForm_pushButton")
        self.gridLayout.addWidget(self.VerdictForm_pushButton, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.JuryInstructions_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.JuryInstructions_pushButton.setObjectName("JuryInstructions_pushButton")
        self.gridLayout.addWidget(self.JuryInstructions_pushButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCriminal = QtWidgets.QMenu(self.menubar)
        self.menuCriminal.setObjectName("menuCriminal")
        self.menuGeneral = QtWidgets.QMenu(self.menubar)
        self.menuGeneral.setObjectName("menuGeneral")
        self.menuCivil = QtWidgets.QMenu(self.menubar)
        self.menuCivil.setObjectName("menuCivil")
        self.menuProbation = QtWidgets.QMenu(self.menubar)
        self.menuProbation.setObjectName("menuProbation")
        self.menuClerk = QtWidgets.QMenu(self.menubar)
        self.menuClerk.setObjectName("menuClerk")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
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
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionGeneral_Motion_Entry = QtWidgets.QAction(MainWindow)
        self.actionGeneral_Motion_Entry.setObjectName("actionGeneral_Motion_Entry")
        self.actionFail_to_Appear_Minor_Traffic_Offense = QtWidgets.QAction(MainWindow)
        self.actionFail_to_Appear_Minor_Traffic_Offense.setObjectName("actionFail_to_Appear_Minor_Traffic_Offense")
        self.actionOmnibus_Motion_Form = QtWidgets.QAction(MainWindow)
        self.actionOmnibus_Motion_Form.setObjectName("actionOmnibus_Motion_Form")
        self.actionJury_Instructions = QtWidgets.QAction(MainWindow)
        self.actionJury_Instructions.setObjectName("actionJury_Instructions")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOptions)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuCriminal.addAction(self.actionGeneral_Motion_Entry)
        self.menuCriminal.addSeparator()
        self.menuCriminal.addAction(self.actionFail_to_Appear_Minor_Traffic_Offense)
        self.menuGeneral.addAction(self.actionOmnibus_Motion_Form)
        self.menuGeneral.addAction(self.actionJury_Instructions)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGeneral.menuAction())
        self.menubar.addAction(self.menuCriminal.menuAction())
        self.menubar.addAction(self.menuCivil.menuAction())
        self.menubar.addAction(self.menuProbation.menuAction())
        self.menubar.addAction(self.menuClerk.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())

        self.retranslateUi(MainWindow)
        self.VerdictForm_pushButton.clicked.connect(MainWindow.pushButtonVerdictForm)
        self.JuryInstructions_pushButton.clicked.connect(MainWindow.pushButtonJuryInstructions)
        self.pushButton.clicked.connect(MainWindow.pushButtonOmnibusMotion)
        self.TransferEntryDialog.clicked.connect(MainWindow.pushButtonTransferEntry)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MuniEntry"))
        self.TransferEntryDialog.setText(_translate("MainWindow", "Transfer Entry"))
        self.pushButton.setText(_translate("MainWindow", "Omnibus Motion"))
        self.VerdictForm_pushButton.setText(_translate("MainWindow", "Verdict Form"))
        self.JuryInstructions_pushButton.setText(_translate("MainWindow", "Jury Instructions"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCriminal.setTitle(_translate("MainWindow", "Criminal"))
        self.menuGeneral.setTitle(_translate("MainWindow", "General"))
        self.menuCivil.setTitle(_translate("MainWindow", "Civil"))
        self.menuProbation.setTitle(_translate("MainWindow", "Probation"))
        self.menuClerk.setTitle(_translate("MainWindow", "Clerk"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionExit.setText(_translate("MainWindow", "Templates"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionGeneral_Motion_Entry.setText(_translate("MainWindow", "General Motion Entry"))
        self.actionFail_to_Appear_Minor_Traffic_Offense.setText(_translate("MainWindow", "Fail to Appear - Minor Traffic Offense"))
        self.actionOmnibus_Motion_Form.setText(_translate("MainWindow", "Omnibus Motion Form"))
        self.actionJury_Instructions.setText(_translate("MainWindow", "Jury Instructions"))
