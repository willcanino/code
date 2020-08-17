import flask
import pathlib
import datetime
import json
from app import app

# There are two possible approaches to making a form
# We could use a completely 'Pythonic' approach as use as little HTML
# as possible, which would probably be the most ideal approach
# (for me personally), however, our 'client' , willcanino, has
# not the slightest clue how to use Python.  Therefore, using the
# 'Pythonic' approach would give our client very little room to grow
# and ulitmately limit his ability to expand the website without
# a lot of assistance from me. Obviously, I would like my client to
# be as self-sufficient as possible, and rely on me as little as possible.
# Which leads me to take the less 'Pythonic' approach but the better approach
# for the client, which is accepting the input as POST request.

@app.route('/')
def wills_pizza():
    return flask.render_template('index.html')

@app.route('/handle_pizza_data', methods=['POST'])
def handle_pizza_data():
    # flask.request.args is data from the url
    # flask.request.form is data sent through the form
    post_request = flask.request.form
    pizza_dir = pathlib.Path('./pizza-data')
    pizza_dir.mkdir(exist_ok=True)
    # This is `slightly` risky file naming because if the user makes another POST request within one second
    # of sending there previous one, there will be filenaming conflicts.
    # With the current implementation, the old file will just be overwritten,
    # mainly so that the data is consistent
    post_data_loc = pizza_dir / f"{format(datetime.datetime.today(), '%Y-%m-%d_%I.%M.%S.%p')}.json"
    with post_data_loc.open(mode='w') as file:
        post_dict = dict(post_request)
        post_dict.pop('submit', None)
        json.dump(post_dict, file, indent=4)

    print(f"flask.request.form={post_request}")
    print(f"dict={dict(post_request)}")
    flask.flash('Data submitted successfully!')
    return flask.redirect(flask.url_for('wills_pizza'))
