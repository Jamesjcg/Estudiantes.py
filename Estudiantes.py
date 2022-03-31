from ctypes.wintypes import PINT
import statistics as st
import csv


class Solucion:
    def __init__(self):
        self.n = 0
    
    def imprimir_todo(self):# Imprime todo el archivo
      with open('datosprueba.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
                 print(row)
    
    def prom_est_med(self):# Calcula el promedio de cada estudiantes y media del grupo
        with open('datosprueba.csv', newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                suma=0
                for colum in reader:
                    matematicas = int(colum[5])
                    lenguaje = int(colum[6])
                    ciencias = int(colum[7])
                    ingles = int(colum[8])
                    ciudadanas = int(colum[9])
                    promed = (matematicas+lenguaje+ciencias+ingles+ciudadanas)/5
                    
                    suma=suma+promed
                    media =suma/100
                    print("AQUI", matematicas, "LENGUAJE", colum[6], "CIENCIAS", colum[7],
                        'INGLES', colum[8], 'CIUDADANIAS', colum[9], "EL PROMEDIO TOTAL ES", promed)
                    print(colum)
                print("LA MEDIA TOTAL ES:", media)

    def mayor_prom(self): #Datos del mayor promedio
        with open('datosprueba.csv', newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                mayor=0
                for colum in reader:
                    matematicas = int(colum[5])
                    lenguaje = int(colum[6])
                    ciencias = int(colum[7])
                    ingles = int(colum[8])
                    ciudadanas = int(colum[9])
                    suma = (matematicas+lenguaje+ciencias+ingles+ciudadanas)/5
                    
                    if suma>mayor:
                        mayor=suma

                print("EL estudiante con mayor promedio es", colum , "Con un promedio de:",mayor)
    
    def menor_mayor_prom(self): #Numero de personas que tienen promedio por debajo de la media y # por encima
        with open('datosprueba.csv', newline='') as File:  
            reader = csv.reader(File)
            for row in reader:
                mayor=0
                menor=0
                for colum in reader:
                    matematicas = int(colum[5])
                    lenguaje = int(colum[6])
                    ciencias = int(colum[7])
                    ingles = int(colum[8])
                    ciudadanas = int(colum[9])
                    suma = (matematicas+lenguaje+ciencias+ingles+ciudadanas)/5
                    
                    if suma>mayor:
                        mayor=mayor + 1
                    else:
                        menor=menor + 1
                print ("Los estudiantes con promedio por debajo de la media son:", menor, " Y Los estudiantes con promedio por encima de la media son:",mayor)


    
datos=Solucion()
i=0

while i!=5:
    print("""
        1. Imprimir todo el archivo 
        2. Calcular el promedio de cada estudiantes y media del grupo
        3. Datos de la persona con mayor promedio
        4. Cuántas personas tienen promedio por debajo de la media y cuantos por encima
        5. Salir
          """)
    i = int(input('Ingrese una opción: '))

    if i == 1:
       datos.imprimir_todo() 
    elif i == 2:
           datos.prom_est_med()
    elif i == 3:
           datos.mayor_prom()
    elif i == 4:
           datos.menor_mayor_prom()
