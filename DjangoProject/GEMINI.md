# GEMINI.md

This file provides context for the Gemini agent to understand and work with this project.
You should respond as being a senior software developer with experience in Python and Django.
You will always obeserve the best practices and recomendations for code and archytecture.

## Project Overview

*   **Project Name:** sohia
*   **Description:** Sophia is a project to help manage private libraries.
*   **Python Version:** 3.10.12
*   **Web Framework:** Django 5.2.4
*   **Database:** SQLite

Sophia is a project to help manage private libraries. Helping you to categorise and find books, magazines and documents, known as Entries.
You can register entries with all relavant metadata to help you categorise and find what you are looking for.
Also you may register quotes and passages from the entries.

Sophia is meant to run in small single board computers (SBC), like Raspberry Pi, and will have a hardware interface with leds built in the bookshelves to help you locate the entry you are looking for. In the future we may add RF tags and suport for barcode.

The main way you can interact with Sophia is through the web interface, running in the local network. There you can register new entries and the relevant data like title, author, year of publication, ISBN, image ant etc.

    Sophia is the Greek word for "wisdom." It's a simple, beautiful, and direct name that gets straight to the core purpose of a library.

## API Endpoints

*   `api/library/books/`:
    *   **GET**: Returns a list of all books.
    *   **POST**: Creates a new book.
        *   **Payload Example**:
            ```json
            {
                "title": "The Hitchhiker's Guide to the Galaxy",
                "author": 1, // Author ID
                "published_date": "1979-10-12",
                "number_of_pages": 123,
                "isbn": "9780345391803"
            }
            ```
*   `api/library/books/<isbn>/`:
    *   **GET**: Returns a single book by ISBN.
    *   **PUT**: Updates an existing book by ISBN. (Requires full payload)
    *   **PATCH**: Partially updates an existing book by ISBN. (Allows partial payload)
    *   **DELETE**: Deletes a single book by ISBN.
*   `api/library/books/author/<int:author_id>`:
    *   **GET**: Returns a list of books by the author.

*   `api/library/authors/`:
    *   **GET**: Returns a list of all authors.
    *   **POST**: Creates a new author.
        *   **Payload Example**:
            ```json
            {
                "name": "Douglas Adams",
                "birth_date": "1952-03-11",
                "death_date": "2000-01-01",
                "country": "USA"
            }
            ```
*   `api/library/authors/<id>/`:
    *   **GET**: Returns a single author by ID.
    *   **PUT**: Updates an existing author by ID. (Requires full payload)
    *   **PATCH**: Partially updates an existing author by ID. (Allows partial payload)
    *   **DELETE**: Deletes a single author by ID.
*   `api/library/authors/books/<id>/`:
    *   **GET**: Returns a single author by ID with a list of books by the author.

*   `api/library/openlibrary/isbn/<isbn>/`:
    *   **GET**: Searches for a book by ISBN on OpenLibrary and returns its data.
*   `api/library/openlibrary/key/<key>/`:
    *   **GET**: Retrieves data from OpenLibrary using an OpenLibrary key (OLID).



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
    python -m venv .venv
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

### Docker

*   Building dockerimage
    ```bash
    docker build . -t sophia_image --no-cache
    ```
*   Runing application
    ```bash
    docker compose up
    ```

## Development Guidelines

### Coding Style

*   **Linter:** Ruff
<!-- *   **Formatter:** Black -->
*   **Command to run linter/formatter:**
    ```bash
    # Example
    ruff check .
    <!-- black . -->
    ```

### Testing

*   **Testing Framework:** (unittest)
*   **How to run tests:**
    ```bash
    python manage.py test
    ```
*   **Location of tests:** `tests.py`

### Project Structure

*   Briefly describe the purpose of the main directories and files.
    *   `sophia/`: Contains the main Django project settings.
    *   `library/`: main django app domain.
    *   `library/templates/library`: For Django templates.
    *   `library/models`: library models
    *   `library/migrations`: library migration files
    *   `manage.py`: Django's command-line utility.

## Deployment

*   Instructions on how to deploy the application to a staging or production environment.
*   Mention the hosting platform (e.g., Heroku, AWS, Vercel) and any specific configurations.

## Important Commands

