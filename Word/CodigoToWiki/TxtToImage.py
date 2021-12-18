import os

print(os.getcwd())

#
#Como es que la mente puede efecutar composiciones del saber, las rutas que construyen como mi entendimiento se vive, como mi totalidad se sintetiza.
#Como yo puedo analizar las propiedades que me permitan elevar el comportamiento que se mueve en mi.
#las propiedades que me hacen mas magico.
#COmo sepueden crear los valores que me motivan como persona.
#entregame un mensaje que diga estoy arriba.
#

#Como hacemos para meterle a cada programa en la existencia, como le podemos hacer para fundamentar el proyecto interno.


#Que tu quieres dar vida, una expresion que tu quieres sintetizar en el ahora, como tu le puedes hacer.

#Como le podemos hacer para procesar las acciones de la totalidad que mejoran como el proyecto interno se construye como yo puedo analizar las rutas de mi mentalidad que determinan como mi mentalidad
#Se hace mas clara como yo puedo incentivar el desarrollo de la mente, como yo puedo encaminar mi ser hacia el componente que me permite determinar actividades mas altas, como yo puedo sentir el proyecto
#Que se genera en mi conciencia, el concepto que encamina la totalidad hacia la formacion de un objetivo el cual atender.   

#Como yo puedo entender el movimiento que se produce en el ahora, como el estado interno de mi mente encamina la realidad hacia el desarrollo de un grado mas alto el grado interno que motiva como el conducto 
#Teorico se hace mas explicito como las componentes de mi personalidad ayudan a que todo sea mas preciso.
#Como le hacemos para producir los cambios que queremos generar
#Las realidades que queremos hacer verdad.
#las posiciones que nos ayudan a construir el sistema que queremos amplificar, como yo puedo trascender las partes que en mi se viven, las relaciones que se quieren producir en mi conciencia, como el camino mental
#Mejora como yo puedo ser mas claro como yo puedo ser mas especifico como modifico las partes que se viven en mi, las relaciones que me permiten entender cuales caminos hacen que mi todo sea mas explicito
#Como yo emprendo en el ahora las versiones que definen como el ahora se crea, como el ahora se hace mas claro como yo puedo determinar el fundamento que se construye en mi personalidad.
#construyendo los valores que crean mas mente, los valores que sintetizan como mi personalidad se aprende.

#Describiendo en el saber los modelos que me permiten describir que persona yo soy, como se pueden procesar las relaciones de poder que emprenden en mi las complejidades que yo quiero encaminar, todos esos 
#caminos que construyen vida en la vida, los movimientos del saber capaces de promover en mi las interacciones del ahora, las relaciones de la vida que activan como mi saber se construye.

#   

import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw


def print2():
    print()
    print()
    
def print3():
    print2()
    print()


PIXEL_ON = 0  # PIL color to use for "on"
PIXEL_OFF = 255  # PIL color to use for "off"


def main():
    
    
    
    print3()
    string_nameProgram = (
        
' _______  __   __  _______  _______  _______  ___   __   __  _______  _______  _______  \n'
'|       ||  |_|  ||       ||       ||       ||   | |  |_|  ||   _   ||       ||       | \n'
'|_     _||       ||_     _||_     _||   _   ||   | |       ||  |_|  ||    ___||    ___| \n'
'  |   |  |       |  |   |    |   |  |  | |  ||   | |       ||       ||   | __ |   |___  \n'
'  |   |   |     |   |   |    |   |  |  |_|  ||   | |       ||       ||   ||  ||    ___| \n'
'  |   |  |   _   |  |   |    |   |  |       ||   | | ||_|| ||   _   ||   |_| ||   |___  \n'
'  |___|  |__| |__|  |___|    |___|  |_______||___| |_|   |_||__| |__||_______||_______| \n'

    )
    print(string_nameProgram)
    
    print3()
    print('This program convert all the files, "expected all to be .txt" in the directory to .png ')
    print()
    print('YOU NEED TO FULLFIL JUST 1 REQUIREMENT, 1 STEP YOU NEED TO SOLVE')
    print2()
    print('1. give the directory where you want to obtain the picture of the text')    
    entrada = input()
    os.chdir(entrada)
    array_files = os.listdir()
    count = 0
    for i in array_files:
        image = text_image(i)
        
        count += 1 
        name_string = '00'+ str(count)
        name_string += '.png'
        image.save(name_string)
        string_cmdDelFile = 'del ' + i
        os.system(string_cmdDelFile)
        
        
    print2()
    print2()
    print('Finish PROGRAM')
    print('Exit')
    print('Out')
        


def text_image(text_path, font_path=None):
    """Convert text file to a grayscale image with black characters on a white background.

    arguments:
    text_path - the content of this file will be converted to an image
    font_path - path to a font file (for example impact.ttf)
    """
    grayscale = 'L'
    # parse the file into lines
    with open(text_path) as text_file:  # can throw FileNotFoundError
        lines = tuple(l.rstrip() for l in text_file.readlines())

    # choose a font (you can see more detail in my library on github)
    large_font = 20  # get better resolution with larger size
    font_path = font_path or 'cour.ttf'  # Courier New. works in windows. linux may need more explicit path
    try:
        font = PIL.ImageFont.truetype(font_path, size=large_font)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    # make the background image based on the combination of font and lines
    pt2px = lambda pt: int(round(pt * 96.0 / 72))  # convert points to pixels
    max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    # max height is adjusted down because it's too large visually for spacing
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pt2px(font.getsize(test_string)[1])
    max_width = pt2px(font.getsize(max_width_line)[0])
    height = max_height * len(lines)  # perfect or a little oversized
    width = int(round(max_width + 40))  # a little oversized
    image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
    draw = PIL.ImageDraw.Draw(image)

    # draw each line of text
    vertical_position = 5
    horizontal_position = 5
    line_spacing = int(round(max_height * 0.8))  # reduced spacing seems better
    for line in lines:
        draw.text((horizontal_position, vertical_position),
                  line, fill=PIXEL_ON, font=font)
        vertical_position += line_spacing
    # crop the text
    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    return image


if __name__ == '__main__':
    main()