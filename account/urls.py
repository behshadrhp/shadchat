from django.urls import path

from account import views


urlpatterns = [
    # login path
    path("login/", views.LoginView.as_view(), name="login"),
    # register path
    path("register/", views.RegisterView.as_view(), name="register"),
    # logout path
    path("logout/", views.LogoutView.as_view(), name="logout"), 
]
