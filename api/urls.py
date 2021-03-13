from django.contrib import admin
from django.urls import path
from api import views as user_view


app_name = "api"


urlpatterns = [
    path("", user_view.home, name='home'),
    path("result", user_view.result, name="result"),
]
