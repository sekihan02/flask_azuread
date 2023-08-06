from flask import Blueprint, request
from app import oidc

bp = Blueprint('chat', __name__, url_prefix='/')

@bp.route('/')
@oidc.require_login
def hello_world():
    info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])
    username = info.get('preferred_username')
    email = info.get('email')
    return 'Hello, {0}!'.format(email)

@bp.route('/api', methods=['POST'])
@oidc.accept_token(require_token=True)
def my_api():
    return json.dumps({'hello': 'Welcome {0}!'.format(g.oidc_token_info['sub'])})
