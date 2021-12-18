import pytest
import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from settings import create_arraignments_database_connection

arraignments_database = create_arraignments_database_connection()

@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app

"""Functions for Testing"""
def start_NoJailPleaDialog(qtbot, judicial_officer, case):
    dialog = NoJailPleaDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

def start_LeapPleaLongDialog(qtbot, judicial_officer, case):
    dialog = LeapPleaLongDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

def start_LeapPleaShortDialog(qtbot, judicial_officer, case):
    dialog = LeapPleaShortDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

def start_FTABondDialog(qtbot, judicial_officer, case):
    dialog = FTABondDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

def start_NotGuiltyBondDialog(qtbot, judicial_officer, case):
    dialog = NotGuiltyBondDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    return dialog

