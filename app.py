from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("/front-end/html/index.html")