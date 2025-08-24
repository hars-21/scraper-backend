import psycopg2
from config import DB_CONN

conn = psycopg2.connect(DB_CONN)

cur = conn.cursor()
cur.execute("Select * from mydata")
records = cur.fetchall()
