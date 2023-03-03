from django.db import migrations
from django.conf import settings
from django.contrib.auth.hashers import make_password


def add_user(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))

    User.objects.create(
        username="user1",
        email='user1@user1.user1',
        password=make_password('user1'),
    )
    User.objects.create(
        username="user2",
        email='user2@user2.user2',
        password=make_password('user2'),
    )
    User.objects.create(
        username="user3",
        email='user3@user3.user3',
        password=make_password('user3'),
    )


def remove_user(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))
    User.objects.get(username='user1').delete()
    User.objects.get(username='user2').delete()
    User.objects.get(username='user3').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_user, remove_user),


    ]
