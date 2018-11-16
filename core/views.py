from django.shortcuts import render
from .helpers import VenueHelpers


def homepage(request):
    return render(request, 'core/index.html')

def cafe(request, id):
    venue = VenueHelpers()
    ## UNCOMMENT THE BELOW TO SETUP DEFAULT VENUE FOR DEVELOPMENT ##
    ##if not venue.check_default_venue_exists():
       ## venue.create_default_venue()
    ##default_venue = venue.get_default_venue()

    ## GET A CAFE BY IT'S ID ##
    cafe = venue.get_venue(id)
    
    return render(request, 'core/cafe.html', {'cafe':cafe})