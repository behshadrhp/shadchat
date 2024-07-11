from django.urls import path

from chat import views


urlpatterns = [
    # chat on pv page
    path("pv/<str:username>/", views.PVChatView.as_view(), name="chat-pv"),
]
