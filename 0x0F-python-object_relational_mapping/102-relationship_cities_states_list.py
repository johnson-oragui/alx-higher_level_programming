#!/usr/bin/python3
"""Module that retrieves and prints all cities along with\
        their associated states from a MySQL database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":

    # Get the command-line arguments
    db_username = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]

    con = f'mysql+mysqldb://{db_username}:{db_pass}@localhost:3306/{db_name}'
    # Create the engine to connect to the MySQL server
    engine = create_engine(con)

    # Create all tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all City objects and their associated State objects
    cities = session.query(City).join(State).order_by(City.id)

    # Display the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
