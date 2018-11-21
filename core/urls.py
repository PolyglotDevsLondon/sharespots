from django.urls import path

from . import views

#app_name = 'core'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cafe/<int:id>', views.cafe, name='cafe'),
    path('about-us', views.about_us, name='about')
]
