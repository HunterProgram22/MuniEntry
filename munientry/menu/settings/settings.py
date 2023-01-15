from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QGroupBox, QRadioButton, QVBoxLayout
from loguru import logger
from munientry.appsettings.paths import ICON_PATH


def open_workflow_settings(mainwindow, _signal=None) -> None:
    settings_menu = SettingDialog(mainwindow)
    settings_menu.exec()


class SettingDialog(QDialog):
    def __init__(self, mainwindow, parent=None):
        super().__init__(parent)
        self.mainwindow = mainwindow
        self.setWindowIcon(QIcon(f'{ICON_PATH}gavel.ico'))
        self.setWindowTitle('Workflow Settings')
        button_group = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        group_box = QGroupBox('Workflow Setting')

        self.workflow_on_radioButton = QRadioButton('Workflow On')
        self.workflow_off_radioButton = QRadioButton('Workflow Off')

        self.workflow_on_radioButton.toggled.connect(self.set_workflow)
        self.workflow_off_radioButton.toggled.connect(self.set_workflow)
        if self.mainwindow.digital_workflow.workflow_status == 'ON':
            self.workflow_on_radioButton.setChecked(True)
        else:
            self.workflow_off_radioButton.setChecked(True)

        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.workflow_on_radioButton)
        radio_layout.addWidget(self.workflow_off_radioButton)

        group_box.setLayout(radio_layout)

        button_box = QDialogButtonBox(button_group)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(group_box)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def set_workflow(self):
        if self.sender().isChecked():
            if self.sender().text() == 'Workflow On':
                self.mainwindow.digital_workflow.workflow_status = 'ON'
                logger.info(self.mainwindow.digital_workflow.workflow_status)
            else:
                self.mainwindow.digital_workflow.workflow_status = 'OFF'
                logger.info(self.mainwindow.digital_workflow.workflow_status)
