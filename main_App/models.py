from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models  import AbstractUser

# Model Aeropuerto
class Aereopuerto(models.Model):
    nombre = models.CharField(max_length = 255, null = False)
    ciudad = models.CharField(max_length = 255, null = False)
    sigla = models.CharField(max_length = 3, null = False)

# Model Avion
class Avion(models.Model):
    marca = models.CharField(max_length = 255, null = False)
    modelo = models.CharField(max_length = 255, null = False)
    asientos = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(370)])
    aeropuerto = models.ForeignKey(Aereopuerto,on_delete = models.CASCADE, null = False) # aeropuerto FK

# Model Vuelo
class Vuelo(models.Model):
    fecha = models.DateField(null = False)
    avion = models.ForeignKey(Avion,on_delete = models.CASCADE, null = False) # avion FK
    aeropuerto_salida = models.ForeignKey(Aereopuerto,on_delete = models.CASCADE, null = False, related_name = 'vuelos_salida') # Aereopuerto Salida FK
    aeropuerto_llegada = models.ForeignKey(Aereopuerto,on_delete = models.CASCADE, null = False, related_name = 'vuelos_llegada') # Aereopuertop Entrada FK

# Model Tramo
class Tramo(models.Model):
    distancia = models.CharField(max_length = 10, null = False)
    duracion = models.DurationField(null = False)
    hora_salida = models.TimeField( null = False)
    hora_entrada = models.TimeField( null = False)
    vuelo = models.ForeignKey(Vuelo,on_delete = models.CASCADE, null = False) # Vuelo Fk
    aeropuerto_salida = models.ForeignKey(Aereopuerto,on_delete = models.CASCADE, null = False, related_name ='tramos_salida') # Aereopuerto Salida FK
    aeropuerto_llegada = models.ForeignKey(Aereopuerto,on_delete = models.CASCADE, null = False, related_name ='tramos_llegada') # Aereopuertop Llegada FK

    # Kilometraje
    def kilometraje(self):
        return self.distancia + " Km"
    
# Model Pasajero
class Pasajero(models.Model):
    dni = models.BigIntegerField(primary_key = True, validators = [MaxValueValidator(99999999999)], null = False)
    nombre = models.CharField(max_length = 20, null = False)
    apellido1 = models.CharField(max_length = 20, null = False)
    apellido2 = models.CharField(max_length = 20, null = False)
    telefono = models.CharField(max_length = 20, null = False)
    direccion = models.CharField(max_length = 255, null = False)

# Model Tarifa 
class Tarifa(models.Model):
    nombre = models.CharField(max_length = 20, null = False)
    descripcion = models.CharField(max_length = 255, null = False)
    descuento = models.DecimalField(max_digits=5, decimal_places = 2, default=0, null = False)

    # Formatea tarifa
    def checking(self):
        monto = self.descuento
        if monto == 0:
            return "No tiene"
        else: 
            return str(monto//1) + " %"

# Model Reserva
class Reserva(models.Model):
    fecha = models.DateField(null = False)
    precio = models.DecimalField(max_digits = 10, decimal_places = 2) 
    dni = models.ForeignKey(Pasajero,on_delete = models.CASCADE, null = False) # DNi Pasajero KF
    vuelo = models.ForeignKey(Vuelo,on_delete = models.CASCADE, null = False) # Vuelo Fk
    tramo = models.ForeignKey(Tramo,on_delete = models.CASCADE, null = False) # Tramo 
    tarifa = models.ForeignKey(Tarifa,on_delete = models.CASCADE, null = False) # Tarifa

    # Aplica Tarifa
    def descuento(self): 
        ta = self.tarifa.descuento
        monto = self.precio
        if ta > 0:
            return "$ " + str((monto - ((ta/100) * self.precio)) // 1 ) + ".00"
        else: 
            return "Sin descuento"

# Model Mensajeria 
class Mensaje(models.Model):
    nombre = models.CharField(max_length = 50, null = False)
    email = models.EmailField(max_length = 255, null = False)
    comentario = models.CharField(max_length = 255, null = False)
    fecha = models.DateField(auto_now_add = True)

# Model Rol
class Rol(models.Model):
    nombre = models.CharField(max_length = 255, blank = False, unique = True)

# Model Usuario
class Usuario(AbstractUser):
    createAt = models.DateField(auto_now_add = True)
    rol = models.ForeignKey(Rol, on_delete = models.CASCADE, null = False)
    email = models.EmailField(max_length = 255, blank = False, unique = True)