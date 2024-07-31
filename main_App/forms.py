from django import forms
from .models import Aereopuerto, Avion, Vuelo, Tarifa, Tramo, Pasajero, Reserva, Mensaje, Usuario, Rol
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre','email','comentario']
        exclude = ['createAt']

class PasajeroForm(forms.ModelForm):
    class Meta:
        model = Pasajero        
        fields = ['dni','nombre','apellido1','apellido2','telefono', 'direccion']

class TarifaForm(forms.ModelForm):
    class Meta:
        model = Tarifa
        fields = ['nombre','descripcion','descuento']        

class AeropuertoForm(forms.ModelForm):
    class Meta:
        model = Aereopuerto
        fields = ['nombre','ciudad','sigla']

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['marca','modelo','asientos','aeropuerto']                     

class VueloForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ['fecha','avion','aeropuerto_salida','aeropuerto_llegada']

class TramoForm(forms.ModelForm):
    class Meta:
        model = Tramo
        fields = ['distancia','duracion','hora_salida','hora_entrada', 
                  'vuelo', 'aeropuerto_salida', 'aeropuerto_llegada']   

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha','precio','dni','vuelo', 'tramo', 'tarifa', ]   

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre']

# Nuevo usuario
class UsuarioForm(UserCreationForm):
    rol = forms.ModelChoiceField(queryset = Rol.objects.all(), empty_label = "Seleccione un rol") 

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'rol', 'password1', 'password2']
        exclude = ['createAt']
       
# Edición Usuario
class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'rol']
        exclude = ['createAt']

# Cambiar password usuario
class UsuarioPasswordForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['password1', 'password2']
        exclude = ['username','createAt','first_name', 'last_name', 'email', 'rol']   
