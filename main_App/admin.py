from django.contrib import admin
from .models import Aereopuerto, Avion, Vuelo, Tarifa, Tramo, Pasajero, Reserva, Mensaje, Usuario, Rol
# Register your models here.

admin.site.register(Usuario),
admin.site.register(Aereopuerto),
admin.site.register(Avion),
admin.site.register(Vuelo),
admin.site.register(Tarifa),
admin.site.register(Tramo),
admin.site.register(Pasajero),
admin.site.register(Reserva),
admin.site.register(Mensaje),
admin.site.register(Rol),
