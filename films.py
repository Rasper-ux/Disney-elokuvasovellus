from db import db
import users
from sqlalchemy.sql import text

def get_list():
    sql = text("SELECT id, name, year, runtime FROM films")
    result = db.session.execute(sql)
    return result.fetchall()

def get_review(id):
    sql = text("SELECT F.id, R.review, U.username FROM films F, reviews R, users U WHERE F.id=:id AND F.id=R.film_id AND U.id=R.writer_id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def add_review(content, id):
    user_id = users.user_id()
    try:
        sql = text("INSERT INTO reviews (film_id, writer_id, review) VALUES (:id, :user_id, :content)")
        db.session.execute(sql, {"id":id, "user_id":user_id, "content":content})
        db.session.commit()
        return True
    
    except:
        return False

