"""
@Time    : 2018-11-12 16:02:49
@Author  : xionzhi
@File    : service.__init__.py
@Software: vscode
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

__all__ = ['app', 'db', 'ma', 'api', 'logger']

app = Flask(__name__)
app.config.from_object('config.dev')  # 导入配置文件
app.config[
    'SQLALCHEMY_DATABASE_URI'] = '''{}+{}://{}:{}@{}:{}/{}?charset={}'''.format(
        app.config['DATABASE_DIALECT'], app.config['DATABASE_DRIVER'],
        app.config['DATABASE_USER'], app.config['DATABASE_PASSWORD'],
        app.config['DATABASE_HOST'], app.config['DATABASE_PORT'],
        app.config['DATABASE_NAME'], app.config['DATABASE_CODE'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

logger = app.config['LOGGER']  # 导入配置文件配置


def route_init():
    # loading route
    from service.v1.urls import api
    api.init_app(app)


route_init()
