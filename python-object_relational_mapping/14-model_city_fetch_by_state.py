#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    # 1) Read MySQL credentials and database
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # 2) Create engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}"
        f"@localhost/{db_name}",
        pool_pre_ping=True
    )

    # 3) Bind a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 4) Query City.id, City.name, State.name with a JOIN
    query = (
            session.query(City, State)
            .join(State, City.state_id == State.id)
            .order_by(City.id)
        )

    # 5) Print each in "<state>: (<city_id>) <city>"
    for city, state in query:
        print(f"{state.name}: ({city.id}) {city.name}")

    # 6) Close session
    session.close()
