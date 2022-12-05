#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           charset="utf8", user=argv[1],
                           passwd=argv[2], db=argv[3])
    # creating a cursor
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states On cities.state_id = states.id")
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    conn.close()
