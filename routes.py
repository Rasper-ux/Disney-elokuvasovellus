from app import app
from flask import render_template, request, redirect
import films, users

@app.route("/")
def index():
    list = films.get_list()
    return render_template("index.html", movies=list)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Incorrect usrename or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords differ")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration failed")

@app.route("/film/<int:id>")
def film(id):
    list=films.get_review(id)
    #list2=films.get_stars(id)
    return render_template("film.html", reviews=list, id=id)

@app.route("/send/<int:id>", methods=["POST"])
def send(id):
    content = request.form["content"]
    if films.add_review(content, id):
        return redirect("/")
    else:
        return render_template("error.html", message="The message was not sent successfully")
