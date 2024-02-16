from db import db
import users
from sqlalchemy.sql import text

def get_list():
    sql = text("SELECT id, name, year, runtime FROM films ORDER BY year")
    result = db.session.execute(sql)
    return result.fetchall()

def get_review(id):
    sql = text("SELECT F.id, F.name, R.review, R.stars, U.username FROM films F, reviews R, users U WHERE F.id=:id AND F.id=R.film_id AND U.id=R.writer_id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_name(id):
    sql = text("SELECT name FROM films WHERE id=:id")
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

