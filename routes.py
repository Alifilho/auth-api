from controllers import UserController


def initialize_routes(app):
    app.register_blueprint(UserController.routes)
