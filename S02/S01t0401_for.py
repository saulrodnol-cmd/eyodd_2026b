"""
ESCRIBIR un program que calcule la suma de los 
"n"numeros naturales por ejemplo si n = 100
el programa calculara la suma del 1 al 100
"""
# Importamos biblioteca time
import time

# creando una marca de tiempo
timestamp_01 = time.time()

#programa que calcula la suma de los n numeros naturales n = 100
n = 100
sum = 0

#ciclo for 
for number in range (1,n+1):
    print(str(number) + " ")