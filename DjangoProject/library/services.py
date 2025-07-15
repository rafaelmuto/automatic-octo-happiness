import requests

class OpenLibraryService:
    BASE_URL = "https://openlibrary.org"
    COVERS_URL = "https://covers.openlibrary.org"

    @staticmethod
    def search_by_isbn(isbn: str) -> dict | None:
        """
        Searches for a book by its ISBN using the OpenLibrary API.
        """
        endpoint = f"{OpenLibraryService.BASE_URL}/api/books"
        params = {
            "bibkeys": f"ISBN:{isbn}",
            "format": "json",
            "jscmd": "data"
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()
            return data.get(f"ISBN:{isbn}")
        except requests.exceptions.RequestException as e:
            # Log the error for debugging purposes
            print(f"Error fetching data from OpenLibrary: {e}")
            return None

    @staticmethod
    def get_data_by_key(open_library_key: str) -> dict | None:
        """
        Retrieves data by a specific OpenLibrary key.
        """
        endpoint = f"{OpenLibraryService.BASE_URL}{open_library_key}.json"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from OpenLibrary: {e}")
            return None

    @staticmethod
    def get_book_cover_url(key_type: str, key_value: str, size: str = 'M') -> str:
        """
        Constructs the URL for a book cover image.
        key_type: 'isbn', 'olid', 'lccn', etc.
        size: 'S', 'M', or 'L'
        """
        return f"{OpenLibraryService.COVERS_URL}/b/{key_type}/{key_value}-{size}.jpg"

    @staticmethod
    def get_author_photo_url(author_olid: str, size: str = 'M') -> str:
        """
        Constructs the URL for an author's photo.
        size: 'S', 'M', or 'L'
        """
        return f"{OpenLibraryService.COVERS_URL}/a/olid/{author_olid}-{size}.jpg"
