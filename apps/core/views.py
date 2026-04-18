from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from .forms import CustomUserCreationForm  #aqui se extrae o importa el formulario de brinda Django que se encuentra dentro del archivo forms.py
from django.contrib import messages #Para generar alertas de mensajes de error,correcto ,warnings


# Create your views here.
@login_required
def home_page(request):
    return render(request,"core/home.html")


def exit(request):
    logout(request)
    return redirect("home")


def registrar_usuario(request):
    registrar_form = CustomUserCreationForm()
    print(registrar_form)
    if request.method == 'POST': 
        user_creation_form = CustomUserCreationForm(data=request.POST) #esta linea genera un diccionario de datos que se genera con la informacion que se manda en el formulario
        if user_creation_form.is_valid(): #linea para validar que los datos del formulario sean correctas
            print("Los datos ingresados son correctos")  
            messages.success(request,"Los datos ingresados son correctos")
            if user_creation_form.save(): #Si los datos son correctos se guardan en la BD con el metodo save() y se registra el usuario
                messages.success(request,"Usuario registrado correctamente")
            else:
                messages.error(request,'No se pudo registrar usuario')
                return redirect('sign-up')
        else:
            print("LOs datos son incorrectos")
            messages.error(request,'Los datos son incorrectos')
        
        
        #Si se registra usuario de manera correcta , se procede autenticacion automatica
        user = authenticate(username=user_creation_form.cleaned_data['username'],password=user_creation_form.cleaned_data['password1']) # se crea la autenticacion
        if user: #Se valida si se autentico de manera correcta
            messages.success(request,"Usuario autenticado de forma correcta")
            login(request,user) #Se inicia la sesion de usuario
            return redirect('home')
        else:
            messages.error(request,"NO se pudo autenticar usuario") 
    else:
        user_creation_form=CustomUserCreationForm()

    context = { 
        'registrar_form': registrar_form
    }



    return render(request,"core/sign-up.html",context)


