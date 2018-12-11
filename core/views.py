from django.shortcuts import render, get_object_or_404
from .models import Venue


def homepage(request):
    return render(request, 'core/index.html')

def venue(request, id):
    venue = get_object_or_404(Venue, id=id)
    return render(request, 'core/venue.html', {'venue':venue})

def about_us(request):
    return render(request, 'core/about_us.html')