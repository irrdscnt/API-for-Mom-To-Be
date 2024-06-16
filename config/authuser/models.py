from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin


class AuthUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class AuthUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=2000, blank=True, null=True)
    phone = models.TextField(max_length=2000, blank=True, null=True)
    pregnancy_week = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AuthUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'pregnancy_week']

    def __str__(self):
        return self.email

class NutritionAdvice(models.Model):
    photo = models.ImageField(upload_to='nutrition_photos/')
    description = models.TextField(max_length=2000)
    trimester = models.PositiveIntegerField()
    week=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Trimester {self.trimester} - {self.description[:50]}"

class Baby(models.Model):
    trimester = models.PositiveIntegerField()
    week = models.PositiveIntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='baby/')

    def __str__(self):
        return f"Week {self.week}, Trimester {self.trimester}"
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField(default=datetime.time(0, 0))

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'