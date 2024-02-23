from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text

def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username,password) VALUES (:username,:password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id",0)

def get_info(id):
    sql = text("SELECT U.username, A.age, A.favourite_film FROM users U, user_info A WHERE U.id=:id AND U.id=A.user_id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def add_info(id, age, film):
    try:
        sql = text("INSERT INTO user_info (user_id, age, favourite_film) VALUES (:id, :age, :film)")
        db.session.execute(sql, {"id":id, "age":age, "film":film})
        db.session.commit()
        return True
    except:
        return False

def update_info(id, age, film):
    try:
        sql = text("UPDATE user_info SET age=:age, favourite_film=:film WHERE user_id=:id")
        db.session.execute(sql, {"age":age, "film":film, "id":id})
        db.session.commit()
        return True
    except:
        return False


