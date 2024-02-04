from db import db
import users
from sqlalchemy.sql import text

def get_list():
    sql = text("SELECT name, year, runtime FROM films")
    result = db.session.execute(sql)
    return result.fetchall()
