#!/bin/bash

# Development Environment Setup Script for Sophia

echo "Setting up Sophia development environment..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists, if not create a basic one
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cat > .env << EOF
# Django Settings
SECRET_KEY=your-secret-key-here-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin

# Database Settings
DATABASE_URL=sqlite:///db.sqlite3

# OpenLibrary API Settings
OPENLIBRARY_API_URL=https://openlibrary.org
EOF
    echo "Created .env file. Please update the SECRET_KEY for production."
fi

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Create superuser if it doesn't exist
echo "Creating superuser..."
python manage.py createsuperuser --noinput || echo "Superuser already exists or creation failed"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run tests
echo "Running tests..."
python manage.py test

# Check for common issues
echo "Checking Django configuration..."
python manage.py check

echo ""
echo "Development environment setup complete!"
echo ""
echo "Next steps:"
echo "1. Update the SECRET_KEY in .env file"
echo "2. Run './start-dev.sh' to start the development server"
echo "3. Visit http://127.0.0.1:8001 to access the application"
echo "4. Visit http://127.0.0.1:8001/admin to access the admin interface"
echo ""
echo "Useful commands:"
echo "- python manage.py runserver    # Start development server"
echo "- python manage.py shell        # Open Django shell"
echo "- python manage.py test         # Run tests"
echo "- python manage.py makemigrations # Create migrations"
echo "- python manage.py migrate      # Apply migrations" 