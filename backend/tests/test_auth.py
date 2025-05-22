from fastapi.testclient import TestClient
import main as app

client = TestClient(app)
user ={"username": "admin", "password": "admin"}

def test_login_success():
    response = client.post("/login", json=user)
    assert response.status_code == 200
    assert "token" in response.json()

def test_login_failure():
    response = client.post("/login", json=user)
    assert response.status_code == 401

def test_register_user():
    payload = {"username": "newuser", "password": "secret", "phone": "123456789"}
    response = client.post("/register", json=payload)
    assert response.status_code == 200
    assert response.json()["user"]["username"] == "newuser"
    
