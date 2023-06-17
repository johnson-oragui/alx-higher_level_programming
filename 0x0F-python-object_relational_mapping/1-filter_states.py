#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database."""
import MySQLdb
import sys

# Get the command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

# Connect to the MySQL server
db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name
)

# Create a cursor object to execute queries
cursor = db.cursor()

# Prepare the SQL query
sql_query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

# Execute the query
cursor.execute(sql_query)

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Display the results
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()

