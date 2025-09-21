# Sophia Project Automation Guide

This document explains how to use the automation tools and Cursor Rules setup for the Sophia Django project.

## 🚀 Quick Start

### 1. Setup Development Environment

```bash
# Run the automated setup script
./scripts/setup-dev.sh

# Or use make
make setup
```

### 2. Start Development

```bash
# Start the development server
python manage.py runserver

# Or use make
make run
```

### 3. Run Code Quality Checks

```bash
# Run all quality checks
./scripts/code-quality.sh

# Or use make
make quality
```

## 📁 Automation Structure

```
.cursor/
├── rules/                    # Cursor Rules for consistent development
│   ├── project-structure.mdc # Project overview and structure
│   ├── development-workflow.mdc # Code quality standards
│   ├── api-development.mdc   # API development standards
│   └── database-rules.mdc    # Database design rules
├── instructions/             # Step-by-step guides
│   ├── new-feature.mdc      # New feature development
│   ├── api-endpoint.mdc     # API endpoint creation
│   └── model-creation.mdc   # Django model creation
├── templates/               # Templates for common tasks
│   ├── feature-request.md   # Feature request template
│   └── bug-report.md        # Bug report template
├── snippets/                # Custom code snippets
│   └── django-snippets.json # Django development snippets
└── automation-hub.mdc       # Central automation hub

scripts/
├── setup-dev.sh             # Development environment setup
├── start-dev.sh             # Development environment start
└── code-quality.sh          # Code quality checks

Makefile                     # Common development tasks
```

## 🛠️ Available Commands

### Development Setup

- `make setup` - Setup development environment
- `make install` - Install dependencies
- `make dev` - Setup and start development server

### Database Operations

- `make migrate` - Run migrations
- `make makemigrations` - Create migrations
- `make createsuperuser` - Create admin user
- `make collectstatic` - Collect static files

### Testing & Quality

- `make test` - Run tests
- `make quality` - Run code quality checks
- `make lint` - Run linter
- `make format` - Format code
- `make check` - Check Django configuration

### Docker Operations

- `make docker-build` - Build Docker image
- `make docker-run` - Run Docker container
- `make docker-stop` - Stop Docker container

### Maintenance

- `make clean` - Clean temporary files
- `make backup` - Create database backup
- `make reset-db` - Reset database (WARNING: deletes all data)

## 📋 Using Cursor Rules

### Rules Files

The `.cursor/rules/` directory contains rules that are automatically applied when working in Cursor:

1. **project-structure.mdc** - Project overview and structure guidelines
2. **development-workflow.mdc** - Code quality and Django best practices
3. **api-development.mdc** - REST API development standards
4. **database-rules.mdc** - Database design and optimization rules

### Instruction Files

The `.cursor/instructions/` directory contains step-by-step guides:

1. **new-feature.mdc** - Complete guide for developing new features
2. **api-endpoint.mdc** - Guide for creating API endpoints
3. **model-creation.mdc** - Guide for creating Django models

### Templates

The `.cursor/templates/` directory contains templates for common tasks:

1. **feature-request.md** - Template for feature requests
2. **bug-report.md** - Template for bug reports

## 🎯 Common Workflows

### Creating a New Feature

1. Use the `@new-feature` instruction
2. Follow the step-by-step guide
3. Use `@new-model` for database changes
4. Use `@new-api` for API endpoints
5. Run `make quality` to check your work

### Adding a New Model

1. Use the `@new-model` instruction
2. Create the model following the template
3. Add to admin.py
4. Create and run migrations
5. Update forms and serializers
6. Write tests

### Creating API Endpoints

1. Use the `@new-api` instruction
2. Create serializer
3. Create API views
4. Add URL patterns
5. Write tests

## 🔧 Code Snippets

The `.cursor/snippets/django-snippets.json` file contains custom code snippets:

- `django-model` - Create a new Django model
- `django-view` - Create a new Django view
- `django-form` - Create a new Django form
- `django-serializer` - Create a new DRF serializer
- `django-api-view` - Create new API views
- `django-test` - Create a new test case
- `django-admin` - Create admin configuration
- `django-url` - Create URL patterns

## 🚨 Troubleshooting

### Common Issues

**Virtual environment not found**

```bash
make setup
```

**Migration errors**

```bash
make makemigrations
make migrate
```

**Import errors**

```bash
source .venv/bin/activate
```

**Test failures**

```bash
make test
# Check test output for specific errors
```

### Getting Help

1. Use the instruction files for step-by-step guides
2. Follow the rules files for best practices
3. Run code quality checks to identify issues

## 📚 Best Practices

### Code Organization

- Follow Django's MVT pattern
- Keep related functionality together
- Use appropriate app structure
- Separate concerns (models, views, services)

### Testing

- Write tests for all new functionality
- Use Django's TestCase for database tests
- Mock external API calls
- Aim for high code coverage

### Documentation

- Document API endpoints
- Keep README current
- Comment complex logic

### Git Workflow

- Use descriptive commit messages
- Create feature branches
- Test before committing
- Update requirements.txt when needed

## 🔄 Daily Development Workflow

1. **Start Development**

   ```bash
   make dev
   ```

2. **During Development**

   ```bash
   # Make changes to code
   # Run tests after significant changes
   make test
   ```

3. **Before Committing**

   ```bash
   # Run quality checks
   make quality

   # Ensure all tests pass
   make test
   ```

4. **After Pulling Changes**

   ```bash
   # Install new dependencies
   make install

   # Run migrations
   make migrate

   # Run tests
   make test
   ```

## 🎉 Success!

You now have a fully automated development environment for the Sophia project!

- Use `make help` to see all available commands
- Follow the instruction files for step-by-step guidance
- Use the code snippets to speed up development
- Run quality checks regularly to maintain code standards

Happy coding! 🚀
