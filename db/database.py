import psycopg2
from config import DB_CONN
import json

def get_db_connection():
    conn = psycopg2.connect(DB_CONN)
    return conn

def jobs_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS jobs (id SERIAL PRIMARY KEY, epoch INTEGER, date TIMESTAMP, company TEXT, position TEXT, description TEXT, location TEXT, salary_min INTEGER, salary_max INTEGER, apply_url TEXT, url TEXT)")
    conn.commit()
    cur.close()
    conn.close()

def insert_record(data):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO jobs (epoch, date, company, position, description, location, salary_min, salary_max, apply_url, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data['epoch'], data['date'], data['company'], data['position'], data['description'], data['location'], data['salary_min'], data['salary_max'], data['apply_url'], data['url']))
    conn.commit()
    cur.close()
    conn.close()

def fetch_all_records():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM jobs")
    records = cur.fetchall()
    json_records = []
    for record in records:
        json_record = {
            "id": record[0],
            "epoch": record[1],
            "date": record[2],
            "company": record[3],
            "position": record[4],
            "description": record[5],
            "location": record[6],
            "salary_min": record[7],
            "salary_max": record[8],
            "apply_url": record[9],
            "url": record[10]
        }
        json_records.append(json_record)

    cur.close()
    conn.close()
    return json_records