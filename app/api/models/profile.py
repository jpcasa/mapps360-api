from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """This class represents the profile model."""
    SUBSCRIPTIONS = (
        ('A', 'Free'),
        ('B', 'Agent'),
        ('C', 'Pro'),
        ('D', 'Enterprise')
    )
    user = models.OneToOneField(
        'auth.User',
        on_delete=models.CASCADE
    )
    subscription = models.CharField(
        blank=False,
        max_length=100,
        choices=SUBSCRIPTIONS
    )
    avatar = models.ImageField(
        upload_to='users/avatars/',
        default='users/avatars/user.jpg'
    )
    phone = models.CharField(
        blank=True,
        max_length=100
    )

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.user.email)
