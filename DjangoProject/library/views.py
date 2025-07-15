from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic


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

