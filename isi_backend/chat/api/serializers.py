from chat.models import Message, Thread
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"], username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class ThreadSerializer(serializers.ModelSerializer):
    """Thread serializer."""

    last_message = serializers.SerializerMethodField()

    class Meta:
        """Meta."""

        model = Thread
        fields = ("id", "updated", "participants", "last_message")

    @staticmethod
    def validate_participants(participants):
        """Check participants(count and avoid participants: [1, 1]"""

        if len(participants) != 2:
            raise serializers.ValidationError("Error count participants")
        if participants[0] == participants[1]:
            raise serializers.ValidationError("Error duplication participants")

        return participants

    def create(self, validated_data):
        """Add tread."""

        valid_participants = validated_data.get("participants")
        # find Thread
        thread = (
            Thread.objects.filter(participants=valid_participants[0])
            .filter(participants=valid_participants[1])
            .first()
        )
        if not thread:
            thread = Thread.objects.create()
            thread.participants.set(valid_participants)
            thread.save()
        return thread

    @staticmethod
    def get_last_message(obj):
        """Message."""
        messages = obj.thread_message.filter().order_by("created").first()
        return MessageSerializer(messages).data


class MessagesSerializer(serializers.ModelSerializer):
    """Messages Serializer."""

    class Meta:
        """Meta."""

        model = Message
        fields = ("id", "text", "is_read", "thread", "sender", "created")


class MessageSerializer(serializers.ModelSerializer):
    """One message serializer to create message."""

    class Meta:
        """Meta."""

        model = Message
        fields = ("text",)
