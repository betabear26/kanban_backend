from flask import Flask
from config import FlaskConfig, AppConfig

app = Flask(__name__)
app.config.from_object(FlaskConfig)

@app.route("/.well-known/acme-challenge/YS5aHHHMTF6JnDuUA82BuFesNytm0nr4C973wbF2w8k")
def ssl():
    return AppConfig.SSL

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
    app.run(host='0.0.0.0', port=AppConfig.PORT)