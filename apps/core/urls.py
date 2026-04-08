from django.urls import path
from .views import *

app_name='apps.core'

urlpatterns = [
    #3er parametro es un alias para posterior llamado en una url
    path('',home_page,name='home')
]
