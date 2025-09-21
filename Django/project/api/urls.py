from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('sudoku/', include('sudoku.urls')),
]