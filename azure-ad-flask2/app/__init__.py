from flask import Flask
from flask_oidc_ex import OpenIDConnect

oidc = None

def create_app(config_object):
    global oidc
    app = Flask(__name__)
    app.config.from_object(config_object)

    oidc = OpenIDConnect(app)

    from app.routes import chat  # move the import here
    app.register_blueprint(chat.bp)

    return app
