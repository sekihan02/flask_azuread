# run.py
from app import create_app
from app.routes.chat import chat

app = create_app()
app.register_blueprint(chat)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
