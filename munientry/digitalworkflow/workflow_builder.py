import os

from loguru import logger

from munientry.settings import DW_HEMMETER, DW_ROHRER, DW_BUNNER, DW_MATTOX


class DigitalWorkflow(object):

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.workflow_status = 'ON'
        self.load_digital_workflow_counts()

    def load_digital_workflow_counts(self):
        hemmeter_file_count = self.get_file_count(DW_HEMMETER)
        rohrer_file_count = self.get_file_count(DW_ROHRER)
        bunner_file_count = self.get_file_count(DW_BUNNER)
        # scram_gps_file_count = self.get_file_count(f'{DW_MATTOX}/Scram_GPS//')
        # comm_control_file_count = self.get_file_count(f'{DW_MATTOX}/Comm_Control//')
        self.mainwindow.jour_count_jh_label.setText(str(hemmeter_file_count))
        self.mainwindow.jour_count_jr_label.setText(str(rohrer_file_count))
        self.mainwindow.jour_count_mb_label.setText(str(bunner_file_count))
        # self.mainwindow.count_scram_gps_label.setText(str(scram_gps_file_count))
        # self.mainwindow.count_comm_control_label.setText(str(comm_control_file_count))

    def get_file_count(self, directory):
        try:
            return len(os.listdir(directory))
        except FileNotFoundError as error:
            logger.warning(error)
