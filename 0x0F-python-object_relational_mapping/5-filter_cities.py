#!/usr/bin/python3
"""
script that takes in the name of a state
as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to database
    conn = MySQLdb.connect(host="localhost", port=3306,
                           charset="utf8", user=argv[1],
                           passwd=argv[2], db=argv[3])
    # creating a cursor
    cur = conn.cursor()
    cur.execute("SELECT cities.name \
                 FROM states \
                 INNER JOIN cities ON states.id = cities.state_id \
                 WHERE states.name=%s\
                 ORDER BY cities.id ASC;", (argv[4],))
    query_row = cur.fetchall()
    print(', '.join(["{:s}".format(city[0]) for city in query_row]))
    cur.close()
    conn.close()
