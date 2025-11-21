#!/usr/bin/python3
"""Displays states that match the argument from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         passwd=password,
                         db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query using format with user input
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all results and print
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
