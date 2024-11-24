from django.shortcuts import render
"BookList", "generics.ListAPIView", "from .serializers import BookSerializer"
# api/views.py

from rest_framework import viewsets
from .models import Book  # Ensure this is the correct import for your Book model
from .serializers import BookSerializer  # Ensure this is the correct import for your serializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A view set for viewing and editing book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
