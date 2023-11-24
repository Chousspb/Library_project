from .forms import CustomUserCreationForm
from django.shortcuts import render
from .models import Book, CustomUser
from .serializers import BookSerializer, CustomUserSerializer
from rest_framework import generics
from library.tasks import send_welcome_email

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    form_class = CustomUserCreationForm

    def get(self, request, *args, **kwargs):
        # Render the registration form
        form = self.form_class()
        return render(request, 'registration_form.html', {'form': form})

    def perform_create(self, serializer):
        user = serializer.save()

        # Асинхронная отправка приветственного письма через Celery
        send_welcome_email.delay(user.id)
