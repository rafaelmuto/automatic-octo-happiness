from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('sudoku/', views.SudokuListCreateView.as_view(), name='sudoku-list-create'),
    path('sudoku/<int:pk>/', views.SudokuRetrieveUpdateDestroyView.as_view(), name='sudoku-retrieve-update-destroy'),
]