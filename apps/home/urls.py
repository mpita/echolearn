"""Urls Home."""
from django.urls import path

from .views import home as home_views

urlpatterns = [path("", home_views.HomeTemplateView.as_view(), name="index")]
