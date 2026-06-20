from django.db import models
from django.contrib.auth.models import AbstractUser
from services.idgenerator_svc import generate_id


class User(AbstractUser):
    id = models.CharField(
        primary_key=True,
        default=generate_id,
        max_length=10,
        editable=False
    )

    email = models.EmailField(
        unique=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username'
    ]

    def __str__(self):
        return self.email