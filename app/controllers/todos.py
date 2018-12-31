from app.utils.api import res
from flask import Blueprint, jsonify, request, json
from app.services.todoService import TodoService
from app.schemas.todoSchema import TodoSchema

todos_bp = Blueprint("todos", __name__)
todoService = TodoService()
todoSchema = TodoSchema()
todosSchema = TodoSchema(many=True)


@todos_bp.route("", methods=["GET"])
def get_todos():
    todos = todoService.all()
    result = todosSchema.dump(todos)
    return res.success(result.data, 200)


@todos_bp.route("/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todos = todoService.get_or_404(todo_id)
    result = todoSchema.dump(todos)
    return res.success(result.data, 200)


@todos_bp.route("", methods=["POST"])
def create():
    json_data = request.get_json(force=True)
    data = todoSchema.load(json_data)
    todo = todoService.create(**data.data)
    result = todoSchema.dump(todo)
    return res.success(result.data, 200)


@todos_bp.route("/<int:todo_id>", methods=["PUT"])
def update(todo_id):
    json_data = request.get_json(force=True)
    todo = todoService.get_or_404(todo_id)
    data = todoSchema.load(json_data)
    todoService.update(todo, **data.data)
    result = todoSchema.dump(todo)
    return res.success(result.data, 200)


@todos_bp.route("/<int:todo_id>", methods=["DELETE"])
def delete_user(todo_id):
    todo = todoService.get_or_404(todo_id)

    todoService.delete(todo)

    return res.success({}, 204)
