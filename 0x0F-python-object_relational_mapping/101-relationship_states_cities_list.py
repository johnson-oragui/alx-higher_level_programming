#!/usr/bin/env python3
"""Script to list State and City objects from the hbtn_0e_101_usa database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py\
                <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Get MySQL username, password, and
    # database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create SQLAlchemy engine and session
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all State objects and their associated City objects
    states = session.query(State).order_by(State.id).all()

    # Display the State and City objects
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # Close the session
    session.close()
