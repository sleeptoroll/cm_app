# 自定义正则表达式转换器
from werkzeug.routing import BaseConverter


class ReConverter(BaseConverter):
    """  """

    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(ReConverter, self).__init__(url_map)
        # 保存正则表达式
        self.regex = regex

