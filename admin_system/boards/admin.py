from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)