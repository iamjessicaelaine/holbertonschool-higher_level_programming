#!/usr/bin/python3
"""script lists all states in db hbtn_0e_0_usa that match a user's input"""


import MySQLdb
from sys import argv  # script needs to be able to acknowledge given args

if __name__ == "__main__":  # code below doesn't run on import
    # open database connection w/ important parameters
    opendb = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                             db=argv[3], port=3306)
    # create cursor object so SQl statements can be executed
    cursor = opendb.cursor()
    # createparamterized query 
    sqlparamquery = """SELECT * FROM states WHERE name = %s"""
    # create tuple of parameter values
    argtuple = (argv[4],)
    # time to feed cursor object a parameterized SQL query & arg tuple
    cursor.execute(sqlparamquery, argtuple)
    # fetch all rows ffrom the last executed (SQL) statement
    results = cursor.fetchall()
    # looop through results to print each record
    for row in results:
        print(row)
    # close cursor & connection since no longer needed after results print
    cursor.close()
    opendb.close()
