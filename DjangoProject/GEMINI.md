# GEMINI.md

This file provides context for the Gemini agent to understand and work with this project.

## Project Overview

*   **Project Name:** sohia
*   **Description:** (A brief, one-sentence description of the project)
*   **Python Version:** 3.10.12
*   **Web Framework:** Django 5.2.4
*   **Database:** SQLite

Sophia is a project to help manage private libraries. Helping you to categorise and find books, magazines and documents, known as Entries.
You can register entries with all relavant metadata to help you categorise and find what you are looking for.
Also you may register quotes and passages from the entries.

Sophia is meant to run in small single board computers (SBC), like Raspberry Pi, and will have a hardware interface with leds built in the bookshelves to help you locate the entry you are looking for. In the future we may add RF tags and suport for barcode.

The main way you can interact with Sophia is through the web interface, running in the local network. There you can register new entries and the relevant data like title, author, year of publication, ISBN, image ant etc.

    Sophia is the Greek word for "wisdom." It's a simple, beautiful, and direct name that gets straight to the core purpose of a library.

## Getting Started

### Prerequisites

*   List any software or tools that need to be installed before setting up the project (e.g., Python, pip, virtualenv, Docker).

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up environment variables:**
    *   Copy the `.env.example` file to `.env` and fill in the required values.
5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

### Running the Development Server

*   Provide the command to start the local development server.
    ```bash
    python manage.py runserver
    ```

## Development Guidelines

### Coding Style

*   **Linter:** (e.g., Ruff, Flake8, Pylint)
*   **Formatter:** (e.g., Black, isort)
*   **Command to run linter/formatter:**
    ```bash
    # Example
    ruff check .
    black .
    ```

### Testing

*   **Testing Framework:** (e.g., pytest, unittest)
*   **How to run tests:**
    ```bash
    # Example
    pytest
    ```
*   **Location of tests:** (e.g., `tests/` directory, alongside the code)

### Project Structure

*   Briefly describe the purpose of the main directories and files.
    *   `myproject/`: Contains the main Django project settings.
    *   `app/`: A sample Django app.
    *   `static/`: For static files (CSS, JavaScript, images).
    *   `templates/`: For Django templates.
    *   `manage.py`: Django's command-line utility.

## Deployment

*   Instructions on how to deploy the application to a staging or production environment.
*   Mention the hosting platform (e.g., Heroku, AWS, Vercel) and any specific configurations.

## Important Commands

*   List any other useful commands for managing the project.
    *   `python manage.py makemigrations`: To create new database migrations.
    *   `python manage.py shell`: To open the Django shell.
