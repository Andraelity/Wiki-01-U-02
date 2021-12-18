import os

def print2():
    print()
    print()

def print3():
    print()
    print()
    print()




PROGRAM_NAME = (
    
                                                                                                                                                                                                      
'                                                                                                                                                                                                      \n'
'WWWWWWWW                           WWWWWWWWEEEEEEEEEEEEEEEEEEEEEEBBBBBBBBBBBBBBBBB   PPPPPPPPPPPPPPPPP        AAA                  GGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEE                                \n'
'W::::::W                           W::::::WE::::::::::::::::::::EB::::::::::::::::B  P::::::::::::::::P      A:::A              GGG::::::::::::GE::::::::::::::::::::E                                \n'
'W::::::W                           W::::::WE::::::::::::::::::::EB::::::BBBBBB:::::B P::::::PPPPPP:::::P    A:::::A           GG:::::::::::::::GE::::::::::::::::::::E                                \n'
'W::::::W                           W::::::WEE::::::EEEEEEEEE::::EBB:::::B     B:::::BPP:::::P     P:::::P  A:::::::A         G:::::GGGGGGGG::::GEE::::::EEEEEEEEE::::E                                \n'
' W:::::W           WWWWW           W:::::W   E:::::E       EEEEEE  B::::B     B:::::B  P::::P     P:::::P A:::::::::A       G:::::G       GGGGGG  E:::::E       EEEEEE                                \n'
'  W:::::W         W:::::W         W:::::W    E:::::E               B::::B     B:::::B  P::::P     P:::::PA:::::A:::::A     G:::::G                E:::::E                                             \n'
'   W:::::W       W:::::::W       W:::::W     E::::::EEEEEEEEEE     B::::BBBBBB:::::B   P::::PPPPPP:::::PA:::::A A:::::A    G:::::G                E::::::EEEEEEEEEE                                   \n'
'    W:::::W     W:::::::::W     W:::::W      E:::::::::::::::E     B:::::::::::::BB    P:::::::::::::PPA:::::A   A:::::A   G:::::G    GGGGGGGGGG  E:::::::::::::::E                                   \n'
'     W:::::W   W:::::W:::::W   W:::::W       E:::::::::::::::E     B::::BBBBBB:::::B   P::::PPPPPPPPP A:::::A     A:::::A  G:::::G    G::::::::G  E:::::::::::::::E                                   \n'
'      W:::::W W:::::W W:::::W W:::::W        E::::::EEEEEEEEEE     B::::B     B:::::B  P::::P        A:::::AAAAAAAAA:::::A G:::::G    GGGGG::::G  E::::::EEEEEEEEEE                                   \n'
'       W:::::W:::::W   W:::::W:::::W         E:::::E               B::::B     B:::::B  P::::P       A:::::::::::::::::::::AG:::::G        G::::G  E:::::E                                             \n'
'        W:::::::::W     W:::::::::W          E:::::E       EEEEEE  B::::B     B:::::B  P::::P      A:::::AAAAAAAAAAAAA:::::AG:::::G       G::::G  E:::::E       EEEEEE                                \n'
'         W:::::::W       W:::::::W         EE::::::EEEEEEEE:::::EBB:::::BBBBBB::::::BPP::::::PP   A:::::A             A:::::AG:::::GGGGGGGG::::GEE::::::EEEEEEEE:::::E                                \n'
'          W:::::W         W:::::W          E::::::::::::::::::::EB:::::::::::::::::B P::::::::P  A:::::A               A:::::AGG:::::::::::::::GE::::::::::::::::::::E                                \n'
'           W:::W           W:::W           E::::::::::::::::::::EB::::::::::::::::B  P::::::::P A:::::A                 A:::::A GGG::::::GGG:::GE::::::::::::::::::::E                                \n'
'            WWW             WWW            EEEEEEEEEEEEEEEEEEEEEEBBBBBBBBBBBBBBBBB   PPPPPPPPPPAAAAAAA                   AAAAAAA   GGGGGG   GGGGEEEEEEEEEEEEEEEEEEEEEE                                \n'
'        GGGGGGGGGGGGGEEEEEEEEEEEEEEEEEEEEEENNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR                  AAA         TTTTTTTTTTTTTTTTTTTTTTT     OOOOOOOOO     RRRRRRRRRRRRRRRRR   \n'
'     GGG::::::::::::GE::::::::::::::::::::EN:::::::N       N::::::NE::::::::::::::::::::ER::::::::::::::::R                A:::A        T:::::::::::::::::::::T   OO:::::::::OO   R::::::::::::::::R  \n'
'   GG:::::::::::::::GE::::::::::::::::::::EN::::::::N      N::::::NE::::::::::::::::::::ER::::::RRRRRR:::::R              A:::::A       T:::::::::::::::::::::T OO:::::::::::::OO R::::::RRRRRR:::::R \n'
'  G:::::GGGGGGGG::::GEE::::::EEEEEEEEE::::EN:::::::::N     N::::::NEE::::::EEEEEEEEE::::ERR:::::R     R:::::R            A:::::::A      T:::::TT:::::::TT:::::TO:::::::OOO:::::::ORR:::::R     R:::::R\n'
' G:::::G       GGGGGG  E:::::E       EEEEEEN::::::::::N    N::::::N  E:::::E       EEEEEE  R::::R     R:::::R           A:::::::::A     TTTTTT  T:::::T  TTTTTTO::::::O   O::::::O  R::::R     R:::::R\n'
'G:::::G                E:::::E             N:::::::::::N   N::::::N  E:::::E               R::::R     R:::::R          A:::::A:::::A            T:::::T        O:::::O     O:::::O  R::::R     R:::::R\n'
'G:::::G                E::::::EEEEEEEEEE   N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE     R::::RRRRRR:::::R          A:::::A A:::::A           T:::::T        O:::::O     O:::::O  R::::RRRRRR:::::R \n'
'G:::::G    GGGGGGGGGG  E:::::::::::::::E   N::::::N N::::N N::::::N  E:::::::::::::::E     R:::::::::::::RR          A:::::A   A:::::A          T:::::T        O:::::O     O:::::O  R:::::::::::::RR  \n'
'G:::::G    G::::::::G  E:::::::::::::::E   N::::::N  N::::N:::::::N  E:::::::::::::::E     R::::RRRRRR:::::R        A:::::A     A:::::A         T:::::T        O:::::O     O:::::O  R::::RRRRRR:::::R \n'
'G:::::G    GGGGG::::G  E::::::EEEEEEEEEE   N::::::N   N:::::::::::N  E::::::EEEEEEEEEE     R::::R     R:::::R      A:::::AAAAAAAAA:::::A        T:::::T        O:::::O     O:::::O  R::::R     R:::::R\n'
'G:::::G        G::::G  E:::::E             N::::::N    N::::::::::N  E:::::E               R::::R     R:::::R     A:::::::::::::::::::::A       T:::::T        O:::::O     O:::::O  R::::R     R:::::R\n'
' G:::::G       G::::G  E:::::E       EEEEEEN::::::N     N:::::::::N  E:::::E       EEEEEE  R::::R     R:::::R    A:::::AAAAAAAAAAAAA:::::A      T:::::T        O::::::O   O::::::O  R::::R     R:::::R\n'
'  G:::::GGGGGGGG::::GEE::::::EEEEEEEE:::::EN::::::N      N::::::::NEE::::::EEEEEEEE:::::ERR:::::R     R:::::R   A:::::A             A:::::A   TT:::::::TT      O:::::::OOO:::::::ORR:::::R     R:::::R\n'
'   GG:::::::::::::::GE::::::::::::::::::::EN::::::N       N:::::::NE::::::::::::::::::::ER::::::R     R:::::R  A:::::A               A:::::A  T:::::::::T       OO:::::::::::::OO R::::::R     R:::::R\n'
'     GGG::::::GGG:::GE::::::::::::::::::::EN::::::N        N::::::NE::::::::::::::::::::ER::::::R     R:::::R A:::::A                 A:::::A T:::::::::T         OO:::::::::OO   R::::::R     R:::::R\n'
'        GGGGGG   GGGGEEEEEEEEEEEEEEEEEEEEEENNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRRAAAAAAA                   AAAAAAATTTTTTTTTTT           OOOOOOOOO     RRRRRRRR     RRRRRRR\n'
'                                                                                                                                                                                                      \n'
'                                                                                                                                                                                                      \n'
'                                                                                                                                                                                                      \n'
'                                                                                                                                                                                                      \n'
'                                                                                                                                                                                                      \n'
'                                                                                                                                                                                                      \n'
'                                                                                                                                                                                                      \n'
''
)


