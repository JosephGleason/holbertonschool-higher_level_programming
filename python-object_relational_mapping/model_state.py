#!/usr/bin/python3
"""
Defines the State class for SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String  # ORM column and data types
from sqlalchemy.ext.declarative import declarative_base  # Declarative base


Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to link to.
        id (sqlalchemy.Column): The state's id.
        name (sqlalchemy.Column): The state's name.
    """
    __tablename__ = 'states'  # Name of the MySQL table

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
