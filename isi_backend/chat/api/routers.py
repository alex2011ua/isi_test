from django.urls import path

from chat.api import views
# create Thread
# delete Thread
# list Thread by User
# create or list Messages for Thread
#

urlpatterns = [
    path("thread/", views.ThreadListAdd.as_view(), name="thread_list_add"),
    path(
        "thread/<int:pk>/delete_participants/<int:id_participants>/",
        views.thread_delete,
        name="thread_delete",
    ),
    path("thread/<int:pk>/", views.ThreadInfo.as_view(), name="thread_info"),
    path("message/thread/<int:pk>/", views.get_create_message, name="get_create_messages"),
    path("message/<int:pk>/", views.read_modify_delete, name="message_read_modify_delete"),
    path("message/read/", views.message_read, name="message_read"),
]