print(PROGRAM_NAME)


print2()
print3()


print('USUARIO NECESITO QUE POSICIONES DOS TXT\'S EN DONDE SE EJECUTA EL PROGRAMA')
print('First txt contain\'s the text to paste')
print('Second txt containt\'s the core that you want to show')


VARIABLE_LINKSYMBOL = 'https://raw.githubusercontent.com/Andraelity/Symbol-1/main/Symbol.png'
print()

print2()

print('This program would generate 1-one txt file with the data to make webpage ')
print('https://github.com/Andraelity/Gitrepo.git')
print2()
print('1. Please paste the link of the repo where you want to store the webpage it\'s ')
entrada = input()

VARIABLE_LINKREPO = entrada

container_TxtHmtl = open('index_1.txt', 'w+')



STIRNG_INICIOPAGES = (
'    <!doctype html>\n'
'<html class="no-js" lang="en">\n'
'	<meta name="viewport" content="width=device-width,initial-scale=1"/>\n'
'    <head>\n'
'        <meta charset="utf-8">\n'
'        <meta http-equiv="x-ua-compatible" content="ie=edge">\n'
'        <title>Matrix behavior</title>\n'
'        <meta name="description" content="">\n'
'        <meta name="viewport" content="width=device-width, initial-scale=1">\n'
'		<link rel="canonical" href="http://html5-templates.com/" />\n'
'        <link rel="apple-touch-icon" href="apple-touch-icon.png">\n'
'        <!-- Place favicon.ico in the root directory -->\n'
'        <link rel="stylesheet" href="style.css">\n'
'        <script src="js/vendor/modernizr-2.8.3.min.js"></script>\n'
'    </head>\n'
'    <body>\n'
'        <!--[if lt IE 8]>\n'
'            <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="https://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>\n'
'        <![endif]-->\n'
)

