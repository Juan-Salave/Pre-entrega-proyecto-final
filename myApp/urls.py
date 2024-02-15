from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('servicios', views.servicios, name="servicios"),
    path('crear_personal', views.crear_personal, name="crear_personal"),
    path('crear_cliente', views.crear_cliente, name="crear_cliente"),
    path('crear_servicio', views.crear_servicio, name="crear_servicio"),
    path('buscar_cliente', views.buscar_cliente, name="buscar_cliente"),
]