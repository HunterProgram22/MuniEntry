import pathlib
import sqlite3


PATH = str(pathlib.Path().absolute())
DB_PATH = PATH + "\\resources\\db\\"


def create_offense_list():
    conn = sqlite3.connect(DB_PATH + "charges.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT offense, statute FROM charges")
    offense_list = cursor.fetchall()
    clean_offense_list = []
    clean_statute_list = []
    for i in offense_list:
        clean_offense_list.append(i[0])
        clean_statute_list.append(i[1])
    conn.close()
    return clean_offense_list, clean_statute_list
