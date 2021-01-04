"""Urls Home."""
from django.urls import path

from .views import home as home_views

app_name = "home"
urlpatterns = [path("", home_views.HomeTemplateView.as_view(), name="index")]
