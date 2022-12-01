# Form implementation generated from reading ui file 'munientry/views/ui/ComControlWorkflowDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ComControlWorkflowDialog(object):
    def setupUi(self, ComControlWorkflowDialog):
        ComControlWorkflowDialog.setObjectName("ComControlWorkflowDialog")
        ComControlWorkflowDialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        ComControlWorkflowDialog.resize(1006, 828)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ComControlWorkflowDialog.sizePolicy().hasHeightForWidth())
        ComControlWorkflowDialog.setSizePolicy(sizePolicy)
        ComControlWorkflowDialog.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        ComControlWorkflowDialog.setFont(font)
        ComControlWorkflowDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";")
        self.gridLayout = QtWidgets.QGridLayout(ComControlWorkflowDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(ComControlWorkflowDialog)
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
        self.load_new_entries_Button = QtWidgets.QPushButton(self.frame_3)
        self.load_new_entries_Button.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"font-weight: bold;")
        self.load_new_entries_Button.setObjectName("load_new_entries_Button")
        self.gridLayout_2.addWidget(self.load_new_entries_Button, 8, 0, 1, 1)
        self.open_entry_Button = QtWidgets.QPushButton(self.frame_3)
        self.open_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.open_entry_Button.setObjectName("open_entry_Button")
        self.gridLayout_2.addWidget(self.open_entry_Button, 8, 1, 1, 1)
        self.close_dialog_Button = QtWidgets.QPushButton(self.frame_3)
        self.close_dialog_Button.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"font-weight: bold;")
        self.close_dialog_Button.setObjectName("close_dialog_Button")
        self.gridLayout_2.addWidget(self.close_dialog_Button, 9, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 7, 0, 1, 2)
        self.delete_entry_Button = QtWidgets.QPushButton(self.frame_3)
        self.delete_entry_Button.setStyleSheet("background-color: rgb(255, 96, 82);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.delete_entry_Button.setObjectName("delete_entry_Button")
        self.gridLayout_2.addWidget(self.delete_entry_Button, 9, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.entries_listWidget = QtWidgets.QListWidget(self.frame_3)
        self.entries_listWidget.setObjectName("entries_listWidget")
        self.gridLayout_2.addWidget(self.entries_listWidget, 2, 0, 4, 2)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 2)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 4)
        self.gridLayout_2.setRowStretch(3, 4)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 2)
        self.gridLayout.setRowStretch(0, 4)

        self.retranslateUi(ComControlWorkflowDialog)
        QtCore.QMetaObject.connectSlotsByName(ComControlWorkflowDialog)

    def retranslateUi(self, ComControlWorkflowDialog):
        _translate = QtCore.QCoreApplication.translate
        ComControlWorkflowDialog.setWindowTitle(_translate("ComControlWorkflowDialog", "Community Control Workflow"))
        self.load_new_entries_Button.setText(_translate("ComControlWorkflowDialog", "Check For New Entries"))
        self.open_entry_Button.setText(_translate("ComControlWorkflowDialog", "Open Selected Entry for Review"))
        self.close_dialog_Button.setText(_translate("ComControlWorkflowDialog", "Close Workflow"))
        self.delete_entry_Button.setText(_translate("ComControlWorkflowDialog", "Delete Entry from Workflow"))
        self.label_2.setText(_translate("ComControlWorkflowDialog", "COMMUNITY CONTROL ENTRIES"))
        self.textBrowser.setHtml(_translate("ComControlWorkflowDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Palatino Linotype\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The list below contains draft versions of any entry that imposes a term of community control.</p></body></html>"))
