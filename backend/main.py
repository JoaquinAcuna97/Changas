from auth import login_user, register_user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {
        "message": "Hello from dockerized FastAPI Backend!",
        "title": "Let's do a login form",
    }


@app.post("/login")
def login(data: dict):
    return login_user(data)


@app.post("/register")
def register(data: dict):
    return register_user(data)
