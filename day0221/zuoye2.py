from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    # return "<h1>这是首页</h1>"
    return render_template("index.html")
@app.route("/A.html")
def A():
    # return "这个是A"
    return render_template("A.html")
@app.route("/B.html")
def B():
    # return "这个是B"
    return render_template("B.html")

app.run()