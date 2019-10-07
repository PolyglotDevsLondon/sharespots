from django.contrib import admin
from .models import Venue


class VenueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Venue)