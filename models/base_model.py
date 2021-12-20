#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import models
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    # Class attributes are accessed by classname.attribute_name
    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            dt = "%Y-%m-%dT%H:%M:%S.%f"
            del kwargs['__class__']
            kwargs['created_at'] = datetime.strptime(kwargs["created_at"], dt)
            kwargs['updated_at'] = datetime.strptime(kwargs["updated_at"], dt)
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()
        '''
        The example below is what pop should be doing.
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        '''
        new_dict.pop('_sa_instance_state', None)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def delete(self):
        ''' Deletes the current instance from the storage '''
        models.storage.delete(self)
