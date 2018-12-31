from app.models.todos import Todo
from app.core.service import Service
from app.db import db


class TodoService(Service):
    __model__ = Todo

    def _preprocess_params(self, kwargs):
        return kwargs
