from django.urls import path
from .views import *



urlpatterns = [
    #3er parametro es un alias para posterior llamado en una url
    path('',home_page,name='home'),
    path('signup/',registrar_usuario,name='sign-up')
]


