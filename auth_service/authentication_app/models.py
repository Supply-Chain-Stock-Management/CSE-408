from django.db import models
from django.utils import timezone

class Entity(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PendingUser(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    entity = models.ForeignKey(Entity, on_delete=models.SET_NULL, null=True, blank=True, related_name='pending_users')

    def __str__(self):
        return self.username