from django.contrib import admin
from .models import User, Authorization
# Register your models here.

admin.site.register(User)
admin.site.register(Authorization)