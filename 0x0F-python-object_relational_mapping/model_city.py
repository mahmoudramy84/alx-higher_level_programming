#!/usr/bin/python3
"""contains the class definition of a City."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)