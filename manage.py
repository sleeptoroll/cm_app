from cm_app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 创建flask应用对象和flask管理对象
app = create_app("development")


# 迁移对象保存到app中，并绑定数据库对象db
Migrate(app, db)

# 添加管理命令
manager = Manager(app)
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()
