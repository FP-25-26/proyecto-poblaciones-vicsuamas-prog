from collections import namedtuple
import csv

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    lista = []
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        for pais, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
            tupla = RegistroPoblacion(pais, codigo, año, censo)
            lista.append(tupla)
    return lista

def calcula_paises(poblaciones):
    paises = []
    for a in poblaciones:
        paises.append(a.pais)
    paises = list(set(paises))
    paises.sort()
    return paises

def filtra_por_pais(poblaciones,nombre_o_codigo):
    lista = []
    for a in poblaciones:
        if a.pais == nombre_o_codigo or a.codigo == nombre_o_codigo:
            tupla = (a.año,a.censo)
            lista.append(tupla)
    return lista

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    lista = []
    for a in poblaciones:
        if a.pais in paises:
            if a.año == anyo-1:
                tupla = (a.pais,a.censo)
                lista.append(tupla)
    return lista

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    lista_años =[]
    lista_habitantes =[]
    for a in poblaciones:
        if a.codigo == nombre_o_codigo or a.nombre == nombre_o_codigo:
            lista_años.append(a.año)
            lista_habitantes(a.censo)
    plt.title(titulo)