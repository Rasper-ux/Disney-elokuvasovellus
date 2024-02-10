from db import db
import users
from sqlalchemy.sql import text

def get_list():
    sql = text("SELECT id, name, year, runtime FROM films")
    result = db.session.execute(sql)
    return result.fetchall()

def get_review(id):
    sql = text("SELECT * FROM films WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()
