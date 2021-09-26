from enum import unique
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import Column
from .db import db

#Create models

class Movies(db.Model):
    __tablename__='movies'
    id=db.Column(db.Integer,autoincrement=True,primary_key=True,unique=True)
    name=db.Column(db.String(80),nullable=True)
    genres=db.Column(db.String(60),nullable=True)