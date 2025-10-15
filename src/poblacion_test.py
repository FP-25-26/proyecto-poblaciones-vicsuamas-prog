from poblacion import *
def main():
    ruta = "./data/population.csv"
    datos =lee_poblaciones(ruta)
    paises = ["Spain","France","Italy"]
    año = 2016
    #print(calcula_paises(lee_poblaciones(ruta)))
    #print(filtra_por_pais(datos,"ESP"))
    #print(filtra_por_paises_y_anyo(datos,año,paises))
    #muestra_evolucion_poblacion(datos,"ESP")
    muestra_comparativa_paises_anyo(datos,año,paises)



if __name__ == '__main__':
    main()