from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'


class Category(models.Model):
    parent = models.ForeignKey('main.Category', on_delete=models.RESTRICT, null=True, default=None)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Kategory'
        verbose_name_plural = 'Kategoriyalar'


class Unit(models.Model):
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    class Meta:
        verbose_name = "O'lchov birligi"
        verbose_name_plural = "O'lchov birliklari"