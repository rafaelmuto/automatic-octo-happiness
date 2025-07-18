from django.http import JsonResponse

from ..services import OpenLibraryService

def search_by_isbn_view(request, isbn):
    book_data = OpenLibraryService.search_by_isbn(isbn)
    if book_data:
        return JsonResponse(book_data)
    else:
        return JsonResponse({"error": "Book not found"}, status=404)


def get_data_by_key_view(request, key):
    data = OpenLibraryService.get_data_by_key(f"/{key.replace('-', '/')}")
    if data:
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Data not found"}, status=404)