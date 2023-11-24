from django.urls import path
from .views import BookListCreateView, BookDetailView
from .views import book_list, UserRegistrationView

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