container_TxtHmtl.writelines(STIRNG_INICIOPAGES)


print2()
print('A name to use as a title in the webpage like, example:')
print('Matrix modulation of the sound')
print2()
print('2. NAME THE WEBPAGE')

entrada = input()

VARIABLE_NAMEPAGE = entrada


string_html = (
    '				<div class="article">\n'
)

container_TxtHmtl.writelines(string_html)

print('writing link of the repo to the html')

string_html = (
    '<h1><a href="'+  VARIABLE_LINKREPO  + '">' + VARIABLE_NAMEPAGE +'</a></h1>\n'
)

container_TxtHmtl.writelines(string_html)

print('writing link of the repo link')

string_html = (
    '<h1><a href="'+ VARIABLE_LINKREPO + '">' + VARIABLE_LINKREPO	+'</a></h1>	\n'    
)

container_TxtHmtl.writelines(string_html)



string_html = (
    '<p class="siteSub">From Wikipedia and Andraelity, a relation with Me and Wikipedia</p>\n'
    '<p class="roleNote">This article is about my mentality being deploy in the present time and the internet, everything while we find new ways to love.</p>\n'
    '\n'
    '<div class="articleRight">\n'
    '    <div class="articleRightInner">\n'
)

container_TxtHmtl.writelines(string_html)

string_html = (
    '<img src="' + VARIABLE_LINKSYMBOL +'" alt="Symbol" width="450" height="450"/>\n'
)

container_TxtHmtl.writelines(string_html)

string_html = (
    
    ' </div>\n'
    '    ./Youtube/Andraelity <a href="https://www.youtube.com/channel/UC-4AaN4M3Sq1lY6NVZnfaEw">Andreality</a>\n'
    '</div>\n'
    '<p>\n'
    '    <strong>'+ VARIABLE_NAMEPAGE +'</strong>\n'
    
)

container_TxtHmtl.writelines(string_html)

container_textStart = open('textStart.txt','r+')

for i in container_textStart:
    string_html = i
    container_TxtHmtl.writelines(string_html)

container_textStart.close()


string_html = (
    '</p>	\n'
    '        \n'
    '\n'
    '<div class="contentsPanel">\n'
    '    <div class="contentsHeader">Contents</div>\n'
    '    <ul>\n'
    
)

container_TxtHmtl.writelines(string_html)

#<li><span>2</span><a href="#">Health</a></li>

