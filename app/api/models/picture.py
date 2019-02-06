from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    """This class represents the picture model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='pictures',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="properties/images/"
    )
    show = models.BooleanField(
        default=True
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.image)
