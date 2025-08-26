import requests
import pandas as pd
import db.database as db

def store_jobs(jobs):
    data = jobs[1:]
    df = pd.DataFrame(data)
    for _, row in df.iterrows():
        db.insert_record(row)
    return {"message": "Jobs stored successfully!"}

def fetch_jobs():
    try:
        response = requests.get("https://remoteok.com/api")
        response.raise_for_status()
        jobsData = response.json()
        store_jobs(jobsData)
        return jobsData
    except requests.RequestException as e:
        print(f"Error: {e}")
        return {"error": str(e)}