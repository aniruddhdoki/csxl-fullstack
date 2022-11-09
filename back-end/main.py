from fastapi import FastAPI
from typing import List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database.settings import Base, engine, get_db
from models import LinkCreate
from database.crud import get_all_links, create_db_link, delete_db_link:

app = FastAPI()

@app.get("/api/health")
def read_root():
    return "Hello World!"

origins = [
  "http://localhost:3000",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"]
  allow_headers=["*"],
)
