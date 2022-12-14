"""Django models utilities."""

from django.db import models

class CRideModel(models.Model):
    """ComparteRide base model.

    CRideModel acts as an abstract class, which every
    other model in the project will inherit from. This class 
    provides every table with the following attributes:
        + created (DateTime): Stores the datetime the object was created at.
        + modified (DateTime): Stores the datetime the object was last modified.
    """

    created = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        help_text='Date and time on which the object was created at.'
    )

    modified = models.DateTimeField(
        'modified_at',
        auto_now=True,
        help_text='Date and time on which the object was last modified.'
    )

    class Meta:
        """Meta options"""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']