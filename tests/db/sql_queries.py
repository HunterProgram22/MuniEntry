from PyQt5.QtSql import QSqlQuery


def sql_query_offense_type(key):
    charges_database = open_db_connection("con_charges")
    # charges_database = open_charges_db_connection()
    query = QSqlQuery(charges_database)
    query.prepare("SELECT * FROM charges WHERE statute LIKE '%' || :key || '%'")
    query.bindValue(":key", key)
    query.exec()
    while query.next():
        statute = query.value(2)
        offense_type = query.value(4)
        if statute == key:
            query.finish()
            charges_database.close()
            return offense_type