"""Test module for General Notice of Hearing Dialog UI Functionality."""
import pytest
from PyQt6.QtCore import QDate
from tests.conftest import enter_data, mouse_click

HEMMETER_NOTICE = 'General Notice Of Hearing Entry Case Information - Judge Marianne T. Hemmeter'
ROHRER_NOTICE = 'General Notice Of Hearing Entry Case Information - Judge Kyle E. Rohrer'



def test_hemmeter_dialog_opens(hemmeter_gen_hearing_notice_dialog):
    assert hemmeter_gen_hearing_notice_dialog.windowTitle() == HEMMETER_NOTICE


def test_rohrer_dialog_opens(rohrer_gen_hearing_notice_dialog):
    assert rohrer_gen_hearing_notice_dialog.windowTitle() == ROHRER_NOTICE


def test_continuance_calculator(hemmeter_gen_hearing_notice_dialog):
    date = QDate(2024, 1, 1)
    date_new = QDate(2023, 12, 1)
    hemmeter_gen_hearing_notice_dialog.old_speedy_trial_dateEdit.setDate(date)
    hemmeter_gen_hearing_notice_dialog.old_hearing_dateEdit.setDate(date_new)
    hemmeter_gen_hearing_notice_dialog.new_hearing_dateEdit.setDate(date)
    assert hemmeter_gen_hearing_notice_dialog.old_hearing_dateEdit.date().toString('MMMM dd, yyyy') == 'December 01, 2023'
    assert hemmeter_gen_hearing_notice_dialog.speedy_trial_date_label.text() == 'February 01, 2024'