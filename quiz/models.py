from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, is_staff=False, is_active=True, is_superuser=False):

        if not username:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Must have pas')

        user = self.model(
            username=username
        )
        user.is_staff = is_staff
        user.is_active = is_active
        user.is_superuser = is_superuser
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, username, password=None,):
        user = self.create_user(
            username,
            password=password,
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField("Пароль", max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.get_username()


class Poll(models.Model):
    name = models.CharField(max_length=200, )
    start_date = models.DateTimeField(default=datetime.now())
    end_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=4096)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    choice_pk = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    choice_text = models.CharField(max_length=200)
    anon_id = models.IntegerField()

    def __str__(self):
        return self.choice_text
