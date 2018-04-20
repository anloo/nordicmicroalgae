import mysql.connector
from flask import current_app, g

def get_connection():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host = current_app.config['DB_HOST'],
            db = current_app.config['DB_NAME'],
            user = current_app.config['DB_USER'],
            passwd = current_app.config['DB_PASS'],
            use_unicode = True,
            charset = 'utf8'
        )
    return g.db

def close_connection(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()
