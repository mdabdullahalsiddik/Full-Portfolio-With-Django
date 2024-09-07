from django.urls import path
from . views import index , about , resume , services , service_details , portfolio , portfolio_details , contact

urlpatterns = [
     path('', index, name='index'),
     path('about', about , name='about'),
     path('resume', resume , name='resume'),
     path('services', services , name='services'),
     path('service-details', service_details , name='service-details'),
     path('portfolio', portfolio , name='portfolio'),
     path('portfolio-details', portfolio_details , name='portfolio-details'),
     path('contact', contact , name='contact'),
    
]
