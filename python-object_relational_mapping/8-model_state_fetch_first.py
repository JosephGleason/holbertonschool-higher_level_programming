#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
If the table is empty, prints Nothing.
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State


if __name__ == "__main__":
    # Read MySQL credentials and database name
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name    = sys.argv[3]

    # Create the engine (default port 3306)
    engine = create_engine(
        f"mysql+mysqldb://{mysql_user}:{mysql_pass}"
        f"@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Open a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first state by id
    first_state = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if no rows
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()
