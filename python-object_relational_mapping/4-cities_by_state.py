#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa,
displaying (city_id, city_name, state_name), sorted by city id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Assigning arguments to the requested variable names
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Creates a cursor to get SQL queries
    cur = db.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Prints list of states
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
