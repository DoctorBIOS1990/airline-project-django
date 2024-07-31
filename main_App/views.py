from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import role_required
from django.contrib.auth import login,logout

from .models import Aereopuerto, Avion, Vuelo, Tarifa, Tramo, Pasajero, Reserva, Mensaje, Rol, Usuario
from .forms import MensajeForm, PasajeroForm, TarifaForm, AeropuertoForm, AvionForm, VueloForm, TramoForm,ReservaForm, RolForm, UsuarioForm, UsuarioEditForm, UsuarioPasswordForm, AuthenticationForm
from .forms import AuthenticationForm
from main_App.querys import *

def index(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "¡Gracias por su mensaje"
            return render(request, 'index.html',{'form': form, 'success_message': mensaje})
    else:
        mensaje = ""
        form = MensajeForm()
    return render(request, 'index.html', {'form': form, 'success_message': mensaje})
 
 
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user  = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('index')

@login_required
def dashboard(request):
    # Capture data
    return render(request, 'dashboard.html',{
        'count_pasajeros': is_empty( pasajeros_count(), True ),
        'count_aviones': is_empty( aviones_count(), True ),
        'count_aeropuertos': is_empty( aeropuertos_count(), True ),
        'count_tramos': is_empty( tramos_count(), True ),
        'count_vuelos': is_empty( vuelos_count(), True ),
        'count_tarifas' : is_empty( tarifas_count(), True ),
        'count_reservas': is_empty( reservas_count(), True ),
        'count_usuarios': is_empty( usuarios_count(), True ),
        })

@login_required
def estadistica(request):
    return render(request, 'estadistica.html', get_data())

# PASAJEROS -------------------------------------------------------------------
@login_required
def listar_pasajeros(request):
    pasajeros = Pasajero.objects.all()
    success_message = request.session.pop('success_message', None)
    return render(request, 'pasajeros/listar.html', 
                  {'pasajeros': pasajeros,
                   'success_message': success_message, 
                   'total': is_empty(pasajeros_count(), True) })

@login_required
def crear_pasajero(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Pasajero creado correctamente!'
            return redirect('listar_pasajeros')
    else:
        form = PasajeroForm()
    return render(request, 'pasajeros/formulario.html', {'form': form})

@login_required
def editar_pasajero(request, pk):
    pasajero = get_object_or_404(Pasajero, pk = pk)
    if request.method == 'POST':
        form = PasajeroForm(request.POST, instance = pasajero)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Datos del pasajero actualizados correctamente!'
            return redirect('listar_pasajeros')
    else:
        form = PasajeroForm(instance = pasajero)
    return render(request, 'pasajeros/editar.html', {'form': form})

@login_required
def eliminar_pasajero(request, pk):
    pasajero = get_object_or_404(Pasajero, pk = pk)
    if request.method == 'POST':
        pasajero.delete()

    return redirect('listar_pasajeros')

# TARIFAS -------------------------------------------------------------------

@login_required
def listar_tarifas(request):
    tarifas = Tarifa.objects.all()
    success_message = request.session.pop('success_message', None)
    return render(request, 'tarifas/listar.html', 
                  {'tarifas': tarifas, 
                   'success_message': success_message,
                   'total': is_empty(tarifas_count(), True)})

@login_required
def crear_tarifa(request):
    if request.method == 'POST':
        form = TarifaForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Tarifa creada correctamente!'
            return redirect('listar_tarifas')
    else:
        form = TarifaForm()
    return render(request, 'tarifas/formulario.html', {'form': form})

@login_required
def editar_tarifa(request, pk):
    tarifa = get_object_or_404(Tarifa, pk = pk)
    if request.method == 'POST':
        form = TarifaForm(request.POST, instance = tarifa)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Datos de la tarifa actualizados correctamente!'
            return redirect('listar_tarifas')
    else:
        form = TarifaForm(instance = tarifa)
    return render(request, 'tarifas/editar.html', {'form': form})

@login_required
def eliminar_tarifa(request, pk):
    tarifa = get_object_or_404(Tarifa, pk = pk)
    if request.method == 'POST':
        tarifa.delete()
    return redirect('listar_tarifas')    

# AEROPUERTOS -------------------------------------------------------------------

@login_required
def listar_aeropuertos(request):
    aeropuertos = Aereopuerto.objects.all()
    success_message = request.session.pop('success_message', None)
    return render(request, 'aeropuertos/listar.html', 
                  {'aeropuertos': aeropuertos, 
                   'success_message': success_message,
                   'total': is_empty(aeropuertos_count(), True)})

@login_required
def crear_aeropuerto(request):
    if request.method == 'POST':
        form = AeropuertoForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Aeropuerto creado correctamente!'
            return redirect('listar_aeropuertos')
    else:
        form = AeropuertoForm()
    return render(request, 'aeropuertos/formulario.html', {'form': form})

@login_required
def editar_aeropuerto(request, pk):
    aeropuerto = get_object_or_404(Aereopuerto, pk = pk)
    if request.method == 'POST':
        form = AeropuertoForm(request.POST, instance = aeropuerto)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Datos del aeropuerto actualizados correctamente!'
            return redirect('listar_aeropuertos')
    else:
        form = AeropuertoForm(instance = aeropuerto)
    return render(request, 'aeropuertos/editar.html', {'form': form})

@login_required
def eliminar_aeropuerto(request, pk):
    aeropuerto = get_object_or_404(Aereopuerto, pk = pk)
    if request.method == 'POST':
        aeropuerto.delete()
    return redirect('listar_aeropuertos')  

# AVIONES -------------------------------------------------------------------
@login_required
def listar_aviones(request):
    
    aviones = Avion.objects.all()
    success_message = request.session.pop('success_message', None)
    return render(request, 'aviones/listar.html', 
                  {'aviones': aviones, 
                   'success_message': success_message, 
                   'total': is_empty(aviones_count(), True )})

@login_required
def crear_avion(request):
    aeropuertos= Aereopuerto.objects.all()
    if request.method == 'POST':
        form = AvionForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Avion creado correctamente!'
            return redirect('listar_aviones')
    else:
        form = AvionForm()
    return render(request, 'aviones/formulario.html', {'form': form,'aeropuertos':aeropuertos})

@login_required
def editar_avion(request, pk):
    avion = get_object_or_404(Avion, pk = pk)
    if request.method == 'POST':
        form = AvionForm(request.POST, instance = avion)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Datos del avion actualizados correctamente!'
            return redirect('listar_aviones')
    else:
        form = AvionForm(instance = avion)
    return render(request, 'aviones/editar.html', {'form': form})

@login_required
def eliminar_avion(request, pk):
    avion = get_object_or_404(Avion, pk = pk)
    if request.method == 'POST':
        avion.delete()
    return redirect('listar_aviones')  

# VUELOS -------------------------------------------------------------------
@login_required
def listar_vuelos(request):
    vuelos = Vuelo.objects.all()
    success_message = request.session.pop('success_message', None)
    return render(request, 'vuelos/listar.html', 
                  {'vuelos': vuelos, 
                   'success_message': success_message, 
                   'total': is_empty(vuelos_count(), True )})

@login_required
def crear_vuelo(request):
    avion = Avion.objects.all()
    aeropuertos = Aereopuerto.objects.all()
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Vuelo creado correctamente!'
            return redirect('listar_vuelos')
    else:
        form = VueloForm()
    return render(request, 'vuelos/formulario.html', {'form': form,
                                                      'aeropuerto_salida':aeropuertos, 
                                                      'aeropuerto_entrada':aeropuertos, 
                                                      'aviones':avion})
@login_required
def editar_vuelo(request, pk):
    vuelo = get_object_or_404(Vuelo, pk = pk)
    if request.method == 'POST':
        form = VueloForm(request.POST, instance = vuelo)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Datos del vuelo actualizados correctamente!'
            return redirect('listar_vuelos')
    else:
        form = VueloForm(instance = vuelo)
    return render(request, 'vuelos/editar.html', {'form': form})

@login_required
def eliminar_vuelo(request, pk):
    vuelo = get_object_or_404(Vuelo, pk = pk)
    if request.method == 'POST':
        vuelo.delete()
    return redirect('listar_vuelos')


# TRAMO -------------------------------------------------------------------
@login_required
def listar_tramos(request):
    tramos = Tramo.objects.all()
    success_message = request.session.pop('success_message', None)
    return render(request, 'tramos/listar.html', 
                  {'tramos': tramos, 
                   'success_message': success_message, 
                   'total': is_empty(tramos_count(), True )})

@login_required
def crear_tramo(request):
    vuelos = Vuelo.objects.all()
    aeropuertos = Aereopuerto.objects.all()

    if request.method == 'POST':
        form = TramoForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success_message'] = 'Tramo creado correctamente!'
            return redirect('listar_tramos')
    else:
        form = TramoForm()
    return render(request, 'tramos/formulario.html', {'form': form, 'aeropuerto_salida':aeropuertos, 
                                                      'aeropuerto_entrada':aeropuertos,'vuelos':vuelos})

@login_required
def editar_tramo(request, pk):
    tramo = get_object_or_404(Tramo, pk = pk)
    if request.method == 'POST':
        form = TramoForm(request.POST, instance = tramo)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Datos del tramo actualizados correctamente!'
            return redirect('listar_tramos')
    else:
        form = TramoForm(instance = tramo)
    return render(request, 'tramos/editar.html', {'form': form})

@login_required
def eliminar_tramo(request, pk):
    tramo = get_object_or_404(Tramo, pk = pk)
    if request.method == 'POST':
        tramo.delete()
    return redirect('listar_tramos')

# RESERVA -------------------------------------------------------------------
@login_required
def listar_reservas(request):
    reservas = Reserva.objects.all()
    success_message = request.session.pop('success_message', None)
    return render(request, 'reservas/listar.html', 
                  {'reservas': reservas, 
                   'success_message': success_message, 
                   'total': is_empty(reservas_count(), True )})

@login_required
def crear_reserva(request):
    pasajeros = Pasajero.objects.all()
    tarifas = Tarifa.objects.all()
    vuelos = Vuelo.objects.all()
    tramos = Tramo.objects.all()

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success_message'] = 'Reserva creada correctamente!'
            return redirect('listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/formulario.html', {'form': form,'pasajeros':pasajeros, 'tarifas':tarifas, 
                                                        'vuelos':vuelos,'tramos':tramos})

@login_required
def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk = pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance = reserva)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Datos de la reserva actualizados correctamente!'
            return redirect('listar_reservas')
    else:
        form = ReservaForm(instance = reserva)
    return render(request, 'reservas/editar.html', {'form': form})

@login_required
def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk = pk)
    if request.method == 'POST':
        reserva.delete()
    return redirect('listar_reservas')


