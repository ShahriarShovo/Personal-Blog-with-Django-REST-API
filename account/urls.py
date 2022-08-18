from xml.etree.ElementInclude import include
from django.urls import path
from account.views import admin_login


urlpatterns = [
    path('login/', admin_login)
]
