from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about, name='about'),
    path('services', views.service, name='service'),
    path('team', views.team, name='team'),
    path('contact-us', views.contact, name='contact'),
]