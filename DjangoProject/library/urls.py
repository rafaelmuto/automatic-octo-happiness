from django.urls import path


from . import views

app_name = "library"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("books/<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path(
        "author/<int:author_id>/",
        views.IndexByAuthorView.as_view(),
        name="index_by_author",
    ),
    path("authors/", views.AuthorList.as_view(), name="author_list"),
    path("authors/<int:pk>/", views.AuthorDetail.as_view(), name="author_detail"),
    path("authors/add/", views.AuthorCreate.as_view(), name="author_add"),
    path("authors/<int:pk>/edit/", views.AuthorUpdate.as_view(), name="author_edit"),
    path("books/add/", views.BookCreate.as_view(), name="book_add"),
    path("books/<int:pk>/edit/", views.BookUpdate.as_view(), name="book_edit"),
]
