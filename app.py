from flask import Flask, jsonify, render_template
from nordicmicroalgae import database, errors
from nordicmicroalgae.core import py_api as api

# Initialize Flask application
app = Flask(__name__)

# Load settings
app.config.from_object('nordicmicroalgae.settings')

# Close database connection when request has finished
app.teardown_appcontext(database.close_connection)

# Setup error handlers
@app.errorhandler(errors.NotFound)
def handle_not_found(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Routes and views
@app.route('/', methods=['GET'])
def show_about_page():
    return render_template('about.html')

@app.route('/media/<string:media_id>', methods=['GET'])
def show_media_details(media_id):
    media_details = api.media.get_details(database.get_connection(), media_id)
    if media_details is None:
        raise errors.NotFound('Could not find media.')
    return jsonify(media_details)

@app.route('/media/', methods=['GET'])
def show_media_list():
    return jsonify(api.media.get_list(database.get_connection()))

@app.route('/settings/', methods=['GET'])
def show_settings():
    return jsonify(api.system_settings.get(database.get_connection()))

@app.route('/taxa/', methods=['GET'])
def show_taxon_list():
    return jsonify(api.taxa.get_list(database.get_connection()))

@app.route('/taxa/<string:taxon_name>/', methods=['GET'])
def show_taxon_details(taxon_name):
    taxon_details = api.taxa.get_details(database.get_connection(), taxon_name)
    if taxon_details is None:
        raise errors.NotFound('Could not find taxon.')
    return jsonify(taxon_details)
