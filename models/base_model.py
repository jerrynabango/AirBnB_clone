#!/usr/bin/python3
"""parent class BaseModel"""

# uuid: Universally Unique identifier for the model object.
import uuid
from datetime import datetime


class BaseModel:
    """Parent Class."""

    def __init__(self, *args, **kwargs):
        """
        __init__: Initialization function for instance methods
        args: collects number of positional arguments passed
        to the constructor as a tuple.
        kwargs: collect number of keyword arguments passed to
        the constructor as a dictionary
        """

        """
        Checks the kwargs passed to the constructor is not
        empty and returns True
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Human readable string representation"""

    # __name__: The name of the class that implements the interface implemented
    # by this class in Python classes that implement __str__ method and return
    # a string representation of the class object as a string in Python classes
    # id: The id of the object to be created or updated in the database
    # __dict__: dict with keys and values being strings that represent objects
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        from models import storage
        """
        updates the state of the object with the given
        attributes and returns the updated object.
        """
        self.updated_at = datetime.now()

        """save the updated_ at attribute with the current datetime."""
        storage.save()

    def to_dict(self):
        """Converts to dictionary representation."""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = type(self).__name__

        return my_dict
