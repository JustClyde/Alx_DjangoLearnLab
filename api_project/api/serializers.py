from rest_framework import serializers
from .models import Book  # Make sure to import your Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # The model to serialize
        fields = '__all__'  # Include all fields from the Book model
