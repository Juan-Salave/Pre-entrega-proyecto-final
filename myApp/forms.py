from django import forms

class CrearCliente(forms.Form):
    nombre = forms.CharField(label= 'Su Nombre', max_length=40)
    auto = forms.CharField(label= 'Modelo de Auto', max_length=40)
    patente = forms.CharField(label= 'Patente', max_length=40)


class CrearServicio(forms.Form):
    tipo_de_servicio = forms.CharField(label= 'Nuevo Servicio', max_length=100)
    
class CrearPersonal(forms.Form):
    nombre = forms.CharField( max_length=50)
    especialidad = forms.CharField( max_length=50)
    
class BuscarCliente(forms.Form):
    patente = forms.CharField( max_length=40)