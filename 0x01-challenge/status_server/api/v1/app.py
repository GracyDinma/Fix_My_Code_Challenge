#!/usr/bin/python3
"""
Web server 
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response

# Create a Flask application instance
app = Flask(__name__)

# Register the app_views blueprint with the flask app
app.register_blueprint(app_views)

# Define a custom error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)

# Define a custom erro handler for 500 errors (internal server error@app.errorhandler(500)
def internal_server_error(error):
    """ JSON 500 page """
    return make_response(jsonify({"error": "Internal server error"}), 500)

# Define a route for the root endpoint to test server availability
@app.route('/')
def index():
    """ Index page """
    return jsonify({"message": "Welcome to the API!"})

# Ensure the Flask application runs only if executed directly
if __name__ == "__main__":
    # python -m api.v1.app 
    app.run(host="0.0.0.0", port=5000)
