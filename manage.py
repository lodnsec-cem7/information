from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    """项目的配置"""
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
#  加载配置
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
