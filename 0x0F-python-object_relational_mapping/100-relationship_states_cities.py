#!/usr/bin/python3
"""Module that adds a city and its associated state\
        to a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create the database tables based on the defined models
    Base.metadata.create_all(engine)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Create a new city and its associated state
    state = State(name="California")
    city = City(name="San Francisco", state=state)

    # Add the new city and associated state to the session
    session.add(state)
    session.add(city)

    # Commit the session to persist the changes in the database
    session.commit()