# MENSAJES -------------------------------------------------------------------
@role_required(['Administrador', 'Supervisor'])
@login_required
def listar_mensajes(request):
    mensajes = Mensaje.objects.all()
    return render(request, 'mensajes/listar.html', 
                  {'mensajes': mensajes, 
                   'total': is_empty(mensajes_count(), True )})

@role_required(['Administrador', 'Supervisor'])
@login_required
def eliminar_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk = pk)
    if request.method == 'POST':
        mensaje.delete()
    return redirect('listar_mensajes')


""" SEGURIDAD ---------------------------------------------------------------"""

# Rol -------------------------------------------------------------------
@role_required('Administrador')
@login_required
def listar_roles(request):
    roles = Rol.objects.all()
    success_message = request.session.pop('success_message', None)
    return render(request, 'roles/listar.html', 
                  {'roles': roles, 
                   'success_message': success_message})


@role_required('Administrador')
@login_required
def crear_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success_message'] = 'Rol creado correctamente!'
            return redirect('listar_roles')
    else:
        form = RolForm()
    return render(request, 'roles/formulario.html', {'form': form})

@role_required('Administrador')
@login_required
def editar_rol(request, pk):
    rol = get_object_or_404(Rol, pk = pk)
    if request.method == 'POST':
        form = RolForm(request.POST, instance = rol)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Datos del rol actualizados correctamente!'
            return redirect('listar_roles')
    else:
        form = RolForm(instance = rol)
    return render(request, 'roles/editar.html', {'form': form})

