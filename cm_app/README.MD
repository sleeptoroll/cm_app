Component Management APP
========================

## cm_app的启动控制流程

+ /manage.py中创建flask app
  ~~~python
  # 创建flask应用对象
  app = create_app("develop")
  ~~~
+ 使用数据库迁移和flask管理插件管理flask app：
  + 导入flask_script 和 flask_migrate
    ~~~python
    from flask_script import Manager
    from flask_migerate import Migerate, MigerateCommand
    ~~~
  + 添加flask管理对象和数据库迁移对象
    ~~~python
    # 创建flask管理对象
    manager = Manager(app)

    # 迁移对象保存到app中，并绑定数据库对象db
    Migerate(app, db)
    ~~~
  + 添加flask管理命令
    ~~~python
    manager.add_command("db", MigrateCommand)
    ~~~
  + 使用manager管理对象启动app
    ~~~python
    manager.run(host="0.0.0.0", port='5000')
    ~~~

## 常见错误
+ 报错“raise ValueError("urls must start with a leading slash")”
    ~~~python
    @api.route("/index")
    def index():
    return "index page"

    ~~~

    ~~~python
    # 注册蓝图
    app.register_blueprint(api_1_0.api, url_prefix='/api/v1.0')
    ~~~
  > 检查这两个地方的路径("/index"和/api/v1.0')前面是否少了“/”


