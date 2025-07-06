#!/usr/bin/python3
"""
Lists all State objects from the database that contain'a' in their name.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)

    # Session instance
    session = Session()

    states_with_a = session.query(
        State).filter(
        State.name.like('%a%')).order_by(
        State.id).all()

    for state in states_with_a:
        print(f"{state.id}: {state.name}")

        session.close()
