import os

from loguru import logger

from munientry.digitalworkflow.workflow_tools import PdfViewer
from munientry.settings import DW_HEMMETER, DW_ROHRER, DW_BUNNER


class DigitalWorkflow(object):

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.load_digital_workflow_counts()

    def load_digital_workflow_counts(self):
        hemmeter_file_count = self.get_file_count(DW_HEMMETER)
        rohrer_file_count = self.get_file_count(DW_ROHRER)
        bunner_file_count = self.get_file_count(DW_BUNNER)
        self.mainwindow.jour_count_jh_label.setText(str(hemmeter_file_count))
        self.mainwindow.jour_count_jr_label.setText(str(rohrer_file_count))
        self.mainwindow.jour_count_mb_label.setText(str(bunner_file_count))

    def get_file_count(self, directory):
        try:
            return len(os.listdir(directory))
        except FileNotFoundError as error:
            logger.warning(error)

    def open(self, entry):
        self.mainwindow.webview = self.create_pdf_view(entry)

    def create_pdf_view(self, entry):
        webview = PdfViewer(entry)
        return webview


