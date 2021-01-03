"""Views Home."""
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    """TemplateView Home."""

    template_name = "home/home.html"
