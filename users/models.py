from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_types = [
        ('D', 'Doctor'),
        ('P', 'Patient'),
    ]
    user_type = models.CharField(
        max_length = 2,
        choices = user_types,
    )

    def __str__(self):
        return self.username