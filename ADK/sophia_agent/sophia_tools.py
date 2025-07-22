import requests

SOPHIA_LIBRARY_URL = "http://localhost:8001/"

def get_library_books_list() -> dict:
    """ Retrieves a list of books in the library """
    try:
        response = requests.get(SOPHIA_LIBRARY_URL + 'api/library/books/')
        response.raise_for_status()    
        return response.json()
    except Exception as e:
        return {
            'status': 'error',
            'error_message': f'error while fetching data from sophia library: {e}'
        }
    

def get_book_by_isbn(isbn: str) -> dict:
    """ Retrieves a book by it's ISBN """
    try:
        response = requests.get(SOPHIA_LIBRARY_URL + 'api/library/books/' + isbn)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {
            'status': 'error',
            'error_message': f'error while fetching data from sophia library: {e}'
        }
    
        
def get_authors_list() -> dict:
    try:
        response = requests.get(SOPHIA_LIBRARY_URL + 'api/library/authors/')
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {
            'status': 'error',
            'error_message': f'error while fetching data from sophia library: {e}'
        }
    

def get_books_by_author_id(id: str) -> dict:
    try:
        response = requests.get(SOPHIA_LIBRARY_URL + 'api/library/books/author/' + id)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {
            'status': 'error',
            'error_message': f'error while fetching data from sophia library: {e}'
        }
    