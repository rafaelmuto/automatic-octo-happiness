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

API responses follow Django REST Framework's standard format:

```json
[
	{
		"id": 1,
		"title": "The Hitchhiker's Guide to the Galaxy",
		"author": {
			"id": 1,
			"name": "Douglas Adams",
			"birth_date": "1952-03-11",
			"death_date": "2001-05-11",
			"country": "UK"
		},
		"publish_date": "1979-10-12",
		"isbn": "9780345391803"
	}
]
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

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/books/"
```

#### Example Response

```json
[
	{
		"id": 1,
		"title": "The Hitchhiker's Guide to the Galaxy",
		"author": {
			"id": 1,
			"name": "Douglas Adams",
			"birth_date": "1952-03-11",
			"death_date": "2001-05-11",
			"country": "UK"
		},
		"publish_date": "1979-10-12",
		"isbn": "9780345391803"
	}
]
```

### Get Book by ISBN

**GET** `/api/library/books/isbn/{isbn}/`

Returns a specific book by its ISBN.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/books/isbn/9780345391803/"
```

#### Example Response

```json
{
	"id": 1,
	"title": "The Hitchhiker's Guide to the Galaxy",
	"author": {
		"id": 1,
		"name": "Douglas Adams",
		"birth_date": "1952-03-11",
		"death_date": "2001-05-11",
		"country": "UK"
	},
	"publish_date": "1979-10-12",
	"isbn": "9780345391803"
}
```

### Get Book by ID

**GET** `/api/library/books/{id}/`

Returns a specific book by its ID.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/books/1/"
```

### Create New Book

**POST** `/api/library/books/`

Creates a new book in the library.

#### Request Body

```json
{
	"title": "The Hitchhiker's Guide to the Galaxy",
	"author": 1,
	"publish_date": "1979-10-12",
	"isbn": "9780345391803"
}
```

#### Example Request

```bash
curl -X POST "http://localhost:8001/api/library/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Hitchhiker'\''s Guide to the Galaxy",
    "author": 1,
    "publish_date": "1979-10-12",
    "isbn": "9780345391803"
  }'
```

### Update Book

**PUT** `/api/library/books/{id}/`

Updates an existing book by ID.

#### Request Body

```json
{
	"title": "The Hitchhiker's Guide to the Galaxy (Updated)",
	"author": 1,
	"publish_date": "1979-10-12",
	"isbn": "9780345391803"
}
```

### Delete Book

**DELETE** `/api/library/books/{id}/`

Deletes a book from the library.

#### Example Request

```bash
curl -X DELETE "http://localhost:8001/api/library/books/1/"
```

### Get Books by Author

**GET** `/api/library/books/author/{author_id}`

Returns all books by a specific author.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/books/author/1"
```

## 👤 Authors API

### Get All Authors

**GET** `/api/library/authors/`

Returns a list of all authors.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/authors/"
```

#### Example Response

```json
[
	{
		"id": 1,
		"name": "Douglas Adams",
		"birth_date": "1952-03-11",
		"death_date": "2001-05-11",
		"country": "UK"
	}
]
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
	"id": 1,
	"name": "Douglas Adams",
	"birth_date": "1952-03-11",
	"death_date": "2001-05-11",
	"country": "UK"
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
	"id": 1,
	"name": "Douglas Adams",
	"birth_date": "1952-03-11",
	"death_date": "2001-05-11",
	"country": "UK",
	"books": [
		{
			"id": 1,
			"title": "The Hitchhiker's Guide to the Galaxy",
			"author": {
				"id": 1,
				"name": "Douglas Adams",
				"birth_date": "1952-03-11",
				"death_date": "2001-05-11",
				"country": "UK"
			},
			"publish_date": "1979-10-12",
			"isbn": "9780345391803"
		}
	]
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
	"title": "The Hitchhiker's Guide to the Galaxy",
	"authors": ["Douglas Adams"],
	"publish_date": "1979",
	"number_of_pages": 123,
	"cover_url": "https://covers.openlibrary.org/b/id/1234567-M.jpg",
	"openlibrary_key": "OL7353617M"
}
```

### Get Book Details by OpenLibrary Key

**GET** `/api/library/openlibrary/key/{key}/`

Retrieves detailed book information from OpenLibrary using an OpenLibrary key.

#### Example Request

```bash
curl -X GET "http://localhost:8001/api/library/openlibrary/key/OL7353617M/"
```

## 🔧 Error Responses

### Validation Error

```json
{
	"title": ["This field is required."],
	"isbn": ["Enter a valid ISBN."]
}
```

### Not Found Error

```json
{
	"detail": "Not found."
}
```

### Server Error

```json
{
	"detail": "Internal server error"
}
```

## 📝 Rate Limiting

Currently, the API does not implement rate limiting. Future versions will include rate limiting for abuse prevention.

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

    def get_books(self):
        response = self.session.get(f"{self.base_url}books/")
        return response.json()

    def get_book_by_isbn(self, isbn):
        response = self.session.get(f"{self.base_url}books/isbn/{isbn}/")
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

	async getBooks() {
		const response = await fetch(`${this.baseUrl}books/`);
		return await response.json();
	}

	async getBookByIsbn(isbn) {
		const response = await fetch(`${this.baseUrl}books/isbn/${isbn}/`);
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
