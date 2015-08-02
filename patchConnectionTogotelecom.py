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
    host = socket.gethostbyname("www.google.com")
    socket.create_connection((host, 80), 10)
    return True
  except:
    pass
  return False


def hardRestartNetwork():
  system('nmcli nm enable false')
  system('nmcli nm enable true')
  sleep(3)
  system("nmcli con up id '%s'"% connectionName)


def patchTogotelecom():
  activeReseau = system('nmcli nm enable true')
  deconnectionSoft = system('nmcli dev disconnect iface ttyUSB0')
  
  sleep(3)

  if (deconnectionSoft == 0 or deconnectionSoft == 1536):
    activeTGTEL = system("nmcli con up id '%s'"% connectionName)
    if activeTGTEL == 768:
      # si Erreur : le délai d'attente de 90 sec a expiré.
      system('modprobe --force-vermagic usb_wwan usbserial')
      hardRestartNetwork()      
  else:
    # redemarrer le reseau si la methode soft ne marche pas
    hardRestartNetwork()
    
  if is_connected():
    print(u'Connecté le %s '%str(datetime.now().strftime('%d-%m-%Y -> %H:%M:%S')))
  else:
    print(u'Tentative echoué le %s '%str(datetime.now().strftime('%d-%m-%Y -> %H:%M:%S')))

  sleep(3)


# debut de l execution du script
system('modprobe --force-vermagic usb_wwan usbserial')
hardRestartNetwork()
sleep(3)

while True:
    if is_connected():
      sleep(360)
    else:
      print(u'Tentative de reconnexion le %s '%str(datetime.now().strftime('%d-%m-%Y -> %H:%M:%S')))
      patchTogotelecom()