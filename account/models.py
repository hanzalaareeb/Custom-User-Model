from django.db import models
from django.contrib.auth.models import AbstractUser, Group, User, Permission

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
