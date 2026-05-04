from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Rol, Usuarios
#mis posibles cambios para paginar
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import RolForm,UpdateRolForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def registrar_usuario(request):
    
    #Para acceder a los registros de la BD  se usa el nombre_modelo.object.all , con lo ultimo se ordenar por id(- de forma descente,sin guion normal)
    #Similar a un select * from Rol order by id_rol
    roles = Rol.objects.all().order_by('id_rol').filter(status=True)
    #Se imprime la informacion
    #print(roles)

    #INstanciar formulario para registrar roles creado en el archivo forms.py
    rol_formulario = RolForm()
    update_rol_formulario = UpdateRolForm()
    #print(rol_formulario)
    #Obtener parametro atraves de GET
    """ if request.method =='GET':
        rol_search = request.GET.get('search_rol')
        roles = roles.filter( Q(nombre__icontains=rol_search)|
                              Q(descripcion__icontains=rol_search)|
                              Q(status__icontains=rol_search))
    """
    #mis posibles cambios para paginar
    paginator = Paginator(roles,4) #primer atributo lista_elementos, segundo atributo numero de elementos por pagina

    #variable que obtiene el numero de pagina atraves de la URL
    page_number = request.GET.get('usuarios_page')
    #variable que Obtiene elementos para mostrar en la pagina actual
    usuarios_current_page = paginator.get_page(page_number)

    #Ciclo para recorrer todos los roles
    for i in roles:
        #Imprimimos la informacion de manera individual print(i.nombre +" "+ i.descripcion)
        pass
        

    #Valida si el metodo de la peticion es POST (Enviar) si es asi se ejecuta el codigo interno del if
    if request.method == 'POST':
        #Corresponden a los campos del formulario.html dentro de templates
        #print(request.POST.get('name'))
        #print(request.POST.get('descrip'))
        #print(request.POST.get('status'))


        #Hacer registro de la informacion
        
        #nuevo_registro= Rol.objects.create( request.POST )
        nuevo_registro = RolForm(request.POST)
        print(nuevo_registro.errors.as_text())
        if nuevo_registro.is_valid():
            print("Entro al bloque if de is_valid()")
            ultimo_id=Rol.objects.all().order_by('-id_rol').first()
            proximo_id= int(ultimo_id.id_rol + 1) 
            registro_rol=nuevo_registro.save(commit=False)
            registro_rol.id_rol= proximo_id
            print("Entro al print is_valid")
                
            registro_rol.save()
            messages.success(request,f'Se guardo de manera correcta el registro con id {registro_rol.id_rol}')
            return redirect('home')
        else:
            messages.error(request, f"No se guardo la informacion {nuevo_registro.errors.as_text()}" )
            return render(request,"formulario.html",context ={ 
                "roles": usuarios_current_page,
                "rol_formulario": nuevo_registro,
                "update_rol_formulario" : update_rol_formulario
            })
            
    """ rol_formulario_dos= RolForm2()
    
    #Aqui inicia metodo POST formulario dos
    if request.method == 'POST':
        

        #Hacer registro de la informacion
        
        #nuevo_registro= Rol.objects.create( request.POST )
        nuevo_registro_dos = RolForm2(request.POST)
        print(nuevo_registro_dos.errors.as_text())
        #Si cumple la validacion de todos los campos
        if nuevo_registro_dos.is_valid():
            
            print("Entro al bloque if de is_valid()")
            ultimo_id=Rol.objects.all().order_by('-id_rol').first()
            proximo_id= int(ultimo_id.id_rol + 1) 
            print(nuevo_registro_dos.cleaned_data)
            #Obtiene la informacion final que recibio el formulario 

            registro_rol=nuevo_registro_dos.save(commit=False)
            registro_rol.id_rol= proximo_id
            #print("Entro al print is_valid")

            
            registro_rol.save()
            messages.success(request,"Se registro el usuario de manera correcta")
            return redirect('home')
        else:
            messages.error(request, f"No se guardo la informacion {nuevo_registro_dos.errors.as_text()}" )
            return render(request,"formulario.html",context ={ 
        "roles": usuarios_current_page,
        "rol_formulario_dos": nuevo_registro_dos
        

    })
    """        
      #Crear diccionario de contexto
    context ={ 
        "roles": usuarios_current_page,
        "rol_formulario":rol_formulario,
        "update_rol_formulario" : update_rol_formulario
    }
    
    return render(request, "formulario.html", context)


def editar_roles(request,id_rol):
    print(id_rol)
    registro = get_object_or_404(Rol, id_rol=id_rol)
    if request.method == 'POST':
        rol_form = UpdateRolForm(request.POST, instance=registro)
        if rol_form.is_valid():
            editar_rol_form = rol_form.save(commit=False)
            editar_rol_form.status = True
            editar_rol_form.save()
            messages.success(request, f'Se actualizo la informacion del usuario {rol_form.cleaned_data["nombre"]}')
            return redirect('registrar-roles')
        else:
            messages.error(request, f'No se pudo actualizar la informacion del usuario {rol_form.cleaned_data["nombre"]}')
            return redirect('registrar-roles')
    else:
        rol_form = UpdateRolForm(instance=registro)

    return redirect('registrar-roles')


def eliminar_roles(request,id_rol):
    rol= get_object_or_404(Rol,id_rol=id_rol)
    print(id_rol)
    print(rol.id_rol)
    
   
    if rol.status:
        rol.status=False
        rol.save()
        messages.success(request,f'Se elimino el rol con id {rol.id_rol}, y nombre {rol.nombre}')
        return redirect('registrar-roles')
    else:
        messages.error(request,f'No se pudo eliminar el con id {rol.id_rol}')
        return redirect('registrar-roles')
