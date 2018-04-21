#!/usr/bin/env python
# encoding: utf-8

from .qa import qa
from .flask_app import app

app.register_blueprint(qa)
