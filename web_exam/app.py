from flask import Flask, render_template
import bcrypt
import sqlite3

app = Flask(__name__)

#HOME

@app.route("/")
def home():
    return render_template("index.html")


# REGISTER/LOGIN PAGE

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
    


if __name__ == "__main__":
    app.run(debug=True)  # ← add debug=True!