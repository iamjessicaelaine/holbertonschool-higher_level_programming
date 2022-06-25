#!/usr/bin/python3
"""script takes state as an arg and lists cities of the state w/i given db"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    opendb = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                             db=argv[3], port=3306)
    cursor = opendb.cursor()
    # injection protection
    sqlquery = """SELECT cities.name FROM cities JOIN states
    ON cities.state_id = states.id WHERE states.name LIKE %s ORDER BY
    cities.id"""
    # create tuple for user input for injection protection
    argtuple = (argv[4],)
    # execute a query protected from injection
    cursor.execute(sqlquery, argtuple)
    results = cursor.fetchall()
    print(", ".join(row[0] for row in results))
    # close up shop
    cursor.close()
    opendb.close()
