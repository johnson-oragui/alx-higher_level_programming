#!/usr/bin/python3
"""Module that lists all State objects, and corresponding City objects,\
        contained in the mySQL database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create a database engine using the provided arguments
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Retrieve all states from the database and order them by ID
    for state in session.query(State).order_by(State.id):
        # Print state ID and name
        print("{}: {}".format(state.id, state.name))

        # Iterate over the cities associated with the current state
        for city in state.cities:
            # Print city ID and name
            print("    {}: {}".format(city.id, city.name))
