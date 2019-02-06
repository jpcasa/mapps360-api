from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    """This class represents the city model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='cities',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=55,
        blank=False,
        unique=True
    )
    code = models.CharField(
        max_length=10,
        blank=False,
        unique=True
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


class Country(models.Model):
    """This class represents the country model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='countries',
        on_delete=models.CASCADE
    )
    cities = models.ManyToManyField(
        City
    )
    name = models.CharField(
        max_length=55,
        blank=False,
        unique=True
    )
    code = models.CharField(
        max_length=10,
        blank=False,
        unique=True
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} - {}".format(self.code, self.name)


class Address(models.Model):
    """This class represents the address model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='addresses',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        blank=False,
        unique=True
    )
    additional = models.CharField(
        blank=True,
        max_length=100
    )
    postal_code = models.CharField(
        blank=False,
        max_length=100
    )
    lat = models.CharField(
        blank=True,
        max_length=255
    )
    long = models.CharField(
        blank=True,
        max_length=255
    )
    city = models.ForeignKey(
        City,
        related_name='addresses',
        on_delete=models.CASCADE
    )
    country = models.ForeignKey(
        Country,
        related_name='addresses',
        on_delete=models.CASCADE
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
