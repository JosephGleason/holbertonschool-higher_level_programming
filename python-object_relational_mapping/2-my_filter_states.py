#!/usr/bin/python3
"""
Display all values in the states table where name matches the given argument.
Usage: ./2-my_filter_states.py <mysql username>
<mysql password> <database name> <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=mysql_user,
            passwd=mysql_passwd,
            db=mysql_db,
            port=3306
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute SQL query to filter states
        # matching the argument
        query = """SELECT * FROM states
            WHERE  BINARY name = '{}' ORDER BY id ASC;""".format(
            state_name
        )
        cursor.execute(query)

        # Fetch all results and print them
        for row in cursor.fetchall():
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")