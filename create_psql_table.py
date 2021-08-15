import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("charges.sqlite")

if not con.open():
    print("Unable to connect to database")
    sys.exit(1)

# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE charges (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        offense VARCHAR(60) NOT NULL,
        statute VARCHAR(50) NOT NULL,
        degree VARCHAR(5) NOT NULL
    )
    """
    )

print(con.tables())

insertDataQuery = QSqlQuery()
insertDataQuery.prepare(
    """
    INSERT INTO charges (
        offense,
        statute,
        degree
    )
    VALUES (?, ?, ?)
    """
)

# Sample data
data = [
    ("Speeding - School Zone", "R.C. 4511.21(B)(1)", "MM"),
    ("Speeding > 25 mph", "R.C. 4511.21(B)(2)", "MM"),
    ("Speeding > 35 mph", "R.C. 4511.21(B)(3)", "MM"),
    ("Driving in Marked Lanes", "R.C. 4511.33", "MM"),
    ("Driving Under Suspension", "R.C. 4510.11", "M1"),
]

# Use .addBindValue() to insert data
for offense, statute, degree in data:
    insertDataQuery.addBindValue(offense)
    insertDataQuery.addBindValue(statute)
    insertDataQuery.addBindValue(degree)
    insertDataQuery.exec()
