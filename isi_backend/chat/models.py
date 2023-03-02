from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    """Class Thread."""

    participants = models.ManyToManyField(User, related_name="message_thread")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def delete_thread(self):
        """Delete all messages and thread."""
        Message.objects.filter(thread=self).delete()
        self.delete()


class Message(models.Model):
    """Class Message."""

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_message")
    text = models.TextField()
    thread = models.ForeignKey(Thread, related_name="thread_message", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

