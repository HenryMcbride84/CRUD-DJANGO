from django.db import models
from apps.usuarios.models import Perfil

# Create your models here.






class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion= models.CharField(max_length=50)
    estatus= models.BooleanField()
    id_perfil= models.ForeignKey(Perfil,on_delete=models.CASCADE,db_column='id_perfil') 
    
    class Meta:
        managed=False
        db_table='tasks'

