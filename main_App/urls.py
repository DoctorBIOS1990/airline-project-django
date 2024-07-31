from django.urls import path
from .import views

urlpatterns = [
    
    # Principales
    path('', views.index, name = 'index'),
    path('login/', views.iniciar_sesion, name = 'iniciar_sesion'),
    path('logout/', views.cerrar_sesion, name = 'cerrar_sesion'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('denegado/', views.acceso_denegado, name = 'acceso_denegado'),
    path('estadistica/', views.estadistica, name = 'estadistica'),
    path('mensajes/listar', views.listar_mensajes, name = 'listar_mensajes'),
    path('mensajes/eliminar/<int:pk>/', views.eliminar_mensaje, name = 'eliminar_mensaje'),

    # Pasajero
    path('pasajeros/', views.listar_pasajeros, name = 'listar_pasajeros'),
    path('pasajero/crear/', views.crear_pasajero, name = 'crear_pasajero'),
    path('pasajero/editar/<int:pk>/', views.editar_pasajero, name = 'editar_pasajero'),
    path('pasajero/eliminar/<int:pk>/', views.eliminar_pasajero, name = 'eliminar_pasajero'),
    
    # Tarifa
    path('tarifas/', views.listar_tarifas, name = 'listar_tarifas'),
    path('tarifas/crear/', views.crear_tarifa, name = 'crear_tarifa'),
    path('tarifas/editar/<int:pk>/', views.editar_tarifa, name = 'editar_tarifa'),
    path('tarifas/eliminar/<int:pk>/', views.eliminar_tarifa, name = 'eliminar_tarifa'),

    # Aeropuerto
    path('aeropuertos/', views.listar_aeropuertos, name = 'listar_aeropuertos'),
    path('aeropuertos/crear/', views.crear_aeropuerto, name = 'crear_aeropuerto'),
    path('aeropuertos/editar/<int:pk>/', views.editar_aeropuerto, name = 'editar_aeropuerto'),
    path('aeropuertos/eliminar/<int:pk>/', views.eliminar_aeropuerto, name = 'eliminar_aeropuerto'),

    # Avion
    path('aviones/', views.listar_aviones, name = 'listar_aviones'),
    path('aviones/crear/', views.crear_avion, name = 'crear_avion'),
    path('aviones/editar/<int:pk>/', views.editar_avion, name = 'editar_avion'),
    path('aviones/eliminar/<int:pk>/', views.eliminar_avion, name = 'eliminar_avion'),

    # Vuelo
    path('vuelos/', views.listar_vuelos, name = 'listar_vuelos'),
    path('vuelos/crear/', views.crear_vuelo, name = 'crear_vuelo'),
    path('vuelos/editar/<int:pk>/', views.editar_vuelo, name = 'editar_vuelo'),
    path('vuelos/eliminar/<int:pk>/', views.eliminar_vuelo, name = 'eliminar_vuelo'), 

    # Tramo
    path('tramos/', views.listar_tramos, name = 'listar_tramos'),
    path('tramos/crear/', views.crear_tramo, name = 'crear_tramo'),
    path('tramos/editar/<int:pk>/', views.editar_tramo, name = 'editar_tramo'),
    path('tramos/eliminar/<int:pk>/', views.eliminar_tramo, name = 'eliminar_tramo'), 
    
    # Reserva
    path('reservas/', views.listar_reservas, name = 'listar_reservas'),
    path('reservas/crear/', views.crear_reserva, name = 'crear_reserva'),
    path('reservas/editar/<int:pk>/', views.editar_reserva, name = 'editar_reserva'),
    path('reservas/eliminar/<int:pk>/', views.eliminar_reserva, name = 'eliminar_reserva'),               

    # Rol
    path('roles/', views.listar_roles, name = 'listar_roles'),
    path('roles/crear/', views.crear_rol, name = 'crear_rol'),
    path('roles/editar/<int:pk>/', views.editar_rol, name = 'editar_rol'),
    path('roles/eliminar/<int:pk>/', views.eliminar_rol, name = 'eliminar_rol'),          

    # Usuario
    path('usuarios/', views.listar_usuarios, name = 'listar_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name = 'crear_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name = 'editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name = 'eliminar_usuario'),  
    path('usuarios/reset/<int:pk>/', views.cambiar_password, name = 'cambiar_password')
]