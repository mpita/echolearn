"""Admin Course."""
from django.contrib import admin

from .models import Course


@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    """Courses admin."""

    list_display = ("title", "slug", "is_active", "created", "modified")
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("is_active",)
