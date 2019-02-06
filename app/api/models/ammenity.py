from django.db import models
from django.contrib.auth.models import User


class Ammenity(models.Model):
    """This class represents the ammenity model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='ammenities',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=55,
        blank=False,
        unique=True
    )
    icon = models.CharField(
        max_length=255,
        blank=False,
        unique=True
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
