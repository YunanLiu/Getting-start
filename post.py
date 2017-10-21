#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/Login', methods=['GET', 'POST'])
def login():
    return 'Login!'


if __name__ == '__main__':
    app.run()



