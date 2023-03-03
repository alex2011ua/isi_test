from django.urls import path

from chat.api import views
# create Thread
# delete Thread
# list Thread by User
# create or list Messages for Thread
#
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from chat.api.views import RegisterView
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("thread/", views.ThreadCreate.as_view(), name="thread_create"),
    path("user/<int:pk>/", views.UserThreads.as_view(), name="user_threads"),
    path("message/notread/", views.messages_not_read, name="messages_not_read"),
    path("message/thread/<int:pk>/", views.get_create_message, name="get_create_messages"),
]
