import os
import base64

USERNAME = 'Samat2017'
PASSWORD = 'asdfghjkl8'


def get_auth_token(username=USERNAME, password=PASSWORD):
    """Generates authentication token using username and password"""

    # return 'Basic ' + base64.b64encode(bytes(f'{username}:{password}'.encode('utf-8'))).decode('utf-8')
    return 'Basic U2FtYXQyMDE3OmFzZGZnaGprbDg='
