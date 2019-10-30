# __init__.py文件用于初始化app
# 包括通过工厂模式创建app，以及数据库配置信息

from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy

from flask_session import Session
from flask_wtf import CSRFProtect
import redis
from cm_app import api_1_0

# mysql数据库
# 初始化名为db的SQLAlchemy对象,但不传入app参数（只定义不绑定app对象）
# 什么时候用到app对象什么时候再使用init_app(app)函数绑定
db = SQLAlchemy()

# 创建redis连接对象
redis_store = None


""" 使用工厂模式创建app
    定义创建app函数
    传入config类型名的（"development"，"production"）
"""

# 工厂模式


def create_app(config_name):
    app = Flask(__name__)

    # 根据配置模式的名称获取配置类型
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 此时需要传入app对象绑定数据库，则通过init_app函数传入app对象，用于初始化db对象
    db.init_app(app)

    # # 初始化redis工具
    # global redis_store
    # redis_store = redis.StrictRedis(
    #     host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # # 利用flask-session,将session数据保存到redis中
    # Session(app)

    # # 为flask补充csrf防护
    # CSRFProtect(app)

    # 注册蓝图
    app.register_blueprint(api_1_0.api, url_prefix='/api/v1.0')
    
    return app
