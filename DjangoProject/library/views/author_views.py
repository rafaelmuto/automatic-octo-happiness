from django.urls import reverse_lazy
from django.views import generic


from library.models import Author
from library.forms import AuthorForm


class AuthorDetail(generic.DetailView):
    model = Author
    context_object_name = "author"


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


class AuthorDelete(generic.DeleteView):
    model = Author
    template_name = "library/author_confirm_delete.html"
    success_url = reverse_lazy("library:author_list")


class AuthorList(generic.ListView):
    model = Author
    context_object_name = "author_list"

    def get_queryset(self):
        """
        Return the list of authors.
        """
        return Author.objects.all()