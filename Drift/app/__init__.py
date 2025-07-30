from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["DEBUG"] = os.getenv("DEBUG", "false").lower() == "true"

    db.init_app(app)
    csrf.init_app(app)

    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    return app
