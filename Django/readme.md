# Django Study Project

A Python and Django study project for learning web development with Django framework.

## Environment Setup

### Virtual Environment Commands

- **Activate VENV**
  ```bash
  source .venv/bin/activate
  ```

- **Deactivate VENV**
  ```bash
  deactivate
  ```

### Dependencies Management

- **Create/update dependencies in requirements.txt**
  ```bash
  pip freeze > requirements.txt
  ```

- **Install requirements from requirements.txt**
  ```bash
  pip install -r requirements.txt
  ```

## Django Development

### Starting the Server

- **Start the Django development server**
  ```bash
  python manage.py runserver
  ```
  The server will run on http://127.0.0.1:8000/

### Database Management

- **Apply initial migrations**
  ```bash
  python manage.py migrate
  ```

- **Create a superuser for admin access**
  ```bash
  python manage.py createsuperuser
  ```

### Development Commands

- **Check for any issues**
  ```bash
  python manage.py check
  ```

- **Create migrations for model changes**
  ```bash
  python manage.py makemigrations
  ```

- **Apply migrations to database**
  ```bash
  python manage.py migrate
  ```

- **Start interactive shell**
  ```bash
  python manage.py shell
  ```

- **Collect static files (for production)**
  ```bash
  python manage.py collectstatic
  ```

## Getting Started

1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
6. Start development server: `python manage.py runserver`
7. Visit http://127.0.0.1:8000/ in your browser

## Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)