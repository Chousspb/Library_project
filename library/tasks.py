from celery import shared_task
from django.core.mail import send_mail
from library.models import CustomUser

@shared_task # Декоратор, который позволяет использовать функцию как Celery-таск
def send_welcome_email(user_id):
    user = CustomUser.objects.get(id=user_id)
    print(f'Sending email to {user.email}')
    subject = 'Welcome to Our Library!'
    message = f'Hello {user.username},\n\nThank you for registering on our library platform!'
    from_email = 'admin@admin.ru'
    to_email = [user.email]
    send_mail(subject, message, from_email, to_email, fail_silently=False) # Отправляем письмо
