#!/usr/bin/python3
"""print all City objects from db given as an arg"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engin = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                      argv[2],
                                                                      argv[3]))
    Base.metadata.create_all(engin)
    Session = sessionmaker(bind=engin)
    session = Session()
    results = session.query(City, State).filter(City.state_id == State.id)\
                                        .order_by(City.id).all()
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
