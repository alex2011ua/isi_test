from chat.api.serializers import (MessageSerializer, MessagesSerializer,
                                  ThreadSerializer, UserSerializer)
from chat.models import Message, Thread
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status
from rest_framework import viewsets
from django.contrib.auth.models import User


class RegisterView(APIView):
    """view for registering users"""

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserThreads(generics.ListAPIView):
    """View all user's thread with last message with pagination."""

    serializer_class = ThreadSerializer

    def get_queryset(self):
        return Thread.objects.filter(participants=self.kwargs.get("pk"))


@api_view(("GET", "POST"))
@permission_classes([IsAuthenticated])
def get_create_message(request, *args, **kwargs):
    """Return messages or add message in the thread."""

    thread = Thread.objects.filter(id=kwargs.get("pk")).first()
    if not thread:
        raise NotFound
    if request.method == "GET":
        message = Message.objects.filter(thread=thread)
        return Response(
            data=MessagesSerializer(message, many=True).data, status=status.HTTP_200_OK
        )
    if request.method == "POST":
        # create message in the thread wiht user auth
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_message = serializer.save(sender=request.user, thread=thread)
        return Response(data=MessagesSerializer(new_message).data)


@api_view(("GET",))
@permission_classes([IsAuthenticated])
def messages_not_read(request, *args, **kwargs):
    """Return count of unread messages for the user"""

    user = request.user
    count_unread_messages = Message.objects.filter(sender=user, is_read=False).count()
    return Response({"message": count_unread_messages})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    def list(self, request):
        return Response(status=200)

