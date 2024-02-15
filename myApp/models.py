from django.db import models

# Crea Aquí  (->Bases De Datos<-)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    modelo_auto = models.CharField(max_length=40)
    patente = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre +'->'+self.modelo_auto +'->'+self.patente
    
class Servicios(models.Model):
    tipo_de_servicio = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo_de_servicio
    
class Nosotros(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre + '  ------>   ' + self.especialidad
    
    