@role_required('Administrador')
@login_required
def eliminar_rol(request, pk):
    rol = get_object_or_404(Rol, pk = pk)
    if request.method == 'POST':
        rol.delete()
    return redirect('listar_roles')


# Usuario -------------------------------------------------------------------
@role_required('Administrador')
@login_required
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    success_message = request.session.pop('success_message', None)
    return render(request, 'usuarios/listar.html', 
                  {'usuarios': usuarios, 
                   'success_message': success_message,
                   'total': is_empty(usuarios_count(), True) 
                   })

@role_required('Administrador')
@login_required
def crear_usuario(request):
    roles = Rol.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['success_message'] = 'Usuario creado correctamente!'
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/formulario.html', {'form': form,'roles':roles})

@role_required('Administrador')
@login_required
def editar_usuario(request, pk):
    roles = Rol.objects.all()
    usuario = get_object_or_404(Usuario, pk = pk)

    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡Datos del usuario actualizados correctamente!'
            return redirect('listar_usuarios')
    else:
        form = UsuarioEditForm(instance = usuario)
    return render(request, 'usuarios/editar.html', {'form': form, 'rol':roles})

@role_required('Administrador')
@login_required
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk = pk)
    if request.method == 'POST':
        usuario.delete()
    return redirect('listar_usuarios')

@role_required('Administrador')
@login_required
def cambiar_password(request, pk):
    usuario = get_object_or_404(Usuario, pk = pk)

    if request.method == 'POST':
        form = UsuarioPasswordForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            request.session['success_message'] = '¡La Contraseña del usuario ha sido reestablecida!'
            return redirect('listar_usuarios')
    else:
        form = UsuarioPasswordForm(instance = usuario)
    return render(request, 'usuarios/reset.html', {'form': form, 'usuario':usuario})

@login_required
def acceso_denegado(request):
    return render(request, 'denegado.html')