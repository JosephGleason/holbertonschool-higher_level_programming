#!/usr/bin/python3
"""
Lists all states in database hbtn_0e_0_usa,
it should take 3 arguments
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Assigning arguments to the requested variable names
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]

    # Connects to SQL on localhost
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database
    )

    # Creates a cursor to get SQL queries
    cur = db.cursor()

    # Executes SQL query that gets states
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Prints list of states
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
