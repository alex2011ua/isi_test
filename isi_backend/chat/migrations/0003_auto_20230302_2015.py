# Generated by Django 4.1.7 on 2023-03-02 19:15

from django.conf import settings
from django.db import migrations
from django.utils import timezone
import time


def add_new_thread(apps, schema_editor):
    Thread = apps.get_model("chat", "Thread")
    thread = Thread(
        created=timezone.now(),
    )
    Thread.objects.bulk_create((thread,))
    User = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
    user1 = User.objects.get(username="user1")
    user2 = User.objects.get(username="user2")
    thread.participants.set((user1, user2))


def delete_thread(apps, schema_editor):
    Thread = apps.get_model("chat", "Thread")
    Thread.objects.all().delete()


def add_new_message(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
    user = User.objects.get(username="user1")
    Thread = apps.get_model("chat", "Thread")
    thread = Thread.objects.all()[0]
    Message = apps.get_model("chat", "Message")

    message = []
    for number in range(5):
        message.append(
            Message(
                text=f"text message {number}",
                sender=user,
                thread=thread,
                created=timezone.now(),
            )
        )
        time.sleep(0.1)
    Message.objects.bulk_create(message)


def delete_message(apps, schema_editor):
    Message = apps.get_model("chat", "Message")
    Message.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_auto_20230302_1851"),
    ]

    operations = [
        migrations.RunPython(add_new_thread, delete_thread),
        migrations.RunPython(add_new_message, delete_message),
    ]
