#!/usr/bin/python3
"""script changes State name to New Mex where record id is 2"""

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
    result = session.query(State).filter_by(id="2").first()
    result.name = "New Mexico"
    session.commit()
    session.close()
