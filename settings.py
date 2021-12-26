"""A module containing common variables used throughout the application."""

import pathlib
from loguru import logger

from PyQt5.QtSql import QSqlDatabase

PATH = str(pathlib.Path().absolute())

TEMPLATE_PATH = PATH + "\\resources\\templates\\"
SAVE_PATH = PATH + "\\resources\\saved\\"
DB_PATH = PATH + "\\resources\\db\\"
CHARGES_DATABASE = DB_PATH + "\\charges.sqlite"
CASES_DATABASE = DB_PATH + "\\arraignments.sqlite"

PAY_DATE_DICT = {
    "forthwith": 0,
    "within 30 days": 30,
    "within 60 days": 60,
    "within 90 days": 90,
}

LEAP_COMPLETE_DATE_DICT = {
    "forthwith": 0,
    "120 days": 120,
}


@logger.catch
def create_arraignments_database_connection():
    """Opens a connection to the database and returns that connection to the arraignments_database."""
    # try:
    arraignments_database_connection = QSqlDatabase.addDatabase("QSQLITE", "cases")
    arraignments_database_connection.setDatabaseName(CASES_DATABASE)
    # except PermissionError:
    #     arraignments_database_connection = QSqlDatabase.addDatabase("QSQLITE", "cases_second")
    #     arraignments_database_connection.setDatabaseName(CASES_DATABASE)
    return arraignments_database_connection

# -*- mode: python ; coding: utf-8 -*-
# SPEC File Settings
#
# block_cipher = None
#
# #
# a = Analysis(['MuniEntry_app.py'],
#              pathex=[],
#              binaries=[],
#              datas=[('./resources/db/arraignments.sqlite', './resources/db'),
#                     ('./resources/db/charges.sqlite', './resources/db'),
#                     ('./resources/db/Arraignments.xlsx', './resources/db'),
#                     ('./resources/db/Charges.xlsx', './resources/db'),
#                     ('./resources/Templates/Not_Guilty_Bond_Template.docx', './resources/Templates'),
#                     ('./resources/Templates/No_Jail_Plea_Final_Judgment_Template.docx', './resources/Templates'),
#                     ('./resources/Templates/Leap_Plea_Admission_Template.docx', './resources/Templates'),
#                     ('./resources/Templates/Leap_Plea_Precourt_Completion_Template.docx', './resources/Templates'),
#                     ('./resources/Saved/holder.txt', './resources/Saved'),
#                     ],
#              hiddenimports=['lxml._elementpath'],
#              hookspath=[],
#              hooksconfig={},
#              runtime_hooks=[],
#              excludes=[],
#              win_no_prefer_redirects=False,
#              win_private_assemblies=False,
#              cipher=block_cipher,
#              noarchive=False)
# pyz = PYZ(a.pure, a.zipped_data,
#              cipher=block_cipher)
#
# exe = EXE(pyz,
#           a.scripts,
#           [],
#           exclude_binaries=True,
#           name='MuniEntry_app',
#           debug=False,
#           bootloader_ignore_signals=False,
#           strip=False,
#           upx=True,
#           console=True,
#           disable_windowed_traceback=False,
#           target_arch=None,
#           codesign_identity=None,
#           entitlements_file=None )
# coll = COLLECT(exe,
#                a.binaries,
#                a.zipfiles,
#                a.datas,
#                strip=False,
#                upx=True,
#                upx_exclude=[],
#                name='MuniEntry_app')
#