print('a windows path:')
print('Select folder where the files-program-txt are stored')
string_txtNames = 'nameFiles.txt'

contianer_names = open(string_txtNames, 'r+')
count = 0

for i in contianer_names:
    count += 1
    string_manage = '<li><span>' + count + '</span><a href="' + i.strip() +'">' + i.strip() + '</a></li>\n' 
    container_TxtHmtl.writelines(string_manage)

contianer_names.close()

string_html = (
    '</ul>\n'
    '</div>\n'
)

container_TxtHmtl.writelines(string_html)

container_subtitles = open('zzz_finalSubtitles.txt', 'r+')

for i in container_subtitles:
    container_TxtHmtl.writelines(i)


container_subtitles.close()


STRING_ENDPAGES = (
'    					\n'
'					<div class="lavenderBox">\n'
'						<div class="header">Panel title</div>\n'
'						<div class="subtitle linklist"><a href="#">Lorem</a> <a href="#">Ipsum</a> <a href="#">Dolorestitas</a> </div>\n'
'						<div class="linklist">\n'
'							<a href="#">Percipit </a> <a href="#">Mnesarchum </a> <a href="#">Molestie </a> <a href="#">Phaedrum </a> <a href="#">Luptatum constituam </a> <a href="#">Habeo adipisci </a> <a href="#">Inani zril  </a> <a href="#">Forensibus sea </a> <a href="#">Habeo adipisci </a> <a href="#">Minimum corrumpit </a> <a href="#">Regione suscipit </a> <a href="#">Has et partem </a><a href="#">Percipit </a> <a href="#">Mnesarchum </a> <a href="#">Molestie </a> <a href="#">Phaedrum </a> <a href="#">Luptatum constituam </a> <a href="#">Habeo adipisci </a> <a href="#">Inani zril  </a> <a href="#">Vel nisl albucius </a> <a href="#">Habeo adipisci </a> <a href="#">Minimum corrumpit </a> <a href="#">Regione suscipit </a> <a href="#">Percipit maiestatis </a> <a href="#">Regione suscipit </a> <a href="#">Percipit maiestatis </a>\n'
'						</div>\n'
'						\n'
'						<div class="subtitle">Subtitle</div>\n'
'					</div>\n'
'					\n'
'					<div class="categories">\n'
'						<a href="#">Minimum corrumpit </a> <a href="#">Regione suscipit </a> <a href="#">Has et partem </a>\n'
'					</div>\n'
'					\n'
'				</div>\n'
'				<div class="pagefooter">\n'
'					This page was last edited on 29.07.2017 | Template by <a href="http://html5-templates.com/" target="_blank" rel="nofollow">HTML5 Templates</a> <!-- Please leave this link unchanged -->\n'
'					<div class="footerlinks">\n'
'						<a href="#">Privacy policy</a> <a href="#">About</a> <a href="#">Terms and conditions</a> <a href="#">Cookie statement</a> <a href="#">Developers</a>\n'
'					</div>\n'
'				</div>\n'
'			\n'
'			\n'
'			</div>		\n'
'		</div>\n'
'		\n'
'		\n'
'        <script src="https://code.jquery.com/jquery-1.12.0.min.js"></script>\n'
'        <script>window.jQuery </script>\n'
'        <script src="script.js"></script>\n'
'\n'
'\n'
'    </body>\n'
'</html>\n'
'\n'
)

container_TxtHmtl.writelines(STRING_ENDPAGES)

container_TxtHmtl.close()

#
#Hay un punto donde usted puede estar practicando experimentos en sistemas de computo mas avanzados, relaciones conceptuales mas precisas
#Cualidades especificas mas definitivas
#Relaciones conceptuales mas detalladas.
#Usted hace experimentos en el servidor que el provee a usted del caluclo necesario para aprender a manejar como la realidad sucede de maneras mas especificas
#Como el presente momento puede encontrar propiedad
#


#Que concepto puedo entender que concepto puedo sintetizar en la realidad como puedo maximizar las definiciones que explican como la mente se crea
#Como la mente se representa cuales acciones yo quiero poder mejorar en la totalidad
#Que propiedades hacen que mi figura interna pueda hayar mocion.


#Entendiendo las propiedades que mejoran como el concepto se aprende como se pueden modelar las propiedades que definen realidad