import psycopg2
from config import Config

def conectar():

    conn = psycopg2.connect(host=Config.host, database=Config.dbname, user=Config.user, password=Config.password, port=Config.port)

    if conn:
        return conn
    else:
        return None

