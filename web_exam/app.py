from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "your-secret-key"  # needed for flash messages!

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
        email = request.form["email"]
        grade = request.form["grade"]
        password = request.form["password"]
        # save to database next!
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)