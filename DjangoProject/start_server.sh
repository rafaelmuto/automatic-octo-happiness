#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Run Django migrations
python manage.py migrate

# Run collectstatic
# python manage.py collectstatic --noinput

# Run the development server
python manage.py runserver 8001
