#-*- coding:utf-8 -*-
__author__ = 'hermes'

import socket
from os import system
from time import sleep
from datetime import datetime

global connectionName 
connectionName = 'TOGOTELECOM' # Definir le nom de votre reseau

def is_connected():
  # http://stackoverflow.com/questions/20913411/test-if-an-internet-connection-is-present-in-python
  try:
    #host = socket.gethostbyname("www.google.com")
    #socket.create_connection(('173.194.67.94', 80), 25)

    #methode 2 sans test de connection
    socket.gethostbyname("www.google.com")
    return True
  except:
    try:
      socket.create_connection(('173.194.67.94', 80), 15)
      return True
    except:  
      pass
    pass  
  return False


def hardRestartNetwork():
  system('nmcli networking off')
  system('nmcli networking on')
  #sleep(5)
  #system("nmcli connection up '%s'"% connectionName)


def patchTogotelecom():
  activeReseau = system('nmcli networking on')
  deconnectionSoft = system("nmcli connection down '%s'"% connectionName)
  
  sleep(3)
  connectionSoft = system("nmcli connection up '%s'"% connectionName)

  # if (deconnectionSoft == 0 or deconnectionSoft == 1536):
  #   activeTGTEL = system("nmcli connection up '%s'"% connectionName)
  #   if activeTGTEL == 768:
  #     # si Erreur : le délai d'attente de 90 sec a expiré.
  #     #system('modprobe --force-vermagic usb_wwan usbserial')
  #     hardRestartNetwork()      
  # else:
  #   # redemarrer le reseau si la methode soft ne marche pas
  #   hardRestartNetwork()
    
  if is_connected():
    print(u'Connecté le %s '%str(datetime.now().strftime('%d-%m-%Y -> %H:%M:%S')))
  else:
    print(u'Tentative echoué le %s '%str(datetime.now().strftime('%d-%m-%Y -> %H:%M:%S')))

 # sleep(5)


# debut de l execution du script
#system('modprobe --force-vermagic usb_wwan usbserial')
#hardRestartNetwork()
print(u'debut du script > %s '%str(datetime.now().strftime('%d-%m-%Y -> %H:%M:%S')))
sleep(5)


while True:
    if is_connected():
      sleep(15)
    else:
      print(u'Tentative de reconnexion le %s '%str(datetime.now().strftime('%d-%m-%Y -> %H:%M:%S')))
      patchTogotelecom()
