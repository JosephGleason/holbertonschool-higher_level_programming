#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Assigning arguments to the requested variable names
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connects to SQL on localhost
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Creates a cursor to get SQL queries
    cur = db.cursor()

    # Executes SQL query that gets states
    cur.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )

    # Prints list of states
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
