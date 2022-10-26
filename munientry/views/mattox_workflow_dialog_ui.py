# Form implementation generated from reading ui file 'munientry/views/ui/MattoxWorkflowDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MattoxWorkflowDialog(object):
    def setupUi(self, MattoxWorkflowDialog):
        MattoxWorkflowDialog.setObjectName("MattoxWorkflowDialog")
        MattoxWorkflowDialog.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        MattoxWorkflowDialog.resize(1006, 828)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MattoxWorkflowDialog.sizePolicy().hasHeightForWidth())
        MattoxWorkflowDialog.setSizePolicy(sizePolicy)
        MattoxWorkflowDialog.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        MattoxWorkflowDialog.setFont(font)
        MattoxWorkflowDialog.setStyleSheet("background-color: rgb(25, 49, 91);\n"
"font: 75 11pt \"Palatino Linotype\";")
        self.gridLayout = QtWidgets.QGridLayout(MattoxWorkflowDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(MattoxWorkflowDialog)
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
        self.community_control_entries_listWidget = QtWidgets.QListWidget(self.frame_3)
        self.community_control_entries_listWidget.setObjectName("community_control_entries_listWidget")
        self.gridLayout_2.addWidget(self.community_control_entries_listWidget, 4, 0, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.frame_3)
        self.cancel_Button.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"font-weight: bold;")
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout_2.addWidget(self.cancel_Button, 8, 0, 1, 1)
        self.scram_gps_entries_listWidget = QtWidgets.QListWidget(self.frame_3)
        self.scram_gps_entries_listWidget.setObjectName("scram_gps_entries_listWidget")
        self.gridLayout_2.addWidget(self.scram_gps_entries_listWidget, 4, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 6, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
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
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.load_new_entries_Button = QtWidgets.QPushButton(self.frame_3)
        self.load_new_entries_Button.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"font-weight: bold;")
        self.load_new_entries_Button.setObjectName("load_new_entries_Button")
        self.gridLayout_2.addWidget(self.load_new_entries_Button, 7, 0, 1, 1)
        self.open_entry_Button = QtWidgets.QPushButton(self.frame_3)
        self.open_entry_Button.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.open_entry_Button.setObjectName("open_entry_Button")
        self.gridLayout_2.addWidget(self.open_entry_Button, 7, 1, 1, 1)
        self.delete_entry_Button = QtWidgets.QPushButton(self.frame_3)
        self.delete_entry_Button.setStyleSheet("background-color: rgb(255, 96, 82);\n"
"font: 75 11pt \"Palatino Linotype\";\n"
"font-weight: bold;")
        self.delete_entry_Button.setObjectName("delete_entry_Button")
        self.gridLayout_2.addWidget(self.delete_entry_Button, 8, 1, 1, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 2)
        self.gridLayout.setRowStretch(0, 4)

        self.retranslateUi(MattoxWorkflowDialog)
        QtCore.QMetaObject.connectSlotsByName(MattoxWorkflowDialog)

    def retranslateUi(self, MattoxWorkflowDialog):
        _translate = QtCore.QCoreApplication.translate
        MattoxWorkflowDialog.setWindowTitle(_translate("MattoxWorkflowDialog", "Mattox Workflow"))
        self.cancel_Button.setText(_translate("MattoxWorkflowDialog", "Cancel"))
        self.label.setText(_translate("MattoxWorkflowDialog", "<html><head/><body><p><span style=\" text-decoration: underline;\">SCRAM AND GPS BOND ENTRIES</span></p></body></html>"))
        self.label_2.setText(_translate("MattoxWorkflowDialog", "COMMUNITY CONTROL ENTRIES"))
        self.load_new_entries_Button.setText(_translate("MattoxWorkflowDialog", "Check For New Entries"))
        self.open_entry_Button.setText(_translate("MattoxWorkflowDialog", "Open Selected Entry for Review"))
        self.delete_entry_Button.setText(_translate("MattoxWorkflowDialog", "Delete Entry from Workflow"))
