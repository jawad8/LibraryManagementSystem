from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser

# Create your models here.



class USERS(AbstractUser):
    account_types = ((1, "admin"), (2, 'student')) 
    first_name = models.CharField(max_length=200, default=None, null=True)
    account_type = models.IntegerField(choices = account_types, default= 2, null = True)


class BOOKS(models.Model):
    book_id = models.CharField(max_length=200, default=None, null=True)
    book_name = models.CharField(max_length=200, default=None, null=True)
    book_author = models.CharField(max_length=200, default=None, null=True)
    book_description = models.CharField(max_length=200, default=None, null=True, blank=True)