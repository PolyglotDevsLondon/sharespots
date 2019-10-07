from django.contrib import admin
from .models import Venue, Rating


class RatingInline(admin.StackedInline):
    model = Rating

class VenueAdmin(admin.ModelAdmin):
    inlines = [
        RatingInline
    ]

admin.site.register(Venue)