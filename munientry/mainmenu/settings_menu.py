"""Module containing functions and classes related to settings in the main menu.

This module provides functionality to open and manage settings for various features in the
application. It includes the base class `BaseSettingDialog` which provides a common structure for
dialogs that modify settings, and a specific subclass `WorkflowSettingDialog` which is used for
changing the workflow status of the application.

Functions:
    open_dialog: Utility function that creates an instance of a specified dialog class and opens it.
    open_workflow_settings: Function that opens the `WorkflowSettingDialog` for changing the
        workflow status.

Classes:
    BaseSettingDialog: Base class for dialogs that modify settings.
    WorkflowSettingDialog: Subclass of `BaseSettingDialog` that provides a specific implementation
        for changing the workflow status.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Type

from loguru import logger
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QGroupBox,
    QRadioButton,
    QVBoxLayout,
)

from munientry.settings.paths import GAVEL_PATH

if TYPE_CHECKING:
    from munientry.mainwindow import MainWindow


def open_dialog(dialog_class: Type[QDialog], mainwindow: MainWindow) -> None:
    """Creates instance of the specified dialog class and opens it."""
    dialog = dialog_class(mainwindow)
    dialog.exec()


def open_workflow_settings(mainwindow: MainWindow) -> None:
    """Creates instance of SettingDialog class and opens it."""
    open_dialog(WorkflowSettingDialog, mainwindow)


class BaseSettingDialog(QDialog):
    """Base class for obtaining user input to change settings."""

    def __init__(self, mainwindow: MainWindow, parent=None) -> None:
        super().__init__(parent)
        self.mainwindow = mainwindow
        self.setWindowIcon(QIcon(GAVEL_PATH))
        self.create_button_box()
        self.create_layout()

    def create_button_box(self) -> None:
        button_group = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.button_box = QDialogButtonBox(button_group)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def create_layout(self) -> None:
        layout = QVBoxLayout()
        self.setLayout(layout)


class WorkflowSettingDialog(BaseSettingDialog):
    """Subclass for obtaining user input to change workflow settings."""

    def __init__(self, mainwindow: MainWindow, parent=None) -> None:
        super().__init__(mainwindow, parent)
        self.setWindowTitle('Workflow Settings')
        self.create_settings_box()

    def create_settings_box(self) -> None:
        self.workflow_on_radio_button = QRadioButton('Workflow On')
        self.workflow_off_radio_button = QRadioButton('Workflow Off')
        self.workflow_on_radio_button.toggled.connect(self.set_workflow)

        if self.mainwindow.digital_workflow.workflow_status == 'ON':
            self.workflow_on_radio_button.setChecked(True)
        else:
            self.workflow_off_radio_button.setChecked(True)

        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.workflow_on_radio_button)
        radio_layout.addWidget(self.workflow_off_radio_button)

        self.group_box = QGroupBox('Workflow Setting')
        self.group_box.setLayout(radio_layout)

        layout = self.layout()
        layout.addWidget(self.group_box)
        layout.addWidget(self.button_box)

    def set_workflow(self) -> None:
        if self.workflow_on_radio_button.isChecked():
            status = 'ON'
        else:
            status = 'OFF'
        self.mainwindow.digital_workflow.workflow_status = status
        logger.info(f'Workflow status set to {status}.')
