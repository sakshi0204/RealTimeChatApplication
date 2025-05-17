from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Room model (for chat rooms)
class Room(models.Model):
    room_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.room_name

# Message model (for chat messages)
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=50)
    message = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='chat_files/', null=True, blank=True)  # <-- Added FileField for media
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{str(self.room)} - {self.sender} at {self.created_at}"

# Custom User model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('faculty', 'Faculty'),
        ('alumni', 'Alumni'),
    ]
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    college_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username
