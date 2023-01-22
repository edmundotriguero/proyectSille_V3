from django.urls import path
from web.views import inicio, historia, info, telas, sastreria, camisas


urlpatterns = [


    path('', inicio, name='index'),

    path('info', info, name='info'),
    path('historia', historia, name='historia'),
    path('telas', telas, name='telas'),
    path('sastreria', sastreria, name='sastreria'),
    path('camisas', camisas, name='camisas'),


]
