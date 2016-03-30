#! /usr/bin/env python3.4
# -*- coding: utf-8 -*-
# config.py - configration for crysadm web and redis server
__author__ = 'powergx'

# Redis����������
class RedisConfig():
    def __init__(self, host, port, db, password=None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password

# Crysadm ����
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    SESSION_TYPE = 'memcached'
    SECRET_KEY = 'CB5366E0-01ED-4017-A9F7-BFCF4EE28AD6'
    REDIS_CONF = RedisConfig(host='127.0.0.1', port=6379, db=0)
    PASSWORD_PREFIX = "1A4C8B19-069A-4D21-94B2-09FE32D27506"
    ENCRYPT_PWD_URL = None
    SERVER_IP = '0.0.0.0'
    SERVER_PORT = 4000

# ��������ʱ����
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

# ����������ģʽ
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

# ����ģʽ
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
