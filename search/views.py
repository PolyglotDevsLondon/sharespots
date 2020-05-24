from core.models import Venue
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def search(request):
    search_venue = request.GET.get('search_venue')
    searched_venues = Venue.objects.filter(name__icontains=search_venue)
    # apply the filter on Venue model with search_venue
    # render the search list to FE
    # return render(request, 'core/venue.html', {'venue_detail': venue_detail})
    return HttpResponse(searched_venues)
