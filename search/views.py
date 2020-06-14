from core.models import Venue
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from django.db.models import Value, TextField
from django.db.models.functions import Concat, Greatest
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def search(request):
    user_search_venue = request.GET.get('search')
    trigram_check = Venue.objects.annotate(
        similarity=Greatest(TrigramSimilarity('post_code', user_search_venue), TrigramSimilarity('name', user_search_venue)
    )).filter(similarity__gte=0.3).order_by('-similarity')
    context = {'searched_venues': trigram_check}
    return render(request, 'search/venues.html', context)
