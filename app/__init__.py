from flask import Flask
from .auth.v1 import version1
from .auth.v2 import version_2_auth
from .auth.v2.models.db_model import Bball_Db
from app.config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    with app.app_context():
        Bball_Db.init_db(app_config.get('DATABASE_URI'))
        Bball_Db.build_tables()

    app.register_blueprint(version1)
    app.register_blueprint(version_2_auth)
    
    return app
    