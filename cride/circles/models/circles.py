"""Circle model"""

#Django
from django.db import models

#Utilities
from cride.utils.models import CRideModel


class Circle(CRideModel):
    """Circle model.
    
    A circel is a private group where rides are offered and taken
    by its members. To join a circle, a user must receive an unique
    invitation code from an existing circle member.
    """

    name = models.CharField('circle name', max_length=40)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(
        upload_to='circles.pictures',
        blank=True,
        null=True
    )

    #Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified_circle',
        default=False,
        help_text='Verified circles are also known as official communities'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Public cirlces are listed in main page so everyone know about their existence'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members.'
    )

    members_limit = models.PositiveIntegerField(
        default = 0,
        help_text='If circle is limited, this will be the limit of the number of members.'
    )

    def __str__(self):
        """Return circle's Slug name"""
        return self.slug_name

    
    class Meta(CRideModel.Meta):
        """Circle Metadata"""
        
        ordering = ['-rides_taken', '-rides_offered']