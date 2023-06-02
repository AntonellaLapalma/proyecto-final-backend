from django.db import models

# Create your models here.
class Cliente(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30,)
    apellido = models.CharField(max_length=30)
    celular = models.CharField(max_length=30)
    email = models.EmailField()
    activo = models.BooleanField()

    def __str__(self):
        return 'dni: %s, nombre: %s, apellido: %s, celular: %s, email: %s, activo: %s' %(self.dni,self.nombre,self.apellido,self.celular,self.email,self.activo)
    
 
