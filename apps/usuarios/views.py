from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def registrar_usuario(request):
    return HttpResponse("<h1>Registrar usuarios</h1>")

