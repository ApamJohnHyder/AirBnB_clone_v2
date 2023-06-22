#!/usr/bin/python3
""" Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ contains state ID and name """
    state_id = ""
    name = ""
