from core.models import Venue
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def search(request):
    search_venue = request.GET.get('search')
    searched_venues = Venue.objects.filter(name__icontains=search_venue)
    context = {'searched_venues': searched_venues}
    return render(request, 'search/venue_list.html', context)
