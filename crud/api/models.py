from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class ModelUser(models.Model):
    username = models.CharField("Username", max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    password = models.CharField("Password",
                                max_length=128,
                                validators=[RegexValidator(
                                    regex=r'^(?=.*[A-Z])(?=.*\d).{8,}$',
                                    message='Не правильно задан пароль')]
                                )
    last_login = models.DateTimeField(default=timezone.datetime.now())
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ('username', 'password',)

    def __str__(self):
        return self.username

