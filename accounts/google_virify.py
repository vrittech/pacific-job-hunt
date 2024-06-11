# utils.py

from google.auth.transport import requests
from google.oauth2 import id_token

GOOGLE_CLIENT_ID = ["698950373821-j8vpbqpj94ihubrttrgp8rbq2vg78n8e.apps.googleusercontent.com"]
def VerifyGoogleToken(token):
    # print(token)
    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_CLIENT_ID
        )    
        return idinfo,True
    except ValueError as e:
        # Invalid token
        print(f'Error verifying Google ID token: {e}')
        return None,False
        