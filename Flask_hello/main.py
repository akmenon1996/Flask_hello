from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to my Page!<h1>"

@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user = user)

@app.route("/shopping")
def shopping():
    food = ["Cheese", "Tuna","Chicken", "Chips"]
    return render_template("shopping.html", food = food)

if __name__ == "__main__":
    app.run(debug=True)

