from django.urls import path
from  . import views

urlpatterns = [
    path('transacciones/', views.mostrar_transacciones,name='transacciones'),
]
