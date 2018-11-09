from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

DATABASE_DIALECT = 'mysql'
DATABASE_DRIVER = 'pymysql'
DATABASE_HOST = '127.0.0.1'
DATABASE_PASSWORD = '123456'
DATABASE_USER = 'root'
DATABASE_NAME = 'wufazhuce'
DATABASE_PORT = 3306
DATABASE_CODE = 'utf8'

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = '''{}+{}://{}:{}@{}:{}/{}?charset={}'''.format(
        DATABASE_DIALECT, DATABASE_DRIVER, DATABASE_USER, DATABASE_PASSWORD,
        DATABASE_HOST, DATABASE_PORT, DATABASE_NAME, DATABASE_CODE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


def route_init():
    from service.v1.urls import api
    api.init_app(app)


route_init()
