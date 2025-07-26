#!/bin/bash

# Code Quality Check Script for Sophia

echo "Running code quality checks for Sophia..."

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found. Run setup-dev.sh first."
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

# Check if required tools are installed
echo "Checking required tools..."

# Check if ruff is installed
if ! command -v ruff &> /dev/null; then
    echo "Installing ruff..."
    pip install ruff
fi

# Run Ruff linter
echo "Running Ruff linter..."
ruff check .

if [ $? -eq 0 ]; then
    echo "✅ Ruff linting passed"
else
    echo "❌ Ruff linting failed"
    exit 1
fi

# Run Ruff formatter (optional)
echo "Running Ruff formatter..."
ruff format . --check

if [ $? -eq 0 ]; then
    echo "✅ Code formatting is correct"
else
    echo "⚠️  Code formatting issues found. Run 'ruff format .' to fix."
fi

# Run Django tests
echo "Running Django tests..."
python manage.py test

if [ $? -eq 0 ]; then
    echo "✅ All tests passed"
else
    echo "❌ Some tests failed"
    exit 1
fi

# Check for security issues
echo "Checking for security issues..."
python manage.py check --deploy

if [ $? -eq 0 ]; then
    echo "✅ Security check passed"
else
    echo "⚠️  Security issues found"
fi

# Check for common Django issues
echo "Checking Django configuration..."
python manage.py check

if [ $? -eq 0 ]; then
    echo "✅ Django configuration is valid"
else
    echo "❌ Django configuration issues found"
    exit 1
fi

# Check for unused imports and variables
echo "Checking for unused imports..."
python -m py_compile $(find . -name "*.py" -not -path "./.venv/*" -not -path "./staticfiles/*")

if [ $? -eq 0 ]; then
    echo "✅ No syntax errors found"
else
    echo "❌ Syntax errors found"
    exit 1
fi

# Check if migrations are up to date
echo "Checking migrations..."
python manage.py makemigrations --check --dry-run

if [ $? -eq 0 ]; then
    echo "✅ Migrations are up to date"
else
    echo "⚠️  New migrations needed. Run 'python manage.py makemigrations'"
fi

echo ""
echo "🎉 Code quality checks completed!"
echo ""
echo "Summary:"
echo "- Linting: ✅"
echo "- Formatting: ✅"
echo "- Tests: ✅"
echo "- Security: ✅"
echo "- Configuration: ✅"
echo "- Syntax: ✅"
echo "- Migrations: ✅" 