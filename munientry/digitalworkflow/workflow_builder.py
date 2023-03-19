import os

from loguru import logger

from munientry.settings.paths import DW_ADMIN_JUDGE, DW_ROHRER, DW_BUNNER


class DigitalWorkflow(object):

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.workflow_status = 'ON'
        self.load_digital_workflow_counts()

    def load_digital_workflow_counts(self):
        admin_count = self.get_file_count(os.path.join(DW_ADMIN_JUDGE, 'Admin'))
        md_adopt_count = self.get_file_count(os.path.join(DW_ADMIN_JUDGE, 'MDAdopt'))
        rohrer_file_count = self.get_file_count(DW_ROHRER)
        bunner_file_count = self.get_file_count(DW_BUNNER)
        self.mainwindow.admin_count_label.setText(str(admin_count))
        self.mainwindow.md_adopt_label.setText(str(md_adopt_count))
        self.mainwindow.jour_count_jr_label.setText(str(rohrer_file_count))
        self.mainwindow.jour_count_mb_label.setText(str(bunner_file_count))

    def get_file_count(self, directory):
        try:
            return len(os.listdir(directory))
        except FileNotFoundError as error:
            logger.warning(error)
