#!/usr/bin/python3
"""
Script that lists all cities from the db hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    cur.execute(query)

    rows = cur.fetchall()
    for elt in rows:
        print(elt)

    cur.close()
    db.close()
