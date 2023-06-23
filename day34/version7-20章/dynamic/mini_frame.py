#!/usr/bin/python
# author luke

import time
import re

URL_FUNC_DICT = dict()

def route(url):
    def set_func(func):
        URL_FUNC_DICT[url]=func
        # def call_func(*args, **kwargs):
        #   return func(*args, **kwargs)
        # return call_func
    return set_func


@route('/index.py')
def index():
    with open("./templates/index.html", encoding="utf-8") as f:
        content = f.read()

    #这是实际要从数据库里边查出来
    my_stock_info = "哈哈哈，我是本月最佳员工。。。。"

    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content

@route('/center.py')
def center():
    with open("./templates/center.html", encoding="utf-8") as f:
        content = f.read()

    my_stock_info = "这里是从mysql查询出来的数据。。。"

    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content




def application(environ, start_response):
    # 由mini_frame框架添加响应码和头部
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ['PATH_INFO']
    # file_name = "/index.py"

    func=URL_FUNC_DICT[file_name]
    return func()
