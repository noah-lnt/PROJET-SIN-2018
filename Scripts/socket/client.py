#!/usr/bin/env python
# coding: utf-8

import socket
import time
from threading import Thread

from colorama import init
from colorama import Fore, Back, Style
init()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 1111))
test = "client"
s.send(test.encode())

class Afficheur(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        while True:
	        r  = s.recv(2048)
	        if(r.decode("utf-8")  != ""):
	        	command_name = r.decode("utf-8")
	        	print(command_name)
	        	if(command_name == "connection return"):
	        		print(Fore.YELLOW + "value condition")
	        		print(Style.RESET_ALL)
	        	else:
	        		print(Fore.YELLOW + "COMMAND INCONNUE")
	        		print(Style.RESET_ALL)

# Création des threads
thread_1 = Afficheur("1")

# Lancement des threads
thread_1.start()

while True:
	
	print("Commande à exécuter:")
	command_name = "client_" + input("COMMAND >>")
	s.send(command_name.encode())

