from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    """This class represents the review model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='reviews',
        on_delete=models.CASCADE
    )
    stars = models.IntegerField(
        blank=False,
        default=1
    )
    review = models.TextField(
        blank=False
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} - {}".format(self.stars, self.user.username)
