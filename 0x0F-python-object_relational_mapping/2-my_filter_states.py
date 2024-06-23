#!/usr/bin/pyhton3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import mySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(query)

    rows = cur.fetchall()
    for elts in rows:
        print(elts)

    cur.close()
    db.close()
