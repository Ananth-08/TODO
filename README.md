# Todo Application Backend

## Project Overview

The Todo Application Backend is developed using FastAPI, SQLAlchemy, and SQLite. The system provides RESTful APIs to manage todo items and supports complete CRUD operations along with filtering functionality.

The project follows a layered architecture to separate API handling, business logic, and data storage.

---

## Features

The application supports the following functionalities:

* Create Todo
* View All Todos
* View Todo by ID
* Update Todo
* Delete Todo
* Filter Todos by Completion Status

---

## Technology Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Docker
* Git & GitHub

---

## Project Structure

```text
todo-app/
│
├── backend/
│   ├── app/
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── main.py
│
├── requirements.txt
├── DockerFile
├── .gitignore
└── todo.db
```

---

## Todo Data Model

The application manages Todo items with the following attributes:

| Field      | Type     |
| ---------- | -------- |
| id         | Integer  |
| title      | String   |
| completed  | Boolean  |
| created_at | DateTime |

---

## System Workflow

```text
Client
  │
  ▼
API Routes (main.py)
  │
  ▼
CRUD Operations (crud.py)
  │
  ▼
Database Models (models.py)
  │
  ▼
SQLite Database (todo.db)
```

---

## Progress Completed

### Project Initialization

* Project structure created
* Virtual environment configured
* Git repository initialized
* Dependencies configured

### Database Layer

* SQLite database configured
* SQLAlchemy setup completed
* Database session management implemented

### Data Layer

* Todo model defined
* Request and response schemas created
* Data validation structure established

### Business Logic Layer

* CRUD operations implemented
* Create Todo functionality completed
* View Todo functionality completed
* Update Todo functionality completed
* Delete Todo functionality completed
* Todo filtering functionality completed

### API Layer

* REST API endpoints implemented
* Request validation integrated
* Error handling implemented

### Development Environment

* Docker configuration added
* Dependency management configured
* GitHub repository configured

---

## API Endpoints

| Method | Endpoint              | Description             |
| ------ | --------------------- | ----------------------- |
| POST   | /todos                | Create a new todo       |
| GET    | /todos                | Retrieve all todos      |
| GET    | /todos/{id}           | Retrieve a todo by ID   |
| PUT    | /todos/{id}           | Update an existing todo |
| DELETE | /todos/{id}           | Delete a todo           |
| GET    | /todos?completed=true | Filter completed todos  |

---

## Current Status

The backend implementation has been completed with support for all planned CRUD operations and filtering functionality. The project is currently ready for testing, integration, and deployment.
