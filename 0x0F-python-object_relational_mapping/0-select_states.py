#!/usr/bin/python3
"""Module that lists all states from a MySQL database."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to select all rows from the 'states' table
    cursor.execute("SELECT * FROM `states`")

    # Fetch all rows from the result set and print them
    [print(state) for state in cursor.fetchall()]

    # Close the database connection
    db.close()

