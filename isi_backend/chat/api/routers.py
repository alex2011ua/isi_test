from chat.api import views
from chat.api.views import RegisterView
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
from chat.api.views import UserViewSet, ThreadViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="sign_up"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),

    path(
        "user/<int:pk>/", views.UserThreads.as_view(), name="user_threads"
    ),  # View all user's thread with last message with pagination
    path(
        "message/thread/<int:pk>/", views.get_create_message, name="get_create_messages"
    ),
    path("message/notread/", views.messages_not_read, name="messages_not_read"),
]

router = DefaultRouter()
thread_router = DefaultRouter()

router.register(r"users", UserViewSet, basename="user")
router.register(r"threads", ThreadViewSet, basename="thread")

urlpatterns.extend(router.urls)
urlpatterns.extend(thread_router.urls)