*   List any other useful commands for managing the project.
    *   `python manage.py makemigrations`: To create new database migrations.
    *   `python manage.py migrate`: Run all migrations.
    *   `python manage.py collectstatic`: Collect static files
    *   `python manage.py shell`: To open the Django shell.
    *   `python manage.py test`: Run all unit tests.

# Tasks

## 1. API Implementation [DONE]

**Step 1: Install and Configure DRF**

*   **Install:** `pip install djangorestframework`
*   **Configure:** Add `'rest_framework'` to your `INSTALLED_APPS` in `sophia/settings.py`.

**Step 2: Create a Serializer**

*   **File:** `library/serializers.py`
*   **Code:**
    ```python
    from rest_framework import serializers
    from .models import Book, Author

    class AuthorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Author
            fields = ['id', 'name', 'birth_date']

    class BookSerializer(serializers.ModelSerializer):
        author = AuthorSerializer(read_only=True)

        class Meta:
            model = Book
            fields = ['id', 'title', 'author', 'published_date', 'isbn']
    ```

**Step 3: Create an API View**

*   **File:** `library/api.py`
*   **Code:**
    ```python
    from rest_framework import generics
    from .models import Book
    from .serializers import BookSerializer

    class BookListAPIView(generics.ListAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
    ```

**Step 4: Define API URLs**

*   **Create a new file:** `library/api_urls.py`
*   **Code:**
    ```python
    from django.urls import path
    from . import api

    urlpatterns = [
        path('books/', api.BookListAPIView.as_as_view(), name='book-list'),
    ]
    ```

**Step 5: Include API URLs in the Main Project**

*   **File:** `sophia/urls.py`
*   **Modification:**
    ```python
    # In sophia/urls.py

    urlpatterns = [
        # ... existing urls
        path('api/library/', include('library.api_urls')), # Add this line
    ]
    ```

## 2. Implement .env for Configurations [DONE]

**Step 1: Install `python-dotenv`**

*   **Install:** `pip install python-dotenv`

**Step 2: Configure Django to load environment variables**

*   Open `sophia/settings.py`.
*   Add the following lines at the very top of the file to load the `.env` file:
    ```python
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    load_dotenv() # This loads the environment variables from .env
    ```
*   Replace hardcoded sensitive values (e.g., `SECRET_KEY`, database credentials) with `os.getenv()` calls. For example:
    ```python
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key-for-development')
    ```

**Step 3: Create a `.env` file**

*   Create a new file named `.env` in the project root directory (where `manage.py` is located).
*   Add your key-value pairs to this file, e.g.:
    ```
    SECRET_KEY=your_actual_secret_key_here
    DATABASE_NAME=mydatabase
    DATABASE_USER=myuser
    DATABASE_PASSWORD=mypassword
    ```

**Step 4: Update `.gitignore`**

*   Add `.env` to your `.gitignore` file to prevent it from being committed to version control.
    ```
    # .gitignore
    .env
    ```

## 3. Implementing OpenLibraryService [REJECTED]

**Step 1: Install the `requests` library**

*   **Install:** `pip install requests`
*   **Update:** Add `requests` to your `requirements.txt`.

**Step 2: Create the Service Class File**

*   **File:** `library/services.py`
*   **Code:**
    ```python
    import requests
    import os

    class OpenLibraryService:
        BASE_URL = "https://openlibrary.org"

        @staticmethod
        def search_books(query):
            # Example: Search by title
            # https://openlibrary.org/search.json?q=the+lord+of+the+rings
            endpoint = f"{OpenLibraryService.BASE_URL}/search.json"
            params = {"q": query}
            try:
                response = requests.get(endpoint, params=params)
                response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data from OpenLibrary: {e}")
                return None

        @staticmethod
        def get_book_details(olid):
            # Example: Get details by OLID
            # https://openlibrary.org/books/OL7353617M.json
            endpoint = f"{OpenLibraryService.BASE_URL}/books/{olid}.json"
            try:
                response = requests.get(endpoint)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error fetching book details from OpenLibrary: {e}")
                return None
    ```

**Step 3: Integrate the Service (Example in a View)**

