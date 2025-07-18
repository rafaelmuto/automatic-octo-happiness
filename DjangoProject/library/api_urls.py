from django.urls import path

from .api import author_api, book_api, openlibrary_api

urlpatterns = [
    path("authors/", author_api.AuthorListAPIView.as_view(), name="author-list"),
    path("authors/<int:pk>/", author_api.RetrieveUpdateDestroyAPIView.as_view(), name="author-detail-pk"),
    path("authors/books/<int:pk>/", author_api.AuthorDetailAPIView.as_view(), name="author-books-detail"),
    path("books/", book_api.BookListAPIView.as_view(), name="book-list"),
    path("books/isbn/<str:isbn>/", book_api.BookDetailByIsbnAPIView.as_view(), name="book-detail-isbn"),
    path("books/<int:pk>/", book_api.RetrieveUpdateDestroyAPIView.as_view(), name="book-detail-pk"),
    path("books/author/<int:author_id>", book_api.BookListByAuthorIdAPIView.as_view(), name="book-author-list"),
    path("openlibrary/isbn/<str:isbn>/", openlibrary_api.search_by_isbn_view, name="openlibrary-isbn"),
    path("openlibrary/key/<str:key>/", openlibrary_api.get_data_by_key_view, name="openlibrary-key"),
]
