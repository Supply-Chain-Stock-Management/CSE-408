from django.db import models
from django.contrib.auth.models import User

class EmailLog(models.Model):
    recipient = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('SENT', 'Sent'),
        ('FAILED', 'Failed'),
        ('PENDING', 'Pending'),
    ])
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return f"EmailLog(id={self.id}, recipient='{self.recipient}', status='{self.status}')"

