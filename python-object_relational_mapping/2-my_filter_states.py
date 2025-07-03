#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
whose name matches the provided argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Assigning arguments to the requested variable names
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
        ).format(state_name)
    # Executes SQL query that gets states
    cur.execute(query)

    # Prints list of states
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
