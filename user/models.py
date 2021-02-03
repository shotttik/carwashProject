from django.db import models
from django.contrib.auth.models import AbstractUser
from .status_choices import Status
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        validate_email(email)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('status', 3)
        extra_fields.setdefault('phone', 0)
        extra_fields.setdefault('joined', timezone.now())
        extra_fields.setdefault('salary', 0)
        extra_fields.setdefault('image', "images/placeholder.jpg")
        extra_fields.setdefault('birthdate', timezone.now())

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='E-Mail', unique=True)
    birthdate = models.DateField(verbose_name='Birthdate')
    phone = models.CharField(verbose_name='Mobile phone number', max_length=9, unique=True)
    joined = models.DateField(verbose_name="Joined")
    image = models.ImageField(upload_to='images/')
    status = models.PositiveSmallIntegerField(choices=Status.choices)
    salary = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Salary", default=0,
                                 help_text="In USD")

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
