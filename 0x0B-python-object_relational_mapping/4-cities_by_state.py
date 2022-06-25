#!/usr/bin/python3
"""script lists all cities from the dataase hbtn_0e_4_usa"""


import MySQLdb
from sys import argv  # script needs to take 3 arguments

# code should not be executed when imported
if __name__ == "__main__":
    # open database connection based on parameters & scripts args
    opendb = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                             db=argv[3], port=3306)
    # create cursor object used to execute SQL statements
    cursor = opendb.cursor()
    # SQL query we want to execute
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC""")
    # fetch all records from executed query
    results = cursor.fetchall()
    # loop through records and print each one
    for row in results:
        print(row)
    # close up shop
    cursor.close()
    opendb.close()
