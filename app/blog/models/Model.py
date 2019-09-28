from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class BlogCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        self.name = name


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    tags = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)

    category_id = db.Column(db.Integer, db.ForeignKey(BlogCategory.id))
    category = db.relationship('BlogCategory', foreign_keys=category_id)
