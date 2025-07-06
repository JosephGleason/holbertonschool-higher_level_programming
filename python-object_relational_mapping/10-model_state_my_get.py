#!/usr/bin/python3
"""
Prints the State object with the id passed as an argument
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    # Create the engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    get_state = session.query(State).filter(State.id == int(state)).first()

    if get_state:
        print(f"{get_state.id}")
    else:
        print("Not found")

    session.close()
