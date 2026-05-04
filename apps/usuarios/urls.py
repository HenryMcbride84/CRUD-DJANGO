from django.urls import path
from  . import views



urlpatterns = [
    path('usuarios/', views.registrar_usuario,name='registrar-roles'),
    #COn esta linea se pasan parametros a una URL int enteros str: cadenas
    path('usuarios/editar/<int:id_rol>',views.editar_roles,name='editar-rol'),
     path('usuarios/eliminar/<int:id_rol>',views.eliminar_roles,name='eliminar-rol')
                                                    
]
