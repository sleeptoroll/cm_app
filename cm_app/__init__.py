# __init__.py文件用于初始化app
# 包括通过工厂模式创建app，以及数据库配置信息
import redis
import logging

from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from logging.handlers import RotatingFileHandler
from cm_app.utils.commons import ReConverter


# mysql数据库
# 初始化名为db的SQLAlchemy对象,但不传入app参数（只定义不绑定app对象）
# 什么时候用到app对象什么时候再使用init_app(app)函数绑定
db = SQLAlchemy()

# 创建redis连接对象
redis_store = None


# 设置日志的记录等级.*
# 注意：如果在config_name=development设置为开发模式,会开启Debug=True
# 这时无论日志等级为四种中的哪一种，都会自动覆盖日志等级为DEBUG
logging.basicConfig(level=logging.DEBUG)  # 分DEBUG，INFO，WARN，ERROR四种级别
# 创建日志记录器，指明日志保存路径、每个日志文件最大大小、保存日志个数上限
file_log_handler = RotatingFileHandler(
    "logs/log", maxBytes=1024*1024*100, backupCount=6)
# 创建日志记录的格式
formatter = logging.Formatter(
    '%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)


""" 使用工厂模式创建app
    定义创建app函数
    传入config类型名的（"development"，"production"）
"""


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

    # 为了防止循环导入db的问题，在注册蓝图之前再导入.即什么时候注册蓝图，什么时候导入相关对象
    from cm_app import api_1_0

    # 注册蓝图之前为flask引入自定义re转换器
    # (from cm_app.utils.commons import ReConverter)
    app.url_map.converters["re"] = ReConverter

    # 注册蓝图
    app.register_blueprint(api_1_0.api, url_prefix='/api/v1.0')

    # 注册提供静态文件蓝图
    from cm_app.web_html.web_html import html
    app.register_blueprint(web_html.web_html.html) #此处不需要添加前缀url_prefix

    return app
