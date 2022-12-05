#!/usr/bin/python3
"""
write a script that takes in arguments
and displays all values in the states
table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that
is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           charset="utf8", user=argv[1],
                           passwd=argv[2], db=argv[3])
    # creating a cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE \
                name=%s ORDER BY states.id ASC", (argv[4],))
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    conn.close()
