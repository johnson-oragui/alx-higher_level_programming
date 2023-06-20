#!/usr/bin/python3
"""Module that defines the State model representing\
        a state for a MySQL database using SQLAlchemy."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

# Create the base class for the declarative models
Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state's name.
        cities (sqlalchemy.orm.relationship): The State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # Define the relationship between State and City models
    cities = relationship("City", backref="state", cascade="all, delete")
