
# class Article(db.Model):

#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), nullable=False)
#     content = db.Column(db.Text, nullable=False)


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