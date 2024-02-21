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
            return render_template("login.html", error=True, message="Täytä kaikki kentät")
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("login.html", error=True, message="Väärä käyttäjätunnus tai salasana")


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
            return render_template("register.html", error=True, message="Täytä kaikki kentät")
        if password1 != password2:
            return render_template("register.html", error=True, message="Salasanat poikkeavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("register.html", error=True, message="Rekisteröityminen epäonnistui")

@app.route("/film/<int:id>")
def film(id):
    list=films.get_review(id)
    name=films.get_name(id)
    alikes=films.get_alikes(id)
    return render_template("film.html", reviews=list, id=id, name=name[0][0], alikes=alikes, error=False)

@app.route("/send/<int:id>", methods=["POST"])
def send(id):
    list=films.get_review(id)
    name=films.get_name(id)
    alikes=films.get_alikes(id)
    content = request.form["content"]
    stars = request.form["stars"]
    if len(content)==0 or len(stars)==0:
        return render_template("film.html", reviews=list, id=id, name=name[0][0], alikes=alikes, error=True, message="Valitse tähdet ja kirjoita arvostelu")
    if len(content)>100:
        return render_template("film.html", reviews=list, id=id, name=name[0][0], alikes=alikes, error=True, message="Arvostelu oli liian pitkä, max 100 merkkiä sallittu")
    if films.add_review(content, int(stars), id):
        return redirect("/")
    else:
        return render_template("film.html", reviews=list, id=id, name=name[0][0], alikes=alikes, error=True, message="Arvostelun lähetys ei onnistunut")
