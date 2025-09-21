from django.shortcuts import render, HttpResponse
from rest_framework import generics, status
from .models import Sudoku
from .serializers import SudokuSerializer

# Create your views here.
def base(request):
    return HttpResponse("Hello, World! from api app")

class SudokuListCreateView(generics.ListCreateAPIView):
    """
    GET: List all Sudoku puzzles
    POST: Create a new Sudoku puzzle
    """

    queryset = Sudoku.objects.all()
    serializer_class = SudokuSerializer

    def perform_create(self, serializer):
        """
        Customize the creation process
        This method is called when creating a new Sudoku
        """
        if self.request.user.is_authenticated:
            # If user is logged in, associate the Sudoku with them
            serializer.save(created_by=self.request.user)
        else:
            # If user is not logged in, create without user association
            serializer.save()

class SudokuRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a specific Sudoku puzzle
    PUT/PATCH: Update a specific Sudoku puzzle
    DELETE: Delete a specific Sudoku puzzle
    """
    queryset = Sudoku.objects.all()
    serializer_class = SudokuSerializer
    