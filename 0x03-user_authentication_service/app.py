#!/usr/bin/env python3

"""Basic Flask app"""

from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """returns a message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users(email, password) -> str:
    """creates a new user"""
    try:
        user = AUTH.register_user(email=email, password=password)
        return jsonify({"email": "{user.email}", "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
