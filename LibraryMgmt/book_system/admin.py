from django.contrib import admin
from .models import BOOKS
from .models import USERS

# Register your models here.

admin.site.register(BOOKS)
admin.site.register(USERS)

