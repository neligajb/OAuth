from flask import Flask, render_template, request
from helpers import get_token
import state_vars
import google_access
app = Flask(__name__)


@app.route('/')
def index():
    state_var = state_vars.state_generator()
    return render_template('index.html', state_var=state_var, client_id=google_access.client_id)


@app.route('/oauth2callback')
def callback():
    response = get_token(request.args['code'], request.args['state'])
    if response is "bad state var":
        return "Forbidden"
    return render_template('callback.html', response=response)

if __name__ == '__main__':
    app.run()
