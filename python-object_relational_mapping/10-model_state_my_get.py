#!/usr/bin/python3
"""
Prints the id of the State object with the given name from
the database hbtn_0e_6_usa. If not found, prints Not found.
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    # Read credentials and target state name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name  = sys.argv[3]
    state    = sys.argv[4]

    # Create the engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query by state name
    get_state = session.query(State).filter(State.name == state).first()

    # Print the result or Not found
    if get_state:
        print(f"{get_state.id}")
    else:
        print("Not found")

    session.close()
