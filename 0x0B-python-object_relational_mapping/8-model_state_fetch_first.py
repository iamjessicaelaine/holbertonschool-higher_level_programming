#!/usr/bin/python3
"""script prints the first State objects of given db argument"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engin = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                      argv[2],
                                                                      argv[3]))
    Base.metadata.create_all(engin)
    Session = sessionmaker(bind=engin)
    session = Session()
    result = session.query(State).order_by(State.id).first()
    if result is not None:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")
    session.close()
