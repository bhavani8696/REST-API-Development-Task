# REST API Development Task

## Project Overview
This is a User Management REST API developed using FastAPI. The project provides user registration, login with JWT authentication, and complete CRUD operations.

## Features
- User Registration
- User Login (JWT Authentication)
- Get All Users
- Get User by ID
- Update User
- Delete User
- Swagger API Documentation
- Postman Collection

## Technologies Used
- FastAPI
- Python
- SQLAlchemy
- SQLite
- JWT Authentication
- Passlib (bcrypt)
- Uvicorn

## Project Structure

```
REST_API_Project/
│── app/
│   ├── main.py
│   ├── routes.py
│   ├── crud.py
│   ├── auth.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│── requirements.txt
│── README.md
```

## Installation

```bash
git clone https://github.com/bhavani8696/REST-API-Development-Task.git
cd REST_API_Project
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Documentation

Swagger UI:

https://rest-api-development-ev8p.onrender.com/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /register | Register User |
| POST | /login | User Login |
| GET | /users | Get All Users |
| GET | /users/{id} | Get User by ID |
| PUT | /users/{id} | Update User |
| DELETE | /users/{id} | Delete User |

## Live Demo

https://rest-api-development-ev8p.onrender.com/docs

## GitHub Repository

https://github.com/bhavani8696/REST-API-Development-Task

## Author

**Pasam Siva Bhavani**
