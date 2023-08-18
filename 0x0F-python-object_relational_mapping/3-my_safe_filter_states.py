#!/usr/bin/python3
"""
This script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
and is safe from MySQL injections!.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    where name matches the argument.
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows = cursor.fetchall()

    for row in rows:
        print(row)
