from multiprocessing import context
from urllib import request
from django.shortcuts import render

from apanel.models import Slider

from ecommerce.models import Producto

import random

# Create your views here.


def inicio(request):
    template_name = 'web/index.html'
    contexto = {}

    if request.method == 'GET':
        obj = Slider.objects.filter(estado=True).all().order_by('orden')


        cam = Producto.objects.filter(categoria_id=1, estado=True).all()

        tra = Producto.objects.filter(categoria_id=3, estado=True).all()

        nov = Producto.objects.filter(categoria_id=2, estado=True).all()


        obj_cam = []


        tra_ale = random.choice(tra)

        nov_ale = random.choice(nov)

        for num in range(1, 5):
            aletory = random.choice(cam)
            obj_aux = {}
            obj_aux["nombre"] = aletory.nombre
            obj_aux["img"] = str(aletory.img)

            obj_cam.append(obj_aux)


        contexto = {'obj':obj,'cam':obj_cam,'tra':tra_ale,'nov':nov_ale}

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