# blog/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Page(models.Model):
    title = models.CharField(max_length=150, null=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

# Perfil extendido del usuario para añadir campos adicionales.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=250, blank=True)
    website_url = models.URLField(max_length=250, blank=True)

