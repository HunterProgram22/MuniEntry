"""Module for extracting scheduling data and loading into the MuniEntry Database."""
from datetime import datetime

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
    date_string = case_data.get('final_pretrial_date')
    date_object = datetime.strptime(date_string, '%B %d, %Y')
    logger.info(date_object)
    new_date_format = date_object.strftime('%Y-%m-%d')
    logger.info(new_date_format)
    new_date_object = datetime.strptime(new_date_format, '%Y-%m-%d').date()
    logger.info(new_date_object)
    new_date_object = str(new_date_object)
    query.addBindValue(new_date_object)
    query.addBindValue(case_data.get('final_pretrial_time'))
    query.exec()
    close_db_connection(conn)

