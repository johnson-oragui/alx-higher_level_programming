#!/usr/bin/python3
"""
Module that lists all states starting with N from the hbtn_0e_0_usa database.
"""

import MySQLdb
import sys


def list_states_with_N(username, password, database):
    """Lists all states starting with N from the hbtn_0e_0_usa database.
    
    Args:
        username: The username
        password: The password
        database: The database
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve states starting with N
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows and print the state names
    states = cursor.fetchall()
    for state in states:
        print(state[1])

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # List all states starting with N
    list_states_with_N(username, password, database)

