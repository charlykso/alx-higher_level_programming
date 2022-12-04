#!/usr/bin/python3

"""
lists all states from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           charset="utf8", user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    conn.close()
