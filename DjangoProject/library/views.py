from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .services import OpenLibraryService

from .models import Book


class IndexView(generic.ListView):
    model = Book
    context_object_name = "book_list"

    def get_queryset(self):
        """
        Return the list of books.
        """
        return Book.objects.all()

class IndexByAuthorView(generic.ListView):
    model = Book
    context_object_name = "book_list"

    def get_queryset(self):
        """
        Return the list of books by a specific author.
        """
        author_id = self.kwargs.get("author_id")
        return Book.objects.filter(author_id=author_id)


def open_library_view_isbn(request):
    isbn = "9780140328721"  # Example ISBN
    book_data = OpenLibraryService.search_by_isbn(isbn)
    if book_data:
        # Do something with the book data
        print(book_data['title'])
    else:
        # Handle the case where the book is not found
        print("Book not found.")
