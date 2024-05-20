# task-management-api
a simple task management api 

This is a simple RESTful API built with FastAPI for task management. It allows you to perform basic CRUD (Create, Read, Update, Delete) operations on a collection of books stored in a database.

## Note
must have python installed if not fellow the guide [https://realpython.com/installing-python/]

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/martcpp/task-management-api.git
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   cd app
   ```

3. **Run the application:**

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

## using docker
1. **Clone the repository:**

   ```bash
   git clone https://github.com/martcpp/task-management-api.git
   ```
   ```bash
   cd task-management-api
   ```

2. **Run the application:**

   ```bash
   docker-compose build .
   docker up
   ```

   The API will be available at `http://localhost:8000`

## Endpoints
`http://localhost:8000/docs` for more information about  the API documentation


## Dependencies

- FastAPI: Web framework for building APIs with Python.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- uvicorn: ASGI server for running FastAPI applications.
- postgreSQL: MySQL server for running FastAPI applications with MySQL support enabled
- psycopg2-binary : for connecting to to postgresql databases
