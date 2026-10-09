# ✅ To-Do REST API with JWT Authentication

[![Tests](https://github.com/mihail-serban-udescu/flask-todo-jwt/actions/workflows/test.yml/badge.svg)](https://github.com/mihail-serban-udescu/flask-todo-jwt/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen.svg)](https://flask-todo-jwt.onrender.com)

## 🌐 Live Demo

**URL:** [https://flask-todo-jwt.onrender.com](https://flask-todo-jwt.onrender.com)

**Note:** Hosted on Render free tier — may take ~30 sec to wake up after 15 min of inactivity.
A RESTful API for managing personal tasks, built with Flask and secured with JWT authentication. Each user can only access their own tasks.

## ✨ Features

- 🔐 **JWT Authentication** — register, login, protected routes
- 🔒 **Password hashing** with bcrypt (never store plain passwords)
- ✅ **Full CRUD** for tasks (Create, Read, Update, Delete)
- 👤 **Per-user isolation** — users only see their own tasks
- 🎯 **RESTful endpoints** with proper HTTP status codes
- 📦 **SQLite database** with SQLAlchemy ORM
- 🏗️ **Modular architecture** — Flask Blueprints + Application Factory
- 🌍 **Environment-based config** with python-dotenv
- 🐳 **Dockerized** — Dockerfile + docker-compose
- ✅ **Tested** — 10 Pytest tests
- 🔄 **CI/CD** — GitHub Actions workflow

## 🛠️ Tech Stack

- **Python 3.12+** — developed and tested
- **Flask 3.0** — web framework
- **Flask-SQLAlchemy 3.1** — ORM
- **Flask-JWT-Extended 4.6** — JWT authentication
- **Flask-Bcrypt 1.0** — password hashing
- **SQLite** — database (dev)
- **python-dotenv** — config management
- **Docker** — containerization
- **Pytest** — testing
- **GitHub Actions** — CI/CD

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/mihail-serban-udescu/flask-todo-jwt.git
cd flask-todo-jwt

# Create virtual environment
python -m venv venv

# Activate venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Copy .env.example to .env
copy .env.example .env     # Windows
cp .env.example .env       # Linux/Mac

# Run the server
python run.py
Server runs at http://localhost:5000

🐳 Run with Docker
bash
# Build and run with Docker Compose
docker compose up -d

# View logs
docker compose logs

# Stop
docker compose down
Server runs at http://localhost:5000

🧪 Run Tests
bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run with coverage
pytest --cov=app --cov-report=term-missing
🔌 API Endpoints
🔓 Public (no auth required)
Method	Endpoint	Description
POST	/api/auth/register	Register new user
POST	/api/auth/login	Login and get JWT token
🔒 Protected (JWT required)
Method	Endpoint	Description
GET	/api/auth/me	Get current user info
GET	/api/tasks	List all user's tasks
POST	/api/tasks	Create new task
GET	/api/tasks/<id>	Get specific task
PUT	/api/tasks/<id>	Update task
DELETE	/api/tasks/<id>	Delete task
🚀 Usage Examples
1. Register a new user
bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"pass123"}'
Response:

json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "email": "test@test.com",
    "created_at": "2026-10-06T03:13:28"
  }
}
2. Login and get JWT token
bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"pass123"}'
Response:

json
{
  "message": "Login successful",
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "user": {"id": 1, "email": "test@test.com"}
}
3. Create a task (with token)
bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{"title":"Buy groceries","description":"Milk, eggs, bread"}'
4. List all tasks
bash
curl http://localhost:5000/api/tasks \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
5. Test protected route (401 without token)
bash
curl http://localhost:5000/api/tasks
Response:

json
{"msg": "Missing Authorization Header"}
📁 Project Structure
text
flask-todo-jwt/
├── app/
│   ├── __init__.py           # Application factory
│   ├── extensions.py         # db, jwt, bcrypt instances
│   ├── models.py             # User + Task models
│   ├── auth/
│   │   ├── __init__.py
│   │   └── routes.py         # Register, login, /me
│   └── tasks/
│       ├── __init__.py
│       └── routes.py         # CRUD for tasks
├── tests/
│   ├── __init__.py
│   └── test_api.py           # 10 Pytest tests
├── .github/
│   └── workflows/
│       └── test.yml          # GitHub Actions CI
├── config.py                 # Configuration class
├── run.py                    # Entry point
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
└── .gitignore
🔐 Security Features
✅ Passwords hashed with bcrypt (never stored plaintext)

✅ JWT tokens signed with secret key

✅ Tokens expire after 1 hour

✅ Protected routes require valid token

✅ Per-user data isolation — users can't access others' tasks

✅ Environment variables for secrets (not in git)

🎯 HTTP Status Codes
Code	Meaning
200	OK (successful GET/PUT/DELETE)
201	Created (successful POST)
400	Bad Request (missing fields, invalid data)
401	Unauthorized (missing/invalid token)
404	Not Found (task doesn't exist)
409	Conflict (email already registered)
🎯 Roadmap
☑ Docker support
☑ GitHub Actions CI
□ Deploy to Render/Railway
□ Refresh tokens
□ Password reset via email
□ Task categories/tags
□ Due dates and reminders
□ Pagination for large task lists
📄 License
MIT