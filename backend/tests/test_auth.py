from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_login_success():
    response = client.post("/login", json={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    assert "token" in response.json()


def test_login_failure():
    response = client.post("/login", json={"username": "user", "password": "wrong"})
    assert response.status_code == 401


def test_register_user():
    payload = {"username": "newuser", "password": "secret", "phone": "123456789"}
    response = client.post("/register", json=payload)
    assert response.status_code == 200
    assert response.json()["user"]["username"] == "newuser"
