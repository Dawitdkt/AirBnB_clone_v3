#!/usr/bin/python3
"""
Sets up Flask application
"""

from flask import Flask, jsonify, make_response
from os import getenv

from flask_cors import CORS

from models import storage
from api.v1.views import app_views


app = Flask(__name__)
CORS(app, orgins='0.0.0.0')
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(self):
    """Closes storage session"""
    storage.close()
    
@app.errorhandler(404)
def page_not_found(error):
    """Returns JSON error repsponse"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=int(port), threaded=True)
