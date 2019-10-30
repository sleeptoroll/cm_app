import redis

# 基础配置类


class Config(object):
    # 安全密钥
    SECRECT_KEY = "fdjlKKJDWEksajdf12LKLJe4"

    # mysql数据配置信息
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@sleeptoroll.xyz:3306/db_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    # # redis数据库配置信息
    # REDIS_HOST = "192.168.1.88"
    # REDIS_PORT = 6379

    # # flask-session配置信息
    # SESSION_TYPE = "redis"
    # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # SESSION_USER_SIGNER = True  # 对cookie中的sessionid进行隐藏处理
    # PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期，单位秒


# 开发模式配置类，继承继承配置类
class DevelopmentConfig(Config):
    DEBUG = True


# 生产模式配置类，继承继承配置类
class ProductionConfig(Config):
    pass


# 字典映射配置名字和配置类型的关系
config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
