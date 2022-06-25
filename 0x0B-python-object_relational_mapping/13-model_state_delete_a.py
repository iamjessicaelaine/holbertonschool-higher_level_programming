#!/usr/bin/python3
"""script deletes states containg "a" from db given as arg"""

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
    resultz = session.query(State).filter(State.name.like("%a%"))
    for record in resultz:
        session.delete(record)
    session.commit()
    session.close()
