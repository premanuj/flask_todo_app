from app.db import db


class Todo(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    isdeleted = db.Column(db.Boolean, unique=False, default=True)

    def __init__(self, title, description):
        self.title = title
        self.description = description
