from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    text = models.CharField(max_length=100)
    complete = models.BooleanField()

    def __str__(self):
        return str(self.text)