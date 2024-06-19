from django.urls import path

from home import views


urlpatterns = [
    # home page
    path("", views.HomeView.as_view(), name="home"),
    # about us page 
    path("about-us/", views.AboutUSView.as_view(), name="about-us"),
    # contact us page
    path("contact-us/", views.ContactUSView.as_view(), name="contact-us"),  
]
