from django.urls import reverse_lazy
from django.views import generic


from library.models import Book
from library.forms import BookForm


class BookDetail(generic.DetailView):
    model = Book
    context_object_name = "book"


class BookCreate(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:index")


class BookUpdate(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = "library/book_form.html"
    success_url = reverse_lazy("library:index")


class BookDelete(generic.DeleteView):
    model = Book
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("library:index")


class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"

    def get_queryset(self):
        """
        Return the list of books.
        """
        return Book.objects.all()


class BookListByAuthorView(generic.ListView):
    model = Book
    context_object_name = "book_list"

    def get_queryset(self):
        """
        Return the list of books by a specific author.
        """
        author_id = self.kwargs.get("author_id")
        return Book.objects.filter(author_id=author_id)