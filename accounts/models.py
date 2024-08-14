from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_company_admin = models.BooleanField(default=False)
    is_client_customer = models.BooleanField(default=False)
