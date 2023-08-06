from flask_oidc_ex import OpenIDConnect
from app import create_app

from flask_dance.contrib.azure import make_azure_blueprint, azure

class ReverseProxied(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        # scheme = environ.get('HTTP_X_FORWARDED_PROTO')
        scheme = 'https'  # ハードコードしてhttpsを使用
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

app = create_app('app.config.Config')
app.wsgi_app = ReverseProxied(app.wsgi_app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
# ssl_context=('openssl/server.crt', 'openssl/server.key'), 