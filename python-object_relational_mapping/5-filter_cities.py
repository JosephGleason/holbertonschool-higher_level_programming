#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Assigning arguments to the requested variable names
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Creates a cursor to get SQL queries
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state,)
    )

    # Prints list of states
    rows = cur.fetchall()
    city_names = []
    for row in rows:
        city_name = row[0]
        city_names.append(city_name)
    print(", ".join(city_names))

    cur.close()
    db.close()
