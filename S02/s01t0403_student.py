'''
NOTAS: 
1. Identifico el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiantes
2. Es ver cuanto crece el numero de
operaciones en mi algoritmo conforme
crece el tamaño de la entrada
Agrego las bigO identificadas 
Teniendo en cuenta la Cota superior asintotica
O(1) + O(4) = O(n+4) = O(n)
'''

# Creando una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack']
student_list_02 = ['Mike','Saul','Walter','Jessy']

# Verificando la presencia de un estudiante 
def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student: # O(n)
            print("✅ Estudiante encontrado") # O(1)
            return student # O(1)
    # Si no encuentro al estudiante
    print("❌ Estudiante no encontrado") # O(1)
    return None # O(1)

# Probando algoritmo
check_student("Walter",student_list_02)
