from app import app
from flask import render_template, request, redirect
from flask import session
import films, users

@app.route("/")
def index():
    list = films.get_list(0)
    return render_template("index.html", movies=list, film="")

@app.route("/order/<int:number>")
def order(number):
    list = films.get_list(number)
    return render_template("index.html", movies=list)

@app.route("/search", methods=["GET"])
def search():
    query = request.args["query"]
    film = films.search(query)
    return render_template("index.html", movies=film, film=query)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", error=False, username="", password="")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if session["csrf_token"] != request.form["csrf_token"]:
            return render_template("login.html", error=True, message="Kirjautuminen ei onnistu", username=username, password=password)    
        if len(username)==0 or len(password)==0:
            return render_template("login.html", error=True, message="Täytä kaikki kentät", username=username, password=password)
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("login.html", error=True, message="Väärä käyttäjätunnus tai salasana", username=username, password=password)


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", error=False, username="", password1="", password2="")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if session["csrf_token"] != request.form["csrf_token"]:
            return render_template("register.html", error=True, message="Rekisteröityminen ei onnistu", username=username, password1=password1, password2=password2)
        if len(username)==0 or len(password1)==0 or len(password2)==0:
            return render_template("register.html", error=True, message="Täytä kaikki kentät", username=username, password1=password1, password2=password2)
        if password1 != password2:
            return render_template("register.html", error=True, message="Salasanat poikkeavat", username=username, password1=password1, password2=password2)
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("register.html", error=True, message="Käyttäjätunnus on jo käytössä", username=username, password1=password1, password2=password2)

@app.route("/film/<int:id>")
def film(id):
    list=films.get_review(id)
    name=films.get_name(id)
    alikes=films.get_alikes(id)
    return render_template("film.html", reviews=list, id=id, name=name[0][0], alikes=alikes, error=False, content="")

@app.route("/send/<int:id>", methods=["POST"])
def send(id):
    list=films.get_review(id)
    name=films.get_name(id)
    alikes=films.get_alikes(id)
    content = request.form["content"]
    stars = request.form["stars"]
    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("film.html", reviews=list, id=id, name=name[0][0], alikes=alikes, error=True, message="Arvostelun lähetys ei onnistu", content=content)
    if len(content)==0 or len(stars)==0:
        return render_template("film.html", reviews=list, id=id, name=name[0][0], alikes=alikes, error=True, message="Valitse tähdet ja kirjoita arvostelu", content=content)
    if len(content)>100:
        return render_template("film.html", reviews=list, id=id, name=name[0][0], alikes=alikes, error=True, message="Arvostelu oli liian pitkä, max 100 merkkiä sallittu", content=content)
    if films.add_review(content, int(stars), id):
        return redirect("/")
    else:
        return render_template("film.html", reviews=list, id=id, name=name[0][0], alikes=alikes, error=True, message="Arvostelun lähetys ei onnistunut", content=content)

@app.route("/user")
def user():
    user_id = users.user_id()
    if user_id == 0:
        return False
    info = users.get_info(user_id)
    if len(info)==0:
        return render_template("user.html", id=user_id, info=False, age="", content="")
    else:
        return render_template("user.html", id=user_id, info=info, age="", content="") 

@app.route("/info/<int:id>", methods=["POST"])
def add_info(id):
    age=request.form["age"]
    content=request.form["content"]
    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("user.html", id=id, info=False, message="Lähetys ei onnistu", age=age, content=content)
    if len(content)==0 or len(age)==0:
        return render_template("user.html", id=id, info=False, message="Täytä molemmat kentät", age=age, content=content)
    if len(content)>121:
        return render_template("user.html", id=id, info=False, message="Elokuvan nimi ei voi olla noin pitkä", age=age, content=content)
    try:
        age2=int(age)
    except:
        return render_template("user.html", id=id, info=False, message="Anna ikä numerona", age=age, content=content)
    if int(age)<0 or int(age)>120:
        return render_template("user.html", id=id, info=False, message="Kirjoita oikea ikäsi", age=age, content=content)
    if users.add_info(id, age2, content):
        info = users.get_info(id)
        return render_template("user.html", id=id, info=info, age="", content="")
    else:
        return render_template("user.html", id=id, info=False, message="Lähetys epäonnistui", age=age, content=content)

@app.route("/update_info/<int:id>")
def update_info(id):
    return render_template("update_info.html", id=id, error=False, age="", content="")

@app.route("/send_update/<int:id>", methods=["POST"])
def send_update(id):
    age=request.form["age"]
    content=request.form["content"]
    if session["csrf_token"] != request.form["csrf_token"]:
        return render_template("update_info.html", id=id, error=True, message="Päivitys ei onnistu", age=age, content=content)
    if len(content)==0 or len(age)==0:
        return render_template("update_info.html", id=id, error=True, message="Täytä molemmat kentät", age=age, content=content)
    if len(content)>121:
        return render_template("update_info.html", id=id, error=True, message="Elokuvan nimi ei voi olla noin pitkä", age=age, content=content)
    try:
        age2=int(age)
    except:
        return render_template("update_info.html", id=id, error=True, message="Anna ikä numerona", age=age, content=content)
    if int(age)<0 or int(age)>120:
        return render_template("update_info.html", id=id, error=True, message="Kirjoita oikea ikäsi", age=age, content=content)
    if users.update_info(id, age2, content):
        info = users.get_info(id)
        return render_template("user.html", id=id, info=info, age="", content="")
    else:
        return render_template("update_info.html", id=id, error=True, message="Päivitys epäonnistui", age=age, content=content)

@app.route("/show_info/<int:id>")
def show_info(id):
    info = users.get_info(id)
    return render_template("show_user.html", info=info)
