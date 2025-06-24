import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev'),
    )

    from .main import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    print("Flask app created and blueprint registered.")

    return app