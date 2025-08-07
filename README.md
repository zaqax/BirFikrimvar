# Bir Fikrim Var - Python (Django) Version

This is the Python version of "Bir Fikrim Var" project, implemented with Django.

## Project Structure

The project follows a standard Django application structure:

- **accounts**: User authentication and management
- **posts**: Post, comment, and like functionality
- **core**: Common templates, static files, and settings

## Requirements

- Python 3.8+
- Django 4.2+
- PostgreSQL (or SQLite for development)
- Other dependencies listed in requirements.txt

## Getting Started

### 1. Clone the repository

```bash
git clone [repository-url]
cd [repository-folder]/python-version
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up the database

```bash
python manage.py migrate
```

### 4. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

The application should now be running on `http://127.0.0.1:8000/`

## Features

- User registration and authentication
- Create, read, update, and delete posts
- Comment on posts
- Like/unlike posts
- Form validation
- Admin interface for content management

## Technologies Used

- Django 4.2+
- Django ORM for database operations
- Django Forms for form validation
- Django Authentication for user management
- Bootstrap for frontend styling