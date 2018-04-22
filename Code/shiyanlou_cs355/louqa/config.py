#!/usr/bin/env python
# encoding: utf-8

class FlaskConfig(object):
    # 配置了数据库服务相关信息，如帐号，密码等
    SQLALCHEMY_DATABASE_URL = "mysql://qa:1qaz@localhost/qa"

