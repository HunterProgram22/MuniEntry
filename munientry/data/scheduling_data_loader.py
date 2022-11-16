"""Module for extracting scheduling data and loading into the MuniEntry Database."""
from loguru import logger
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

from munientry.data.connections import open_db_connection, close_db_connection



def save_scheduling_data(case_data):
    logger.info(f' The case data is: {case_data}')
    conn = open_db_connection('con_munientry_db')
    query = QSqlQuery(conn)
    query.prepare(
       """
       INSERT INTO sched_final_pretrial (
       case_number,
       date,
       time
       )
       VALUES (?, ?, ?)
       """
    )
    query.addBindValue(case_data.get('case_number'))
    query.addBindValue(case_data.get('final_pretrial_date'))
    query.addBindValue(case_data.get('final_pretrial_time'))
    query.exec()
    close_db_connection(conn)

