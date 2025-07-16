from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic


from library.models import Author
from library.forms import AuthorForm


class AuthorDetail(LoginRequiredMixin, generic.DetailView):
    model = Author
    context_object_name = "author"


class AuthorCreate(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "library/author_form.html"
    success_url = reverse_lazy("library:author_list")


class AuthorUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "library/author_form.html"
    success_url = reverse_lazy("library:author_list")


class AuthorDelete(LoginRequiredMixin, generic.DeleteView):
    model = Author
    template_name = "library/author_confirm_delete.html"
    success_url = reverse_lazy("library:author_list")


class AuthorList(LoginRequiredMixin, generic.ListView):
    model = Author
    context_object_name = "author_list"

    def get_queryset(self):
        """
        Return the list of authors.
        """
        return Author.objects.all()