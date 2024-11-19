from django.db import models

class Fabrica(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fabricas'

    def __str__(self):   
	    return self.nombre




class Producto(models.Model):

    nombre = models.CharField(max_length=50, blank=False, null=False)  
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    precio = models.PositiveIntegerField(blank=False, null=False, default=999999)
    fabrica = models.ForeignKey(Fabrica, models.DO_NOTHING,blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'productos'
        
    def __str__(self):   
        return self.nombre