from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def hello():
    return "Hello mega world"

@app.route("/get/<int:id>")
def show(id):
    return f'You asked for {id}'

@app.route("/getJson")
def sendJson():
    return {
        "userName" : "Admin",
        "password" : "Password",
        "image" : "This is the user image"
    }

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=5000)