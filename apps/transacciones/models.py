from django.db import models



# Create your models here.


class UnidadTransporte(models.Model): 
    id_unidad_transporte= models.AutoField(primary_key=True) 
    placa = models.CharField(max_length=30,blank=True,null=False)    
    no_economico = models.IntegerField()
    
    class Meta:
        managed = False
        db_table= 'unidad_transporte'    


class Transacciones(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    serial = models.CharField(max_length=255, blank=True,null=True)
    estatus= models.BooleanField()
    id_unidad_transporte =models.ForeignKey(UnidadTransporte,null=True,on_delete=models.CASCADE,db_column='id_unidad_transporte') 
    

    class Meta:
         managed= False
         db_table='transacciones'


class Member(models.Model):
    firstname= models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)

    