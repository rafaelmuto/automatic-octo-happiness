from django.urls import path
from . import api

urlpatterns = [
    path("books/", api.BookListAPIView.as_view(), name="book-list"),
    path(
        "openlibrary/isbn/<str:isbn>/", api.search_by_isbn_view, name="openlibrary-isbn"
    ),
    path(
        "openlibrary/key/<str:key>/", api.get_data_by_key_view, name="openlibrary-key"
    ),
]
