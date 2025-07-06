#!/usr/bin/python3
"""
Lists all state objects from db hbtn6usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
# creates a class that you can then use to create session objects
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
            pool_pre_ping=True
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    print(f"{first_state.id}: {first_state.name}")

    session.close()
