from django.urls import path

from support import views


urlpatterns = [
    # contact us page
    path("contact-us/", views.ContactUSView.as_view(), name="contact-us"), 
]
