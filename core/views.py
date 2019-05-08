from django.shortcuts import render, get_object_or_404
from .models import Venue


def homepage(request):
    #return render(request, 'core/index.html')
    venue_list = (
        Venue.objects.all()
        #.orderby('created_at')
    )
    context = {'venues': venue_list}
    return render(request, 'core/index.html', context)

def venue_detail(request, id):
    venue_detail = get_object_or_404(Venue, id=id)
    return render(request, 'core/venue.html', {'venue_detail':venue_detail})

def about_us(request):
    return render(request, 'core/about_us.html')