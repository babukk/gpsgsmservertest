
from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# Модель 'Пользователи/Учётные записи'

# --------------------------------------------------------------------------------------------------
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(_('Имя пользователя'), unique=True, db_index=True, max_length=120)
    # Добавляем поля:
    username = models.CharField('Имя пользователя', unique=True, db_index=True, max_length=120)
    email = models.EmailField('email')
    is_active = models.BooleanField(default=True)
    # флаг 'сотрудник'
    is_staff = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    # Устанавливаем USERNAME_FIELD, которое определяет уникальный идентификатор для модели User значением username:
    USERNAME_FIELD = 'username'

    # обязательные поля (их пока нет):
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    # ----------------------------------------------------------------------------------------------
    def __str__(self):
        return self.username

    class Meta:
        # ordering = ['username']
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"
