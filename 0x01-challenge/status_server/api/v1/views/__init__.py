#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint

# Create a Flask Blueprintnamed "app_views" with URL prefix "/api/vi"
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

# Import views (routes) from other modules
from api.v1.views.index import *
