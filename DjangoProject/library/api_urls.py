from django.urls import path
from . import api

urlpatterns = [
    path("books/", api.BookListAPIView.as_view(), name="book-list"),
    path("books/<str:isbn>/", api.BookDetailAPIView.as_view(), name="book-detail"),
    path("authors/", api.AuthorListAPIView.as_view(), name="author-list"),
    path("authors/<int:pk>/", api.AuthorDetailAPIView.as_view(), name="author-detail"),
    path("authors/name/<str:name>/", api.AuthorSearchAPIView.as_view(), name="author-search"),
    path("openlibrary/isbn/<str:isbn>/", api.search_by_isbn_view, name="openlibrary-isbn"),
    path("openlibrary/key/<str:key>/", api.get_data_by_key_view, name="openlibrary-key"),
]
