from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    substituted_mail = models.EmailField()

    def __str__(self):
        return self.user.username
