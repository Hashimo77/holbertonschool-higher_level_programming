#!/usr/bin/python3
"""
Script that lists all states starting with 'N' from the database.
Usage: ./1-filter_states.py <username> <password> <database>
"""
import sys
import MySQLdb


def main():
    """Main function"""
    # Arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # Execute query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and display results
    for row in cursor.fetchall():
        print(row)

    # Close connections
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
