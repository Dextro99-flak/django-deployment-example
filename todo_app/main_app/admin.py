from django.contrib import admin
from main_app.models import Task, UserProfile
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Task)
admin.site.register(UserProfile)
