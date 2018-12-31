from app.controllers.todos import todos_bp


def register_route(app):
    app.register_blueprint(todos_bp, url_prefix="/todos")
