import redis
from redis import StrictRedis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session

class Config(object):
    """项目的配置"""
    DEBUG = True
    SECRET_KEY = "b'5NHGKRGy6RaiTNvWMQCzzusBQ3tSRXAx2Cj+ERJGIBRnxDzTejFs6pO8cyaC86Rb'"
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis 的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # Session保存配置
    SESSION_TYPE = "redis" # 制定session保存到redis中
    SESSION_USE_SIGNER = True # 让cookie中的session_id被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT) # 使用redis实例
    PERMANENT_SESSION_LIFETIME = 86400 # 设置session的有效时间

app = Flask(__name__)
#  加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
# 开启当前项目CSRF保护
CSRFProtect(app)

Session(app)

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
