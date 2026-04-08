from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Rol, Users
# Create your views here.
def registrar_usuario(request):
    
    #Para acceder a los registros de la BD  se usa el nombre_modelo.object.all
    roles = Rol.objects.all()
    #Se imprime la informacion
    print(roles)

    #Ciclo para recorrer todos los roles
    for i in roles:
        #Imprimimos la informacion de manera individual
        print(i.nombre +" "+ i.descripcion)

    #Valida si el metodo de la peticion es POST (Enviar) si es asi se ejecuta el codigo interno del if
    if request.method == 'POST':
        #Corresponden a los campos del formulario.html dentro de templates
        print(request.POST.get('name'))
        print(request.POST.get('descrip'))
        print(request.POST.get('status'))


        #Hacer registro de la informacion
        
        nuevo_registro= Rol.objects.create(  id_rol=4, nombre= request.POST.get('name'), descripcion= request.POST.get('descrip'), status= True)
    
        nuevo_registro.save()
        print("Se realizo registro")
        
      #CRear diccionario de contexto
    context ={ 
        "roles": roles

    }
      

    return render(request, "formulario.html", context)
