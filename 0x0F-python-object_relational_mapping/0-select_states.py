#!/usr/bin/env python3

import sys
import MySQLdb

def list_states(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()
    
    # Execute the SQL query to retrieve states
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    
    # Fetch all the rows from the result set
    rows = cursor.fetchall()
    
    # Display the results
    for row in rows:
        print(row)
    
    # Close the cursor and database connection
    cursor.close()
    db.close()

# Check if the script is being run directly
if __name__ == '__main__':
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Call the function to list states
    list_states(username, password, database)

