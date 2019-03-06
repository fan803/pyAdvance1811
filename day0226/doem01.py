"""
1,微程序，也就是一个web接口
"""

def index(env,response):
    print(env)
    # print(env["PATH_INFO"])
    # print(env["QUERY_STRING"])
    """
    

    :param env: 环境
    :param response: 响应
    :return:
    """
    response("200 OK",[("Content-type", "text / html")])
    return [b"<h1>beautiful</h1>"]

#搭建服务器
from wsgiref.simple_server  import make_server
#创建服务器对象
httpd = make_server("", 8000, index)
print("等待中……")
#让服务器一直工作
httpd.serve_forever()
