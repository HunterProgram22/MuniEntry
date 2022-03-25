import pytest

import MuniEntry_app
import main_window

def open_daily_case_list_db_connection():
    return QSqlDatabase.database("con_daily_case_lists", open=True)


daily_case_list_database = open_daily_case_list_db_connection()


def enter_data(field, data: str):
    return QtBot.keyClicks(field, data)

def mouse_click(button):
    return QtBot.mouseClick(button, QtCore.Qt.LeftButton)


@pytest.fixture
def app(qtbot):
    app = main_window.Window(daily_case_list_database)
    qtbot.addWidget(app)
    mouse_click(app.bunner_radioButton)
    mouse_click(app.arraignments_radioButton)
    enter_data(app.arraignment_cases_box, 'ROWEDDA - 21TRD09200')
    return app


def test_window_opens(qtbot):
    pass