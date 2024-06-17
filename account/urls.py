from django.urls import path

from account import views


urlpatterns = [
    # logout path
    path("logout/", views.LogoutView.as_view(), name="logout"), 
]
