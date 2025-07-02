#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    # --- Database Connection ---
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    
    # Create a cursor object/ used to run sql cmnds
    cur = db.cursor()
       
    # --- Execute the SQL query ---
    # The SQL query to select all states, sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # --- Fetch all the results ---
    # results will be a list of tuples, e.g., [(1, 'California'), (2, 'Arizona'), ...]
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    cur.close()
    db.close()