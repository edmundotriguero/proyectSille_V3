from django.shortcuts import render, redirect

from django.urls import reverse,reverse_lazy

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from tienda.models import Cotizaciones, Pedido, DetallePedido

from tienda.forms import DatosClienteForm


from django.contrib.auth.decorators import login_required, permission_required




@login_required(login_url='/b/login/')
@permission_required('', login_url='bases:sin_privilegios')
def profile(request):

    detalle = request.session.get("carrito")
    template_name = ''
    if detalle:
       
        return HttpResponseRedirect(reverse_lazy('tienda:pedido_new'))
        
    else:

        template_name = 'perfil/index.html'
       # user = request.user
        #print(user)
        

    return render(request, template_name)
        

@login_required(login_url='/b/login/')
@permission_required('', login_url='bases:sin_privilegios')
def cotizaciones(request):
    template_name = 'perfil/cotizaciones.html'

    user = request.user.pk
    #print(user.pk)
    cot = Pedido.objects.filter(user_created=user).all()

    print(cot)

    

    contexto = {'obj':cot}

    return render(request, template_name, contexto)    


def pedido_info(request, id):

    template_name = 'perfil/pedido_info.html'
    contexto = {}
    obj = DetallePedido.objects.filter(pedido_id=id, estado=True).all()

    if not obj:
        return HttpResponse('Registro no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': obj}

   

    return render(request, template_name, contexto)