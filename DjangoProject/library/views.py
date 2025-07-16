from django.urls import reverse_lazy
from django.views import generic


from .forms import AuthorForm, BookForm
from .models import Author, Book


class AuthorCreate(generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "library/author_form.html"
    success_url = reverse_lazy("library:author_list")


class AuthorUpdate(generic.UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "library/author_form.html"
    success_url = reverse_lazy("library:author_list")


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


class AuthorDelete(generic.DeleteView):
    model = Author
    template_name = "library/author_confirm_delete.html"
    success_url = reverse_lazy("library:author_list")


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


class AuthorList(generic.ListView):
    model = Author
    context_object_name = "author_list"

    def get_queryset(self):
        """
        Return the list of authors.
        """
        return Author.objects.all()


class AuthorDetail(generic.DetailView):
    model = Author
    context_object_name = "author"


class BookDetail(generic.DetailView):
    model = Book
    context_object_name = "book"
