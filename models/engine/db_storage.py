#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy.engine import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    classes = {"User": User, "State": State,
               "City": City, "Amenity": Amenity,
               "Place": Place, "Review": Review}

    def __init__(self):
        host = getenv("HBNB_MYSQL_HOST", "localhost")
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        db_name = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, pwd, host, db_name),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            self.__sesssion.drop_all()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objects = {}
        if cls is None:
            for x in self.classes:
                res = self.__session.query(self.classes[x]).all()
                for obj in res:
                    key = "{}.{}".format(x, obj.id)
                    objects[key] = obj
        else:
            res = self.__session.query(cls).all()
            for obj in res:
                key = "{}.{}".format(cls, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete obj from database """
        if obj is not None:
            cls = self.classes[obj.__name__]
            self.__session.query(cls).filter(cls.id == obj.id).delete(
                synchronize_session='fetch'
            )
            self.__session.commit()

    def reload(self):
        """Loads storage data from database"""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory=session_fact)
        self.__session = Session()

    def close(self):
        """ Here we close """
        self.__session.remove()
