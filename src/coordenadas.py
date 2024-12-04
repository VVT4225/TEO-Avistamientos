## Definición de tipos
# Creación de una tupla con nombre para las coordenadas
from collections import namedtuple
from math import radians, sin, cos, asin, sqrt
Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def a_radianes(coordenadas):
    '''Convierte unas coordenadas en grados a radianes

    @param coordenadas: Coordenadas que se quieren convertir a radianes
    @type coordenadas: Coordenadas(float, float)
    @return: Las coordenadas convertidas a radianes
    @rtype: Coordenadas(float, float)
    
    Ayuda:
    Usa la función radians para convertir a radianes. Por ejemplo,
    latitud_radianes = radians(latitud)
    '''
    return Coordenadas(radians(coordenadas.latitud), radians(coordenadas.longitud)) 


def distancia_harvesine(coordenadas1, coordenadas2):
    '''Devuelve la distancia de harvesine entre dos coordenadas

    @param coordenadas1: Coordenadas del primer punto
    @type coordenadas1: Coordenadas(float, float)
    @param coordenadas2: Coordenadas del segundo punto
    @type coordenadas2: Coordenadas(float, float)
    @return: La distancia harvesine entre las dos coordenadas dadas como parámetro
    @rtype: float
    '''
    coord1_rad = a_radianes(coordenadas1)
    coord2_rad = a_radianes(coordenadas2)
    dif_lat = coord2_rad.latitud - coord1_rad.latitud
    dif_lon = coord2_rad.longitud - coord1_rad.longitud
    a = sin(dif_lat/2)*2 + cos(coord1_rad.latitud) * cos(coord2_rad.latitud) * sin(dif_lon/2)*2
    r = 6371
    d = 2 * r * asin(sqrt(a))
    return d

def redondear(coordenadas):
    '''Devuelve unas coordenadas cuya latitud y longitud son 
    el redondeo de la latitud y la longitud de las coordenadas originales

    @param coordenadas: Coordenadas que se quieren convertir a radianes
    @type coordenadas: Coordenadas(float, float)
    @return: Las coordenadas redondeadas
    @rtype: Coordenadas(float, float)

    Ayuda:
    Usa la función round para redondear. Por ejemplo,
    latitud_redondeada = round(latitud)
    '''
    return Coordenadas(round(coordenadas.latitud),round(coordenadas.longitud))