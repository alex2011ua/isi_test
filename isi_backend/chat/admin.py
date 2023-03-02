from django.contrib import admin
from django.contrib.auth.models import Group

from chat.models import Message, Thread


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "thread", "text", "created", "is_read")


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ("created", "updated")
    raw_id_fields = ("participants",)


admin.site.unregister(Group)
