from flask import Blueprint, render_template, redirect, url_for
from flask_dance.contrib.azure import make_azure_blueprint, azure

chat_bp = Blueprint('chat', __name__)

# azure_bp = make_azure_blueprint(
#     client_id="26aa7479-578f-43fa-ab23-444bd3f9dcc5",
#     client_secret="oA88Q~C5Z3.k4enrl2WRWqrkbAtKZAtMP0lnKah3",
#     redirect_url="https://flask-bot-logintest.delightfulmoss-c4e46ed1.westus2.azurecontainerapps.io/login/azure/authorized",
#     tenant="d84f34b0-9a73-4404-93f7-e8630a3ce520",
# )
azure_bp = make_azure_blueprint(
    client_id="26aa7479-578f-43fa-ab23-444bd3f9dcc5",
    client_secret="oA88Q~C5Z3.k4enrl2WRWqrkbAtKZAtMP0lnKah3",
    redirect_url="https://flask-bot-logintest.delightfulmoss-c4e46ed1.westus2.azurecontainerapps.io/login/azure/authorized",
    tenant="d84f34b0-9a73-4404-93f7-e8630a3ce520",
    scope=["openid", "profile", "offline_access"],
    prompt="consent"
)

@chat_bp.route("/")
def index():
    if not azure.authorized:
        return redirect(url_for("azure.login"))
    resp = azure.get("/me")
    assert resp.ok
    return render_template('index.html')
