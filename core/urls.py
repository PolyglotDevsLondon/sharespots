from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('venue-detail/<int:id>', views.venue_detail, name='cafe'),
    path('about-us', views.about_us, name='about'),
    path('contact', views.contact, name='contact')

]
