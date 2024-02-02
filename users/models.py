from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13)
    image_user = models.ImageField(default='media/user_default_image.png', upload_to='media/')

    def __str__(self):
        return self.username


class Meta:
  db_table = 'users_table'

