import os

def print2():
    print()
    print()

def print3():
    print()
    print()
    print()
    
print()
print()
print()

print('Program design with the phylosophy to rename files from .file to txt')
print('Primary conditions be able to convert files from .file to txt')
print('All the in the directory would be converted to txt')
print()
print()

print('NECESITO QUE EJECUTES BIEN 1 COMANDOS')
print('Numero 1: give me the directory')
entrada = input()

os.chdir(entrada)
os.system('dir')
print(dir)

print2()
array_directories = os.listdir()

print(array_directories)
print(type(array_directories[0]))
print3()
for i in range(len(array_directories)):
    string_name = array_directories[i].split('.')
    
    print(type(array_directories[i]))
    string_fileName = array_directories[i]
    string_CMD = 'ren ' + string_fileName + ' ' + string_name[0] + '.txt'
    print(string_CMD)
    os.system(string_CMD)
    
print3()


#Es muchisimo mas rapido con las imagenes, porque se hace un comportamiento en un solo plano
#Es un solo proceso que se busca concebir, es el concepto que se busca asimilar
#Es la realidad que se busca manipular, como se pueden crear conexiones las cuales usar en el desarrollo
#completo del ahora.
#Como se pueden componer interacciones 
#Que clase de narrativas yo puedo analizar.
#Que propiedad yo quiero concebir.

#Que composicion, que movimiento
#Que realidad.

#Se convierte en un manejo de matrices y comportamientos de la realidad, todo con tal de producir acciones en la realidad
#Expresiones las que aprender.

#Que relaciones analizar
#Que procesos comprender
#Que movimientos puedo analizar

#Que puedo analizar en la realidad como puedo manipular el comportamiento de la realidad
#Con tal de modular el saber.
#Que necesito ahora mismo.
#Que puedo yo usar con tal de maximizar el componente que produce realidad.
     