from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import db.database as db
import services.job_scraper as job_scraper

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Server!"}

@app.get("/jobs")
async def read_jobs():
    records = db.fetch_all_records()
    return records
