#!/usr/bin/python3
"""
Defines the City class for SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base  # Import the declarative Base from model_state


class City(Base):
    """
    Represents a city for a MySQL database.

    Attributes:
        id (sqlalchemy.Column): auto-incrementing primary key
        state_id (sqlalchemy.Column): integer FK to states.id
        name (sqlalchemy.Column): string name of the city
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
