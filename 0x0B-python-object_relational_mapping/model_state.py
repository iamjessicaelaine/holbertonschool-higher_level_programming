#!/usr/bin/python3
"""defines class State and an instance declaration of Base class"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# declaring base: a catalog of clsses & tables in declarative system
Base = declarative_base()


# mapping the class to the table
class State(Base):
    """defining the object state & its respective table"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
