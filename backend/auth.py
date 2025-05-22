from fastapi import HTTPException


def login_user(data: dict):
    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "admin":
        return {"message": "Login successful", "token": "mocked-jwt-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")


def register_user(data: dict):
    username = data.get("username")
    password = data.get("password")
    phone = data.get("phone")

    # Simulate success
    return {
        "message": f"User '{username}' registered successfully",
        "user": {"username": username, "phone": phone, "password": password},
    }
