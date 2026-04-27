from django.shortcuts import render
from .models import UnidadTransporte
#Importa de models las clases que modelan nuestras Tablas (MOdelos)
# Create your views here.
def mostrar_transacciones(request):

    #Funciona semejante a un select * from tabla
    
    unidades_transporte = UnidadTransporte.objects.all()
    for unidad in unidades_transporte:
        print(unidad.placa)
        print(unidad.no_economico)

    #Es mas recomendable pasar un diccionario que una variable
    lista_nombres=['Yo','Tu','El']

    context={
        'unidades_transporte': unidades_transporte,
        'lista_pronombres':lista_nombres
    }

    return render(request,'transacciones.html', context)