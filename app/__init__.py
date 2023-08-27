from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache


# Extensions
db = SQLAlchemy()
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})



def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    

    # Initialize extensions
    db.init_app(app)
    cache.init_app(app)

    # Import and register blueprints
    from app.main import main_blueprint

    app.register_blueprint(main_blueprint)

    app.static_folder = 'static'
    return app