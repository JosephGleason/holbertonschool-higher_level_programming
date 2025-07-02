#!/usr/bin/python3
"""
Lists all states in database hbtn_0e_0_usa,
it should take 3 arguments
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Ensure correct number of command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <mysql_database>", file=sys.stderr)
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = None # Initialize db to None for finally block
    cur = None # Initialize cur to None for finally block

    try:
        # Connects to SQL on localhost
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Creates a cursor to get SQL queries
        cur = db.cursor()

        # Executes SQL querie that gets states
        cur.execute("SELECT id, name FROM states ORDER BY id ASC") 

        # Prints list of states
        for row in cur.fetchall():
            print(row)

    except MySQLdb.OperationalError as e:
        # This will catch connection errors and print them
        print(f"MySQL Error: {e}", file=sys.stderr) # Print to stderr for errors
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        # Ensure cursor and database connections are closed
        if cur:
            cur.close()
        if db:
            db.close()