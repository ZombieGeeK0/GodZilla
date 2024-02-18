# importamos las librerías necesarias
from colorama import Fore, Back
from sys import argv
import os, sys

# declaramos los argumentos
para1 = argv
para2 = argv

# hacemos las funciones principales
def sherlock():
    os.system('clear')
    title = '''
\033[31m   ▄████████    ▄█    █▄       ▄████████    ▄████████  ▄█        ▄██████▄   ▄████████    ▄█   ▄█▄ 
\033[31m  ███    ███   ███    ███     ███    ███   ███    ███ ███       ███    ███ ███    ███   ███ ▄███▀ 
\033[31m  ███    █▀    ███    ███     ███    █▀    ███    ███ ███       ███    ███ ███    █▀    ███▐██▀   
\033[31m  ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███       ███    ███ ███         ▄█████▀    
\033[31m▀███████████ ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███       ███    ███ ███        ▀▀█████▄    
\033[31m         ███   ███    ███     ███    █▄  ▀███████████ ███       ███    ███ ███    █▄    ███▐██▄   
\033[31m   ▄█    ███   ███    ███     ███    ███   ███    ███ ███▌    ▄ ███    ███ ███    ███   ███ ▀███▄ 
\033[31m ▄████████▀    ███    █▀      ██████████   ███    ███ █████▄▄██  ▀██████▀  ████████▀    ███   ▀█▀ 
\033[31m                                           ███    ███ ▀                                 ▀         
'''
    print(title)

    print(Fore.RED + Back.RESET + '========================================================================================')
    os.system(Fore.BLUE + Back.RESET + f'cd sherlock && cd sherlock && python3 sherlock.py {para2[2]}')
    print(Fore.RED + Back.RESET + '========================================================================================')
    print(Fore.BLUE + Back.RESET + '[?] Proceso finalizado con éxito.')
    print(Fore.RESET + Back.RESET)
    sys.exit()


def install():
    os.system('clear')
    title = '''
\033[31m ▄█  ███▄▄▄▄      ▄████████     ███        ▄████████\033[34m  ▄█        ▄█          ▄████████    ▄████████ 
\033[31m███  ███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███\033[34m ███       ███         ███    ███   ███    ███ 
\033[31m███▌ ███   ███   ███    █▀     ▀███▀▀██   ███    ███\033[34m ███       ███         ███    █▀    ███    ███ 
\033[31m███▌ ███   ███   ███            ███   ▀   ███    ███\033[34m ███       ███        ▄███▄▄▄      ▄███▄▄▄▄██▀ 
\033[31m███▌ ███   ███ ▀███████████     ███     ▀███████████\033[34m ███       ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
\033[31m███  ███   ███          ███     ███       ███    ███\033[34m ███       ███         ███    █▄  ▀███████████ 
\033[31m███  ███   ███    ▄█    ███     ███       ███    ███\033[34m ███▌    ▄ ███▌    ▄   ███    ███   ███    ███ 
\033[31m█▀    ▀█   █▀   ▄████████▀     ▄████▀     ███    █▀ \033[34m █████▄▄██ █████▄▄██   ██████████   ███    ███ 
\033[31m                                                    \033[34m ▀         ▀                        ███    ███ 
'''
    print(title)
    print(Fore.RED + Back.RESET + '========================================================================================')
    os.system(Fore.BLUE + Back.RESET + f'sudo su && sudo apt-get update && apt-get install git -y && sudo apt-get install python3 && pip3 install colorama && sudo apt-get install python3-pip && git clone https://github.com/sherlock-project/sherlock')
    print(Fore.RED + Back.RESET + '========================================================================================')
    print(Fore.BLUE + Back.RESET + '[?] Proceso finalizado con éxito.')
    print(Fore.RESET + Back.RESET)
    sys.exit()

def credits():
    os.system('clear')
    title = '''
\033[31m ▄████████    ▄████████    ▄████████\033[34m ████████▄   ▄█      ███        ▄████████ 
\033[31m███    ███   ███    ███   ███    ███\033[34m ███   ▀███ ███  ▀█████████▄   ███    ███ 
\033[31m███    █▀    ███    ███   ███    █▀ \033[34m ███    ███ ███▌    ▀███▀▀██   ███    █▀  
\033[31m███         ▄███▄▄▄▄██▀  ▄███▄▄▄    \033[34m ███    ███ ███▌     ███   ▀   ███        
\033[31m███        ▀▀███▀▀▀▀▀   ▀▀███▀▀▀    \033[34m ███    ███ ███▌     ███     ▀███████████ 
\033[31m███    █▄  ▀███████████   ███    █▄ \033[34m ███    ███ ███      ███              ███ 
\033[31m███    ███   ███    ███   ███    ███\033[34m ███   ▄███ ███      ███        ▄█    ███ 
\033[31m████████▀    ███    ███   ██████████\033[34m ████████▀  █▀      ▄████▀    ▄████████▀  
\033[31m             ███    ███             \033[34m                                          
'''
    print(title)
    print(Fore.RED + Back.RESET + '========================================================================================')
    options = '''
[?] Este proyecto ha sido creado por ZombieGeek0.
[?] GitHub: https://www.github.com/ZombieGeek0.
[?] GitHub del proyecto: https://github.com/ZombieGeek0/GodZilla.
'''
    print(Fore.BLUE + Back.RESET + options)
    print(Fore.RED + Back.RESET + '========================================================================================')
    print(Fore.BLUE + Back.RESET + '[?] Proceso finalizado con éxito.')
    print(Fore.RESET + Back.RESET)
    sys.exit()

# hacemos el menú
def menu():
    if para1[1] == '--install':
        install()

    elif para1[1] == '--sherlock':
        sherlock()

    elif para1[1] == '--credits':
        credits()

    else:
        print(Fore.RED + Back.RESET + '\n[?] Error: Revisa si has incluido todos los parámetros necesarios en la petición.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

menu()
