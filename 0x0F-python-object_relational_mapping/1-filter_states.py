#!/usr/bin/python3

import sys
import MySQLdb

def list_states_with_N(username, password, database):
    """
    Lists all states with a name starting with N from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")

    # Fetch all rows and print states with names starting with N
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # List all states with names starting with N
    list_states_with_N(username, password, database)

