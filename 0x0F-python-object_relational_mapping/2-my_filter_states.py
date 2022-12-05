#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           charset="utf8", user=argv[1],
                           passwd=argv[2], db=argv[3])
    # creating a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name \
                LIKE '{:s}' ORDER BY states.id ASC".format(argv[4]))
    query_row = cur.fetchall()
    for row in query_row:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    conn.close()
