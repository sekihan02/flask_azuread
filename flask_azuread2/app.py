from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your secret key
app.config['SERVER_NAME'] = 'flask-bot.delightfulmoss-c4e46ed1.westus2.azurecontainerapps.io'  # Add this line
app.config['PREFERRED_URL_SCHEME'] = 'https'

oauth = OAuth(app)

tenant_id = 'd84f34b0-9a73-4404-93f7-e8630a3ce520'
azure = oauth.register(
    'azure',
    client_id='26aa7479-578f-43fa-ab23-444bd3f9dcc5',  # Replace with your Client ID
    client_secret='6e0c21c7-9271-4983-b59f-5333521834ac',  # Replace with your Client Secret
    access_token_url=f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token',  # Replace with your Tenant ID
    authorize_url=f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize',  # Replace with your Tenant ID
    api_base_url='https://graph.microsoft.com/v1.0/',
    client_kwargs={
        'scope': 'user.read'
    },
)

@app.route('/')
def index():
    if 'azure_token' in session:
        me = azure.get('me')
        return jsonify(me.data)
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    redirect_uri = url_for('authorized', _external=True)
    return azure.authorize_redirect(redirect_uri)
# @app.route('/login')
# def login():
#     redirect_uri = 'https://flask-bot.delightfulmoss-c4e46ed1.westus2.azurecontainerapps.io/login/authorized'
#     app.logger.info(f'Redirect URI: {redirect_uri}')  # This will log the Redirect URI
#     return azure.authorize_redirect(redirect_uri)


@app.route('/login/authorized')
def authorized():
    resp = azure.authorize_access_token()

    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error'],
            request.args['error_description']
        )

    session['azure_token'] = resp['access_token']

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
