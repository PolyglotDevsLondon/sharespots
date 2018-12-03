from django.contrib import admin
from .models import Venue, Rating

admin.site.register(Venue, Rating)
