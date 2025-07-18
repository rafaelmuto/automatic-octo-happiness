from rest_framework import generics

from ..models import Author
from ..serializers import AuthorSerializer

class AuthorListAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorSearchAPIView(generics.ListAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Author.objects.filter(name__icontains=name)