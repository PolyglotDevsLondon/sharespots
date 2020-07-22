from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models, migrations
from django.contrib.postgres.operations import TrigramExtension


class Migration(migrations.Migration):
    operations = [
        TrigramExtension()
    ]

class Rating(models.Model):
    rate = models.IntegerField(
        blank=True, null=True,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    def __str__(self):
        return str(self.rate)


class Venue(models.Model):

    name = models.CharField(max_length=150)
    featured = models.BooleanField(default=False)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    post_code = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    wifi = models.OneToOneField('Rating', on_delete=models.CASCADE, null=True, related_name='wifi')
    food = models.OneToOneField('Rating', on_delete=models.CASCADE, null=True, related_name='food')
    atmosphere = models.OneToOneField('Rating', on_delete=models.CASCADE, null=True, related_name='atmosphere')
    sockets = models.OneToOneField('Rating', on_delete=models.CASCADE, null=True, related_name='sockets')
    coffee = models.OneToOneField('Rating', on_delete=models.CASCADE, null=True, related_name='coffee')
    slogan = models.CharField(max_length=250, null=True)
    image = models.URLField(max_length=200, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def set_long_and_lat(self):
        location = self.post_code + self.address_2
        result = geocoder.arcgis(location).json
        if result is not None:
            self.latitude = round(result['lat'], 6)
            self.longitude = round(result['lng'], 6)

    # Overriding save, to set long & lat points from postcode entered
    def save(self, *args, **kwargs):
        self.set_long_and_lat()
        super(Venue, self).save(*args, **kwargs)

    def __str__(self):
        return '{0} - created at: {1}'.format(self.name, self.created_at)
