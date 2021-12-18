import os


def print2():
    print()
    print()

def print3():
    print()
    print()
    print()
    
    
    
print2()
print('THIS PROGRAM GIVE YOU TWO TXT\'S:')
print('ONE WITH THE HTML STRINGS THAT YOU CAN PASTE IN THE WIKI INDEX WEBPAGE ')
print('THE SECOND WOULD CONTAIN HTML STRINGS THAT LINK YOU WITH THE FILE IN THE REPO ')
    
print2()

print('son dos carpetas USUARIO')
print()
print('La primera carpeta contiene el las imagenes')
print('esta carpeta contiene los nombres de los archivos que quiero linkear ')
print('En un txt el cual pegar en un html')
print('junto a las imagenes intercaladas por nombre ')
print('La segunda carpeta contiene las imagenes del codigo')


print2()
print('DEBES CUMPLIR 3 ENTRADAS DE CODIGO CORRECTAS')
print2()

print('1.ESCRIBIR DIRECTORIO DE IMAGENES TO PARSER:')
entrada = input()

os.chdir(entrada)

#Es un punto que unicamente se puede resolver en el momento en que usted este resolviendo el punto
#Es algo que le solicita a usted respuesta unicamente cuando se le presente
#Pero la unica forma que usted tiene de responder a esa pregunta tan dificil es usted enfrentandose a la busqueda de
#la solucion especifica de esa complejidad que esta esta tratando de responder.

#Eso es matematica y eso es velocidad 
#Una serie de reglas que parametrizan el desarrollo de la velocidad que usted esta buscando.
#EL desarrollo analitico que le permite modelar el trabajo del saber.

#Ya que cual es el componente que necesito, como puedo aprender a formalizar las caracteristicas

list_imgDirectories = os.listdir()

BASE_DIRECTORY = 'D:\INTERNET\Wiki-Andresito-02\Wiki-01-U-02\Word\CodigoToWiki'
os.chdir(BASE_DIRECTORY)

fun_create = open('za_imgDocument.txt', 'w+')


for i in range(len(list_imgDirectories)):
    #
    #<img src='img/logo.png' alt="logo"></a>
    #
    string_htmlParser  = '<img src=\'img/' + list_imgDirectories[i] + '\' alt="logo">' + '\n'
    fun_create.writelines(string_htmlParser)

fun_create.close()



print2()
print3()

print('Finish first step')
print2()
print('Este directorio solo tiene archivos de codigo')
print('Es una propiedad capaz de centrar el desarrollo de codigo')
print2()
print2()
print('2. ESCRIBE EL DIRECTORIO DE LOS ARCHIVOS DE CODIGO QUE QUIERES CONVERTIR A HTML LINK:')
entrada = input()
os.chdir(entrada)

list_codeDirectories = os.listdir()

os.chdir(BASE_DIRECTORY)

print2()
print('#base repo example:  https://github.com/Andraelity/Wiki-01-U-02')
print2()
print('3. GET THE REPONAME WHERE THE WEBPAGE WILL BE STORED:')
#base repo example https://github.com/Andraelity/Wiki-01-U-02
entrada = input()


fun_create = open('zb_fileNamesGitHub.txt', 'w+')

#<h1><a href="https://github.com/Andraelity/Wiki-01-U-02.git">Matrix behavior</a></h1>

for i in range(len(list_codeDirectories)):
    string_htmlParser2  = entrada + '/tree/main/' + list_codeDirectories[i]
    string_htmlNameFileParser = '<h1><a href="'+ string_htmlParser.strip() + '">'+ string_htmlParser.strip() + '</a></h1>' + '\n'
    fun_create.writelines(string_htmlNameFileParser)

fun_create.close()

#Que componente quiero analizar ahora, como el desarrollo de este suceso se produce a si mismo en pro de la generacion 
#De componentes mas precisos.




print2()
print('exit')
print('finish program')
print('End of cycle')



#Cual es la siguiente apreciacion de la realidad
#Cual es el siguiente concepto 

#Yo espero que esto provea el siguiente concepto 
  
#El comando que yo quiero paremetrizar con el concepto que se vive ahora mismo proviene de un analisis mas preciso
#un analisis mas especifico de la realidad como se pueden comprender las interacciones que producen como la mente se vive como el saber
#Se puede maximizar como yo puedo modelar el desarrollo que motiva el aprendizaje de las partes, como yo puedo analizar el fundamento que nos conecta
#Con las partes
#Lo que yo busco es bajar documentacion, sobre como se crea el credito de desarrollo teorico explicito, texto son scripts
#Texto son las propiedades que motivan como el componente interno se desarrolla como se pueden armonizar las cualidades
#Que motivan como el analisis se representa como se pueden armonizar las composiciones de la realidad 
#Como yo puedo sintetizar abstraccioens.
#Es la capacidad de estar viendo narrativas en internet
#Es la capacidad de promover las componentes que producen un componente mas explicito
#Un componente mas especifico
#Es el tipo de realidad que nos permite sintetizar abstracciones como yo puedo comprender el movimiento que orienta
#El saber que se mueve en mi 
#Esa es la prueba que el contexto mecanico evolutivo maquinario y productorio
#Baja su cualidad en la capacidad de este sostenerse a si mismo 
#Es la prueba que me determina que mi realidad es mas grande.

#pero lo principal en este de ecosistemas seria, la capacidad de pronosticar y diferenciar acciones sobre la realidad
#Acciones las cuales determinar
#Expresioens las cuales definir
#Conceptos los cuales concebir
#Conceptos los cuales maravillar
#las relaciones humanas que promueven como la expresion interna se aprende
