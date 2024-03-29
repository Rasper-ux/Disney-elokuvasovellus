from db import db
import users
from sqlalchemy.sql import text

def get_list(order):
    if order==0:
        sql = text("SELECT id, name, year, runtime FROM films ORDER BY year")
    if order==1:
        sql = text("SELECT id, name, year, runtime FROM films ORDER BY year DESC")
    if order==2:
        sql = text("SELECT F.id, F.name, F.year, F.runtime, AVG(R.stars) FROM films F, reviews R WHERE F.id=R.film_id GROUP BY F.id ORDER BY AVG(R.stars) DESC")
    if order==3:
        sql = text("SELECT id, name, year, runtime FROM films ORDER BY runtime")
    result = db.session.execute(sql)
    return result.fetchall()

def get_review(id):
    sql = text("SELECT F.id, F.name, R.review, R.stars, U.username, U.id FROM films F, reviews R, users U WHERE F.id=:id AND F.id=R.film_id AND U.id=R.writer_id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_name(id):
    sql = text("SELECT name FROM films WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_alikes(id):
    sql = text("SELECT F.name FROM alike A, films F WHERE A.film1_id=:id AND A.film2_id=F.id;")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def add_review(content, stars, id):
    user_id = users.user_id()
    try:
        sql = text("INSERT INTO reviews (film_id, writer_id, review, stars) VALUES (:id, :user_id, :content, :stars)")
        db.session.execute(sql, {"id":id, "user_id":user_id, "content":content, "stars":stars})
        db.session.commit()
        return True
    
    except:
        return False

def search(query):
    sql = text("SELECT id, name, year, runtime FROM films WHERE name LIKE :query")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    return result.fetchall()
