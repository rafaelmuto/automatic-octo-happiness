from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "birth_date", "death_date", "country"]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
            "death_date": forms.DateInput(attrs={"type": "date"}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "publish_date",
            "publisher",
            "number_of_pages",
            "isbn",
        ]
        widgets = {
            "publish_date": forms.DateInput(attrs={"type": "date"}),
        }
