# GEMINI.md

This file provides context for the Gemini agent to understand and work with this project.
You should respond as being a senior software developer with experience in Python and Django.
You will always obeserve the best practices and recomendations for code and archytecture.

## Project Overview

- **Project Name:** sohia
- **Description:** Sophia is a project to help manage private libraries.
- **Python Version:** 3.10.12
- **Web Framework:** Django 5.2.4
- **Database:** SQLite

Sophia is a project to help manage private libraries. Helping you to categorise and find books, magazines and documents, known as Entries.
You can register entries with all relavant metadata to help you categorise and find what you are looking for.
Also you may register quotes and passages from the entries.

Sophia is meant to run in small single board computers (SBC), like Raspberry Pi, and will have a hardware interface with leds built in the bookshelves to help you locate the entry you are looking for. In the future we may add RF tags and suport for barcode.

The main way you can interact with Sophia is through the web interface, running in the local network. There you can register new entries and the relevant data like title, author, year of publication, ISBN, image ant etc.

    Sophia is the Greek word for "wisdom." It's a simple, beautiful, and direct name that gets straight to the core purpose of a library.

## API Endpoints

- `api/library/books/`:
  - **GET**: Returns a list of all books.
  - **POST**: Creates a new book.
    - **Payload Example**:
      ```json
      {
      	"title": "The Hitchhiker's Guide to the Galaxy",
      	"author": 1, // Author ID
      	"published_date": "1979-10-12",
      	"number_of_pages": 123,
      	"isbn": "9780345391803"
      }
      ```
- `api/library/books/<isbn>/`:
  - **GET**: Returns a single book by ISBN.
  - **PUT**: Updates an existing book by ISBN. (Requires full payload)
  - **PATCH**: Partially updates an existing book by ISBN. (Allows partial payload)
  - **DELETE**: Deletes a single book by ISBN.
- `api/library/books/author/<int:author_id>`:

  - **GET**: Returns a list of books by the author.

- `api/library/authors/`:
  - **GET**: Returns a list of all authors.
  - **POST**: Creates a new author.
    - **Payload Example**:
      ```json
      {
      	"name": "Douglas Adams",
      	"birth_date": "1952-03-11",
      	"death_date": "2000-01-01",
      	"country": "USA"
      }
      ```
- `api/library/authors/<id>/`:
  - **GET**: Returns a single author by ID.
  - **PUT**: Updates an existing author by ID. (Requires full payload)
  - **PATCH**: Partially updates an existing author by ID. (Allows partial payload)
  - **DELETE**: Deletes a single author by ID.
- `api/library/authors/books/<id>/`:

  - **GET**: Returns a single author by ID with a list of books by the author.

- `api/library/openlibrary/isbn/<isbn>/`:
  - **GET**: Searches for a book by ISBN on OpenLibrary and returns its data.
- `api/library/openlibrary/key/<key>/`:
  - **GET**: Retrieves data from OpenLibrary using an OpenLibrary key (OLID).

## Getting Started

### Prerequisites

- List any software or tools that need to be installed before setting up the project (e.g., Python, pip, virtualenv, Docker).

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
    - Copy the `.env.example` file to `.env` and fill in the required values.
5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

### Running the Development Server

- Provide the command to start the local development server.
  ```bash
  python manage.py runserver
  ```

### Docker

- Building dockerimage
  ```bash
  docker build . -t sophia_image --no-cache
  ```
- Runing application
  ```bash
  docker compose up
  ```

## Development Guidelines

### Coding Style

- **Linter:** Ruff
<!-- *   **Formatter:** Black -->
- **Command to run linter/formatter:**
  ```bash
  # Example
  ruff check .
  <!-- black . -->
  ```

### Testing

- **Testing Framework:** (unittest)
- **How to run tests:**
  ```bash
  python manage.py test
  ```
- **Location of tests:** `tests.py`

### Project Structure

- Briefly describe the purpose of the main directories and files.
  - `sophia/`: Contains the main Django project settings.
  - `library/`: main django app domain.
  - `library/templates/library`: For Django templates.
  - `library/models`: library models
  - `library/migrations`: library migration files
  - `manage.py`: Django's command-line utility.

## Deployment

- Instructions on how to deploy the application to a staging or production environment.
- Mention the hosting platform (e.g., Heroku, AWS, Vercel) and any specific configurations.

## Important Commands

