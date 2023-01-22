from multiprocessing import context
from urllib import request
from django.shortcuts import render

from apanel.models import Slider

# Create your views here.


def inicio(request):
    template_name = 'web/index.html'
    contexto = {}

    if request.method == 'GET':
        obj = Slider.objects.filter(estado=True).all().order_by('orden')

        contexto = {'obj':obj}

    return render(request, template_name, contexto)





def info(request):
    template_name = 'web/info.html'
    contexto = {}

    return render(request, template_name, contexto)

def historia(request):
    template_name = 'web/historia.html'
    contexto = {}

    return render(request, template_name, contexto)


def telas(request):
    template_name = 'web/telas.html'
    contexto = {}

    return render(request, template_name, contexto)


def sastreria(request):
    template_name = 'web/sastreria.html'
    contexto = {}

    return render(request, template_name, contexto)


def camisas(request):
    template_name = 'web/camisas.html'
    contexto = {}

    return render(request, template_name, contexto)