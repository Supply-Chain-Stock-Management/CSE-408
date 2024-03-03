from django.db import models
from django.utils import timezone

class PendingUser(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
