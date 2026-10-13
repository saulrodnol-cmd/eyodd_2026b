#Array
#from array import *
import array as arr

#creacion de un arreglo 
#i:Entero con signo 
#I;Entero sin signo
#f:Numero decimal
#d:Numero decimal doble 
#u:Caracteres unucode
my_array = arr.array('i',[10,22,300,1,2,3,4,5,6,7,8,9,10])

#Interacion automatica
#for num in my_array:
   # print(num)

#Acceso individual a los elementos
#print(my_array[0])#Primer elemento
#print(my_array[1])#Segundo elemnto    
#print(my_array[1])#Tercer elemento 

#El tamaño de un arreglo 
#print(len(my_array))

#Interacion por indices
for i in range(len(my_array)):
    if my_array[i]% 2 == 0:
        print(f"Elemntos Num {i+1}:{my_array[i]}")
