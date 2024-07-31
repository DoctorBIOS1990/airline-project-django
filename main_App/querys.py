from .models import Aereopuerto, Avion, Vuelo, Tarifa, Tramo, Pasajero, Reserva, Usuario, Mensaje
from django.db.models import Sum, Max, Min, Count
from django.db import connection

# Check Empty 
def is_empty(data, option):
    if ((data == 0)) and (option):
        return "---"
    elif (data == 0):
        return "No hay registros."
    return data

# Counts
def pasajeros_count():
    return Pasajero.objects.count()

def mensajes_count():
    return Mensaje.objects.count()

def aviones_count():
    return Avion.objects.count()

def aeropuertos_count():
    return Aereopuerto.objects.count()

def tramos_count():
    return Tramo.objects.count()

def vuelos_count():
    return Vuelo.objects.count()

def tarifas_count():
    return Tarifa.objects.count()

def reservas_count():
    return Reserva.objects.count()

def usuarios_count():
    return Usuario.objects.count()

# Analitica
def total_facturado():
     return Reserva.objects.all().aggregate(total = Sum('precio')) 

def max_facturado():
     return Reserva.objects.all().aggregate(max = Max('precio')) 

def min_facturado():
     return Reserva.objects.all().aggregate(min = Min('precio')) 

def distancia_recorrida():
     return Tramo.objects.all().aggregate(total = Sum('distancia')) 

def asientos_total():
     return Avion.objects.all().aggregate(total = Sum('asientos')) 

def max_bonificacion():
    return Tarifa.objects.all().aggregate(max = Max('descuento'))

def get_data():
    return {
        'count_pasajeros': pasajeros_count(),
        'count_aviones': aviones_count(),
        'count_aeropuertos': aeropuertos_count(),
        'count_tramos': tramos_count(),
        'count_vuelos': vuelos_count(),
        'count_tarifas' : tarifas_count(),
        'count_reservas': reservas_count(),
        'total_facturado': total_facturado(),
        'max_facturado': max_facturado(),
        'min_facturado': min_facturado(),
        'distancia': distancia_recorrida(),
        'disponibilidad': asientos_total(),
        'asignacion': aviones_Asig(),
        'max_descuento': max_bonificacion(),
        'visitas_Ciudades': visitas_Ciudades(),
        'tarifa_popular': tarifa_popular(),
        }

# Query SQL - Cantidad Aviones por Aeropuertos
def aviones_Asig():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT aero.nombre, COUNT(avion.aeropuerto_id) AS Asignados
            FROM main_App_avion AS avion
            INNER JOIN main_App_aereopuerto AS aero
            ON avion.aeropuerto_id = aero.id
            GROUP BY avion.aeropuerto_id, aero.nombre
        """)
        results = cursor.fetchall()
    return results

# Query SQl - Contabilizando ciudades visitadas
def visitas_Ciudades():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT d.Ciudad as Ciudad, COUNT(r.tramo_id) as Viajes
            FROM main_App_reserva AS r
            LEFT JOIN main_App_tramo AS t ON r.tramo_id = t.id
            INNER JOIN main_App_aereopuerto AS d ON t.aeropuerto_llegada_id = d.id
            GROUP BY d.Ciudad
        """)
        results = cursor.fetchall()
    return results

# Query SQL - Tarifa mas comprada
def tarifa_popular():
    with connection.cursor() as cursor:
        cursor.execute("""
                SELECT b.nombre, a.Solicitadas as MaxSolicitadas
                FROM (
                    SELECT tarifa_id, COUNT(*) as Solicitadas
                    FROM main_App_reserva
                    GROUP BY tarifa_id
                ) a
                LEFT JOIN main_App_tarifa b ON a.tarifa_id = b.id
                WHERE a.Solicitadas = (
                    SELECT MAX(Solicitadas)
                    FROM (
                        SELECT tarifa_id, COUNT(*) as Solicitadas
                        FROM main_App_reserva
                        GROUP BY tarifa_id
                    ) c
                )
        """)
        results = cursor.fetchall()
    return results

