import pytest
from app import create_app
from app.extensions import db


@pytest.fixture
def app():
    """Creează o instanță Flask pentru testare."""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    """Client HTTP pentru testare."""
    return app.test_client()


def test_home_returns_404(client):
    """Ruta / nu există."""
    response = client.get("/")
    assert response.status_code == 404


def test_register_success(client):
    """Înregistrare user nou."""
    response = client.post(
        "/api/auth/register",
        json={"email": "test@test.com", "password": "pass123"},
    )
    assert response.status_code == 201
    assert response.json["message"] == "User registered successfully"
    assert response.json["user"]["email"] == "test@test.com"


def test_register_missing_fields(client):
    """Înregistrare fără email/parolă."""
    response = client.post("/api/auth/register", json={})
    assert response.status_code == 400


def test_register_short_password(client):
    """Parolă prea scurtă."""
    response = client.post(
        "/api/auth/register",
        json={"email": "test@test.com", "password": "123"},
    )
    assert response.status_code == 400


def test_register_duplicate_email(client):
    """Email deja înregistrat."""
    data = {"email": "test@test.com", "password": "pass123"}
    client.post("/api/auth/register", json=data)
    response = client.post("/api/auth/register", json=data)
    assert response.status_code == 409


def test_login_success(client):
    """Login cu credențiale corecte."""
    client.post(
        "/api/auth/register",
        json={"email": "test@test.com", "password": "pass123"},
    )
    response = client.post(
        "/api/auth/login",
        json={"email": "test@test.com", "password": "pass123"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json


def test_login_wrong_password(client):
    """Login cu parolă greșită."""
    client.post(
        "/api/auth/register",
        json={"email": "test@test.com", "password": "pass123"},
    )
    response = client.post(
        "/api/auth/login",
        json={"email": "test@test.com", "password": "wrong"},
    )
    assert response.status_code == 401


def test_tasks_requires_auth(client):
    """Ruta /api/tasks necesită token."""
    response = client.get("/api/tasks")
    assert response.status_code == 401


def test_create_task_success(client):
    """Creează un task cu token valid."""
    client.post(
        "/api/auth/register",
        json={"email": "test@test.com", "password": "pass123"},
    )
    login = client.post(
        "/api/auth/login",
        json={"email": "test@test.com", "password": "pass123"},
    )
    token = login.json["access_token"]

    response = client.post(
        "/api/tasks",
        json={"title": "Test task", "description": "Test description"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201
    assert response.json["title"] == "Test task"


def test_list_tasks_empty(client):
    """Listă goală după login."""
    client.post(
        "/api/auth/register",
        json={"email": "test@test.com", "password": "pass123"},
    )
    login = client.post(
        "/api/auth/login",
        json={"email": "test@test.com", "password": "pass123"},
    )
    token = login.json["access_token"]

    response = client.get(
        "/api/tasks",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.json == []