# importamos las librerías
import os, sys
from colorama import Fore, Back

# configuramos los colores de colorama
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# hacemos el menú
def menu():
    os.system('clear')
    title = '''
\033[31m   ▄██████▄   ▄██████▄  ████████▄  \033[34m ▄███████▄   ▄█   ▄█        ▄█          ▄████████ 
\033[31m  ███    ███ ███    ███ ███   ▀███ \033[34m██▀     ▄██ ███  ███       ███         ███    ███ 
\033[31m  ███    █▀  ███    ███ ███    ███ \033[34m      ▄███▀ ███▌ ███       ███         ███    ███ 
\033[31m ▄███        ███    ███ ███    ███ \033[34m ▀█▀▄███▀▄▄ ███▌ ███       ███         ███    ███ 
\033[31m▀▀███ ████▄  ███    ███ ███    ███ \033[34m  ▄███▀   ▀ ███▌ ███       ███       ▀███████████ 
\033[31m  ███    ███ ███    ███ ███    ███ \033[34m▄███▀       ███  ███       ███         ███    ███ 
\033[31m  ███    ███ ███    ███ ███   ▄███ \033[34m███▄     ▄█ ███  ███▌    ▄ ███▌    ▄   ███    ███ 
\033[31m  ████████▀   ▀██████▀  ████████▀  \033[34m ▀████████▀ █▀   █████▄▄██ █████▄▄██   ███    █▀  
\033[31m                                   \033[34m                 ▀         ▀          
\033[31m[~] By ZombieGeek0: https://www.github.com/ZombieGeek0/GodZilla
\033[31m[~] GitHub: https://github.com/ZombieGeek0           
'''
    print(title)

    options = '''
\033[34m[00]: Salir                                         \033[31m█\033[33m█\033[35m█\033[37m█\033[31m█\033[33m█\033[35m█\033[37m█
\033[34m[01]: Volver al menú                                \033[32m█\033[34m█\033[36m█\033[30m█\033[32m█\033[34m█\033[36m█\033[30m█ 
\033[34m[02]: Realizar una búsqueda con Sherlock
'''
    print(options)

    choice = input(Fore.RED + Back.RESET + '[?] -->  ')



menu()
