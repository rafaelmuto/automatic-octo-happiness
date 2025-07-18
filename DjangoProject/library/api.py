from rest_framework import generics
from django.http import JsonResponse

from .models.book import Book
from .models.author import Author
from .serializers import BookSerializer, AuthorSerializer

from .services import OpenLibraryService


class AuthorListAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorSearchAPIView(generics.ListAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Author.objects.filter(name__icontains=name)


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn'


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
