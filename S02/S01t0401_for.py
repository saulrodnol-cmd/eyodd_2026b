"""
Escribir un programa qye calcule
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculara la suma del 1 al 100
"""
# Importamos biblioteca time
import time

 #Creando una marca de tiempo
timestamp_01 = time.time()

#Porgrama que calcula las suma
#de los "n" numeros naturales
n = 100
Total_sum = 0

#Ciclo for 
for number in range(1,n+1):
    Total_sum = Total_sum + number
    # 1: sum <- 0 + 1
    # sum = 1
    # 2: sum <- 1 + 2
    # sum = 3
    # 3: sum <- 3 + 4
    # ...
    # 100: sum <- sum_(-1) + 100
print(f"la suma de 1 hasta{n} es: {Total_sum}")

# tomando el tiempo final
timestamp_02 = time.time()

# impresion del tiempo de ejecucion
print(f"tiempo de ejecucion: {(timestamp_02-timestamp_01) * 1e6:.2f}  μs")