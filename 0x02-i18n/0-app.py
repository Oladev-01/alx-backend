#!/usr/bin/env python3
"""flask instance"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def ret_index():
    """return index.html"""
    return render_template('index.html')
