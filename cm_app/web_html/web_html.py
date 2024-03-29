from flask import Blueprint, current_app


# 提供静态文件蓝图
html = Blueprint("web_html", __name__)


# 127.0.0.1:5000/
# 127.0.0.1:5000/index.html
# 127.0.0.1:5000/register.html
@html.route("/<re(r'.*'):html_file_name>")
def get_html(html_file_name):
    """ 提供html文件 """
    # 如果html_file_name为空，表示访问路径为/, 请求的是主页index.html
    if not html_file_name:
        html_file_name = "index.html"

    # 如果资源名不是favicon.ico
    if html_file_name != "favicon.ico":
        html_file_name = "html/" + html_file_name

    # flask提供的返回静态文件的方法
    return current_app.send_static_file(html_file_name)
