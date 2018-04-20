from flask import Flask, jsonify

app = Flask(__name__)

# Test routes
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Media routes
@app.route('/media', methods=['GET'])
def show_media_list():
    return jsonify({'media': []})

@app.route('/media/artists', methods=['GET'])
def show_media_artist_list():
    return jsonify({'artists': []})

@app.route('/media/<string:media_id>', methods=['GET'])
def show_media_details(media_id):
    return jsonify({'media_id': media_id})

# Settings routes
@app.route('/settings', methods=['GET'])
def show_settings_list():
    return jsonify({'settings': []})

@app.route('/settings/<string:settings_key>', methods=['GET'])
def show_settings_details(settings_key):
    return jsonify({'settings_key': 'settings_value'})

# Taxa routes
@app.route('/taxa', methods=['GET'])
def show_taxon_list():
    return jsonify({'taxa': []})

@app.route('/taxa/<string:taxon_name>', methods=['GET'])
def show_taxon_details(taxon_name):
    return jsonify({'name': taxon_name})
