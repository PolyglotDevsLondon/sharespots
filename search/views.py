from core.models import Venue
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from django.shortcuts import render


def search(request):
    user_search_venue = request.GET.get('search')
    search_venues = get_search_venues(user_search_venue)
    context = {'searched_venues': search_venues}
    return render(request, 'search/venues.html', context)


def get_search_venues(user_search_venue):
    search_venues = Venue.objects.annotate(
        similarity=Greatest(TrigramSimilarity('post_code', user_search_venue),
                            TrigramSimilarity('name', user_search_venue)
                            )).filter(similarity__gte=0.3).order_by('-similarity')
    return search_venues
