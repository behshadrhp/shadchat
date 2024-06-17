import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar
from dotenv import load_dotenv

from account.views import LogoutView

# Loading environment variable"s
load_dotenv()

if settings.DEBUG:
    ADMIN_DIRECTORY = os.environ.setdefault("ADMIN_DIRECTORY", "admin")
else:
    ADMIN_DIRECTORY = os.environ.get("ADMIN_DIRECTORY")

urlpatterns = [
    # customize logout admin panel
    path(f"{ADMIN_DIRECTORY}/logout/", LogoutView.as_view(), name="logout-admin"),
    # admin panel
    path(f"{ADMIN_DIRECTORY}/", admin.site.urls),
    # account app dir
    path("account/", include("account.urls")),
    # home app dir
    path("", include("home.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#  Media static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug toolbar
if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
