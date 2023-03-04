# Form implementation generated from reading ui file 'munientry/views/ui/HemmeterWorkflowDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HemmeterWorkflowDialog(object):
    def setupUi(self, HemmeterWorkflowDialog):
        HemmeterWorkflowDialog.setObjectName("HemmeterWorkflowDialog")
        HemmeterWorkflowDialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        HemmeterWorkflowDialog.resize(1006, 828)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HemmeterWorkflowDialog.sizePolicy().hasHeightForWidth())
        HemmeterWorkflowDialog.setSizePolicy(sizePolicy)
        HemmeterWorkflowDialog.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        HemmeterWorkflowDialog.setFont(font)
        HemmeterWorkflowDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";")
        self.gridLayout = QtWidgets.QGridLayout(HemmeterWorkflowDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(HemmeterWorkflowDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font-weight: bold;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setVerticalSpacing(24)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.open_entry_Button = QtWidgets.QPushButton(self.frame_3)
        self.open_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.open_entry_Button.setObjectName("open_entry_Button")
        self.gridLayout_2.addWidget(self.open_entry_Button, 4, 0, 1, 1)
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_3)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_2.addWidget(self.close_dialog_Button, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 2)
        self.entries_tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.entries_tableWidget.setObjectName("entries_tableWidget")
        self.entries_tableWidget.setColumnCount(0)
        self.entries_tableWidget.setRowCount(0)
        self.gridLayout_2.addWidget(self.entries_tableWidget, 2, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 2)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 4)
        self.gridLayout_2.setRowStretch(2, 7)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 2)

        self.retranslateUi(HemmeterWorkflowDialog)
        QtCore.QMetaObject.connectSlotsByName(HemmeterWorkflowDialog)

    def retranslateUi(self, HemmeterWorkflowDialog):
        _translate = QtCore.QCoreApplication.translate
        HemmeterWorkflowDialog.setWindowTitle(_translate("HemmeterWorkflowDialog", "Judge Hemmeter Digital Workflow"))
        self.open_entry_Button.setText(_translate("HemmeterWorkflowDialog", "Open Entry for Review"))
        self.close_dialog_Button.setText(_translate("HemmeterWorkflowDialog", "Close Workflow"))
        self.label.setText(_translate("HemmeterWorkflowDialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">ADMINISTRATIVE ENTRIES PENDING REVIEW</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("HemmeterWorkflowDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Palatino Linotype\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The entries listed below are Administrative Entries that are not case specific. After selecting the entry and opening it for review, select whether to accept or reject the entry.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If the entry is accepted, the Administrative Judge\'s digital signature will be attached along with a file stamp, then the entry will be sent to the Clerk\'s Office to be placed in the Administrative Journal.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If the entry is rejected, the person that created the entry will be notified.</p></body></html>"))
