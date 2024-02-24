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
            return render_template("register.html", error=True, message="Käyttäjätunnus on jo käytössä")

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

@app.route("/user")
def user():
    user_id = users.user_id()
    if user_id == 0:
        return False
    info = users.get_info(user_id)
    if len(info)==0:
        return render_template("user.html", id=user_id, info=False)
    else:
        return render_template("user.html", id=user_id, info=info)

@app.route("/info/<int:id>", methods=["POST"])
def add_info(id):
    age=request.form["age"]
    content=request.form["content"]
    if len(content)==0 or len(age)==0:
        return render_template("user.html", id=id, info=False, message="Täytä molemmat kentät")
    if len(content)>121:
        return render_template("user.html", id=id, info=False, message="Elokuvan nimi ei voi olla noin pitkä")
    if int(age)<0 or int(age)>120:
        return render_template("user.html", id=id, info=False, message="Kirjoita oikea ikäsi")
    if users.add_info(id, int(age), content):
        info = users.get_info(id)
        return render_template("user.html", id=id, info=info)
    else:
        return render_template("user.html", id=id, info=False, message="Lähetys epäonnistui")

@app.route("/update_info/<int:id>")
def update_info(id):
    return render_template("update_info.html", id=id, error=False)

@app.route("/send_update/<int:id>", methods=["POST"])
def send_update(id):
    age=request.form["age"]
    content=request.form["content"]
    if len(content)==0 or len(age)==0:
        return render_template("update_info.html", id=id, error=True, message="Täytä molemmat kentät")
    if len(content)>121:
        return render_template("update_info.html", id=id, error=True, message="Elokuvan nimi ei voi olla noin pitkä")
    if int(age)<0 or int(age)>120:
        return render_template("update_info.html", id=id, error=True, message="Kirjoita oikea ikäsi")
    if users.update_info(id, int(age), content):
        info = users.get_info(id)
        return render_template("user.html", id=id, info=info)
    else:
        return render_template("update_info.html", id=id, error=True, message="Päivitys epäonnistui")

@app.route("/show_info/<int:id>")
def show_info(id):
    info = users.get_info(id)
    return render_template("show_user.html", info=info)
