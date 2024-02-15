from django.shortcuts import render, redirect
from myApp.models import Cliente, Servicios, Nosotros
from .forms import CrearCliente, CrearServicio, BuscarCliente, CrearPersonal

# CREAMOS NUESTRAS VISTAS DE HTML 

def index(request):
    return render(request, 'myApp/index.html')

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'myApp/clientes.html', {
        'cliente':clientes})
    
def servicios(request):
    servi = Servicios.objects.all()
    return render(request, 'myApp/servicios.html', {
        'servi':servi})

def nosotros(request):
    equipo = Nosotros.objects.all()
    return render(request, 'myApp/nosotros.html', {
        'equipo':equipo})


# VISTA DEL FORMULARIO CREAR CLIENTE:

def crear_cliente(request):
    if request.method == 'POST':
        formulario_clientes = CrearCliente(request.POST)
        print(formulario_clientes)
        if formulario_clientes.is_valid():
            informacion = formulario_clientes.cleaned_data
            cliente_guardar = Cliente (nombre=informacion['nombre'], modelo_auto=informacion['auto'],patente=informacion['patente'])
            cliente_guardar.save()
            return render(request, 'myApp/index.html')
        else:
            formulario_clientes= CrearCliente()
    
    return render(request, 'myApp/crear_cliente.html', {
        'form':CrearCliente })
 
    
 # VISTA DEL FORMULARIO CREAR SERVICIO:
    
def crear_servicio(request):
    if request.method == 'POST':
        formulario_servicio = CrearServicio(request.POST)
        print(formulario_servicio)
        if formulario_servicio.is_valid():
            informacion = formulario_servicio.cleaned_data
            nuevo_servi = Servicios (tipo_de_servicio=informacion['tipo_de_servicio'])
            nuevo_servi.save()
            return render(request, 'myApp/index.html')
        else:
            formulario_servicio= CrearServicio()
    
    return render(request, 'myApp/crear_servicio.html', {'form':CrearServicio })


def crear_personal(request):
    if request.method == 'POST':
        formulario_personal = CrearPersonal(request.POST)
        if formulario_personal.is_valid():
            informacion = formulario_personal.cleaned_data
            personal_guardar = Nosotros (nombre=informacion['nombre'],
            especialidad=informacion['especialidad'])
            personal_guardar.save()
            return render(request, 'myApp/index.html')
        else:
            formulario_personal = CrearPersonal()
    
    return render(request, 'myApp/crear_personal.html', {'form':CrearPersonal })

# buscar cliente

def buscar_cliente(request):
    if request.method == 'POST':
        mi_formulario = BuscarCliente(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            cliente = Cliente.objects.filter(patente__icontains=info['patente'])
            return render(request, 'myApp/buscar_cliente.html', {'client':cliente})
    else:
        mi_formulario = BuscarCliente()
    return render(request, 'myApp/buscar_cliente.html', {'formu':mi_formulario })
    
    
