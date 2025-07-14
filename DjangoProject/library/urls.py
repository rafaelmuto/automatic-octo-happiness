from django.urls import path

from . import views

app_name = "library"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('author/<int:author_id>/', views.IndexByAuthorView.as_view(), name='index_by_author'),
]
