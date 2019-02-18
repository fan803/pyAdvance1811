#pip install flask
#from flask import Flask
#创建一个应用
#注册路由
#启动服务
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "首页  "

@app.route("/gs")
def gsinfo():
    return " 傻子"

@app.route("/gs/pay")
def glpay():
    return render_template("pay.html")

app.run()
