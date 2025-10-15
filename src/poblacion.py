from collections import namedtuple
import csv
import matplotlib.pyplot as plt

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
    titulo = f"Grafica {nombre_o_codigo}"
    lista_años =[]
    lista_habitantes =[]
    for a in poblaciones:
        if a.codigo == nombre_o_codigo or a.pais == nombre_o_codigo:
            lista_años.append(a.año)
            lista_habitantes.append(a.censo)
    plt.title(titulo)
    plt.plot(lista_años,lista_habitantes)
    plt.show()


def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    titulo = f"Grafica {paises} {anyo}"
    lista_paises = []
    lista_habitantes = []
    for a in poblaciones:
        if a.año == anyo and a.pais in paises:
            lista_paises.append(a.pais)
            lista_habitantes.append(a.censo)
    plt.title(titulo)
    plt.bar(lista_paises,lista_habitantes)
    plt.show()