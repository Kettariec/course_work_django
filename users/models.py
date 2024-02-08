from django.db import models
from django.contrib.auth.models import AbstractUser
import random

random_code = ''.join(random.sample('0123456789', 6))
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=30,
                               verbose_name='страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/',
                               verbose_name="аватар", **NULLABLE)
    verify_code = models.CharField(max_length=6,
                                   default=random_code,
                                   verbose_name='код верификации')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

        permissions = [
            (
                'set_is_active',
                'Can deactivate user'
            )
        ]
