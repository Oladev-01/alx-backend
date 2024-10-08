#!/usr/bin/env python3
"""flask instance"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def ret_index() -> str:
    """return index.html"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
