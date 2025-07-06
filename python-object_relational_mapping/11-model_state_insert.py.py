#!/usr/bin/python3
"""
Adds a new State object, 'Louisiana', to the database hbtn_0e_6_usa
and prints its new id.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_state = State(name="Louisiana")
    session.add(new_state) # stages the object for insertion
    session.commit() # INSERT SQL query is actually executed
    print(new_state.id) # new_state object will have its id populated
    
    session.close()