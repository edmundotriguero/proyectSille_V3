from django.urls import path
from tienda.views import tienda, datosClienteNew, finPedido, producto_view, cotizacion_download, cotizacionNew, productos_view, pedido_new


urlpatterns = [


    path('', tienda, name='tienda'),
    #path('nosotros', nosotros, name='nosotros'),
    path('cliente/new', datosClienteNew, name='cliente_new'),

    path('pedido/new', pedido_new, name='pedido_new'),
    #path('info', info, name='info'),
    path('finpedido', finPedido, name='fin_pedido'),

    path('producto/<int:pk>/', producto_view, name='producto_id'),

    path('productos/<int:pk>/', productos_view, name='productos'),

    path('cotizaciones/new', cotizacionNew, name='cotizacion_new'),  # Se esta utilizando para la lista de perdidos del cliente ya no se tiene cotizaciones




    path('cotizacion/pdf', cotizacion_download, name='cotizacion_pdf' )

]
