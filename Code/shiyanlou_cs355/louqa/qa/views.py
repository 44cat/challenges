#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint
from flask import render_template

qa = Blueprint('qa',__name__,url_prefix="")

@qa.route('/')
@qa.route('/',defaults={'title':None})
def index(title):
    return render_template('qa/index.html',title=title,tem_str="world")


