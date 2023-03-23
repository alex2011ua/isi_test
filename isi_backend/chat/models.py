from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Thread(models.Model):
    """Thread model"""

    participants = models.ManyToManyField(
        User, related_name="message_thread", verbose_name=_("User participants")
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated date"))

    class Meta:
        verbose_name = _("thread")
        verbose_name_plural = _("threads")

    def __str__(self):
        all_participants = map(str, (list(self.participants.all())))
        return _("Participants: ") + ", ".join(all_participants)

    def __repr__(self):
        all_participants = map(str, (list(self.participants.all())))
        return _("Participants: ") + ", ".join(all_participants)


class Message(models.Model):
    """Model Message"""

    sender = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="user_message",
        verbose_name=_("Sender user"),
    )
    text = models.TextField(verbose_name=_("Text message"))
    thread = models.ForeignKey(
        Thread,
        related_name="thread_message",
        on_delete=models.DO_NOTHING,
        verbose_name=_("Thread name"),
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created date"))
    is_read = models.BooleanField(default=False, verbose_name=_("Read?"))

    def __str__(self):
        return _("Text message:") + self.text

    def __repr__(self):
        return "message_id: " + str(self.pk)

    class Meta:
        verbose_name = _("message")
        verbose_name_plural = _("messages")
        ordering = ["-created"]
