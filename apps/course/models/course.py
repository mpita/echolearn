"""Model Course."""
from django.db import models
from django.utils.text import slugify

from apps.utils.models import AppModel


def image_course_upload_url(instance, filename):
    """
    Url image.

    :param filename: Archivo/Imagen
    :return: path: Ruta de Imagen
    """
    url = "image/course/{}/{}".format(instance.slug, filename)
    return url.lower()


class Course(AppModel):
    """Model Courses."""

    title = models.CharField("Title", max_length=200, unique=True)
    image = models.ImageField(upload_to=image_course_upload_url, blank=True)
    slug = models.SlugField("Slug", max_length=200, blank=True, unique=True)
    description = models.TextField("Description")
    is_active = models.BooleanField(
        "active status", default=True, help_text="Used for disabling the Course."
    )

    def save(self, *args, **kwargs):
        """Modify slug when saving if it is empty."""
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        """Return the string representation of the object."""
        return self.title
