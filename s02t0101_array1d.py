# Array 
# from array import *
import array as arr 

# Creacion de un arreglo 
# i: Entero con signo
# I: entero sin signo
# f: numero decimal
# d: numero decimal doble
# u: carácteres unicode
my_array = arr.array('i',[10,22,300,1,2,3,4,5,6,7,8,9,10,11])

# Iteracion automatica
# for num in my_array:
    # print(num)

# Acceso inidival a los elementos
# print(my_array[0]) # Primer elemento
# print(my_array[1]) # Segundo elemento
# print(my_array[2]) # Tercer elemento

# Tamaño de un arreglo
# Length
# print(len(my_array))

# Iteracion por indices 
# for i in range(len(my_array)):
#     if my_array[i] % 2 == 0:
        # print(f"Elemento Num {i+1}:{my_array[i]}")

# Busqueda de un elemento
num_to_search = 200 

#Modifucando un valor usando
#backet notation
my_array[7] = 200

try:
    print(f"Localizando {num_to_search}: {my_array.index(num_to_search)}")
except:
    print("⚠️ Numero no escontrado!!!")
