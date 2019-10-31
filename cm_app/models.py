from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from . import db

# 注意在添加完models创建表后，需要在视图函数中导入
# 否则在使用python manage.py db migrate命令做迁移时是没有任何作用的
class BaseModel(object):
    """ 模型基类，为每个模型补充创建时间和更新时间 """
    create_time = db.Column(DateTime, default=datetime.now)
    update_time = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Article(BaseModel, db.Model):

    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(32))


# db.drop_all()
# db.create_all()

# # 表中添加单条记录
# atc1 = Article(title="python自学指南", content="如何高效自学python")
# db.session.add(atc1)
# db.session.commit()

# # 表中批量添加记录
# atc2 = Article(title="mysql", content="mysql从删库到跑路")
# atc3 = Article(title="NodeJS", content="Node入门指南")
# atc4 = Article(title="JQuery", content="JQuery权威指南")
# atc5 = Article(title="JAVA", content="Java权威指南")

# db.session.add_all([atc2, atc3, atc4, atc5])
# db.session.commit()
