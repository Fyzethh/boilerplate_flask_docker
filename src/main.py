from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    test = "Terricolas"
    return f"<p>Hello, {test}</p>"