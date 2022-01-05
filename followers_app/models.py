from django.db import models
from django.contrib.auth.models import User


class Followers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='followers')