from django.db import models

class Venue(models.Model):

    name = models.CharField(max_length=150)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    post_code = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} - created at: {1}'.format(self.name, self.created_at)
