from django.urls import path
from . import views

urlpatterns = [
    path('tasks/',views.mostrar_info,name="tasks")
]
