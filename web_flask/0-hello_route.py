#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/airbnb-onepage', methods=['GET'])
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=5000, debug=True)
=======
    app.run(host="0.0.0.0", port=5000, debug=None)
>>>>>>> 9f3160da15e4d03e7cf8fd289f634e58d1fc0eb3
