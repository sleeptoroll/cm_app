目录说明
=======

+ 目录api_1_0 通过以版本号的方式定义api1.0版本蓝图
+ 在当前版本目录中定义类似demo,user.py等视图函数
+ 目录api_1_0的__init__文件中定义具体的蓝图对象,流程如下：
  + 首先在/api_1_0/__init__.py文件中创建蓝图对象
    ~~~python
    # 创建蓝图对象
    api = Blueprint("api_1_0", __name__)
    ~~~
  + 然后在视图函数中，使用相对路径导入蓝图对象api，使用@api.route()方法设置路由。使用相对路径,  . 表示当前api_1_0目录下
    ~~~python
    from . import api

    @api.route('/index')
    ~~~
    > 在创建蓝图对象的时候统一使用版本号作为前缀，则在定义路由时不需要再添加版本号前缀，直接使用/index    
  + 再在api_1_0/__init__文件中导入demo.py，让蓝图知道视图函数demo的存在。使用相对路径,  . 表示当前api_1_0目录下
    ~~~python
    # 导入蓝图视图函数demo
    from . import demo
    ~~~
  + 最后将蓝图注册到flask应用中（/cm_app/__init__.py)中：首先通过绝对路径导入蓝图目录api_1_0,然后注册蓝图
    ~~~python
    # 注册蓝图
    app.register_blueprint(api_1_0.api, url_prefix='api/v1.0')
    ~~~

