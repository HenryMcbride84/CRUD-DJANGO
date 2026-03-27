from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def registrar_usuario(request): 
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('email'))
    return render(request, "formulario.html")
