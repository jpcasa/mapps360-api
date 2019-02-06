from django.db import models
from django.contrib.auth.models import User

class FloorPlan(models.Model):
    """This class represents the picture model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='floor_plans',
        on_delete=models.CASCADE
    )
    plan = models.ImageField(
        upload_to="properties/floor_plans/"
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.plan)
