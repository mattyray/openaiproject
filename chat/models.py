from django.db import models
from django.conf import settings

class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    is_user = models.BooleanField(default=True)  # True if message is from user, False if from AI
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.text[:50]}"
