from django.urls import path

from chat import views


urlpatterns = [
    # chat on pv page
    path("pv/", views.PVChatView.as_view(), name="pv-chat"),
]
