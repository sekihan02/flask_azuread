from flask import Flask, redirect, url_for, session
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your secret key
oauth = OAuth(app)

tenantid = 'd84f34b0-9a73-4404-93f7-e8630a3ce520'
azure = oauth.remote_app(
    'azure',
    consumer_key='26aa7479-578f-43fa-ab23-444bd3f9dcc5',  # Replace with your Client ID
    consumer_secret='6e0c21c7-9271-4983-b59f-5333521834ac',  # Replace with your Client Secret
    request_token_params={'scope': 'user.read'},
    base_url='https://graph.microsoft.com/v1.0/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url=f'https://login.microsoftonline.com/{tenantid}/oauth2/v2.0/token',  # Replace with your Tenant ID
    authorize_url=f'https://login.microsoftonline.com/{tenantid}/oauth2/v2.0/authorize'  # Replace with your Tenant ID
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
    return azure.authorize(callback=url_for('authorized', _external=True))

@app.route('/login/authorized')
def authorized():
    resp = azure.authorized_response()

    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error'],
            request.args['error_description']
        )

    session['azure_token'] = (resp['access_token'], '')

    return redirect(url_for('index'))

@azure.tokengetter
def get_azure_oauth_token():
    return session.get('azure_token')

if __name__ == '__main__':
    app.run()