*   **File:** `library/views.py` (or a new view if preferred)
*   **Modification Example:**
    ```python
    # In library/views.py
    from django.shortcuts import render
    from .services import OpenLibraryService

    def search_openlibrary_view(request):
        query = request.GET.get('q')
        books_data = None
        if query:
            books_data = OpenLibraryService.search_books(query)
        return render(request, 'library/openlibrary_search_results.html', {'books_data': books_data, 'query': query})
    ```

**Step 4: Create a Template for Display (Example)**

*   **File:** `library/templates/library/openlibrary_search_results.html`
*   **Code Example:**
    ```html
    <!-- library/templates/library/openlibrary_search_results.html -->
    <h1>OpenLibrary Search Results</h1>
    <form method="GET" action="">
        <input type="text" name="q" value="{{ query|default_if_none:'' }}" placeholder="Search books...">
        <button type="submit">Search</button>
    </form>

    {% if books_data %}
        <h2>Results for "{{ query }}"</h2>
        <ul>
            {% for doc in books_data.docs %}
                <li>
                    <strong>{{ doc.title }}</strong> by {{ doc.author_name|join:", " }} ({{ doc.first_publish_year }})
                    {% if doc.isbn and doc.isbn.0 %}
                        <br>ISBN: {{ doc.isbn.0 }}
                    {% endif %}
                </li>
            {% empty %}
                <li>No books found.</li>
            {% endfor %}
        </ul>
    {% elif query %}
        <p>No books found for "{{ query }}".</p>
    {% endif %}
    ```

**Step 5: Add URL for the View (Example)**

*   **File:** `library/urls.py`
*   **Modification Example:**
    ```python
    # In library/urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
        # ... existing urls
        path('openlibrary-search/', views.search_openlibrary_view, name='openlibrary-search'),
    ]
    ```



# Future Implementations (backlog)

1.  **Enhanced Entry Management:**
    *   **Bulk Import/Export:** Allow importing/exporting entry data (e.g., CSV, JSON).
    *   **Advanced Search & Filtering:** Implement more sophisticated search options (e.g., by genre, tags, publication year range) and saved searches.
    *   **Custom Metadata Fields:** Enable users to define their own custom fields for entries (e.g., "read status," "personal rating").
    *   **Automated Cover Image Fetching:** Integrate with external APIs (e.g., Google Books API) to atomatically fetch cover images based on ISBN.

2.  **Quote & Passage Features:**
    *   **Quote Tagging/Categorization:** Allow users to tag and categorize quotes for easier retrieval.
    *   **Full-Text Search for Quotes:** Make all registered quotes searchable.

3.  **Hardware Integration (Web Interface):**
    *   **LED Control Interface:** A web interface to directly control the bookshelf LEDs to highlight specific entries.
    *   **RFID/Barcode Scanning Integration:** Web interface support for registering new entries or locating existing ones via RFID/barcode scans.

4.  **User Experience & Reporting:**
    *   **Library Dashboard:** Display statistics like total entries, most common authors, recently added items.
    *   **Responsive Web Design:** Ensure the interface is optimized for various screen sizes, including mobile.

# Usefull links in the future

    *   https://github.com/zxing-js/library : js lib to read barcodes 

# TODO



# test books
    - 0451524934
    - 9780618260300
    - 9780345339683
    - 9780743273565
    - 9780061120084
    - 9780141439518
    - 9780142437247
    - 9780618640157
    - 9780060850524
    - 9780486282114
    - 9780486275437
    - 9780142437261
    - 9780486411095
    - 9780141182902
    - 9780140449136
    - 9780140449235
    - 9780140449242
    - 9780141182674
    - 0899661343
    - 9780143039600
    - 9780450013041
    - 9781400043668
    - 0099448823
    - 9780307593313
    - 9780679446699
    - 0870119052
    - 4770016832
    - 0679743464
    - 9780395520215
    - 9780007770120
    - 0261102362
    - 9780345253453
    - 9780553211962
    - 9780805204162
    - 9780143111603
    - 9780425158647
    - 9780553281743
    - 0441013678
    - 9780006480433
    - 9780425190449
    - 9781858788906
    - 9780670919529
    - 9781943138425
    - 9781785996313
    - 0156148501
    - 9781585102655
    - 0679785892
    - 9780679603313
    - 9780748769551
    - 0553380958
    - 9780062472106
    - 0380973634
    - 9781542049184