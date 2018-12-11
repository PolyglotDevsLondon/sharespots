from django.urls import path

from . import views

#app_name = 'core'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('venue/<int:id>', views.venue, name='cafe'),
    path('about-us', views.about_us, name='about')
]
