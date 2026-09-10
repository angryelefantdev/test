import sqlite3

connection = sqlite3.connect("tester.db")
cursor = connection.cursor()

command1 = """
CREATE TABLE IF NOT EXISTS tester(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INT
)
"""

cursor.execute(command1)

command2 = """
INSERT INTO tester (name, age)
VALUES ('roland',28),('angelica',30),('argalia',35)
"""

cursor.execute(command2)

connection.commit()

cursor.execute("SELECT * FROM tester")

rows = cursor.fetchall()

for row in rows:
    print(row)