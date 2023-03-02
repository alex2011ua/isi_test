from django.contrib import admin

from chat.models import Message, Thread


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "thread", "text", "created", "is_read")


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ("created_at", "updated_at")
    raw_id_fields = ("participants",)
