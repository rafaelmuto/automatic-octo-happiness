.PHONY: help install test migrate run clean setup quality docker-build docker-run

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Setup development environment
	@echo "Setting up development environment..."
	@chmod +x scripts/setup-dev.sh
	@./scripts/setup-dev.sh

install: ## Install dependencies
	@echo "Installing dependencies..."
	@source .venv/bin/activate && pip install -r requirements.txt

test: ## Run tests
	@echo "Running tests..."
	@source .venv/bin/activate && python manage.py test

migrate: ## Run migrations
	@echo "Running migrations..."
	@source .venv/bin/activate && python manage.py migrate

makemigrations: ## Create migrations
	@echo "Creating migrations..."
	@source .venv/bin/activate && python manage.py makemigrations

run: ## Run development server
	@echo "Starting development server..."
	@source .venv/bin/activate && python manage.py runserver 8001

shell: ## Open Django shell
	@echo "Opening Django shell..."
	@source .venv/bin/activate && python manage.py shell

collectstatic: ## Collect static files
	@echo "Collecting static files..."
	@source .venv/bin/activate && python manage.py collectstatic --noinput

createsuperuser: ## Create superuser
	@echo "Creating superuser..."
	@source .venv/bin/activate && python manage.py createsuperuser

quality: ## Run code quality checks
	@echo "Running code quality checks..."
	@chmod +x scripts/code-quality.sh
	@./scripts/code-quality.sh

lint: ## Run linter
	@echo "Running linter..."
	@source .venv/bin/activate && ruff check .

format: ## Format code
	@echo "Formatting code..."
	@source .venv/bin/activate && ruff format .

check: ## Check Django configuration
	@echo "Checking Django configuration..."
	@source .venv/bin/activate && python manage.py check

clean: ## Clean up temporary files
	@echo "Cleaning up temporary files..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type d -name ".ruff_cache" -exec rm -rf {} +

docker-build: ## Build Docker image
	@echo "Building Docker image..."
	@docker build . -t sophia_image --no-cache

docker-run: ## Run Docker container
	@echo "Running Docker container..."
	@docker compose up

docker-stop: ## Stop Docker container
	@echo "Stopping Docker container..."
	@docker compose down

full-test: ## Run full test suite with quality checks
	@make quality
	@make test
	@make check

reset-db: ## Reset database (WARNING: This will delete all data)
	@echo "WARNING: This will delete all data in the database!"
	@read -p "Are you sure? [y/N] " -n 1 -r; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		echo "Resetting database..."; \
		source .venv/bin/activate && \
		rm -f db.sqlite3 && \
		python manage.py migrate && \
		python manage.py createsuperuser --noinput; \
	else \
		echo "Database reset cancelled."; \
	fi

backup: ## Create database backup
	@echo "Creating database backup..."
	@cp db.sqlite3 db.sqlite3.backup.$$(date +%Y%m%d_%H%M%S)

restore: ## Restore database from backup
	@echo "Available backups:"
	@ls -la db.sqlite3.backup.* 2>/dev/null || echo "No backups found"
	@echo "To restore, run: cp db.sqlite3.backup.YYYYMMDD_HHMMSS db.sqlite3"

# Task Management Commands
tasks: ## Show current tasks
	@echo "Current Tasks:"
	@echo "=============="
	@head -20 docs/tasks/TODO.md

roadmap: ## Show project roadmap
	@echo "Project Roadmap:"
	@echo "================"
	@head -20 docs/tasks/ROADMAP.md

features: ## Show feature requests
	@echo "Feature Requests:"
	@echo "================="
	@head -20 docs/tasks/FEATURES.md

bugs: ## Show known bugs
	@echo "Known Bugs:"
	@echo "==========="
	@head -20 docs/tasks/BUGS.md
