from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models, migrations
from django.contrib.postgres.operations import TrigramExtension
from os import getenv
import geocoder

class Migration(migrations.Migration):
    operations = [
        TrigramExtension()
    ]



class Venue(models.Model):
    RATING_CHOICES = [(x, str(x)) for x in range(1, 6)]

    name = models.CharField(max_length=150)
    featured = models.BooleanField(default=False)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    post_code = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    wifi = models.IntegerField(choices=RATING_CHOICES)
    food = models.IntegerField(choices=RATING_CHOICES)
    atmosphere = models.IntegerField(choices=RATING_CHOICES)
    sockets = models.IntegerField(choices=RATING_CHOICES)
    coffee = models.IntegerField(choices=RATING_CHOICES)
    slogan = models.CharField(max_length=250, null=True)
    image = models.FileField(upload_to="venue-images", null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def set_long_and_lat(self):
        try:
            api_key = getenv('OPENCAGE_API_KEY')
            location = f"{self.name} {self.address_1} {self.address_2} {self.post_code}"
            result = geocoder.opencage(location, key=api_key).json
            if result is not None:
                self.latitude = round(result['lat'], 6)
                self.longitude = round(result['lng'], 6)
        except Exception as e:
            print(e)

    # Overriding save, to set long & lat points from postcode entered
    def save(self, *args, **kwargs):
        self.set_long_and_lat()
        super(Venue, self).save(*args, **kwargs)

    def __str__(self):
        return '{0} - created at: {1}'.format(self.name, self.created_at)
