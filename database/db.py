from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app(app):
    db.init_app(app)

