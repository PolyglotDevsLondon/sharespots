from core.models import Venue
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from django.db.models import Value, TextField
from django.db.models.functions import Concat
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def search(request):
    user_search_venue = request.GET.get('search')
    vector = SearchVector('name', weight='A', config='english') + SearchVector('post_code', weight='B', config='english')
    query = SearchQuery(user_search_venue)
    rank = SearchRank(vector, query)
    searched_venues = Venue.objects.annotate(rank=rank).filter(rank__gte=0.2).order_by('-rank')
    context = {'searched_venues': searched_venues}
    return render(request, 'search/venues.html', context)
