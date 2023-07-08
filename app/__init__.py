# __init__.py
import os

from flask import Flask
from .routes.chat import chat_bp, azure_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)  # シークレットキーをランダムに生成

    app.register_blueprint(chat_bp)
    app.register_blueprint(azure_bp, url_prefix="/login")

    return app
