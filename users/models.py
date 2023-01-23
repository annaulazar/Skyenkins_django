from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

from users.managers import UserManager


NULLABLE = {'null': True, 'blank': True}


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    ROLE = ((USER, 'Пользователь'), (ADMIN, 'Администратор'))


class User(AbstractUser):

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    username = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(unique=True, verbose_name="Почта", null=False)
    role = models.CharField(max_length=5, choices=UserRoles.ROLE, default=UserRoles.USER, verbose_name='Роль')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER
