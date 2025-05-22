from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from auth import login_user, register_user

app = FastAPI()

# CORS setup
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
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
    return {"message": "Hello from dockerized FastAPI Backend!", "title": "Let's do a login form"}

@app.post("/login")
def login(data: dict):
    return login_user(data)

@app.post("/register")
def register(data: dict):
    return register_user(data)
