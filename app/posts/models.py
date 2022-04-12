from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, DateTime
from geoalchemy2 import Geometry
import time

db = SQLAlchemy()

class Tweet(db.Model):
    id = Column(Integer, primary_key= True)
    msg = Column(Text)
    location = Column(Geometry("POINT", 0))
    epoch_time = Column(Integer, default= time.time())

    def __init__(self, msg, lat, lon):
        self.msg = msg
        self.location = 'POINT({} {})'.format(lat, lon)

    def __repr__(self):
        return f"id= {self.id}; msg= {self.msg}"

