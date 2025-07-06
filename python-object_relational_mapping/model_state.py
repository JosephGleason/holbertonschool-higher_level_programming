#!/usr/bin/python3
"""
Defines the State class for SQLAlchemy ORM.
"""
from sqlalchemy import Column, Integer, String #orm library
from sqlalchemy.ext.declarative import declarative_base

#for declarative models
Base = declarative_base()

class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to link to.
        id (sqlalchemy.Column): The state's id.
        name (sqlalchemy.Column): The state's name.
    """
    __tablename__ = 'states' # Link to the MySQL table named 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
