from flaskext.mysql import MySQL
from quora_app import db,login_manager
from flask_login import
#f = open("quora_app/schema.sql","r")


@login_manager.user_loader
def load_user(user_id):
    conn = db.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * FROM user WHERE email = (%s)",(email))
    user = cursor.fetchone()
    return user

def init_db(app):
    mysql = MySQL(app)

    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'aman'
    app.config['MYSQL_DATABASE_DB'] = 'quora'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    #mysql.init_app()
    conn = mysql.connect()
    cursor =conn.cursor()
    """cursor.execute("DROP TABLE IF EXISTS user")
    sqlCommands = f.read().split(';')

    for command in sqlCommands:
        try:
            cursor.execute(command)
        except :
            print("Skipped: ",command)"""
    #conn.commit()
    return conn,cursor
