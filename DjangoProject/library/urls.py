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
]
