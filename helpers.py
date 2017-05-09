import urllib
import json
from google.appengine.api import urlfetch
from state_vars import verify_state_var
import google_access


def get_token(code, state):

    # verify state variable
    if not verify_state_var(state):
        return "bad state var"

    # exchange the code for a token
    api_access_token_url = "https://www.googleapis.com/oauth2/v4/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    client_id = google_access.client_id
    client_secret = google_access.client_secret
    redirect_uri = "https://boones-oauth-demo.appspot.com/oauth2callback"
    grant_type = "authorization_code"
    fields = [("client_id", client_id), ("client_secret", client_secret), ("redirect_uri", redirect_uri),
              ("grant_type", grant_type), ("code", code)]
    form_data = urllib.urlencode(fields)
    response = urlfetch.fetch(url=api_access_token_url, headers=headers, payload=form_data, method=urlfetch.POST)
    token_json = json.loads(response.content)

    # use token to get user data
    headers = {"Authorization": token_json["token_type"] + " " + token_json["access_token"]}
    user_data_url = "https://www.googleapis.com/plus/v1/people/me"
    response = urlfetch.fetch(url=user_data_url, headers=headers, method=urlfetch.GET)
    user_json = json.loads(response.content)

    return user_json
