class Config:
    SECRET_KEY = "my_secret_key"
    OIDC_CLIENT_SECRETS = {
        "web": {
            "issuer": "https://login.microsoftonline.com/d84f34b0-9a73-4404-93f7-e8630a3ce520/v2.0",
            "auth_uri": "https://login.microsoftonline.com/d84f34b0-9a73-4404-93f7-e8630a3ce520/oauth2/v2.0/authorize",
            "client_id": "2bb0a5ba-a8f9-4c36-9869-53bc137acaf2",
            "client_secret": "fSe8Q~t1twkWnGv-Lc_unQBOmJbUWaaRRUAyVaYX",  # Use your new client secret here
            "redirect_uris": ["https://flask-ad.purplepebble-4ae5a8dc.japaneast.azurecontainerapps.io/login/azure/authorized"],
            "userinfo_uri": "https://graph.microsoft.com/oidc/userinfo",
            "token_uri": "https://login.microsoftonline.com/d84f34b0-9a73-4404-93f7-e8630a3ce520/oauth2/v2.0/token",
            "token_introspection_uri": "https://login.microsoftonline.com/d84f34b0-9a73-4404-93f7-e8630a3ce520/oauth2/v2.0/token/introspection"
        }
    }
    OIDC_ID_TOKEN_COOKIE_SECURE = False
    OIDC_REQUIRE_VERIFIED_EMAIL = False
    OIDC_USER_INFO_ENABLED = True
    OIDC_OPENID_REALM = "flask"
    OIDC_SCOPES = ["openid", "email", "profile"]
    OIDC_INTROSPECTION_AUTH_METHOD = "client_secret_post"
    OIDC_CALLBACK_ROUTE = "/login/azure/authorized"
