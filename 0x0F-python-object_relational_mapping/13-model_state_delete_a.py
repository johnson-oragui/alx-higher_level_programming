#!/usr/bin/python3
"""Module that deletes states containing the letter
'a' from a MySQL database using SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)
    # Create a session object
    session = Session()
    session.query(State).filter(State.name.like('%a%')).delete()
    # # Commit the session to persist the changes
    session.commit()
