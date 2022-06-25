#!/usr/bin/python3
"""script adds State obj "Louisiana" to database given as arg"""

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
    newstate = State(name="Louisiana")
    session.add(newstate)
    result = session.query(State).filter_by(name="Louisiana").first()
    print(str(result.id))
    session.commit()
    session.close()
