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
        return render_template("login.html", error=False)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if len(username)==0 or len(password)==0:
            return render_template("login.html", error=True)
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("login.html", error=True)


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", error=False)
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if len(username)==0 or len(password1)==0 or len(password2)==0:
            return render_template("register.html", error=True)
        if password1 != password2:
            return render_template("register.html", error=True)
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("register.html", error=True)

@app.route("/film/<int:id>")
def film(id):
    list=films.get_review(id)
    name=films.get_name(id)
    #list2=films.get_stars(id)
    return render_template("film.html", reviews=list, id=id, name=name[0][0])

@app.route("/send/<int:id>", methods=["POST"])
def send(id):
    content = request.form["content"]
    stars = request.form["stars"]
    if len(content)==0 or len(stars)==0:
        return render_template("error.html", message="Choose stars and write review")
    if len(content)>100:
        return render_template("error.html", message="The review was too long")
    if films.add_review(content, int(stars), id):
        return redirect("/")
    else:
        return render_template("error.html", message="The review was not sent successfully")