- List any other useful commands for managing the project.
  - `python manage.py makemigrations`: To create new database migrations.
  - `python manage.py migrate`: Run all migrations.
  - `python manage.py collectstatic`: Collect static files
  - `python manage.py shell`: To open the Django shell.
  - `python manage.py test`: Run all unit tests.

# Tasks

## 1. API Implementation [DONE]

**Step 1: Install and Configure DRF**

- **Install:** `pip install djangorestframework`
- **Configure:** Add `'rest_framework'` to your `INSTALLED_APPS` in `sophia/settings.py`.

**Step 2: Create a Serializer**

- **File:** `library/serializers.py`
- **Code:**

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

- **File:** `library/api.py`
- **Code:**

  ```python
  from rest_framework import generics
  from .models import Book
  from .serializers import BookSerializer

  class BookListAPIView(generics.ListAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer
  ```

**Step 4: Define API URLs**

- **Create a new file:** `library/api_urls.py`
- **Code:**

  ```python
  from django.urls import path
  from . import api

  urlpatterns = [
      path('books/', api.BookListAPIView.as_as_view(), name='book-list'),
  ]
  ```

**Step 5: Include API URLs in the Main Project**

- **File:** `sophia/urls.py`
- **Modification:**

  ```python
  # In sophia/urls.py

  urlpatterns = [
      # ... existing urls
      path('api/library/', include('library.api_urls')), # Add this line
  ]
  ```

## 2. Implement .env for Configurations [DONE]

**Step 1: Install `python-dotenv`**

- **Install:** `pip install python-dotenv`

**Step 2: Configure Django to load environment variables**

- Open `sophia/settings.py`.
- Add the following lines at the very top of the file to load the `.env` file:

  ```python
  import os
  from pathlib import Path
  from dotenv import load_dotenv

  load_dotenv() # This loads the environment variables from .env
  ```

- Replace hardcoded sensitive values (e.g., `SECRET_KEY`, database credentials) with `os.getenv()` calls. For example:
  ```python
  SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key-for-development')
  ```

**Step 3: Create a `.env` file**

- Create a new file named `.env` in the project root directory (where `manage.py` is located).
- Add your key-value pairs to this file, e.g.:
  ```
  SECRET_KEY=your_actual_secret_key_here
  DATABASE_NAME=mydatabase
  DATABASE_USER=myuser
  DATABASE_PASSWORD=mypassword
  ```

**Step 4: Update `.gitignore`**

- Add `.env` to your `.gitignore` file to prevent it from being committed to version control.
  ```
  # .gitignore
  .env
  ```

## 3. Implementing OpenLibraryService [REJECTED]

**Step 1: Install the `requests` library**

- **Install:** `pip install requests`
- **Update:** Add `requests` to your `requirements.txt`.

**Step 2: Create the Service Class File**

- **File:** `library/services.py`
- **Code:**

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

- **File:** `library/views.py` (or a new view if preferred)
- **Modification Example:**

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

