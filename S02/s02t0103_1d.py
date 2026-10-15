#Importando el modulo array de la biblioteca 
#array y renombrando  arr
from array import array as arr
#Importando una funcion de otro archivo
#archivo
from s02t010102 import print_array

my_array = arr('i',[2,20,25,20])

print("---ANTES DE LA INSERCCION---")
print_array(my_array)

#Inserccion
my_array.insert(1,90)
print("---DESPUES DE LA INSERCION---")
print_array(my_array)