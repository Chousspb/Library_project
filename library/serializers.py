
from rest_framework import serializers
from .models import Book, CustomUser

class BookSerializer(serializers.ModelSerializer): #  сериализатор для модели Book
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year', 'isbn']

class CustomUserSerializer(serializers.ModelSerializer): #  сериализатор для модели CustomUser
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'date_joined', 'password']
        extra_kwargs = {'password': {'write_only': True}}
