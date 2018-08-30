from django.http import HttpResponse


def homepage(request):
    return HttpResponse('<h1>Hello! I am the homepage</h1>')
