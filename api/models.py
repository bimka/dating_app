from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

from .managers import CustomUserManager

class Client(AbstractUser):    
    avatar = models.ImageField(upload_to = "static/images/", verbose_name="Аватарка")
    gender = models.CharField(
        max_length = 10,
        verbose_name="Пол",
        choices = (('male', 'Кот'), ('female', 'Кошка')),
        default = 'male')
    first_name = models.CharField(
        verbose_name="Имя",
        max_length = 30, 
        validators=[MinLengthValidator(2, "Имя не менее 2 символов!")])
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length = 30, 
        validators=[MinLengthValidator(2, "Фамилия не менее 2 символов!")])
    email = models.EmailField(verbose_name="Email", unique=True)    
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []    
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}"
        