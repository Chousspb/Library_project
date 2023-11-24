from django.contrib.auth.models import AbstractUser
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from library.tasks import send_welcome_email
        send_welcome_email.delay(self.id) # Отправляем письмо асинхронно