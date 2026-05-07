from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

""" 
CREATE TABLE rol (
	id_rol serial PRIMARY KEY,
	nombre varchar(50),
	descripcion varchar(255),
	status boolean 
	); """
class Rol(models.Model): 
    id_rol = models.AutoField(primary_key=True) 

    nombre = models.CharField(max_length=50, blank=True,null=True)
    descripcion= models.CharField(max_length=255,blank=True,null=True) 
    status= models.BooleanField(blank=True,null=True)

    class Meta:
        managed = False
        db_table= 'rol'    


""" class Usuarios(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True,null=True)
    password= models.CharField(max_length=255)
    id_rol = models.ForeignKey(Rol, null=True, on_delete=models.CASCADE,db_column='id_rol')

    class Meta:
         db_table='usuarios'
 """
class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    foto = models.CharField(max_length=50, blank=True, null=True)
    estatus = models.BooleanField(blank=True, null=True)
    id_auth_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_auth_user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil'
