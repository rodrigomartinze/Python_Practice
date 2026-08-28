import os
import bcrypt
import sqlite3
from flask import Flask, render_template, request, redirect, flash
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        # logic here next!
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        email = request.form["email"]
        grade = request.form["grade"]
        password = request.form["password"]
        hashed =  bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        conn = sqlite3.connect("math_exam.db")
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO users (usename, name, email, password, grade)
                       """
        )
        
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)