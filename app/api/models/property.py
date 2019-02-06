from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

from .address import Address

class Property(models.Model):
    """This class represents the property model."""
    PRICE_MODES = (
        ('A', 'Arriendo'),
        ('B', 'Compra'),
    )
    PROPERTY_TYPES = (
        ('A', 'Apartamentos'),
        ('B', 'Bodegas'),
        ('C', 'Casas'),
        ('D', 'Consultorios'),
        ('E', 'Edificio de oficinas'),
        ('F', 'Edificio de apartamentos'),
        ('G', 'Fincas'),
        ('H', 'Locales'),
        ('I', 'Lotes'),
        ('J', 'Oficinas')
    )
    STATUS = (
        ('A', 'Público'),
        ('B', 'Privado'),
        ('C', 'Borrador')
    )
    owner = models.ForeignKey(
        'auth.User',  # ADD THIS FIELD
        related_name='properties',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True
    )
    url = models.CharField(
        max_length=255,
        unique=True,
        null=True
    )
    address = models.OneToOneField(
        'api.Address',
        on_delete=models.PROTECT,
        null=True
    )
    ammenities = models.ManyToManyField(
        'api.Ammenity'
    )
    description = models.TextField(
        blank=True
    )
    price = models.IntegerField(
        blank=True,
        null=True
    )
    mode = models.CharField(
        max_length=50,
        choices=PRICE_MODES,
        null=True
    )
    type = models.CharField(
        max_length=255,
        choices=PROPERTY_TYPES,
        null=True
    )
    year_built = models.DateField(
        null=True
    )
    square_meters = models.IntegerField(
        blank=True,
        null=True
    )
    rooms = models.IntegerField(
        blank=True,
        null=True
    )
    bathrooms = models.IntegerField(
        blank=True,
        null=True
    )
    garages = models.IntegerField(
        blank=True,
        null=True
    )
    pictures = models.ManyToManyField(
        'api.Picture'
    )
    floor_plan = models.OneToOneField(
        'api.FloorPlan',
        on_delete=models.PROTECT,
        null=True
    )
    status = models.CharField(
        max_length=255,
        choices=STATUS,
        null=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_modified = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
