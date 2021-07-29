# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/CommunityControlDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommunityControlDialog(object):
    def setupUi(self, CommunityControlDialog):
        CommunityControlDialog.setObjectName("CommunityControlDialog")
        CommunityControlDialog.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CommunityControlDialog.sizePolicy().hasHeightForWidth())
        CommunityControlDialog.setSizePolicy(sizePolicy)
        CommunityControlDialog.setMinimumSize(QtCore.QSize(1000, 800))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        CommunityControlDialog.setFont(font)
        self.continueButton = QtWidgets.QPushButton(CommunityControlDialog)
        self.continueButton.setGeometry(QtCore.QRect(800, 757, 191, 31))
        self.continueButton.setAutoDefault(False)
        self.continueButton.setObjectName("continueButton")
        self.case_information_frame = QtWidgets.QFrame(CommunityControlDialog)
        self.case_information_frame.setGeometry(QtCore.QRect(10, 10, 871, 121))
        self.case_information_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.case_information_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.case_information_frame.setLineWidth(2)
        self.case_information_frame.setObjectName("case_information_frame")
        self.defendant_attorney_name_label = QtWidgets.QLabel(self.case_information_frame)
        self.defendant_attorney_name_label.setGeometry(QtCore.QRect(11, 77, 841, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.defendant_attorney_name_label.setFont(font)
        self.defendant_attorney_name_label.setObjectName("defendant_attorney_name_label")
        self.case_number_label = QtWidgets.QLabel(self.case_information_frame)
        self.case_number_label.setGeometry(QtCore.QRect(11, 11, 841, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.case_number_label.setFont(font)
        self.case_number_label.setObjectName("case_number_label")
        self.defendant_name_label = QtWidgets.QLabel(self.case_information_frame)
        self.defendant_name_label.setGeometry(QtCore.QRect(11, 44, 841, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.defendant_name_label.setFont(font)
        self.defendant_name_label.setObjectName("defendant_name_label")
        self.createEntryButton = QtWidgets.QPushButton(CommunityControlDialog)
        self.createEntryButton.setGeometry(QtCore.QRect(600, 760, 191, 31))
        self.createEntryButton.setAutoDefault(False)
        self.createEntryButton.setObjectName("createEntryButton")
        self.frame = QtWidgets.QFrame(CommunityControlDialog)
        self.frame.setGeometry(QtCore.QRect(10, 130, 981, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 961, 227))
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
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.charges_gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.charges_gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.charges_gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.charges_gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.plea_label_1 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.plea_label_1.setFont(font)
        self.plea_label_1.setObjectName("plea_label_1")
        self.charges_gridLayout.addWidget(self.plea_label_1, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.charges_gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.widget = QtWidgets.QWidget(CommunityControlDialog)
        self.widget.setGeometry(QtCore.QRect(10, 390, 961, 288))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.community_control_required_checkbox = QtWidgets.QCheckBox(self.widget)
        self.community_control_required_checkbox.setObjectName("community_control_required_checkbox")
        self.gridLayout.addWidget(self.community_control_required_checkbox, 1, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 6, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)
        self.type_of_community_control_box = QtWidgets.QComboBox(self.widget)
        self.type_of_community_control_box.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.type_of_community_control_box.setFont(font)
        self.type_of_community_control_box.setObjectName("type_of_community_control_box")
        self.type_of_community_control_box.addItem("")
        self.type_of_community_control_box.addItem("")
        self.type_of_community_control_box.addItem("")
        self.gridLayout.addWidget(self.type_of_community_control_box, 4, 2, 1, 1)
        self.not_refuse_checkbox = QtWidgets.QCheckBox(self.widget)
        self.not_refuse_checkbox.setObjectName("not_refuse_checkbox")
        self.gridLayout.addWidget(self.not_refuse_checkbox, 8, 0, 1, 4)
        self.term_of_community_control_box = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.term_of_community_control_box.sizePolicy().hasHeightForWidth())
        self.term_of_community_control_box.setSizePolicy(sizePolicy)
        self.term_of_community_control_box.setEditable(True)
        self.term_of_community_control_box.setObjectName("term_of_community_control_box")
        self.term_of_community_control_box.addItem("")
        self.term_of_community_control_box.addItem("")
        self.term_of_community_control_box.setItemText(1, "")
        self.term_of_community_control_box.addItem("")
        self.term_of_community_control_box.addItem("")
        self.term_of_community_control_box.addItem("")
        self.gridLayout.addWidget(self.term_of_community_control_box, 3, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 5, 0, 1, 2)
        self.not_consume_checkbox = QtWidgets.QCheckBox(self.widget)
        self.not_consume_checkbox.setMaximumSize(QtCore.QSize(14, 16777215))
        self.not_consume_checkbox.setText("")
        self.not_consume_checkbox.setObjectName("not_consume_checkbox")
        self.gridLayout.addWidget(self.not_consume_checkbox, 7, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(CommunityControlDialog)
        self.createEntryButton.clicked.connect(CommunityControlDialog.create_entry)
        self.createEntryButton.pressed.connect(CommunityControlDialog.update_community_control)
        self.continueButton.pressed.connect(CommunityControlDialog.update_community_control)
        QtCore.QMetaObject.connectSlotsByName(CommunityControlDialog)
        CommunityControlDialog.setTabOrder(self.community_control_required_checkbox, self.term_of_community_control_box)
        CommunityControlDialog.setTabOrder(self.term_of_community_control_box, self.type_of_community_control_box)
        CommunityControlDialog.setTabOrder(self.type_of_community_control_box, self.checkBox_4)
        CommunityControlDialog.setTabOrder(self.checkBox_4, self.comboBox_2)
        CommunityControlDialog.setTabOrder(self.comboBox_2, self.checkBox_2)
        CommunityControlDialog.setTabOrder(self.checkBox_2, self.not_consume_checkbox)
        CommunityControlDialog.setTabOrder(self.not_consume_checkbox, self.not_refuse_checkbox)
        CommunityControlDialog.setTabOrder(self.not_refuse_checkbox, self.createEntryButton)
        CommunityControlDialog.setTabOrder(self.createEntryButton, self.continueButton)

    def retranslateUi(self, CommunityControlDialog):
        _translate = QtCore.QCoreApplication.translate
        CommunityControlDialog.setWindowTitle(_translate("CommunityControlDialog", "Community Control"))
        self.continueButton.setText(_translate("CommunityControlDialog", "Add Other Items"))
        self.defendant_attorney_name_label.setText(_translate("CommunityControlDialog", "TextLabel"))
        self.case_number_label.setText(_translate("CommunityControlDialog", "TextLabel"))
        self.defendant_name_label.setText(_translate("CommunityControlDialog", "TextLabel"))
        self.createEntryButton.setText(_translate("CommunityControlDialog", "Create Entry"))
        self.offense_label_1.setText(_translate("CommunityControlDialog", "Offense:"))
        self.label_9.setText(_translate("CommunityControlDialog", "Fines:"))
        self.label_11.setText(_translate("CommunityControlDialog", "Jail Days:"))
        self.label_13.setText(_translate("CommunityControlDialog", "Finding:"))
        self.label_10.setText(_translate("CommunityControlDialog", "Fines Suspended:"))
        self.plea_label_1.setText(_translate("CommunityControlDialog", "Plea:"))
        self.label_12.setText(_translate("CommunityControlDialog", "Jail Days Suspended:"))
        self.community_control_required_checkbox.setText(_translate("CommunityControlDialog", "Defendant is required to be under the supervision of the Office of Community Control"))
        self.label_2.setText(_translate("CommunityControlDialog", "Term of Community Control:"))
        self.checkBox_2.setText(_translate("CommunityControlDialog", "Pay $150 Diversion supervision fee within 90 Days"))
        self.label_4.setText(_translate("CommunityControlDialog", "Not possess/consume alcohol/drugs of abuse, associate with a person in possession/under influence, patronize establishment that serves alcohol for on-site consumption, and shall submit to alcohol or drug testing at request of probation or other law enforcement officer"))
        self.label_3.setText(_translate("CommunityControlDialog", "Type of Community Control:"))
        self.type_of_community_control_box.setItemText(0, _translate("CommunityControlDialog", "basic"))
        self.type_of_community_control_box.setItemText(1, _translate("CommunityControlDialog", "intensive"))
        self.type_of_community_control_box.setItemText(2, _translate("CommunityControlDialog", "monitored"))
        self.not_refuse_checkbox.setText(_translate("CommunityControlDialog", "Not refuse to consent to alcohol/drug testing at request of probation or other law enforcement officer"))
        self.term_of_community_control_box.setItemText(0, _translate("CommunityControlDialog", "1 Year"))
        self.term_of_community_control_box.setItemText(2, _translate("CommunityControlDialog", "6 Months"))
        self.term_of_community_control_box.setItemText(3, _translate("CommunityControlDialog", "18 Months"))
        self.term_of_community_control_box.setItemText(4, _translate("CommunityControlDialog", "2 Years"))
        self.checkBox_4.setText(_translate("CommunityControlDialog", "Complete the following program:"))
        self.comboBox_2.setItemText(0, _translate("CommunityControlDialog", "Driver Intervention Program"))
        self.comboBox_2.setItemText(1, _translate("CommunityControlDialog", "Anti-theft / Shoplifting Program"))
        self.comboBox_2.setItemText(2, _translate("CommunityControlDialog", "Alcohol / Drug Education Program"))
        self.comboBox_2.setItemText(3, _translate("CommunityControlDialog", "Domestic Violence Offender Program"))
        self.label.setText(_translate("CommunityControlDialog", "Community Control Terms"))
