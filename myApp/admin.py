from django.contrib import admin
from .models import Cliente, Servicios, Nosotros

# Registra (-> BASES DE DATOS <-) aquí

admin.site.register(Cliente)
admin.site.register(Servicios)
admin.site.register(Nosotros)
