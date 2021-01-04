"""Urls Course."""
from django.urls import path

from .views import course as course_views

app_name = "course"
urlpatterns = [path("list/", course_views.CourseListView.as_view(), name="list")]
