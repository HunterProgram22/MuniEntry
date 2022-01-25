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
    for i in offense_list:
        clean_offense_list.append(i[0])
    clean_offense_list.sort()
    conn.close()
    return clean_offense_list

def create_statute_list():
    conn = sqlite3.connect(DB_PATH + "charges.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT offense, statute FROM charges")
    statute_list = cursor.fetchall()
    clean_statute_list = []
    for i in statute_list:
        clean_statute_list.append(i[1])
    clean_statute_list.sort()
    conn.close()
    return clean_statute_list

def create_arraignment_cases_list():
    conn = sqlite3.connect(DB_PATH + "arraignments.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT defendant_last_name, defendant_first_name, case_number FROM cases")
    cases_list = cursor.fetchall()
    clean_cases_list = []
    for i in cases_list:
        name = i[0] + " - " + i[2]
        clean_cases_list.append(name)
    clean_cases_list.sort()
    conn.close()
    clean_cases_list.insert(0, None)
    return clean_cases_list

def create_slated_cases_list():
    conn = sqlite3.connect(DB_PATH + "slated.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT defendant_last_name, defendant_first_name, case_number FROM cases")
    cases_list = cursor.fetchall()
    clean_cases_list = []
    for i in cases_list:
        name = i[0] + " - " + i[2]
        clean_cases_list.append(name)
    clean_cases_list.sort()
    conn.close()
    clean_cases_list.insert(0, None)
    return clean_cases_list

def create_final_pretrial_cases_list():
    conn = sqlite3.connect(DB_PATH + "final_pretrials.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT defendant_last_name, defendant_first_name, case_number FROM cases")
    cases_list = cursor.fetchall()
    clean_cases_list = []
    for i in cases_list:
        name = i[0] + " - " + i[2]
        clean_cases_list.append(name)
    clean_cases_list.sort()
    conn.close()
    clean_cases_list.insert(0, None)
    return clean_cases_list

