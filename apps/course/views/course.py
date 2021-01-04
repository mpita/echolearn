"""Views Course."""
from django.views.generic import ListView

from apps.course.models import Course


class CourseListView(ListView):
    """ListView Course."""

    template_name = "course/course-list.html"
    model = Course
