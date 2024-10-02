from django.contrib import admin

from django.contrib import admin
from .models import Task  # Make sure to import your models

# Register your models here
admin.site.register(Task)