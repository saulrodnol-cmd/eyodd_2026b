#Importando el modulo array de la biblioteca 
#array y renombrando  arr
from array import array as arr

def print_array(input):
    print('[',end =" ")
    for element in input:
        print(element,end=',')
        print("/b]")
        
    

my_array = arr('i',[2,20,25,20])
print_array(my_array)
#Buscar un elemnto 
number_to_search = 15
counter = 0
print(f"se busca{number_to_search}en el arreglo.")
for intenger in my_array:
    if intenger == number_to_search:
        print("Numero encontrado")
        # sirve para terminar el ciclo 
        break
    #Interpretamos contador
    counter+=1
    if counter == len (my_array):
        print("Numero encontrado")
    