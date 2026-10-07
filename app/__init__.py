from flask import Flask
from config import Config
from .extensions import db, jwt, bcrypt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    from .auth.routes import auth_bp
    from .tasks.routes import tasks_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(tasks_bp, url_prefix="/api/tasks")

    # Create tables
    with app.app_context():
        db.create_all()

    return app