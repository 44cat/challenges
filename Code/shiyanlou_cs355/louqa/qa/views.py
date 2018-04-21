#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint

qa = Blueprint('qa',__name__,url_prefix="")

@qa.route('/')
def index():
    #返回带有 HTML 标签装饰的 "Hello World"
    return "<p>Hello World</p>"


