import time
import os
from platform import system

color="\033[36m"

os.system("clear")
logo = color + '''
 ██████  ███████ ████████     ██████  ██ ██████  
██       ██         ██        ██   ██ ██ ██   ██ 
██   ███ █████      ██        ██████  ██ ██████  
██    ██ ██         ██        ██      ██ ██      
 ██████  ███████    ██        ██      ██ ██'''

print(logo)

def pip():
  print('\n[1] Instalar pip')
  print('[00] Regresar al menu principal')
  print('[99] Salir')
  continuar = int(input("[~] Elije una opcion: "))
  if continuar == 1:
      continuar3 = int(input('\n[~] Seguro que quieres instalar pip para python? (1 Si) (2 No): '))
      if continuar3 == 1:
          print('[~] Instalando pip...')
          os.system("wget https://bootstrap.pypa.io/get-pip.py")
          os.system("python get-pip.py")
          print('[~] pip instalado correctamente!')
      elif continuar3 == 2:
          print('[~] Instalacion de pip para python cancelada.')
          print('[~] Regresando al menu principal...')
          time.sleep(2)
          os.system("clear")
          print(logo)
          menu()
  elif continuar == 00:
       print('[~] Regresando al menu principal.')
       time.sleep(2)
       os.system("clear")
       print(logo)
       menu()
  elif continuar == 99:
      print('[~] Saliendo del programa...')
      time.sleep(2)
      exit()
  else:
     print('[~] Error opcion invalida.')
     time.sleep(3)
     os.system("clear")
     time.sleep(2) 
     pip()
  
def pip2():
  print('\n[1] Instalar pip2')
  print('[00] Regresar al menu principal')
  print('[99] Salir')
  continuar2 = int(input("[~] Elije una opcion: "))
  if continuar2 == 1:
     T = int(input('\n[~] Seguro que quieres instalar pip para python? (1 Si) (2 No): '))
     if T == 1:
        print('[~] Instalando pip...')
        os.system("wget https://bootstrap.pypa.io/pip/2.7/get-pip.py")
        os.system("python get-pip.py")
        print('[~] pip instalado correctamente!')
     elif T == 2:
        print('[~] Instalacion de pip para python cancelada.')
        print('[~] Regresando al menu principal...')
        time.sleep(2)
        os.system("clear")
        print(logo)
        menu()
  elif continuar2 == 00:
     print('[~] Regresando al menu principal.')
     time.sleep(2)
     os.system("clear")
     print(logo)
     menu()
  elif continuar2 == 99:
     print('[~] Saliendo del programa...')
     time.sleep(2)
     exit()
  else:
    print('[~] Error opcion invalida.')
    os.system("clear")
    pip2()

def menu():
  print('\n[1] Instalar pip')
  print('[2] Instalar pip2')
  print('[99] Salir')
  elegir = int(input('[~] Selecciona una opcion: '))
  if elegir == 1:
    pip()
  elif elegir == 2:
    pip2()
  elif elegir == 99:
    exit()
  else:
    print('[~] Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    menu()

menu()
