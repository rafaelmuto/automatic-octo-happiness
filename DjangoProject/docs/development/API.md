# Sophia Project - API Documentation

This document provides comprehensive documentation for the Sophia REST API.

## 🔗 Base URL

```
Development: http://localhost:8001/api/library/
Production: https://your-domain.com/api/library/
```

## 📋 API Overview

The Sophia API provides RESTful endpoints for managing books, authors, and library operations. All responses are in JSON format.

### Authentication

Currently, the API uses Django's session-based authentication. Future versions will support token-based authentication.

### Response Format

All API responses follow this standard format:

```json
{
  "data": {...},
  "meta": {
    "pagination": {...},
    "timestamp": "2024-07-25T12:00:00Z"
  },
  "errors": [...]
}
```

### Error Handling

Errors are returned with appropriate HTTP status codes:

- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## 📚 Books API

### Get All Books

**GET** `/api/library/books/`

Returns a list of all books in the library.

#### Query Parameters

- `page` (optional): Page number for pagination (default: 1)
- `page_size` (optional): Number of items per page (default: 20)
- `search` (optional): Search term for title or author
- `author` (optional): Filter by author ID
- `sort_by` (optional): Sort field (title, author, published_date)
- `sort_order` (optional): Sort order (asc, desc)

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/books/?page=1&page_size=10"
```

#### Example Response

```json
{
	"data": [
		{
			"id": 1,
			"title": "The Hitchhiker's Guide to the Galaxy",
			"author": {
				"id": 1,
				"name": "Douglas Adams"
			},
			"isbn": "9780345391803",
			"published_date": "1979-10-12",
			"number_of_pages": 123,
			"created_at": "2024-07-25T10:00:00Z",
			"updated_at": "2024-07-25T10:00:00Z"
		}
	],
	"meta": {
		"pagination": {
			"page": 1,
			"page_size": 10,
			"total_count": 50,
			"total_pages": 5
		},
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

### Get Book by ISBN

**GET** `/api/library/books/{isbn}/`

Returns a specific book by its ISBN.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/books/9780345391803/"
```

#### Example Response

```json
{
	"data": {
		"id": 1,
		"title": "The Hitchhiker's Guide to the Galaxy",
		"author": {
			"id": 1,
			"name": "Douglas Adams",
			"birth_date": "1952-03-11",
			"country": "UK"
		},
		"isbn": "9780345391803",
		"published_date": "1979-10-12",
		"number_of_pages": 123,
		"created_at": "2024-07-25T10:00:00Z",
		"updated_at": "2024-07-25T10:00:00Z"
	},
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

### Create New Book

**POST** `/api/library/books/`

Creates a new book in the library.

#### Request Body

```json
{
	"title": "The Hitchhiker's Guide to the Galaxy",
	"author": 1,
	"isbn": "9780345391803",
	"published_date": "1979-10-12",
	"number_of_pages": 123
}
```

#### Example Request

```bash
curl -X POST "http://localhost:8001/api/library/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Hitchhiker'\''s Guide to the Galaxy",
    "author": 1,
    "isbn": "9780345391803",
    "published_date": "1979-10-12",
    "number_of_pages": 123
  }'
```

#### Example Response

```json
{
	"data": {
		"id": 1,
		"title": "The Hitchhiker's Guide to the Galaxy",
		"author": 1,
		"isbn": "9780345391803",
		"published_date": "1979-10-12",
		"number_of_pages": 123,
		"created_at": "2024-07-25T10:00:00Z",
		"updated_at": "2024-07-25T10:00:00Z"
	},
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

### Update Book

**PUT** `/api/library/books/{isbn}/`

Updates an existing book by ISBN.

#### Request Body

```json
{
	"title": "The Hitchhiker's Guide to the Galaxy (Updated)",
	"author": 1,
	"isbn": "9780345391803",
	"published_date": "1979-10-12",
	"number_of_pages": 150
}
```

#### Example Request

```bash
curl -X PUT "http://localhost:8001/api/library/books/9780345391803/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Hitchhiker'\''s Guide to the Galaxy (Updated)",
    "author": 1,
    "isbn": "9780345391803",
    "published_date": "1979-10-12",
    "number_of_pages": 150
  }'
```

### Delete Book

**DELETE** `/api/library/books/{isbn}/`

Deletes a book from the library.

#### Example Request

```bash
curl -X DELETE "http://localhost:8001/api/library/books/9780345391803/"
```

#### Example Response

```json
{
	"data": {
		"message": "Book deleted successfully"
	},
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

### Get Books by Author

**GET** `/api/library/books/author/{author_id}/`

Returns all books by a specific author.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/books/author/1/"
```

## 👤 Authors API

### Get All Authors

**GET** `/api/library/authors/`

Returns a list of all authors.

#### Query Parameters

- `page` (optional): Page number for pagination (default: 1)
- `page_size` (optional): Number of items per page (default: 20)
- `search` (optional): Search term for author name
- `sort_by` (optional): Sort field (name, birth_date)
- `sort_order` (optional): Sort order (asc, desc)

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/authors/"
```

#### Example Response

```json
{
	"data": [
		{
			"id": 1,
			"name": "Douglas Adams",
			"birth_date": "1952-03-11",
			"death_date": "2001-05-11",
			"country": "UK",
			"created_at": "2024-07-25T10:00:00Z",
			"updated_at": "2024-07-25T10:00:00Z"
		}
	],
	"meta": {
		"pagination": {
			"page": 1,
			"page_size": 20,
			"total_count": 25,
			"total_pages": 2
		},
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

### Get Author by ID

**GET** `/api/library/authors/{id}/`

Returns a specific author by ID.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/authors/1/"
```

#### Example Response

```json
{
	"data": {
		"id": 1,
		"name": "Douglas Adams",
		"birth_date": "1952-03-11",
		"death_date": "2001-05-11",
		"country": "UK",
		"created_at": "2024-07-25T10:00:00Z",
		"updated_at": "2024-07-25T10:00:00Z"
	},
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

### Create New Author

**POST** `/api/library/authors/`

Creates a new author.

#### Request Body

```json
{
	"name": "Douglas Adams",
	"birth_date": "1952-03-11",
	"death_date": "2001-05-11",
	"country": "UK"
}
```

#### Example Request

```bash
curl -X POST "http://localhost:8001/api/library/authors/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Douglas Adams",
    "birth_date": "1952-03-11",
    "death_date": "2001-05-11",
    "country": "UK"
  }'
```

### Update Author

**PUT** `/api/library/authors/{id}/`

Updates an existing author.

#### Request Body

```json
{
	"name": "Douglas Adams",
	"birth_date": "1952-03-11",
	"death_date": "2001-05-11",
	"country": "United Kingdom"
}
```

### Delete Author

**DELETE** `/api/library/authors/{id}/`

Deletes an author from the library.

### Get Author with Books

**GET** `/api/library/authors/books/{id}/`

Returns an author with all their books.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/authors/books/1/"
```

#### Example Response

```json
{
	"data": {
		"id": 1,
		"name": "Douglas Adams",
		"birth_date": "1952-03-11",
		"death_date": "2001-05-11",
		"country": "UK",
		"books": [
			{
				"id": 1,
				"title": "The Hitchhiker's Guide to the Galaxy",
				"isbn": "9780345391803",
				"published_date": "1979-10-12"
			}
		],
		"created_at": "2024-07-25T10:00:00Z",
		"updated_at": "2024-07-25T10:00:00Z"
	},
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

## 🔍 OpenLibrary Integration API

### Search Books by ISBN

**GET** `/api/library/openlibrary/isbn/{isbn}/`

Searches for a book by ISBN on OpenLibrary.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/openlibrary/isbn/9780345391803/"
```

#### Example Response

```json
{
	"data": {
		"title": "The Hitchhiker's Guide to the Galaxy",
		"authors": ["Douglas Adams"],
		"publish_date": "1979",
		"number_of_pages": 123,
		"cover_url": "https://covers.openlibrary.org/b/id/1234567-M.jpg",
		"openlibrary_key": "OL7353617M"
	},
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

### Get Book Details by OpenLibrary Key

**GET** `/api/library/openlibrary/key/{key}/`

Retrieves detailed book information from OpenLibrary using an OpenLibrary key.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/openlibrary/key/OL7353617M/"
```

## 🔖 Bookmarks API

### Get Bookmarks for Book

**GET** `/api/library/books/{isbn}/bookmarks/`

Returns all bookmarks for a specific book.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/books/9780345391803/bookmarks/"
```

#### Example Response

```json
{
	"data": [
		{
			"id": 1,
			"page_number": 42,
			"note": "The answer to life, the universe, and everything",
			"created_at": "2024-07-25T10:00:00Z"
		}
	],
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

### Create Bookmark

**POST** `/api/library/books/{isbn}/bookmarks/`

Creates a new bookmark for a book.

#### Request Body

```json
{
	"page_number": 42,
	"note": "The answer to life, the universe, and everything"
}
```

#### Example Request

```bash
curl -X POST "http://localhost:8001/api/library/books/9780345391803/bookmarks/" \
  -H "Content-Type: application/json" \
  -d '{
    "page_number": 42,
    "note": "The answer to life, the universe, and everything"
  }'
```

## 📊 Search API

### Advanced Search

**GET** `/api/library/search/`

Performs advanced search with multiple filters.

#### Query Parameters

- `q` (optional): Search query
- `author` (optional): Filter by author name
- `genre` (optional): Filter by genre
- `min_rating` (optional): Minimum rating
- `max_rating` (optional): Maximum rating
- `published_after` (optional): Books published after date
- `published_before` (optional): Books published before date
- `sort_by` (optional): Sort field
- `sort_order` (optional): Sort order (asc, desc)
- `page` (optional): Page number
- `page_size` (optional): Items per page

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/search/?q=science fiction&author=Douglas&sort_by=title"
```

### Search Suggestions

**GET** `/api/library/search/suggestions/`

Returns search suggestions based on partial input.

#### Query Parameters

- `q` (required): Partial search query (minimum 2 characters)

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/search/suggestions/?q=hitch"
```

#### Example Response

```json
{
	"data": {
		"suggestions": [
			"The Hitchhiker's Guide to the Galaxy",
			"Hitchhiker's Guide to the Galaxy",
			"Hitchhiker's Guide"
		]
	},
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

## 🔧 Error Responses

### Validation Error

```json
{
	"errors": [
		{
			"field": "title",
			"message": "This field is required."
		},
		{
			"field": "isbn",
			"message": "Enter a valid ISBN."
		}
	],
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

### Not Found Error

```json
{
	"errors": [
		{
			"message": "Book not found with ISBN: 9780000000000"
		}
	],
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

### Server Error

```json
{
	"errors": [
		{
			"message": "Internal server error"
		}
	],
	"meta": {
		"timestamp": "2024-07-25T12:00:00Z"
	}
}
```

## 📝 Rate Limiting

The API implements rate limiting to prevent abuse:

- **Default Limit**: 1000 requests per hour per IP
- **Search Endpoints**: 100 requests per hour per IP
- **External API Calls**: 50 requests per hour per IP

Rate limit headers are included in responses:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
```

## 🔐 Authentication

### Session Authentication

For web applications, use Django's session authentication:

```bash
# Login first
curl -X POST "http://localhost:8001/login/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=password"

# Then make API calls (cookies will be sent automatically)
curl -X GET "http://localhost:8001/api/library/books/"
```

### Future: Token Authentication

Future versions will support token-based authentication:

```bash
# Get token
curl -X POST "http://localhost:8001/api/auth/token/" \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "password"}'

# Use token
curl -X GET "http://localhost:8001/api/library/books/" \
  -H "Authorization: Token your-token-here"
```

## 📚 SDKs and Libraries

### Python Client

```python
import requests

class SophiaClient:
    def __init__(self, base_url="http://localhost:8001/api/library/"):
        self.base_url = base_url
        self.session = requests.Session()

    def get_books(self, page=1, page_size=20):
        response = self.session.get(f"{self.base_url}books/", params={
            "page": page,
            "page_size": page_size
        })
        return response.json()

    def get_book(self, isbn):
        response = self.session.get(f"{self.base_url}books/{isbn}/")
        return response.json()

    def create_book(self, book_data):
        response = self.session.post(f"{self.base_url}books/", json=book_data)
        return response.json()
```

### JavaScript Client

```javascript
class SophiaClient {
	constructor(baseUrl = 'http://localhost:8001/api/library/') {
		this.baseUrl = baseUrl;
	}

	async getBooks(page = 1, pageSize = 20) {
		const response = await fetch(
			`${this.baseUrl}books/?page=${page}&page_size=${pageSize}`
		);
		return await response.json();
	}

	async getBook(isbn) {
		const response = await fetch(`${this.baseUrl}books/${isbn}/`);
		return await response.json();
	}

	async createBook(bookData) {
		const response = await fetch(`${this.baseUrl}books/`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(bookData),
		});
		return await response.json();
	}
}
```

---

**Last Updated**: July 25, 2024
**Version**: 1.0
