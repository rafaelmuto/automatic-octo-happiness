from django.urls import path
from . import views

urlpatterns = [
    path('', views.SudokuListCreateView.as_view(), name='sudoku-list-create'),
    path('<int:pk>/', views.SudokuRetrieveUpdateDestroyView.as_view(), name='sudoku-retrieve-update-destroy'),
]