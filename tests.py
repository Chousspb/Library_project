from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from library.models import Book, CustomUser


class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Sample Book",
            author="Sample Author",
            year=2022,
            isbn="1234567890"
        )

    def test_book_str(self):
        self.assertEqual(str(self.book), "Sample Book")


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username="sample_user",
            email="user@example.com",
        )

    def test_user_str(self):
        self.assertEqual(str(self.user), "sample_user")


class BookAPITest(TestCase):
    class BookAPITest(TestCase):
        def setUp(self):
            self.client = APIClient()
            self.book_data = {
                'title': 'Test Book',
                'author': 'Test Author',
                'year': 2022,
                'isbn': '1234567890',
            }
            self.response = self.client.post(reverse('book_list'), data=self.book_data)

        def test_create_book(self):
            self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Book.objects.count(), 1)
            self.assertEqual(Book.objects.get().title, 'Test Book')

        def test_get_book_list(self):
            response = self.client.get(reverse('book_list'))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]['title'], 'Test Book')