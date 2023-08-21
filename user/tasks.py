from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import string

from celery import shared_task

@shared_task
def generate_random_users(total):
    for i in range(total):
        user_name = f"user_{get_random_string(10,string.ascii_letters)}"
        email = f"{user_name}@gmail.com"
        password = get_random_string(50)
        User.objects.create_user(username=user_name,email=email,password=password)
    return f"{total} random users created successfully!!"