- **File:** `library/templates/library/openlibrary_search_results.html`
- **Code Example:**

  ```html
  <!-- library/templates/library/openlibrary_search_results.html -->
  <h1>OpenLibrary Search Results</h1>
  <form method="GET" action="">
  	<input
  		type="text"
  		name="q"
  		value="{{ query|default_if_none:'' }}"
  		placeholder="Search books..."
  	/>
  	<button type="submit">Search</button>
  </form>

  {% if books_data %}
  <h2>Results for "{{ query }}"</h2>
  <ul>
  	{% for doc in books_data.docs %}
  	<li>
  		<strong>{{ doc.title }}</strong> by {{ doc.author_name|join:", " }} ({{
  		doc.first_publish_year }}) {% if doc.isbn and doc.isbn.0 %} <br />ISBN: {{
  		doc.isbn.0 }} {% endif %}
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

- **File:** `library/urls.py`
- **Modification Example:**

  ```python
  # In library/urls.py
  from django.urls import path
  from . import views

  urlpatterns = [
      # ... existing urls
      path('openlibrary-search/', views.search_openlibrary_view, name='openlibrary-search'),
  ]
  ```

## 4. Advanced Search and Filtering Implementation [TODO]

**Phase 1: Backend Foundation**

**Step 1: Extend Models with Search-Ready Fields**

- **File:** `library/models/book.py`
- **Additions:**

  ```python
  class Book(models.Model):
      # Existing fields...

      # New search-friendly fields
      genre = models.CharField(max_length=100, null=True, blank=True)
      language = models.CharField(max_length=50, default='en')
      reading_status = models.CharField(
          max_length=20,
          choices=[
              ('unread', 'Unread'),
              ('reading', 'Currently Reading'),
              ('finished', 'Finished'),
              ('abandoned', 'Abandoned')
          ],
          default='unread'
      )
      rating = models.PositiveSmallIntegerField(null=True, blank=True)
      tags = models.JSONField(default=list, blank=True)
      summary = models.TextField(blank=True, null=True)

      class Meta:
          indexes = [
              models.Index(fields=['title']),
              models.Index(fields=['publish_date']),
              models.Index(fields=['reading_status']),
              models.Index(fields=['rating']),
              models.Index(fields=['genre']),
              models.Index(fields=['language']),
          ]
  ```

**Step 2: Create Search Service Layer**

- **File:** `library/services/search_service.py`
- **Code:**

  ```python
  from django.db.models import Q, Count, Avg
  from typing import Dict, List, Optional

  class BookSearchService:
      @staticmethod
      def advanced_search(
          query: Optional[str] = None,
          filters: Optional[Dict] = None,
          sort_by: str = 'title',
          sort_order: str = 'asc',
          page: int = 1,
          page_size: int = 20
      ) -> Dict:
          """
          Advanced search with multiple filters and sorting (SQLite compatible)
          """
          queryset = Book.objects.select_related('author')

          # Text search using SQLite's LIKE operator
          if query:
              queryset = BookSearchService._apply_text_search(queryset, query)

          # Apply filters
          if filters:
              queryset = BookSearchService._apply_filters(queryset, filters)

          # Apply sorting
          queryset = BookSearchService._apply_sorting(queryset, sort_by, sort_order)

          # Pagination
          total_count = queryset.count()
          start = (page - 1) * page_size
          end = start + page_size
          books = queryset[start:end]

          return {
              'books': books,
              'total_count': total_count,
              'page': page,
              'page_size': page_size,
              'total_pages': (total_count + page_size - 1) // page_size
          }

      @staticmethod
      def _apply_text_search(queryset, query: str):
          """Apply text search using SQLite's LIKE operator"""
          words = query.split()
          q_objects = Q()
          for word in words:
              word_query = Q(
                  Q(title__icontains=word) |
                  Q(author__name__icontains=word) |
                  Q(publisher__icontains=word) |
                  Q(summary__icontains=word) |
                  Q(genre__icontains=word)
              )
              q_objects &= word_query
          return queryset.filter(q_objects)

      @staticmethod
      def _apply_filters(queryset, filters: Dict):
          """Apply various filters to the queryset"""
          if filters.get('author'):
              queryset = queryset.filter(author__name__icontains=filters['author'])

          if filters.get('genre'):
              queryset = queryset.filter(genre__icontains=filters['genre'])

          if filters.get('reading_status'):
              queryset = queryset.filter(reading_status=filters['reading_status'])

          if filters.get('min_rating'):
              queryset = queryset.filter(rating__gte=filters['min_rating'])

          if filters.get('max_rating'):
              queryset = queryset.filter(rating__lte=filters['max_rating'])

          if filters.get('publish_year_start'):
              queryset = queryset.filter(publish_date__year__gte=filters['publish_year_start'])

          if filters.get('publish_year_end'):
              queryset = queryset.filter(publish_date__year__lte=filters['publish_year_end'])

          if filters.get('language'):
              queryset = queryset.filter(language=filters['language'])

          if filters.get('has_bookmarks'):
              queryset = queryset.filter(bookmark__isnull=False).distinct()

          return queryset

      @staticmethod
      def _apply_sorting(queryset, sort_by: str, sort_order: str):
          """Apply sorting to the queryset"""
          valid_sort_fields = {
              'title', 'author__name', 'publish_date', 'rating',
              'created_at', 'updated_at', 'number_of_pages'
          }

          if sort_by not in valid_sort_fields:
              sort_by = 'title'

          if sort_order == 'desc':
              sort_by = f'-{sort_by}'

          return queryset.order_by(sort_by)
  ```

**Step 3: Create Search Serializers**

- **File:** `library/serializers.py` (additions)
- **Code:**

  ```python
  class BookSearchSerializer(serializers.ModelSerializer):
      author = AuthorSerializer(read_only=True)
      bookmark_count = serializers.SerializerMethodField()

      class Meta:
          model = Book
          fields = [
              'id', 'title', 'author', 'publish_date', 'isbn',
              'genre', 'rating', 'reading_status', 'bookmark_count',
              'number_of_pages', 'language'
          ]

      def get_bookmark_count(self, obj):
          return obj.bookmark_set.count()

  class SearchFilterSerializer(serializers.Serializer):
      query = serializers.CharField(required=False, allow_blank=True)
      author = serializers.CharField(required=False, allow_blank=True)
      genre = serializers.CharField(required=False, allow_blank=True)
      reading_status = serializers.ChoiceField(
          choices=Book.reading_status.field.choices,
          required=False
      )
      min_rating = serializers.IntegerField(min_value=1, max_value=5, required=False)
      max_rating = serializers.IntegerField(min_value=1, max_value=5, required=False)
      publish_year_start = serializers.IntegerField(required=False)
      publish_year_end = serializers.IntegerField(required=False)
      language = serializers.CharField(required=False, allow_blank=True)
      has_bookmarks = serializers.BooleanField(required=False)
      sort_by = serializers.CharField(required=False, default='title')
      sort_order = serializers.ChoiceField(
          choices=[('asc', 'Ascending'), ('desc', 'Descending')],
          required=False,
          default='asc'
      )
      page = serializers.IntegerField(min_value=1, required=False, default=1)
      page_size = serializers.IntegerField(min_value=1, max_value=100, required=False, default=20)
  ```

**Phase 2: API Implementation**

**Step 4: Create Advanced Search API Views**

- **File:** `library/api/search_api.py`
- **Code:**

  ```python
  from rest_framework import status
  from rest_framework.decorators import api_view
  from rest_framework.response import Response
  from ..services.search_service import BookSearchService
  from ..serializers import BookSearchSerializer, SearchFilterSerializer

  @api_view(['GET'])
  def advanced_search_view(request):
      """
      Advanced search endpoint with filtering, sorting, and pagination
      """
      serializer = SearchFilterSerializer(data=request.query_params)
      if not serializer.is_valid():
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      search_result = BookSearchService.advanced_search(
          query=serializer.validated_data.get('query'),
          filters=serializer.validated_data,
          sort_by=serializer.validated_data.get('sort_by', 'title'),
          sort_order=serializer.validated_data.get('sort_order', 'asc'),
          page=serializer.validated_data.get('page', 1),
          page_size=serializer.validated_data.get('page_size', 20)
      )

      book_serializer = BookSearchSerializer(search_result['books'], many=True)

      return Response({
          'books': book_serializer.data,
          'pagination': {
              'page': search_result['page'],
              'page_size': search_result['page_size'],
              'total_count': search_result['total_count'],
              'total_pages': search_result['total_pages']
          }
      })

  @api_view(['GET'])
  def search_suggestions_view(request):
      """
      Get search suggestions based on partial input
      """
      query = request.query_params.get('q', '').strip()
      if len(query) < 2:
          return Response({'suggestions': []})

      suggestions = []

      # Title suggestions
      title_suggestions = Book.objects.filter(
          title__icontains=query
      ).values_list('title', flat=True)[:5]
      suggestions.extend(title_suggestions)

      # Author suggestions
      author_suggestions = Author.objects.filter(
          name__icontains=query
      ).values_list('name', flat=True)[:5]
      suggestions.extend(author_suggestions)

      # Genre suggestions
      genre_suggestions = Book.objects.filter(
          genre__icontains=query
      ).values_list('genre', flat=True).distinct()[:5]
      suggestions.extend(genre_suggestions)

      return Response({'suggestions': list(set(suggestions))})

  @api_view(['GET'])
  def search_facets_view(request):
      """
      Get available filter options (facets) for search
      """
      facets = {
          'genres': list(Book.objects.exclude(
              genre__isnull=True
          ).values_list('genre', flat=True).distinct()),
          'languages': list(Book.objects.values_list('language', flat=True).distinct()),
          'reading_statuses': [choice[0] for choice in Book.reading_status.field.choices],
          'authors': list(Author.objects.values_list('name', flat=True).distinct()),
          'publish_years': list(Book.objects.exclude(
              publish_date__isnull=True
          ).values_list('publish_date__year', flat=True).distinct().order_by('publish_date__year'))
      }

      return Response(facets)
  ```

**Step 5: Update API URLs**

- **File:** `library/api_urls.py` (additions)
- **Code:**

  ```python
  from .api import search_api

  urlpatterns += [
      path("search/", search_api.advanced_search_view, name="advanced-search"),
      path("search/suggestions/", search_api.search_suggestions_view, name="search-suggestions"),
      path("search/facets/", search_api.search_facets_view, name="search-facets"),
  ]
  ```

**Phase 3: Frontend Implementation**

**Step 6: Create Search Template**

- **File:** `library/templates/library/advanced_search.html`
- **Code:**

  ```html
  {% extends "library/base.html" %}

  {% block content %}
  <div class="search-container">
      <!-- Search Form -->
      <form method="get" class="search-form">
          <div class="search-input-group">
              <input type="text" name="query" value="{{ request.GET.query }}"
                     placeholder="Search books, authors, or content..."
                     class="search-input">
              <button type="submit" class="search-button">Search</button>
          </div>

          <!-- Advanced Filters -->
          <div class="filters-section">
              <h3>Filters</h3>
              <div class="filter-grid">
                  <div class="filter-group">
                      <label>Author:</label>
                      <input type="text" name="author" value="{{ request.GET.author }}">
                  </div>

                  <div class="filter-group">
                      <label>Genre:</label>
                      <select name="genre">
                          <option value="">All Genres</option>
                          {% for genre in facets.genres %}
                          <option value="{{ genre }}" {% if request.GET.genre == genre %}selected{% endif %}>
                              {{ genre }}
                          </option>
                          {% endfor %}
                      </select>
                  </div>

                  <div class="filter-group">
                      <label>Reading Status:</label>
                      <select name="reading_status">
                          <option value="">All Statuses</option>
                          {% for status in facets.reading_statuses %}
                          <option value="{{ status }}" {% if request.GET.reading_status == status %}selected{% endif %}>
                              {{ status|title }}
                          </option>
                          {% endfor %}
                      </select>
                  </div>

                  <div class="filter-group">
                      <label>Rating:</label>
                      <input type="number" name="min_rating" value="{{ request.GET.min_rating }}"
                             min="1" max="5" placeholder="Min">
                      <input type="number" name="max_rating" value="{{ request.GET.max_rating }}"
                             min="1" max="5" placeholder="Max">
                  </div>

                  <div class="filter-group">
                      <label>Publish Year:</label>
                      <input type="number" name="publish_year_start" value="{{ request.GET.publish_year_start }}"
                             placeholder="From">
                      <input type="number" name="publish_year_end" value="{{ request.GET.publish_year_end }}"
                             placeholder="To">
                  </div>
              </div>
          </div>

          <!-- Sort Options -->
          <div class="sort-section">
              <label>Sort by:</label>
              <select name="sort_by">
                  <option value="title" {% if request.GET.sort_by == 'title' %}selected{% endif %}>Title</option>
                  <option value="author__name" {% if request.GET.sort_by == 'author__name' %}selected{% endif %}>Author</option>
                  <option value="publish_date" {% if request.GET.sort_by == 'publish_date' %}selected{% endif %}>Publish Date</option>
                  <option value="rating" {% if request.GET.sort_by == 'rating' %}selected{% endif %}>Rating</option>
              </select>
              <select name="sort_order">
                  <option value="asc" {% if request.GET.sort_order == 'asc' %}selected{% endif %}>Ascending</option>
                  <option value="desc" {% if request.GET.sort_order == 'desc' %}selected{% endif %}>Descending</option>
              </select>
          </div>
      </form>

      <!-- Search Results -->
      <div class="search-results">
          {% if books %}
          <div class="results-header">
              <h2>Found {{ pagination.total_count }} book{{ pagination.total_count|pluralize }}</h2>
              <div class="pagination-info">
                  Page {{ pagination.page }} of {{ pagination.total_pages }}
              </div>
          </div>

          <div class="books-grid">
              {% for book in books %}
              <div class="book-card">
                  <h3><a href="{% url 'library:book-detail' book.id %}">{{ book.title }}</a></h3>
                  <p class="author">by {{ book.author.name }}</p>
                  {% if book.genre %}<p class="genre">{{ book.genre }}</p>{% endif %}
                  {% if book.rating %}<p class="rating">★ {{ book.rating }}/5</p>{% endif %}
                  <p class="status">{{ book.reading_status|title }}</p>
              </div>
              {% endfor %}
          </div>

          <!-- Pagination -->
          {% if pagination.total_pages > 1 %}
          <div class="pagination">
              {% if pagination.page > 1 %}
              <a href="?{{ request.GET.urlencode }}&page={{ pagination.page|add:'-1' }}" class="page-link">Previous</a>
              {% endif %}

              {% for page_num in pagination.page_range %}
              <a href="?{{ request.GET.urlencode }}&page={{ page_num }}"
                 class="page-link {% if page_num == pagination.page %}active{% endif %}">
                  {{ page_num }}
              </a>
              {% endfor %}

              {% if pagination.page < pagination.total_pages %}
              <a href="?{{ request.GET.urlencode }}&page={{ pagination.page|add:'1' }}" class="page-link">Next</a>
              {% endif %}
          </div>
          {% endif %}

          {% else %}
          <div class="no-results">
              <h2>No books found</h2>
              <p>Try adjusting your search criteria or filters.</p>
          </div>
          {% endif %}
      </div>
  </div>
  {% endblock %}
  ```

**Step 7: Create Search View**

- **File:** `library/views/search_views.py`
- **Code:**

  ```python
  from django.views.generic import TemplateView
  from django.contrib.auth.mixins import LoginRequiredMixin
  from ..services.search_service import BookSearchService

  class AdvancedSearchView(LoginRequiredMixin, TemplateView):
      template_name = 'library/advanced_search.html'

      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)

          # Get search parameters
          query = self.request.GET.get('query', '').strip()
          filters = {
              'author': self.request.GET.get('author', '').strip(),
              'genre': self.request.GET.get('genre', '').strip(),
              'reading_status': self.request.GET.get('reading_status', '').strip(),
              'min_rating': self.request.GET.get('min_rating'),
              'max_rating': self.request.GET.get('max_rating'),
              'publish_year_start': self.request.GET.get('publish_year_start'),
              'publish_year_end': self.request.GET.get('publish_year_end'),
              'language': self.request.GET.get('language', '').strip(),
          }

          # Remove empty filters
          filters = {k: v for k, v in filters.items() if v}

          # Perform search if there are any parameters
          if query or filters:
              search_result = BookSearchService.advanced_search(
                  query=query,
                  filters=filters,
                  sort_by=self.request.GET.get('sort_by', 'title'),
                  sort_order=self.request.GET.get('sort_order', 'asc'),
                  page=int(self.request.GET.get('page', 1)),
                  page_size=20
              )

              context['books'] = search_result['books']
              context['pagination'] = {
                  'page': search_result['page'],
                  'total_count': search_result['total_count'],
                  'total_pages': search_result['total_pages'],
                  'page_range': range(1, search_result['total_pages'] + 1)
              }
          else:
              context['books'] = []
              context['pagination'] = {'total_count': 0}

          # Get facets for filter options
          context['facets'] = self._get_facets()

          return context

      def _get_facets(self):
          """Get available filter options"""
          from ..models import Book, Author

          return {
              'genres': list(Book.objects.values_list('genre', flat=True).distinct()),
              'reading_statuses': [choice[0] for choice in Book.reading_status.field.choices],
              'authors': list(Author.objects.values_list('name', flat=True).distinct()),
          }
  ```

**Step 8: Add URL for Search View**

- **File:** `library/urls.py` (additions)
- **Code:**

  ```python
  from .views.search_views import AdvancedSearchView

  urlpatterns += [
      path('search/', AdvancedSearchView.as_view(), name='advanced-search'),
  ]
  ```

**Phase 4: Enhanced Features**

**Step 9: SQLite Full-Text Search (FTS5)**

- **File:** `library/services/sqlite_search_service.py`
- **Code:**

  ```python
  import sqlite3
  from django.db import connection
  from django.conf import settings

  class SQLiteFullTextSearch:
      @staticmethod
      def setup_fts_table():
          """Setup SQLite FTS5 virtual table for full-text search"""
          with connection.cursor() as cursor:
              # Create FTS5 virtual table
              cursor.execute("""
                  CREATE VIRTUAL TABLE IF NOT EXISTS books_fts USING fts5(
                      title, author_name, summary, publisher, genre,
                      content='books',
                      content_rowid='id'
                  )
              """)

              # Create triggers to keep FTS table in sync
              cursor.execute("""
                  CREATE TRIGGER IF NOT EXISTS books_ai AFTER INSERT ON books BEGIN
                      INSERT INTO books_fts(rowid, title, author_name, summary, publisher, genre)
                      VALUES (new.id, new.title,
                             (SELECT name FROM library_author WHERE id = new.author_id),
                             new.summary, new.publisher, new.genre);
                  END
              """)

              cursor.execute("""
                  CREATE TRIGGER IF NOT EXISTS books_ad AFTER DELETE ON books BEGIN
                      INSERT INTO books_fts(books_fts, rowid, title, author_name, summary, publisher, genre)
                      VALUES('delete', old.id, old.title,
                             (SELECT name FROM library_author WHERE id = old.author_id),
                             old.summary, old.publisher, old.genre);
                  END
              """)

              cursor.execute("""
                  CREATE TRIGGER IF NOT EXISTS books_au AFTER UPDATE ON books BEGIN
                      INSERT INTO books_fts(books_fts, rowid, title, author_name, summary, publisher, genre)
                      VALUES('delete', old.id, old.title,
                             (SELECT name FROM library_author WHERE id = old.author_id),
                             old.summary, old.publisher, old.genre);
                      INSERT INTO books_fts(rowid, title, author_name, summary, publisher, genre)
                      VALUES (new.id, new.title,
                             (SELECT name FROM library_author WHERE id = new.author_id),
                             new.summary, new.publisher, new.genre);
                  END
              """)

      @staticmethod
      def full_text_search(query: str):
          """Perform full-text search using SQLite FTS5"""
          with connection.cursor() as cursor:
              cursor.execute("""
                  SELECT rowid, title, author_name, summary, publisher, genre,
                         rank FROM books_fts
                  WHERE books_fts MATCH ?
                  ORDER BY rank
              """, [query])

              results = cursor.fetchall()
              return results
  ```

**Step 10: Management Command for FTS Setup**

- **File:** `library/management/commands/setup_fts.py`
- **Code:**

  ```python
  from django.core.management.base import BaseCommand
  from library.services.sqlite_search_service import SQLiteFullTextSearch

  class Command(BaseCommand):
      help = 'Setup SQLite FTS5 full-text search'

      def handle(self, *args, **options):
          self.stdout.write('Setting up SQLite FTS5...')
          SQLiteFullTextSearch.setup_fts_table()
          self.stdout.write(self.style.SUCCESS('FTS5 setup completed successfully'))
  ```

**Step 11: Search Analytics**

- **File:** `library/models/search_analytics.py`
- **Code:**

  ```python
  from django.db import models
  from django.contrib.auth.models import User

  class SearchQuery(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
      query = models.CharField(max_length=500)
      filters = models.JSONField(default=dict)
      results_count = models.IntegerField()
      search_duration = models.FloatField(null=True)  # in seconds
      created_at = models.DateTimeField(auto_now_add=True)

      class Meta:
          indexes = [
              models.Index(fields=['created_at']),
              models.Index(fields=['query']),
              models.Index(fields=['user']),
          ]
          db_table = 'search_queries'

  class PopularSearch(models.Model):
      query = models.CharField(max_length=500, unique=True)
      search_count = models.IntegerField(default=1)
      last_searched = models.DateTimeField(auto_now=True)

      class Meta:
          indexes = [
              models.Index(fields=['-search_count']),
              models.Index(fields=['-last_searched']),
          ]
          db_table = 'popular_searches'
  ```

**Implementation Timeline:**

1. **Week 1**: Model extensions and database migrations for SQLite
2. **Week 2**: Search service layer with SQLite-compatible queries
3. **Week 3**: API endpoints and SQLite FTS5 setup
4. **Week 4**: Frontend templates and views
5. **Week 5**: Testing, optimization, and SQLite-specific performance tuning

**Key Features:**

- **Text Search**: Multi-field search using SQLite's LIKE operator
- **Advanced Filtering**: Filter by author, genre, reading status, rating, publish year, language
- **Sorting**: Sort by title, author, publish date, rating, etc.
- **Pagination**: Efficient pagination for large result sets
- **Search Suggestions**: Auto-complete suggestions for titles, authors, genres
- **Faceted Search**: Dynamic filter options based on available data
- **Full-Text Search**: Optional SQLite FTS5 integration for better text search
- **Search Analytics**: Track search queries and popular searches
- **Performance Optimized**: Database indexes and caching for SQLite

# TODO

## 🔴 High Priority Tasks

### 1. Advanced Search and Filtering Implementation [PLANNED]

- **Status**: Not started
- **Description**: Implement sophisticated search with filtering, sorting, and pagination
- **Components**:
  - Extend Book model with search-friendly fields (genre, language, reading_status, rating, tags, summary)
  - Create search service layer with SQLite-compatible queries
  - Implement API endpoints for advanced search
  - Create frontend templates and views for search interface
  - Add SQLite FTS5 full-text search capabilities
  - Implement search analytics and suggestions

### 2. Enhanced Book Model [PLANNED]

- **Status**: Not started
- **Description**: Add missing fields to Book model for better categorization
- **Components**:
  - Add genre, language, reading_status, rating, tags, summary fields
  - Create database migrations
  - Update forms and serializers
  - Add database indexes for performance

### 3. Comprehensive Testing Suite [TODO]

- **Status**: Minimal tests exist
- **Description**: Create comprehensive test coverage
- **Components**:
  - Unit tests for models, views, and services
  - API endpoint tests
  - Integration tests
  - Test data fixtures
  - Coverage reporting

### 4. User Authentication and Authorization [TODO]

- **Status**: Not implemented
- **Description**: Add user management and access control
- **Components**:
  - User registration and login
  - User-specific book collections
  - Permission-based access control
  - User profiles and preferences

## 🟡 Medium Priority Tasks

### 5. Quote and Passage Management [TODO]

- **Status**: Not implemented
- **Description**: Add functionality to manage quotes and passages from books
- **Components**:
  - Quote model with book reference
  - Quote tagging and categorization
  - Full-text search for quotes
  - Quote management interface

### 6. Enhanced Bookmark System [TODO]

- **Status**: Basic model exists
- **Description**: Improve bookmark functionality
- **Components**:
  - Bookmark categories and tags
  - Bookmark search and filtering
  - Bookmark export functionality
  - Enhanced bookmark interface

### 7. Data Import/Export Features [TODO]

- **Status**: Not implemented
- **Description**: Allow bulk import/export of book data
- **Components**:
  - CSV import/export functionality
  - JSON import/export
  - Data validation and error handling
  - Import progress tracking

### 8. Automated Cover Image Fetching [TODO]

- **Status**: Not implemented
- **Description**: Automatically fetch book covers from external APIs
- **Components**:
  - Google Books API integration
  - OpenLibrary cover image integration
  - Cover image storage and management
  - Fallback cover generation

## 🟢 Low Priority Tasks

### 9. Library Dashboard and Analytics [TODO]

- **Status**: Not implemented
- **Description**: Create dashboard with library statistics
- **Components**:
  - Total books, authors, and genres statistics
  - Reading progress tracking
  - Most popular authors and genres
  - Recently added items
  - Reading goals and achievements

### 10. Responsive Web Design [TODO]

- **Status**: Basic templates exist
- **Description**: Improve UI/UX for various screen sizes
- **Components**:
  - Mobile-responsive design
  - Modern CSS framework integration
  - Improved navigation and layout
  - Dark/light theme support

### 11. Hardware Integration Preparation [TODO]

- **Status**: Not implemented
- **Description**: Prepare for future hardware integration
- **Components**:
  - LED control interface
  - RFID/barcode scanning support
  - Hardware API endpoints
  - Device management interface

### 12. Performance Optimization [TODO]

- **Status**: Not implemented
- **Description**: Optimize application performance
- **Components**:
  - Database query optimization
  - Caching implementation
  - Static file optimization
  - API response optimization

## 📋 Technical Debt and Maintenance

### 13. Code Quality Improvements [TODO]

- **Status**: Basic structure exists
- **Description**: Improve code quality and maintainability
- **Components**:
  - Code documentation
  - Type hints implementation
  - Error handling improvements
  - Logging implementation

### 14. Security Enhancements [TODO]

- **Status**: Basic Django security
- **Description**: Enhance application security
- **Components**:
  - Input validation
  - CSRF protection
  - Rate limiting
  - Security headers

### 15. Deployment and DevOps [TODO]

- **Status**: Basic Docker setup exists
- **Description**: Improve deployment and operations
- **Components**:
  - Production deployment configuration
  - Environment-specific settings
  - Monitoring and logging
  - Backup and recovery procedures

## 📊 Task Status Summary

- **🔴 High Priority**: 4 tasks
- **🟡 Medium Priority**: 4 tasks
- **🟢 Low Priority**: 4 tasks
- **📋 Technical Debt**: 3 tasks
- **Total**: 15 tasks

## 🎯 Next Steps

1. Start with **Advanced Search and Filtering** implementation
2. Extend the **Book model** with new fields
3. Implement **comprehensive testing**
4. Add **user authentication** system
5. Continue with **quote management** features

This task list provides a roadmap for developing Sophia from its current state to a fully-featured library management system.

---

# Usefull links in the future

    *   https://github.com/zxing-js/library : js lib to read barcodes

# Test Books

    - this is a list of ISBNs that are known to be in the OpenLibrary database and can be used for testing.
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
