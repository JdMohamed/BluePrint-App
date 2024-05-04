from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'

    db.init_app(app)

    from blueprintapp.blueprints.todos.routes import todos
    from blueprintapp.blueprints.people.routes import people
    from blueprintapp.blueprints.core.routes import core

    app.register_blueprint(people, url_prefix='/people')
    app.register_blueprint(todos, url_prefix='/todos')
    app.register_blueprint(core, url_prefix='/')
    migrate = Migrate(app, db)

    return app
