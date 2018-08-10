# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
GENDER =(('M','Male'),('F','Female'),('T','Transgender'))

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=30)
	age = models.IntegerField(default=0)
	gender = models.CharField(max_length=1,choices=GENDER)
	password = models.CharField(max_length=20 )

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []


	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'







