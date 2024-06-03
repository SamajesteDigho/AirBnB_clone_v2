#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") == "db":
        def cities():
            """ Collect the cities """
            from models import storage
            return storage.all(cls=City)
