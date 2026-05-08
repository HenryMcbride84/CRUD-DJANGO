from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def mostrar_info(request):

    tareas= Tasks.objects.all()
    buscador=request.GET.get('buscar')

    if buscador:
        tareas = tareas.filter(
            Q(nombre__icontains=buscador) |
            Q(id_perfil__name__icontains=buscador)
            
        )

    paginador = Paginator(tareas,3)
    numero_pagina= request.GET.get('pagina')
    pagina= paginador.get_page(numero_pagina)
    
    context={
        'pagina':pagina
    }
    return render(request,'tasks.html',context)
